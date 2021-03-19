from PyQt5.QtGui import QFont, QColor, QBrush

from ui.myselfSelectFundWindowsUI import Ui_Dialog

from PyQt5.QtWidgets import QApplication, QLabel, QHBoxLayout, QMainWindow, QPushButton, QWidget, QDialog, \
    QAbstractItemView, QTableWidgetItem, QTableWidget

from PyQt5.QtCore import QTimer
from PyQt5 import sip

from tool.Fund import Fund
from tool.MyselfSelectFund import MyselfSelectFund


class MyselfSelectFundWindows(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyselfSelectFundWindows, self).__init__(parent)
        self.setupUi(self)
        self.timer = QTimer(self)

        self.btnSwitchWindow.clicked.connect(self.SwitchWindow)
        self.btnRefresh.clicked.connect(self.refresh)
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000 * 60 * 5)  # 5分钟一刷新

        self.miniWindowFlag = False

    def SwitchWindow(self):
        self.hide()

        if not self.miniWindowFlag:
            from model.miniWindow import MiniWindow
            self.miniWindow = MiniWindow()
            self.miniWindowFlag = True
            self.miniWindow.SetFatherWindow(self)

        self.miniWindow.show()

    def SetFatherWindow(self, father):
        self.mainWindow = father

    def CreateTable(self):
        fund = Fund()
        myselfSelectFund = MyselfSelectFund()

        myselfSelectFundDict = myselfSelectFund.GetMyselfSelectFundDict()

        funds = list()

        while (not funds) or (funds and (not funds[0])):
            for fundCode in myselfSelectFundDict:
                fundCurrentInformation = fund.GetFundCurrentInformation(fundCode)
                if '错误' not in fundCurrentInformation:
                    funds.append(fundCurrentInformation)

        self.tabFundDetail.setRowCount(len(funds))
        self.tabFundDetail.setColumnCount(len(funds[0]))
        self.tabFundDetail.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabFundDetail.setHorizontalHeaderLabels(list(funds[0].keys()))
        # self.tabFundDetail.resizeRowToContents(0)

        for row, fundInformation in enumerate(funds):
            # font = QFont()
            rate = float(fundInformation['涨跌幅'])
            fontColor = QColor()
            if rate > 0:
                fontColor.setNamedColor('red')
            elif rate < 0:
                fontColor.setNamedColor('green')
            else:
                fontColor.setNamedColor('black')
            for col, value in enumerate(fundInformation.values()):
                item = QTableWidgetItem(value)
                item.setForeground(QBrush(fontColor))
                self.tabFundDetail.setItem(row, col, item)

    def refresh(self):
        self.gridLayout.removeWidget(self.tabFundDetail)
        sip.delete(self.tabFundDetail)

        self.tabFundDetail = QTableWidget()
        self.CreateTable()
        self.gridLayout.addWidget(self.tabFundDetail)
