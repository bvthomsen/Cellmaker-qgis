# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cellmaker1.ui'
#
# Created: Sun May 18 18:46:34 2014
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

class Ui_CellMaker1(object):
    def setupUi(self, CellMaker1):
        CellMaker1.setObjectName(_fromUtf8("CellMaker1"))
        CellMaker1.resize(456, 180)
        CellMaker1.setModal(False)
        self.buttonBox = QtGui.QDialogButtonBox(CellMaker1)
        self.buttonBox.setGeometry(QtCore.QRect(270, 140, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.dsbYmin = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbYmin.setGeometry(QtCore.QRect(80, 80, 141, 22))
        self.dsbYmin.setMaximum(10000000.0)
        self.dsbYmin.setSingleStep(100.0)
        self.dsbYmin.setObjectName(_fromUtf8("dsbYmin"))
        self.label_7 = QtGui.QLabel(CellMaker1)
        self.label_7.setGeometry(QtCore.QRect(230, 110, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_3 = QtGui.QLabel(CellMaker1)
        self.label_3.setGeometry(QtCore.QRect(230, 50, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.leCellName = QtGui.QLineEdit(CellMaker1)
        self.leCellName.setGeometry(QtCore.QRect(80, 20, 281, 20))
        self.leCellName.setObjectName(_fromUtf8("leCellName"))
        self.label = QtGui.QLabel(CellMaker1)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.dsbYmax = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbYmax.setGeometry(QtCore.QRect(300, 80, 141, 22))
        self.dsbYmax.setMaximum(10000000.0)
        self.dsbYmax.setSingleStep(100.0)
        self.dsbYmax.setObjectName(_fromUtf8("dsbYmax"))
        self.label_2 = QtGui.QLabel(CellMaker1)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dsbSizeX = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbSizeX.setGeometry(QtCore.QRect(80, 110, 61, 22))
        self.dsbSizeX.setDecimals(0)
        self.dsbSizeX.setMinimum(1.0)
        self.dsbSizeX.setMaximum(100000.0)
        self.dsbSizeX.setSingleStep(100.0)
        self.dsbSizeX.setProperty("value", 1000.0)
        self.dsbSizeX.setObjectName(_fromUtf8("dsbSizeX"))
        self.label_4 = QtGui.QLabel(CellMaker1)
        self.label_4.setGeometry(QtCore.QRect(230, 80, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(CellMaker1)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.dsbXmax = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbXmax.setGeometry(QtCore.QRect(300, 50, 141, 22))
        self.dsbXmax.setMaximum(10000000.0)
        self.dsbXmax.setSingleStep(100.0)
        self.dsbXmax.setObjectName(_fromUtf8("dsbXmax"))
        self.label_5 = QtGui.QLabel(CellMaker1)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.dsbXmin = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbXmin.setGeometry(QtCore.QRect(80, 50, 141, 22))
        self.dsbXmin.setMaximum(10000000.0)
        self.dsbXmin.setSingleStep(100.0)
        self.dsbXmin.setObjectName(_fromUtf8("dsbXmin"))
        self.dsbValue = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbValue.setGeometry(QtCore.QRect(300, 110, 141, 22))
        self.dsbValue.setMaximum(10000000.0)
        self.dsbValue.setSingleStep(100.0)
        self.dsbValue.setObjectName(_fromUtf8("dsbValue"))
        self.cbShow = QtGui.QCheckBox(CellMaker1)
        self.cbShow.setGeometry(QtCore.QRect(370, 20, 91, 20))
        self.cbShow.setChecked(True)
        self.cbShow.setObjectName(_fromUtf8("cbShow"))
        self.label_8 = QtGui.QLabel(CellMaker1)
        self.label_8.setGeometry(QtCore.QRect(10, 140, 61, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lblProjection = QtGui.QLabel(CellMaker1)
        self.lblProjection.setGeometry(QtCore.QRect(80, 140, 191, 16))
        self.lblProjection.setObjectName(_fromUtf8("lblProjection"))
        self.dsbSizeY = QtGui.QDoubleSpinBox(CellMaker1)
        self.dsbSizeY.setGeometry(QtCore.QRect(160, 110, 61, 22))
        self.dsbSizeY.setDecimals(0)
        self.dsbSizeY.setMinimum(1.0)
        self.dsbSizeY.setMaximum(100000.0)
        self.dsbSizeY.setSingleStep(100.0)
        self.dsbSizeY.setProperty("value", 1000.0)
        self.dsbSizeY.setObjectName(_fromUtf8("dsbSizeY"))
        self.label_10 = QtGui.QLabel(CellMaker1)
        self.label_10.setGeometry(QtCore.QRect(150, 110, 16, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(CellMaker1)
        self.label_11.setGeometry(QtCore.QRect(70, 110, 16, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.retranslateUi(CellMaker1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CellMaker1.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CellMaker1.reject)
        QtCore.QMetaObject.connectSlotsByName(CellMaker1)
        CellMaker1.setTabOrder(self.leCellName, self.cbShow)
        CellMaker1.setTabOrder(self.cbShow, self.dsbXmin)
        CellMaker1.setTabOrder(self.dsbXmin, self.dsbXmax)
        CellMaker1.setTabOrder(self.dsbXmax, self.dsbYmin)
        CellMaker1.setTabOrder(self.dsbYmin, self.dsbYmax)
        CellMaker1.setTabOrder(self.dsbYmax, self.dsbSizeX)
        CellMaker1.setTabOrder(self.dsbSizeX, self.dsbValue)
        CellMaker1.setTabOrder(self.dsbValue, self.buttonBox)

    def retranslateUi(self, CellMaker1):
        CellMaker1.setWindowTitle(_translate("CellMaker1", "Create cells", None))
        self.label_7.setText(_translate("CellMaker1", "Initial value", None))
        self.label_3.setText(_translate("CellMaker1", "X maximum", None))
        self.label.setText(_translate("CellMaker1", "Cell layer", None))
        self.label_2.setText(_translate("CellMaker1", "X minimum", None))
        self.label_4.setText(_translate("CellMaker1", "Y maximum", None))
        self.label_6.setText(_translate("CellMaker1", "Size (m)", None))
        self.label_5.setText(_translate("CellMaker1", "Y minimum", None))
        self.cbShow.setText(_translate("CellMaker1", "Show layer", None))
        self.label_8.setText(_translate("CellMaker1", "Projection", None))
        self.lblProjection.setText(_translate("CellMaker1", "***", None))
        self.label_10.setText(_translate("CellMaker1", "Y", None))
        self.label_11.setText(_translate("CellMaker1", "X", None))

