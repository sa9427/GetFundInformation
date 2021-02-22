# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'miniWindowsUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(489, 62)
        self.btnSwitchWindow = QtWidgets.QPushButton(Dialog)
        self.btnSwitchWindow.setGeometry(QtCore.QRect(400, 20, 75, 23))
        self.btnSwitchWindow.setObjectName("btnSwitchWindow")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnSwitchWindow.setText(_translate("Dialog", "切换窗口"))

