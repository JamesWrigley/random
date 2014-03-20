#! /usr/bin/python3


import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.center()

    def initUI(self):
        okButton = QtGui.QPushButton("Ok")
        cancelButton = QtGui.QPushButton("Cancel")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.resize(400, 250)
        self.setWindowTitle("YABT - Yet Another Box Test")
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
