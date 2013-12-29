# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cellmaker1.ui'
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

class Ui_CellMaker1(object):
    def setupUi(self, CellMaker1):
        CellMaker1.setObjectName(_fromUtf8("CellMaker1"))
        CellMaker1.resize(456, 181)
        CellMaker1.setModal(False)
        self.buttonBox = QtGui.QDialogButtonBox(CellMaker1)
        self.buttonBox.setGeometry(QtCore.QRect(270, 140, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.dsbYmin = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbYmin.setGeometry(QtCore.QRect(80, 80, 121, 22))
        self.dsbYmin.setMaximum(10000000.0)
        self.dsbYmin.setSingleStep(100.0)
        self.dsbYmin.setObjectName(_fromUtf8("dsbYmin"))
        self.label_7 = QtGui.QLabel(CellMaker1)
        self.label_7.setGeometry(QtCore.QRect(250, 110, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_3 = QtGui.QLabel(CellMaker1)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.leCellName = QtGui.QLineEdit(CellMaker1)
        self.leCellName.setGeometry(QtCore.QRect(80, 20, 281, 20))
        self.leCellName.setObjectName(_fromUtf8("leCellName"))
        self.label = QtGui.QLabel(CellMaker1)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.dsbYmax = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbYmax.setGeometry(QtCore.QRect(320, 80, 121, 22))
        self.dsbYmax.setMaximum(10000000.0)
        self.dsbYmax.setSingleStep(100.0)
        self.dsbYmax.setObjectName(_fromUtf8("dsbYmax"))
        self.label_2 = QtGui.QLabel(CellMaker1)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dsbSize = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbSize.setGeometry(QtCore.QRect(80, 110, 121, 22))
        self.dsbSize.setMinimum(100.0)
        self.dsbSize.setMaximum(100000.0)
        self.dsbSize.setSingleStep(100.0)
        self.dsbSize.setProperty(_fromUtf8("value"), 1000.0)
        self.dsbSize.setObjectName(_fromUtf8("dsbSize"))
        self.label_4 = QtGui.QLabel(CellMaker1)
        self.label_4.setGeometry(QtCore.QRect(250, 80, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(CellMaker1)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.dsbXmax = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbXmax.setGeometry(QtCore.QRect(320, 50, 121, 22))
        self.dsbXmax.setMaximum(10000000.0)
        self.dsbXmax.setSingleStep(100.0)
        self.dsbXmax.setObjectName(_fromUtf8("dsbXmax"))
        self.label_5 = QtGui.QLabel(CellMaker1)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.dsbXmin = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbXmin.setGeometry(QtCore.QRect(80, 50, 121, 22))
        self.dsbXmin.setMaximum(10000000.0)
        self.dsbXmin.setSingleStep(100.0)
        self.dsbXmin.setObjectName(_fromUtf8("dsbXmin"))
        self.dsbValue = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbValue.setGeometry(QtCore.QRect(320, 110, 121, 22))
        self.dsbValue.setMaximum(10000000.0)
        self.dsbValue.setSingleStep(100.0)
        self.dsbValue.setObjectName(_fromUtf8("dsbValue"))
        self.cbShow = QtGui.QCheckBox(CellMaker1)
        self.cbShow.setGeometry(QtCore.QRect(370, 20, 91, 20))
        self.cbShow.setChecked(True)
        self.cbShow.setObjectName(_fromUtf8("cbShow"))

        self.retranslateUi(CellMaker1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CellMaker1.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CellMaker1.reject)
        QtCore.QMetaObject.connectSlotsByName(CellMaker1)
        CellMaker1.setTabOrder(self.leCellName, self.cbShow)
        CellMaker1.setTabOrder(self.cbShow, self.dsbXmin)
        CellMaker1.setTabOrder(self.dsbXmin, self.dsbXmax)
        CellMaker1.setTabOrder(self.dsbXmax, self.dsbYmin)
        CellMaker1.setTabOrder(self.dsbYmin, self.dsbYmax)
        CellMaker1.setTabOrder(self.dsbYmax, self.dsbSize)
        CellMaker1.setTabOrder(self.dsbSize, self.dsbValue)
        CellMaker1.setTabOrder(self.dsbValue, self.buttonBox)

    def retranslateUi(self, CellMaker1):
        CellMaker1.setWindowTitle(QtGui.QApplication.translate("CellMaker1", "Create cells", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("CellMaker1", "Initial value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CellMaker1", "X maximum", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CellMaker1", "Cell layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CellMaker1", "X minimum", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CellMaker1", "Y maximum", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("CellMaker1", "Celle size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CellMaker1", "Y minimum", None, QtGui.QApplication.UnicodeUTF8))
        self.cbShow.setText(QtGui.QApplication.translate("CellMaker1", "Show layer", None, QtGui.QApplication.UnicodeUTF8))

