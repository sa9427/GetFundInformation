# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fundDetailWindowsUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(791, 121)
        self.tabFundDetail = QtWidgets.QTableWidget(Dialog)
        self.tabFundDetail.setGeometry(QtCore.QRect(10, 10, 771, 71))
        self.tabFundDetail.setObjectName("tabFundDetail")
        self.tabFundDetail.setColumnCount(0)
        self.tabFundDetail.setRowCount(0)
        self.btnAddSelection = QtWidgets.QPushButton(Dialog)
        self.btnAddSelection.setGeometry(QtCore.QRect(670, 90, 75, 23))
        self.btnAddSelection.setObjectName("btnAddSelection")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnAddSelection.setText(_translate("Dialog", "添加自选"))

