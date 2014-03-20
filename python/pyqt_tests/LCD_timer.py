#! /usr/bin/python3


import sys
import time
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
        timer_start_button = QtGui.QPushButton("Start Timer")

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd_widget)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(numberEntry_widget)
        hbox.addWidget(timer_start_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        self.resize(400, 250)
        self.setWindowTitle("YAT - Yet Another Timer")
        self.show()

    def timer(self, value):
        current_time = round(time.time(), 2)
        end_time = current_time + value

        while current_time <= end_time:
            time.sleep(1)
            self.lcd_widget
            current_time += 1

        return(0)

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
