#! /usr/bin/python3


import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.center()

    def initUI(self):
        names = ["Cls", "Bck", "", "Close", "7", "8", "9", "/", "4", "5", "6",
                 "*", "1", "2", "3", "-", "0", ".", "=", "+"]

        grid = QtGui.QGridLayout()

        j = 0
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
               (1, 0), (1, 1), (1, 2), (1, 3),
               (2, 0), (2, 1), (2, 2), (2, 3),
               (3, 0), (3, 1), (3, 2), (3, 3),
               (4, 0), (4, 1), (4, 2), (4, 3)]

        for i in names:
            button = QtGui.QPushButton(i)
            if j == 2:
                grid.addWidget(QtGui.QLabel(""), 0, 2)
                j += 1
            else:
                grid.addWidget(button, pos[j][0], pos[j][1])
                j += 1

        self.setLayout(grid)

        self.resize(400, 250)
        self.setWindowTitle("YAGT - Yet Another Grid Test")
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
