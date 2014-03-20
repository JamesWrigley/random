#! /usr/bin/python3


import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.center()

    def initUI(self):
        lcd_widget = QtGui.QLCDNumber(self)
        lcd_widget.display("00.00")
        numberEntry_widget = QtGui.QLineEdit(self)
        numberEntry_widget.setInputMask("00.00")

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd_widget)
        vbox.addWidget(numberEntry_widget)

        self.setLayout(vbox)
        
        self.resize(400, 250)
        self.setWindowTitle("Timer")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
