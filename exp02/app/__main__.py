import sys
import serial

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal

from .ui_mainwindow import Ui_MainWindow

class SerialHandler(QThread):
    sig_1 = pyqtSignal(str)
    
    def __init__(self):
        super(SerialHandler, self).__init__()
        self.ser = serial.Serial()
        self.ser.port = 'COM26'
        self.ser.baudrate = 38400
        self.ser.timeout = 0.1

    def run(self):
        self.ser.open()
        while(self.ser.isOpen()):
            data = self.ser.readline().decode()
            if len(data) != 0:
                self.sig_1.emit(data)
    
    def close(self):
        self.terminate()
        self.ser.close()
        print('COM PORT Closed.')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.ser_open)
        self.pushButton_2.clicked.connect(self.ser_close)
        
        self.serHandler = SerialHandler()
        self.serHandler.sig_1.connect(self.append_str)

    def ser_open(self):
        self.textBrowser.append('open serial')
        self.serHandler.start()

    def ser_close(self):
        self.textBrowser.append('close serial')
        self.serHandler.close()
    
    def append_str(self, data):
        self.textBrowser.append(data.strip('\r\n'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())