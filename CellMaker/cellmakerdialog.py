# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CellMakerDialog
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
from PyQt4 import QtCore, QtGui
from ui_cellmaker1 import Ui_CellMaker1
from ui_cellmaker2 import Ui_CellMaker2
from ui_cellmaker3 import Ui_CellMaker3
from ui_cellmaker4 import Ui_CellMaker4
from qgis.gui import QgsMessageBar
import qgis.utils
from pyspatialite import dbapi2 as db


class CellMakerDialog1(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_CellMaker1()
        self.ui.setupUi(self)
        
    def accept(self):

        class XminGeXmax(Exception): pass
        class YminGeYmax(Exception): pass
        class MbrBadSize(Exception): pass
        class MissingCell(Exception): pass
#        class ExistingTable(Exception): pass
       
        self.Vlayer = self.ui.leCellName.text()
        self.Vxmin = float(self.ui.dsbXmin.text().replace(",", "."))
        self.Vymin = float(self.ui.dsbYmin.text().replace(",", "."))
        self.Vxmax = float(self.ui.dsbXmax.text().replace(",", "."))
        self.Vymax = float(self.ui.dsbYmax.text().replace(",", "."))       
        self.VsizeX = float(self.ui.dsbSizeX.text().replace(",", "."))        
        self.VsizeY = float(self.ui.dsbSizeY.text().replace(",", "."))        
        self.Vval  = float(self.ui.dsbValue.text().replace(",", "."))        
        self.Vnrows = int((self.Vymax - self.Vymin)//self.VsizeY)
        self.Vncols = int((self.Vxmax - self.Vxmin)//self.VsizeX)
        self.Vshow = self.ui.cbShow.isChecked()
#        self.Vexists = True

        try:
            if self.Vxmin >= self.Vxmax:
                raise XminGeXmax, (QtGui.QApplication.translate("@default","x maximum value must be greater than x minimum"))

            if self.Vymin >= self.Vymax:
                raise YminGeYmax, (QtGui.QApplication.translate("@default","y maximum value must be greater than y minimum"))

            if len(self.Vlayer) == 0:
                raise MissingCell, (QtGui.QApplication.translate("@default","The cell layer has to be defined"))
                
            if ((self.Vymax - self.Vymin)%self.VsizeY > 0.0) or ((self.Vxmax - self.Vxmin)%self.VsizeX > 0.0):
                raise MbrBadSize, (QtGui.QApplication.translate("@default","The length and height of the defined rectangle has to be an integer multiplum of the cell X and Y-size"))

 #           conn = db.connect(super(self).database_name)
 #           cur = conn.cursor()
 #           table = sanitize(self.Vlayer)
 #           try:
 #               sql = 'SELECT * FROM ' + table + ' LIMIT 1'
 #               cur.execute(sql)
 #           except db.OperationalError:
 #               self.Vexists = False

 #           conn.commit()                        
 #           conn.close

 #           if self.Vexists:
 #               raise ExistingTable, (QtGui.QApplication.translate("@default","The chosen name for the cell layer results in a tablename which already exist in the database"))
                
        except XminGeXmax, e:
            qgis.utils.iface.messageBar().pushMessage(QtGui.QApplication.translate("@default","Error"), unicode(e), QgsMessageBar.CRITICAL, 5)
            self.ui.dsbXmin.setFocus()
            return
        except YminGeYmax, e:
            qgis.utils.iface.messageBar().pushMessage(QtGui.QApplication.translate("@default","Error"), unicode(e), QgsMessageBar.CRITICAL, 5)
            self.ui.dsbYmin.setFocus()
            return
        except MissingCell, e:
            qgis.utils.iface.messageBar().pushMessage(QtGui.QApplication.translate("@default","Error"), unicode(e), QgsMessageBar.CRITICAL, 5)
            self.ui.leCellName.setFocus()
            return
        except MbrBadSize, e:
            reply = QtGui.QMessageBox.question(self, QtGui.QApplication.translate("@default","Illegal combination of cellsize and extends"),unicode(e) + QtGui.QApplication.translate("@default","\nMay the function adjust the extends values ?"),
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
   
            if reply == QtGui.QMessageBox.Yes:
                import math
                self.Vxmin = math.floor(self.Vxmin/self.VsizeX) * self.VsizeX
                self.Vxmax = math.ceil(self.Vxmax/self.VsizeX) * self.VsizeX
                self.Vymin = math.floor(self.Vymin/self.VsizeY) * self.VsizeY
                self.Vymax = math.ceil(self.Vymax/self.VsizeY) * self.VsizeY
                self.ui.dsbXmin.setValue(self.Vxmin)
                self.ui.dsbYmin.setValue(self.Vymin)
                self.ui.dsbXmax.setValue(self.Vxmax)
                self.ui.dsbYmax.setValue(self.Vymax)
            self.ui.dsbSizeX.setFocus()
            return
#        except ExistingTable, e:
#            reply = QtGui.QMessageBox.question(self, QtGui.QApplication.translate("@default","Duplicate tablename"),unicode(e) + QtGui.QApplication.translate("@default","\nOverwrite the existing table ?"),
#                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
#   
#            if reply == QtGui.QMessageBox.No:
#                self.ui.leCellName.setFocus()
#                return

        QtGui.QDialog.accept(self)


class CellMakerDialog2(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_CellMaker2()
        self.ui.setupUi(self)


        self.ui.rbSimpleOverlay.clicked.connect(self.typeOverlay)
        self.ui.rbLineOverlay.clicked.connect(self.typeOverlay)
        self.ui.rbAreaOverlay.clicked.connect(self.typeOverlay)
        self.ui.rbSimpleOverlay.click()

    def typeOverlay(self):
    
        if self.ui.rbSimpleOverlay.isChecked():
            rt = 0
        if self.ui.rbLineOverlay.isChecked():
            rt = 1
        if self.ui.rbAreaOverlay.isChecked():
            rt = 2

        for i in xrange(self.ui.lwOverlays.count()):
            self.ui.lwOverlays.item(i).setSelected(False)
            self.ui.lwOverlays.item(i).setHidden(False if rt == 0 or rt == self.ui.lwOverlays.item(i).data(32) else True)
            
    def accept(self):

        class WrongActionForPoint(Exception): pass
        class WrongActionForLine(Exception): pass
        class WrongActionForPolygon(Exception): pass
       
        if self.ui.rbSimpleOverlay.isChecked():
            self.Vtype = 1
        if self.ui.rbLineOverlay.isChecked():
            self.Vtype = 2
        if self.ui.rbAreaOverlay.isChecked():
            self.Vtype = 3
            
        self.Vcells = self.ui.cbCells.currentText()
        self.Voverlays = self.ui.lwOverlays.selectedItems()
        self.Vfactor  = float(self.ui.dsbFactor.text().replace(",", "."))        
        #oType = self.ui.cbOverlays.itemData(self.ui.cbOverlays.currentIndex())
        
        #try:

        #    if oType == 0 and self.Vtype != 1:
        #        raise WrongActionForPoint, (QtGui.QApplication.translate("@default","Only simple overlay is allowed for point layers"))

        #    if oType == 1 and self.Vtype == 3:
        #        raise WrongActionForPoint, (QtGui.QApplication.translate("@default","Only simple and line overlay is allowed for line layers"))

        #    if oType == 2 and self.Vtype == 2:
        #        raise WrongActionForPolygon, (QtGui.QApplication.translate("@default","Only simple and area overlay is allowed for polygon layers"))

        #except WrongActionForPoint, e:
        #    qgis.utils.iface.messageBar().pushMessage(QtGui.QApplication.translate("@default","Error: "), unicode(e), QgsMessageBar.CRITICAL, 5)
        #    self.ui.rbSimpleOverlay.setFocus()
        #    return

        #except WrongActionForLine, e:
        #    qgis.utils.iface.messageBar().pushMessage(QtGui.QApplication.translate("@default","Error: "), unicode(e), QgsMessageBar.CRITICAL, 5)
        #    self.ui.rbSimpleOverlay.setFocus()
        #    return

        #except WrongActionForPolygon, e:
        #    qgis.utils.iface.messageBar().pushMessage(QtGui.QApplication.translate("@default","Error: "), unicode(e), QgsMessageBar.CRITICAL, 5)
        #    self.ui.rbSimpleOverlay.setFocus()
        #    return

        QtGui.QDialog.accept(self)

 
        
class CellMakerDialog3(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_CellMaker3()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pbRasterFile, QtCore.SIGNAL("clicked()"), self.SetOutputFile)
        
    def SetOutputFile(self):

        saveAscName = QtGui.QFileDialog.getSaveFileName(self, QtGui.QApplication.translate("@default","Choose filename for rasterfile"), QtGui.QApplication.translate("@default","",'ESRI Asc file (*.asc)'))
        if saveAscName != "": self.ui.leRasterFile.setText(saveAscName)
    
    def accept(self):

        class MissingFileName(Exception): pass
       
        if self.ui.rbValues.isChecked():
            self.Vcol = "value"
        else:
            self.Vcol = "overlays"
            
        self.Vcells = self.ui.cbCells.currentText()
        self.Vfilename = self.ui.leRasterFile.text()
        
        try:
            if len(self.Vfilename) == 0:
                raise MissingFileName, (QtGui.QApplication.translate("@default","The raster file name has to be defined"))

        except MissingFileName, e:
            qgis.utils.iface.messageBar().pushMessage(QtGui.QApplication.translate("@default","Error: "), unicode(e), QgsMessageBar.CRITICAL, 5)
            self.ui.leRasterFile.setFocus()
            return

        QtGui.QDialog.accept(self)

class CellMakerDialog4(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_CellMaker4()
        self.ui.setupUi(self)

    
    def accept(self):

        self.Vcells = self.ui.cbCells.currentText()
        self.Vvacuum = self.ui.cbVacuum.isChecked()
        QtGui.QDialog.accept(self)
