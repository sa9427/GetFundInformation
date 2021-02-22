from ui.fundDetailWindowsUI import Ui_Dialog

from PyQt5.QtWidgets import QApplication, QLabel, QHBoxLayout, QMainWindow, QPushButton, QWidget, QDialog, \
    QAbstractItemView, QTableWidgetItem

from tool.Fund import Fund
from tool.MyselfSelectFund import MyselfSelectFund

class FundDetailWindows(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(FundDetailWindows, self).__init__(parent)
        self.setupUi(self)

        self.btnAddSelection.clicked.connect(self.AddMyselfSelectFund)

    def SetFatherWindow(self, father):
        self.mainWindow = father

    def CreateTable(self, fundCode, fundName):
        self.fundCode = fundCode
        self.fundName = fundName

        fund = Fund()
        fundCurrentInformation = fund.GetFundCurrentInformation(self.fundCode)

        self.tabFundDetail.setRowCount(1)
        self.tabFundDetail.setColumnCount(len(fundCurrentInformation))
        self.tabFundDetail.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabFundDetail.setHorizontalHeaderLabels(list(fundCurrentInformation.keys()))
        # self.tabFundDetail.resizeRowToContents(0)

        for col, value in enumerate(fundCurrentInformation.values()):
            item = QTableWidgetItem(value)
            self.tabFundDetail.setItem(0, col, item)

    def AddMyselfSelectFund(self):
        myselfSelectFund = MyselfSelectFund()
        myselfSelectFund.AddMyselfSelectFund(self.fundCode, self.fundName)