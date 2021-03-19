# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myselfSelectFundWindowsUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(792, 340)
        self.btnSwitchWindow = QtWidgets.QPushButton(Dialog)
        self.btnSwitchWindow.setGeometry(QtCore.QRect(654, 300, 101, 23))
        self.btnSwitchWindow.setObjectName("btnSwitchWindow")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 771, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabFundDetail = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tabFundDetail.setObjectName("tabFundDetail")
        self.tabFundDetail.setColumnCount(0)
        self.tabFundDetail.setRowCount(0)
        self.gridLayout.addWidget(self.tabFundDetail, 0, 0, 1, 1)
        self.btnRefresh = QtWidgets.QPushButton(Dialog)
        self.btnRefresh.setGeometry(QtCore.QRect(520, 300, 101, 23))
        self.btnRefresh.setObjectName("btnSwitchWindow_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnSwitchWindow.setText(_translate("Dialog", "切换窗口"))
        self.btnRefresh.setText(_translate("Dialog", "刷新基金信息"))

