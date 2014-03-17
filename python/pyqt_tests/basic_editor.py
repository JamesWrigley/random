#! /usr/bin/python3

# A noobish text editor

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()
        
    def initUI(self):
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QtGui.QAction(QtGui.QIcon("/usr/share/icons/oxygen/32x32/actions/application-exit.png"), "&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(self.close)

        saveAction = QtGui.QAction(QtGui.QIcon("/usr/share/icons/oxygen/16x16/actions/document-save.png"), "&Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("Save File")
        saveAction.triggered.connect(self.saveFile())

        # Make the status bar, tool bar, and menu bar
        self.statusBar()
        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAction)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

        self.setWindowTitle("A Noob's Window")
        self.resize(500, 300)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def saveFile(self):
        foo # Yes, it isn't finished yet

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
