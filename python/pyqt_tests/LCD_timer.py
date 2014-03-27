#! /usr/bin/python3


import sys
import time
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.lcd_widget = QtGui.QLCDNumber(self)
        self.lcd_widget.display(0)
        numberEntry_widget = QtGui.QLineEdit(self)
        numberEntry_widget.setToolTip("Countdown time (in whole seconds, or value will be rounded)")
        timer_start_button = QtGui.QPushButton("Start Timer")
        timer_start_button.clicked.connect(lambda: self.timer(numberEntry_widget.text()))

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.lcd_widget)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(numberEntry_widget)
        hbox.addWidget(timer_start_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        self.resize(400, 250)
        self.setWindowTitle("YAT - Yet Another Timer")
        self.center()
        self.show()


    def timer(self, value):
        try:
            # In case the user enters letters or something
            length_of_time = round(float(value), 0)
        except ValueError:
            QtGui.QMessageBox.warning(self, "Error", "Please enter numbers only")
            return(1)

        self.lcd_widget.display(length_of_time)

        countdown = length_of_time
        qtimer = QtCore.QTimer()
        qtimer.timeout.connect(lambda: self.lcd_widget.display(countdown))

        qtimer.start(5000)
        self.lcd_widget.display("Foo")

        while countdown > 0:
            try:
                countdown -= 1
                print(countdown)
            finally:
                qtimer.start(1000)

        print("Done")


    def update_lcd(self, value):
        self.lcd_widget.display(value)


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
