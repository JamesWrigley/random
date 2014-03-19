#! /usr/bin/python3
# A noobish text editor


import os
import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.file_path = ""

        self.initUI()
        
    def initUI(self):
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QtGui.QAction(QtGui.QIcon("/usr/share/icons/oxygen/32x32/actions/application-exit.png"), "&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(self.close)

        saveAction = QtGui.QAction(QtGui.QIcon("/usr/share/icons/oxygen/32x32/actions/document-save.png"), "&Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("Save File")
        saveAction.triggered.connect(lambda: self.saveFile(textEdit.toPlainText()))

        # Make the status bar, tool bar, and menu bar
        self.statusBar()
        self.toolbar = self.addToolBar("Exit")
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")

        # Add items to the toolbar and menus
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(saveAction)
        fileMenu.addAction(exitAction)
        fileMenu.addAction(saveAction)

        # Window drawing options
        self.setWindowTitle("YATE")
        self.resize(600, 400)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def saveFile(self, documentContents):
        save_dialog = lambda: QtGui.QFileDialog.getSaveFileName(self, "Save File", os.path.expanduser("~"))

        if not os.path.isfile(self.file_path): # Check if file exists
            with open(save_dialog(), "w") as file_object:
                file_object.write(documentContents)
                self.file_path = os.path.abspath(file_object.name)
        else:
            with open(self.file_path, "w") as file_object:
                file_object.write(documentContents)

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
