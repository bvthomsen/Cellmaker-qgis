# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CellMaker
                                 A QGIS plugin
 Create and populate rectangular cells
                              -------------------
        begin                : 2013-12-12
        copyright            : (C) 2013 by Bo Victor Thomsen
        email                : bvt@aestas.dk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries

from pyspatialite import dbapi2 as db
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import resources
from cellmakerdialog import CellMakerDialog1, CellMakerDialog2, CellMakerDialog3, CellMakerDialog4
import os.path
import shutil
from qgis.gui import QgsMessageBar
import qgis.utils

def sanitize(tablename):
    return tablename.lower().replace(u' ',u'_').replace(u'å',u'aa').replace(u'æ',u'ae').replace(u'ø',u'oe')  

#def populateCelltableDropDown (cbCells):

#    cbCells.clear()
#    ctUri = QgsDataSourceURI()
#    ctUri.setDatabase(self.database_name)
#    ctUri.setDataSource('', 'celltables','','','cid')
#    ctLayer = QgsVectorLayer(ctUri.uri(), 'Cell Tables', 'spatialite')                

#    for f in ctLayer.getFeatures():
#        cbCells.addItem(f['name'])

#    return cbCells

class CellMaker:

    def __init__(self, iface):
        
        # Usual initialization stuff
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        home = os.path.expanduser("~") + "/Cellmaker"
        if not os.path.exists(home): 
            os.makedirs(home)
        if not os.path.isfile(home + "/cellmaker.sqlite"): 
            shutil.copyfile(os.path.dirname(__file__) + "/cellmaker.sqlite", home + "/Cellmaker.sqlite")
            
        self.database_name = home + "/cellmaker.sqlite" # os.path.dirname(__file__) + "/cellmaker.sqlite"
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'cellmaker_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Structural changes to the database
        conn = db.connect(self.database_name)
        cur = conn.cursor()

        # New columns sizex and sizey in celltables
        sql = 'SELECT sizex, sizey from celltables limit 1'
        try:
            cur.execute(sql)
        except db.OperationalError:
            sql = 'ALTER TABLE celltables RENAME TO qwerty_cell'
            cur.execute(sql)
            sql = 'CREATE TABLE celltables (cid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,sizex DOUBLE NOT NULL,sizey DOUBLE NOT NULL,value DOUBLE NOT NULL,xmin DOUBLE NOT NULL,ymin DOUBLE NOT NULL,xmax DOUBLE NOT NULL,ymax DOUBLE NOT NULL,srid INTEGER NOT NULL)'
            cur.execute(sql)
            sql = 'INSERT INTO celltables (name,sizex,sizey,value,xmin,ymin,xmax,ymax,srid) SELECT name,size,size,value,xmin,ymin,xmax,ymax,srid FROM qwerty_cell'
            cur.execute(sql)
            sql = 'DROP TABLE qwerty_cell'
            cur.execute(sql)

        # New view 
        sql = 'CREATE VIEW IF NOT EXISTS  "celltables_view" AS SELECT * FROM celltables ORDER BY name COLLATE NOCASE'
        cur.execute(sql)
        conn.commit()                        
        conn.close
                
        # Create instances of the 3 dialogs
        self.dlg1 = CellMakerDialog1()
        self.dlg2 = CellMakerDialog2()
        self.dlg3 = CellMakerDialog3()
        self.dlg4 = CellMakerDialog4()
        
    def initGui(self):

        # Create action that will start plugin configuration
        self.action1 = QAction(QIcon(":/plugins/cellmaker/icon.png"),QApplication.translate("@default","Create cells.."), self.iface.mainWindow())
        self.action2 = QAction(QIcon(":/plugins/cellmaker/icon.png"),QApplication.translate("@default","Overlay cells with layer.."), self.iface.mainWindow())
        self.action3 = QAction(QIcon(":/plugins/cellmaker/icon.png"),QApplication.translate("@default","Save cell layer as raster.."), self.iface.mainWindow())
        self.action4 = QAction(QIcon(":/plugins/cellmaker/icon.png"),QApplication.translate("@default","Delete cell layer from database.."), self.iface.mainWindow())

        # connect the actions to the run method
        self.action1.triggered.connect(self.run1)
        self.action2.triggered.connect(self.run2)
        self.action3.triggered.connect(self.run3)
        self.action4.triggered.connect(self.run4)

        # Add toolbar buttons and menu items
        self.iface.addPluginToMenu(QApplication.translate("@default","&Cell Maker"), self.action1)
        self.iface.addPluginToMenu(QApplication.translate("@default","&Cell Maker"), self.action2)
        self.iface.addPluginToMenu(QApplication.translate("@default","&Cell Maker"), self.action3)
        self.iface.addPluginToMenu(QApplication.translate("@default","&Cell Maker"), self.action4)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(QApplication.translate("@default","&Cell Maker"), self.action1)
        self.iface.removePluginMenu(QApplication.translate("@default","&Cell Maker"), self.action2)
        self.iface.removePluginMenu(QApplication.translate("@default","&Cell Maker"), self.action3)
        self.iface.removePluginMenu(QApplication.translate("@default","&Cell Maker"), self.action4)
        self.iface.removeToolBarIcon(self.action1)
        self.iface.removeToolBarIcon(self.action2)
        self.iface.removeToolBarIcon(self.action3)
        self.iface.removeToolBarIcon(self.action4)

    # run method that performs all the real work
    def run1(self):
    
        # show the dialog
        layer = self.iface.activeLayer()
        if layer:
            if layer.type() == QgsMapLayer.VectorLayer:
                mbr = layer.boundingBoxOfSelected()
                crsSrc = layer.crs()
                crsDest = self.iface.mapCanvas().mapRenderer().destinationCrs()
                xform = QgsCoordinateTransform(crsSrc, crsDest)
                mbr = xform.transform(mbr)
                self.dlg1.ui.dsbXmin.setValue(mbr.xMinimum())
                self.dlg1.ui.dsbYmin.setValue(mbr.yMinimum())
                self.dlg1.ui.dsbXmax.setValue(mbr.xMaximum())
                self.dlg1.ui.dsbYmax.setValue(mbr.yMaximum())
                self.dlg1.ui.lblProjection.setText(crsDest.description())
     
        self.dlg1.show()
        self.dlg1.ui.leCellName.setFocus()

        # Run the dialog event loop
        result = self.dlg1.exec_()
        # See if OK was pressed
        if result == 1:
            nrows = self.dlg1.Vnrows        
            ncols = self.dlg1.Vncols
            ncells = ncols*nrows
            layerName = self.dlg1.Vlayer
           
            if (ncells > 100000): 
                reply = QMessageBox.question(self.dlg1, QApplication.translate("@default","Generate cells (number > 100.000) ?"),
                    QApplication.translate("@default","This command will create ") + unicode(ncells) + QApplication.translate("@default"," cells in layer ") + layerName + QApplication.translate("@default",". Do yo want to continue ?"), 
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

                if reply == QMessageBox.No:   
                    return
                else:
                    pass

            # Create new cell table in spatialite database
            
            canvas = self.iface.mapCanvas()
            mapRenderer = canvas.mapRenderer()
            srs=mapRenderer.destinationCrs()
            srid = srs.postgisSrid()

            conn = db.connect(self.database_name)
            cur = conn.cursor()

            # Create table in spatialite database

            notDone = True
            while (notDone):
                try:
                    table = sanitize(layerName)
                    sql = "CREATE TABLE " + table + " (gid INTEGER PRIMARY KEY NOT NULL, rowno INTEGER NOT NULL DEFAULT 0, colno INTEGER NOT NULL DEFAULT 0, value DOUBLE NOT NULL DEFAULT 0, overlays INTEGER NOT NULL DEFAULT 0)"
                    cur.execute(sql)
                    ok = True
                    notDone = False                    
                except db.OperationalError , e:
                    ok = False
                    layerName, notDone = QInputDialog.getText(self.dlg1, QApplication.translate('@default','Duplicate tablename'),QApplication.translate('@default','The chosen layername: "') + layerName + QApplication.translate('@default','" results in an existing tablename: "') + table + '"\n' + QApplication.translate('@default','Alternative layername: "'))
                    if layerName == "":
                        notDone = False
                
            if ok:
                sql = "SELECT AddGeometryColumn('" + table + "','geom'," + str(srid) + ", 'POLYGON', 'XY')"
                cur.execute(sql)
                sql = "SELECT CreateSpatialIndex('" + table + "', 'geom')"
                cur.execute(sql)
                sql = "INSERT INTO celltables (name, sizex, sizey, value, xmin, ymin, xmax, ymax,srid) VALUES('" +  layerName + "', " + str(self.dlg1.VsizeX) + ", " + str(self.dlg1.VsizeY) + ", " + str(self.dlg1.Vval) + ", " + str(self.dlg1.Vxmin) + ", " + str(self.dlg1.Vymin) + ", " + str(self.dlg1.Vxmax) + ", " + str(self.dlg1.Vymax) + ", " + str(srid) + ")"
                cur.execute(sql)

                conn.commit()                        
                conn.close
                

                # establish connection to the new table
                uri = QgsDataSourceURI()
                uri.setDatabase(self.database_name)
                uri.setDataSource('',table,'geom','','gid')
                layer = QgsVectorLayer(uri.uri(), layerName, 'spatialite')                

                # generate feature
                ymax = self.dlg1.Vymin
                sizex = self.dlg1.VsizeX
                sizey = self.dlg1.VsizeY
                fields = layer.pendingFields()
                feats = [] 
                for i in range(0,nrows):
                    ymin = ymax
                    ymax = ymax + sizey
                    xmax = self.dlg1.Vxmin
                    for j in range(0,ncols):
                        feat = QgsFeature(fields)
                        feat[0] = i*ncols + j
                        feat[1] = i
                        feat[2] = j
                        feat[3] = 0.0
                        feat[4] = 0
                        xmin = xmax
                        xmax = xmin + sizex
                        feat.setGeometry(QgsGeometry.fromPolygon([[QgsPoint(xmin,ymin),QgsPoint(xmin,ymax),QgsPoint(xmax,ymax),QgsPoint(xmax,ymin),QgsPoint(xmin,ymin)]]))
                        feats.append(feat)
                        if len(feats) >= 20000:
                            QMessageBox.information(self.dlg1, 'Features',str(len(feats)), QMessageBox.Ok | QMessageBox.Ok)
                            layer.dataProvider().addFeatures(feats)
                            feats = []
                       
                if len(feats) > 0:
                    layer.dataProvider().addFeatures(feats)

                # If checked, add new layer to canvas
                if self.dlg1.Vshow:
                    QgsMapLayerRegistry.instance().addMapLayer(layer)

            else:
                conn.commit()                        
                conn.close

            

    # run method that performs all the real work
    def run2(self):
        
        # Populate cbCells dropdown         
        self.dlg2.ui.cbCells.clear()
        # Create uri for cellmaker database / celltables table
        ctUri = QgsDataSourceURI()
        ctUri.setDatabase(self.database_name)
        ctUri.setDataSource('', 'celltables_view','','','cid')
        ctLayer = QgsVectorLayer(ctUri.uri(), 'Cell Tables', 'spatialite')                

        for f in ctLayer.getFeatures():
            self.dlg2.ui.cbCells.addItem(f['name'])
        
        # Populate lvOverlays listview         
        self.dlg2.ui.lwOverlays.clear()
        canvas = self.iface.mapCanvas()
        allLayers = canvas.layers()
        for i in allLayers:
            if i.type() == QgsMapLayer.VectorLayer and i.geometryType() < 3:
                item = QListWidgetItem()
                item.setText(i.name())
                item.setHidden(False)
                item.setData (32,i.geometryType())
                self.dlg2.ui.lwOverlays.addItem(item)        

        # check combobox items
        if self.dlg2.ui.lwOverlays.count() == 0 or self.dlg2.ui.cbCells.count() == 0:
            qgis.utils.iface.messageBar().pushMessage(QApplication.translate("@default","Error"), QApplication.translate("@default","Missing cell layers and / or vector layers"), QgsMessageBar.CRITICAL,5)
            return 
            
        # show the dialog
        self.dlg2.show()
        self.dlg2.ui.rbSimpleOverlay.click()
        self.dlg2.ui.cbCells.setFocus()
        
        result = self.dlg2.exec_()
        if result == 1:

            overlays = self.dlg2.Voverlays
            facval =  self.dlg2.Vfactor
            cells =  self.dlg2.Vcells
            oltype =  self.dlg2.Vtype

            for o in overlays:
                overlay = o.text()
                # find corresponding layer
                for i in allLayers:
                    if i.name() == overlay:
                        oLayer = i
                        crsDest = oLayer.crs()
                        oType = i.geometryType()
                        break
                
                # find cell table and extends
                for f in ctLayer.getFeatures():
                    if f['name'] == cells: 
                        crsSrc = QgsCoordinateReferenceSystem( f['srid'], QgsCoordinateReferenceSystem.EpsgCrsId )
                        mbr = QgsRectangle(f['xmin'], f['ymin'],f['xmax'], f['ymax'])
                        xform = QgsCoordinateTransform(crsSrc, crsDest)
                        mbr = xform.transform(mbr)
                        break

                # Generate index for overlay layer                    
                request=QgsFeatureRequest()
                request.setFilterRect(mbr)
                index = QgsSpatialIndex()
                for f in oLayer.getFeatures(request): index.insertFeature(f)
                
                # Open cell layer
                ctUri.setDataSource('',sanitize(cells),'geom','','gid')
                cLayer = QgsVectorLayer(ctUri.uri(), cells, 'spatialite')  

                # Iterate cell layer
                att = {}
                counter = 0
                number = 0
                for g in cLayer.getFeatures():
                    number += 1
                    xover = g['overlays']
                    xval =  g['value']
                    xid = g.id()    
                    # Find intersection MBR's in index 
                    ids = index.intersects(g.geometry().boundingBox())
                    # Iterate intersected overlay features
                    for id in ids:
                        oFeat = QgsFeature()
                        oLayer.getFeatures(QgsFeatureRequest().setFilterFid(id)).nextFeature(oFeat) 
                        # cell intersects actual layer object ?
                        if oFeat.geometry().intersects(g.geometry()):
                            xover += 1
                            gg = g.geometry()
                            fg = oFeat.geometry()

                            if oltype == 1:
                                xval += facval
                            elif oltype == 2:
                                try:
                                    xval += fg.intersection(gg).length() * facval
                                except:
                                    pass
                            elif oltype == 3:
                                try:
                                    xval += fg.intersection(gg).area() * facval
                                except:
                                    pass

                    if g['overlays'] < xover: 
                        counter += 1
                        att[xid] = {3:xval, 4:xover}
 
                if att <> {}: cLayer.dataProvider().changeAttributeValues(att) 
                qgis.utils.iface.messageBar().pushMessage(QApplication.translate("@default","Total number of cells / additions: "), str(number) + ' / ' + str(counter), QgsMessageBar.INFO, 5)




    # run method that performs all the real work
    def run3(self):

   
        # Populate cbCells dropdown         
        self.dlg3.ui.cbCells.clear()
        ctUri = QgsDataSourceURI()
        ctUri.setDatabase(self.database_name)
        ctUri.setDataSource('', 'celltables_view','','','cid')
        ctLayer = QgsVectorLayer(ctUri.uri(), 'Cell Tables', 'spatialite')                
        for f in ctLayer.getFeatures():
            self.dlg3.ui.cbCells.addItem(f['name'])

        # check combobox items
        if self.dlg3.ui.cbCells.count() == 0:
            qgis.utils.iface.messageBar().pushMessage(QApplication.translate("@default","Error"), QApplication.translate("@default","Missing cell layers"), QgsMessageBar.CRITICAL,5)
            return 

        # show the dialog
        self.dlg3.show()
        self.dlg3.ui.cbCells.setFocus()

        # Run the dialog event loop
        result = self.dlg3.exec_()
        # See if OK was pressed
        if result == 1:

            outfile = self.dlg3.Vfilename
            att = self.dlg3.Vcol
            cells =  self.dlg3.Vcells
        
            for f in ctLayer.getFeatures():
                if f['name'] == cells: 
                    xll = f['xmin']
                    yll = f['ymin']
                    szx =  f['sizex']
                    szy =  f['sizey']
                    ncol = (f['xmax'] - xll) // szx
                    nrow = (f['ymax'] - yll) // szy
                    break    
           
            ctUri.setDataSource('','(select * from ' + sanitize(cells) + ' order by rowno desc, colno asc)','geom','','gid')
            ctLayer = QgsVectorLayer(ctUri.uri(), cells, 'spatialite')  
            fpout = open(outfile, "wt")
            fpout.write("NCOLS " + str(ncol) + "\n")
            fpout.write("NROWS " + str(nrow) + "\n")
            fpout.write("XLLCORNER " + str(xll) + "\n")
            fpout.write("YLLCORNER " + str(yll) + "\n")
            if szx == szy:
                fpout.write("CELLSIZE " + str(szx) + "\n")
            else:
                fpout.write("XCELLSIZE " + str(szx) + "\n")
                fpout.write("YCELLSIZE " + str(szy) + "\n")
            fpout.write("NODATA_VALUE -9999\n")

            counter = 0
            for f in ctLayer.getFeatures():
                counter += 1
                if counter % 20 == 0: fpout.write("\n")    
                fpout.write(str(f[att]) + " ")
            fpout.write("\n")
            fpout.close()
            qgis.utils.iface.messageBar().pushMessage(QApplication.translate("@default","Total number of pixels: "), str(counter), QgsMessageBar.INFO,5)
 

    def run4(self):


        # Populate cbCells dropdown         
        self.dlg4.ui.cbCells.clear()
        ctUri = QgsDataSourceURI()
        ctUri.setDatabase(self.database_name)
        ctUri.setDataSource('', 'celltables_view','','','cid')
        ctLayer = QgsVectorLayer(ctUri.uri(), 'Cell Tables', 'spatialite')                
        for f in ctLayer.getFeatures():
            self.dlg4.ui.cbCells.addItem(f['name'])

        # check combobox items
        if self.dlg4.ui.cbCells.count() == 0:
            qgis.utils.iface.messageBar().pushMessage(QApplication.translate("@default","Error"), QApplication.translate("@default","Missing cell layers"), QgsMessageBar.CRITICAL,5)
            return 

   
        # show the dialog
        self.dlg4.show()
        self.dlg4.ui.cbCells.setFocus()

        # Run the dialog event loop
        result = self.dlg4.exec_()
        # See if OK was pressed
        if result == 1:

            reply = QMessageBox.question(self.dlg1, QApplication.translate("@default","Delete table ") + self.dlg4.Vcells + QApplication.translate("@default"," from database"),
                QApplication.translate("@default","Delete table ? "), 
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.No:   
                return
            else:
                pass

            cells =  sanitize(self.dlg4.Vcells)
        
            # Create new cell table in spatialite database
            conn = db.connect(self.database_name)
            cur = conn.cursor()

            # Remove table in spatialite database

            sql = "DROP TABLE IF EXISTS idx_" + cells + "_geom"
            cur.execute(sql)

            sql = "DROP TABLE IF EXISTS idx_" + cells + "_geom_node"
            cur.execute(sql)

            sql = "DROP TABLE IF EXISTS idx_" + cells + "_geom_parent"
            cur.execute(sql)

            sql = "DROP TABLE IF EXISTS idx_" + cells + "_geom_rowid"
            cur.execute(sql)

            sql = "DELETE FROM celltables where name = '" + self.dlg4.Vcells + "'"
            cur.execute(sql)

            sql = "DELETE FROM geometry_columns where f_table_name = '" + cells + "'"
            cur.execute(sql)

            sql = "DROP TABLE IF EXISTS " + cells 
            cur.execute(sql)

            if self.dlg4.Vvacuum:

                 sql = "VACUUM"  
                 cur.execute(sql)

            conn.commit()                        
            conn.close

            qgis.utils.iface.messageBar().pushMessage(QApplication.translate("@default","Delete Table from database"), QApplication.translate("@default","Table ") + self.dlg4.Vcells + QApplication.translate("@default"," deleted"), QgsMessageBar.INFO,5)
