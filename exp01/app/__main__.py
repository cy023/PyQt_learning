import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from app.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_1.clicked.connect(self.btn1fun)
        self.pushButton_2.clicked.connect(self.btn2fun)
        # 按鍵在qtcreator內編號可能不同，請先確認，並於此處修改

    def btn1fun(self):
        self.textBrowser.append('push botton 1')

    def btn2fun(self):
        self.textBrowser.append('push botton 2')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())