#! /usr/bin/python3

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.Qwidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()


    def initUI(self):


def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
