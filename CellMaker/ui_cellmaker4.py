# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cellmaker4.ui'
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
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.cbCells = QtGui.QComboBox(CellMaker4)
        self.cbCells.setGeometry(QtCore.QRect(80, 10, 361, 22))
        self.cbCells.setObjectName(_fromUtf8("cbCells"))
        self.cbVacuum = QtGui.QCheckBox(CellMaker4)
        self.cbVacuum.setGeometry(QtCore.QRect(80, 40, 131, 17))
        self.cbVacuum.setCheckable(True)
        self.cbVacuum.setChecked(False)
        self.cbVacuum.setObjectName(_fromUtf8("cbVacuum"))

        self.retranslateUi(CellMaker4)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CellMaker4.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CellMaker4.reject)
        QtCore.QMetaObject.connectSlotsByName(CellMaker4)
        CellMaker4.setTabOrder(self.cbCells, self.buttonBox)

    def retranslateUi(self, CellMaker4):
        CellMaker4.setWindowTitle(_translate("CellMaker4", "Delete cell layer", None))
        self.label.setText(_translate("CellMaker4", "Cell layer", None))
        self.cbVacuum.setText(_translate("CellMaker4", "VACUUM database", None))

