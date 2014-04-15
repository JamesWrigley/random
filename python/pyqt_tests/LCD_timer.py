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
        timer_start_button.clicked.connect(lambda: self.restart_timer(numberEntry_widget.text()))
        self.qtimer = QtCore.QTimer(self)
        self.qtimer.timeout.connect(lambda: self.update_lcd(self.length_of_time))

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


    def restart_timer(self, value):
        try:
            # In case the user enters letters or something
            self.length_of_time = round(float(value), 0)
        except ValueError:
            QtGui.QMessageBox.warning(self, "Error", "Please enter numbers only")
            return(1)

        self.lcd_widget.display(self.length_of_time)

        # Reset the timer and the lcd
        self.qtimer.stop()
        # Restart the timer
        self.qtimer.start(1000)


    def update_lcd(self, value):
        self.length_of_time -= 1

        if self.length_of_time >= 0:
            self.lcd_widget.display(self.length_of_time)
        else:
            self.qtimer.stop()


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
