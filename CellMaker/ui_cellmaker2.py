# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cellmaker2.ui'
#
# Created: Wed Dec 25 10:00:25 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CellMaker2(object):
    def setupUi(self, CellMaker2):
        CellMaker2.setObjectName(_fromUtf8("CellMaker2"))
        CellMaker2.resize(456, 180)
        self.buttonBox = QtGui.QDialogButtonBox(CellMaker2)
        self.buttonBox.setGeometry(QtCore.QRect(100, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.cbCells = QtGui.QComboBox(CellMaker2)
        self.cbCells.setGeometry(QtCore.QRect(80, 20, 361, 22))
        self.cbCells.setObjectName(_fromUtf8("cbCells"))
        self.label_9 = QtGui.QLabel(CellMaker2)
        self.label_9.setGeometry(QtCore.QRect(250, 80, 51, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.dsbFactor = QtGui.QDoubleSpinBox(CellMaker2)
        self.dsbFactor.setGeometry(QtCore.QRect(320, 80, 121, 22))
        self.dsbFactor.setMinimum(-999999.0)
        self.dsbFactor.setMaximum(999999.0)
        self.dsbFactor.setProperty(_fromUtf8("value"), 1.0)
        self.dsbFactor.setObjectName(_fromUtf8("dsbFactor"))
        self.label_11 = QtGui.QLabel(CellMaker2)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.cbOverlays = QtGui.QComboBox(CellMaker2)
        self.cbOverlays.setGeometry(QtCore.QRect(80, 50, 361, 22))
        self.cbOverlays.setObjectName(_fromUtf8("cbOverlays"))
        self.label_12 = QtGui.QLabel(CellMaker2)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gbOverlay = QtGui.QGroupBox(CellMaker2)
        self.gbOverlay.setGeometry(QtCore.QRect(80, 80, 151, 91))
        self.gbOverlay.setObjectName(_fromUtf8("gbOverlay"))
        self.rbSimpleOverlay = QtGui.QRadioButton(self.gbOverlay)
        self.rbSimpleOverlay.setGeometry(QtCore.QRect(20, 20, 91, 18))
        self.rbSimpleOverlay.setChecked(True)
        self.rbSimpleOverlay.setObjectName(_fromUtf8("rbSimpleOverlay"))
        self.rbLineOverlay = QtGui.QRadioButton(self.gbOverlay)
        self.rbLineOverlay.setGeometry(QtCore.QRect(20, 40, 82, 18))
        self.rbLineOverlay.setObjectName(_fromUtf8("rbLineOverlay"))
        self.rbAreaOverlay = QtGui.QRadioButton(self.gbOverlay)
        self.rbAreaOverlay.setGeometry(QtCore.QRect(20, 60, 82, 18))
        self.rbAreaOverlay.setObjectName(_fromUtf8("rbAreaOverlay"))

        self.retranslateUi(CellMaker2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CellMaker2.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CellMaker2.reject)
        QtCore.QMetaObject.connectSlotsByName(CellMaker2)

    def retranslateUi(self, CellMaker2):
        CellMaker2.setWindowTitle(QtGui.QApplication.translate("CellMaker2", "Overlay cells with layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("CellMaker2", "Factor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("CellMaker2", "Cell layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("CellMaker2", "Overlay layer", None, QtGui.QApplication.UnicodeUTF8))
        self.gbOverlay.setTitle(QtGui.QApplication.translate("CellMaker2", "Overlay type", None, QtGui.QApplication.UnicodeUTF8))
        self.rbSimpleOverlay.setText(QtGui.QApplication.translate("CellMaker2", "Simple overlay", None, QtGui.QApplication.UnicodeUTF8))
        self.rbLineOverlay.setText(QtGui.QApplication.translate("CellMaker2", "Line overlay", None, QtGui.QApplication.UnicodeUTF8))
        self.rbAreaOverlay.setText(QtGui.QApplication.translate("CellMaker2", "Area overlay", None, QtGui.QApplication.UnicodeUTF8))

