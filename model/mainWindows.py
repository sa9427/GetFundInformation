from ui.mainWindowsUI import Ui_MainWindow

from PyQt5.QtWidgets import QApplication, QLabel, QHBoxLayout, QMainWindow, QPushButton, QWidget, \
    QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5 import QtCore
from PyQt5 import sip
from tool.FundList import FundList


import pandas as pd
import os


class MainWindows(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

        #信号槽绑定信号
        self.btnOpenKeepMarketWindow.clicked.connect(self.OpenKeepMarketWindow)
        self.actUpdataFund.triggered.connect(self.UpdataFund)
        self.cobFundType.currentIndexChanged.connect(self.SelectFundType)
        self.leditFindFund.textChanged.connect(self.ResearchFund)
        self.fundList = FundList()

        from tool.configCreation import Config
        self.config = Config.GetConfig()
        self.config.sections()
        fundListPath = self.config['data']['fundListPath']

        if not os.path.exists(fundListPath):
            self.fundList.createFundList()

        self.FirstFillFundTable()

        #窗体创建flag
        self.myselfSelectFundWindowsFlag = False


    def OpenKeepMarketWindow(self):
        if not self.myselfSelectFundWindowsFlag:
            from model.myselfSelectFundWindow import MyselfSelectFundWindows
            self.myselfSelectFundWindows = MyselfSelectFundWindows()
            self.myselfSelectFundWindowsFlag = True
            self.myselfSelectFundWindows.SetFatherWindow(self)

        self.myselfSelectFundWindows.CreateTable()
        self.myselfSelectFundWindows.show()

    def UpdataFund(self):
        self.fundList.updataFundList()

    def FirstFillFundTable(self):
        data = self.fundList.getFundListFromType()
        self.cobFundType.addItem('')
        self.cobFundType.addItems(self.fundList.getFundType())
        self.FillFundTable(data)

    def SelectFundType(self):
        type = self.cobFundType.currentText()
        #通过基金类型获取基金列表
        data = self.fundList.getFundListFromType(type)
        self.FillFundTable(data)

    def FillFundTable(self, data):
        #移除现有的table空间，并放入新的table控件
        self.formLayout.removeWidget(self.fundTable)
        sip.delete(self.fundTable)

        self.fundTable = QTableWidget()
        self.fundTable.setRowCount(data.shape[0])
        self.fundTable.setColumnCount(data.shape[1])
        self.fundTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.fundTable.setHorizontalHeaderLabels(self.fundList.getFundListType())

        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                item = QTableWidgetItem(data[row][col])
                self.fundTable.setItem(row, col, item)

        #由于每一次都会重新创建table控件，因此需要重新绑定信号与槽
        self.fundTable.doubleClicked.connect(self.GetFundNameFromTable)
        self.formLayout.addWidget(self.fundTable)

    def GetFundNameFromTable(self, index):
        fundCode = self.fundTable.item(self.fundTable.selectedItems()[0].row(),0).text()
        fundName = self.fundTable.item(self.fundTable.selectedItems()[0].row(),1).text()

        from model.fundDetailWindows import FundDetailWindows
        fundDetailWindow = FundDetailWindows()
        fundDetailWindow.SetFatherWindow(self)
        fundDetailWindow.CreateTable(fundCode, fundName)

        # from model.miniWindow import MiniWindow
        # self.miniWindow = MiniWindow()
        fundDetailWindow.show()
        fundDetailWindow.exec_()

    def ResearchFund(self, text):
        type = self.cobFundType.currentText()
        data = self.fundList.getFundListFromFind(type, text)
        self.FillFundTable(data)
