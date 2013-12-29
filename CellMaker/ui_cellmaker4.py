# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cellmaker4.ui'
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

class Ui_CellMaker4(object):
    def setupUi(self, CellMaker4):
        CellMaker4.setObjectName(_fromUtf8("CellMaker4"))
        CellMaker4.resize(457, 71)
        self.buttonBox = QtGui.QDialogButtonBox(CellMaker4)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(270, 40, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(CellMaker4)
        self.label.setGeometry(QtCore.QRect(0, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.cbCells = QtGui.QComboBox(CellMaker4)
        self.cbCells.setGeometry(QtCore.QRect(80, 10, 361, 22))
        self.cbCells.setObjectName(_fromUtf8("cbCells"))

        self.retranslateUi(CellMaker4)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CellMaker4.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CellMaker4.reject)
        QtCore.QMetaObject.connectSlotsByName(CellMaker4)
        CellMaker4.setTabOrder(self.cbCells, self.buttonBox)

    def retranslateUi(self, CellMaker4):
        CellMaker4.setWindowTitle(QtGui.QApplication.translate("CellMaker4", "Delete cell layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CellMaker4", "Cell layer", None, QtGui.QApplication.UnicodeUTF8))

