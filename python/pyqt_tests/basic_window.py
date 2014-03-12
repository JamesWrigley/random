#! /usr/bin/python3

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        button = QtGui.QPushButton("Quit", self)
        button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        button.setToolTip("Quit Program")
        button.resize(button.sizeHint())
        button.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("A Noob's Window")

        self.show()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, "Message", "Are you sure you wish to quit?",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            print("Bye")
            event.accept()
        else:
            event.ignore()

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
