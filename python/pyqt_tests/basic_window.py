#! /usr/bin/python3

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()
        
    def initUI(self):
        exitAction = QtGui.QAction(QtGui.QIcon("exit.png"), "&Exit", self)
        exitAction.setShortcut("Ctrl + Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar().showMessage("Ready")

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

        self.setWindowTitle("A Noob's Window")
        self.resize(300, 150)
        self.center()
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


if __name__ == '__main__':
    main()
