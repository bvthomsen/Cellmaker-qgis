# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cellmaker3.ui'
#
# Created: Sun Dec 29 11:25:30 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CellMaker3(object):
    def setupUi(self, CellMaker3):
        CellMaker3.setObjectName(_fromUtf8("CellMaker3"))
        CellMaker3.setEnabled(True)
        CellMaker3.resize(456, 180)
        self.buttonBox = QtGui.QDialogButtonBox(CellMaker3)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(270, 140, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.cbCells = QtGui.QComboBox(CellMaker3)
        self.cbCells.setGeometry(QtCore.QRect(80, 20, 361, 22))
        self.cbCells.setObjectName(_fromUtf8("cbCells"))
        self.label_11 = QtGui.QLabel(CellMaker3)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(CellMaker3)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.leRasterFile = QtGui.QLineEdit(CellMaker3)
        self.leRasterFile.setGeometry(QtCore.QRect(80, 50, 281, 20))
        self.leRasterFile.setObjectName(_fromUtf8("leRasterFile"))
        self.pbRasterFile = QtGui.QPushButton(CellMaker3)
        self.pbRasterFile.setGeometry(QtCore.QRect(370, 50, 71, 23))
        self.pbRasterFile.setObjectName(_fromUtf8("pbRasterFile"))
        self.gbOverlay = QtGui.QGroupBox(CellMaker3)
        self.gbOverlay.setGeometry(QtCore.QRect(80, 70, 361, 51))
        self.gbOverlay.setObjectName(_fromUtf8("gbOverlay"))
        self.rbValues = QtGui.QRadioButton(self.gbOverlay)
        self.rbValues.setGeometry(QtCore.QRect(20, 20, 171, 18))
        self.rbValues.setChecked(True)
        self.rbValues.setObjectName(_fromUtf8("rbValues"))
        self.rbOverlays = QtGui.QRadioButton(self.gbOverlay)
        self.rbOverlays.setGeometry(QtCore.QRect(190, 20, 171, 18))
        self.rbOverlays.setObjectName(_fromUtf8("rbOverlays"))

        self.retranslateUi(CellMaker3)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CellMaker3.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CellMaker3.reject)
        QtCore.QMetaObject.connectSlotsByName(CellMaker3)
        CellMaker3.setTabOrder(self.cbCells, self.leRasterFile)
        CellMaker3.setTabOrder(self.leRasterFile, self.pbRasterFile)
        CellMaker3.setTabOrder(self.pbRasterFile, self.rbValues)
        CellMaker3.setTabOrder(self.rbValues, self.rbOverlays)
        CellMaker3.setTabOrder(self.rbOverlays, self.buttonBox)

    def retranslateUi(self, CellMaker3):
        CellMaker3.setWindowTitle(QtGui.QApplication.translate("CellMaker3", "Save cell layer as raster", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("CellMaker3", "Cell layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("CellMaker3", "Raster file", None, QtGui.QApplication.UnicodeUTF8))
        self.pbRasterFile.setText(QtGui.QApplication.translate("CellMaker3", "Browse..", None, QtGui.QApplication.UnicodeUTF8))
        self.gbOverlay.setTitle(QtGui.QApplication.translate("CellMaker3", "Data values", None, QtGui.QApplication.UnicodeUTF8))
        self.rbValues.setText(QtGui.QApplication.translate("CellMaker3", "Accumulated values", None, QtGui.QApplication.UnicodeUTF8))
        self.rbOverlays.setText(QtGui.QApplication.translate("CellMaker3", "Number of overlay hits", None, QtGui.QApplication.UnicodeUTF8))

