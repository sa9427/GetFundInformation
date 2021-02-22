# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from model.mainWindows import MainWindows
import sys
from PyQt5.QtWidgets import QApplication

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # 创建一个app，应用
    app = QApplication(sys.argv)

    ui = MainWindows()

    ui.show()

    sys.exit(app.exec())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
