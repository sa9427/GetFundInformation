from ui.miniWindowsUI import Ui_Dialog

from PyQt5.QtWidgets import QApplication, QLabel, QHBoxLayout, QMainWindow, QPushButton, QWidget, QDialog


class MiniWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MiniWindow, self).__init__(parent)
        self.setupUi(self)

        self.btnSwitchWindow.clicked.connect(self.SwitchWindow)

        #窗体创建flag
        self.mainWindowFlag = False

    def SetFatherWindow(self, father):
        self.mainWindow = father

    def SwitchWindow(self):
        self.hide()
        # if not self.mainWindowFlag:
        #     from model.mainWindows import MainWindows
        #     self.mainWindow = MainWindows()
        #     self.mainWindowFlag = True
        self.mainWindow.show()