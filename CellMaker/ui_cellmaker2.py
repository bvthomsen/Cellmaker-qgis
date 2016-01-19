# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cellmaker2.ui'
#
# Created: Sun May 18 18:46:35 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CellMaker2(object):
    def setupUi(self, CellMaker2):
        CellMaker2.setObjectName(_fromUtf8("CellMaker2"))
        CellMaker2.resize(456, 228)
        self.buttonBox = QtGui.QDialogButtonBox(CellMaker2)
        self.buttonBox.setGeometry(QtCore.QRect(250, 190, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.cbCells = QtGui.QComboBox(CellMaker2)
        self.cbCells.setGeometry(QtCore.QRect(80, 20, 361, 22))
        self.cbCells.setObjectName(_fromUtf8("cbCells"))
        self.label_9 = QtGui.QLabel(CellMaker2)
        self.label_9.setGeometry(QtCore.QRect(250, 140, 71, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.dsbFactor = QtGui.QDoubleSpinBox(CellMaker2)
        self.dsbFactor.setGeometry(QtCore.QRect(320, 140, 121, 22))
        self.dsbFactor.setMinimum(-999999.0)
        self.dsbFactor.setMaximum(999999.0)
        self.dsbFactor.setProperty("value", 1.0)
        self.dsbFactor.setObjectName(_fromUtf8("dsbFactor"))
        self.label_11 = QtGui.QLabel(CellMaker2)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(CellMaker2)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gbOverlay = QtGui.QGroupBox(CellMaker2)
        self.gbOverlay.setGeometry(QtCore.QRect(80, 140, 151, 81))
        self.gbOverlay.setObjectName(_fromUtf8("gbOverlay"))
        self.rbSimpleOverlay = QtGui.QRadioButton(self.gbOverlay)
        self.rbSimpleOverlay.setGeometry(QtCore.QRect(20, 20, 131, 18))
        self.rbSimpleOverlay.setChecked(True)
        self.rbSimpleOverlay.setObjectName(_fromUtf8("rbSimpleOverlay"))
        self.rbLineOverlay = QtGui.QRadioButton(self.gbOverlay)
        self.rbLineOverlay.setGeometry(QtCore.QRect(20, 40, 131, 18))
        self.rbLineOverlay.setObjectName(_fromUtf8("rbLineOverlay"))
        self.rbAreaOverlay = QtGui.QRadioButton(self.gbOverlay)
        self.rbAreaOverlay.setGeometry(QtCore.QRect(20, 60, 131, 18))
        self.rbAreaOverlay.setObjectName(_fromUtf8("rbAreaOverlay"))
        self.lwOverlays = QtGui.QListWidget(CellMaker2)
        self.lwOverlays.setGeometry(QtCore.QRect(80, 50, 361, 81))
        self.lwOverlays.setAlternatingRowColors(True)
        self.lwOverlays.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lwOverlays.setObjectName(_fromUtf8("lwOverlays"))

        self.retranslateUi(CellMaker2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CellMaker2.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CellMaker2.reject)
        QtCore.QMetaObject.connectSlotsByName(CellMaker2)
        CellMaker2.setTabOrder(self.cbCells, self.rbSimpleOverlay)
        CellMaker2.setTabOrder(self.rbSimpleOverlay, self.rbLineOverlay)
        CellMaker2.setTabOrder(self.rbLineOverlay, self.rbAreaOverlay)
        CellMaker2.setTabOrder(self.rbAreaOverlay, self.dsbFactor)
        CellMaker2.setTabOrder(self.dsbFactor, self.buttonBox)

    def retranslateUi(self, CellMaker2):
        CellMaker2.setWindowTitle(_translate("CellMaker2", "Overlay cells with layer", None))
        self.label_9.setText(_translate("CellMaker2", "Factor", None))
        self.label_11.setText(_translate("CellMaker2", "Cell layer", None))
        self.label_12.setText(_translate("CellMaker2", "Overlay layer", None))
        self.gbOverlay.setTitle(_translate("CellMaker2", "Overlay type", None))
        self.rbSimpleOverlay.setText(_translate("CellMaker2", "Simple overlay", None))
        self.rbLineOverlay.setText(_translate("CellMaker2", "Line overlay", None))
        self.rbAreaOverlay.setText(_translate("CellMaker2", "Area overlay", None))

