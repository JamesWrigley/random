#! /usr/bin/python3
# A noobish text editor


import os
import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.file_path = ""

        self.initUI()
        
    def initUI(self):
        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setStyleSheet("QTextEdit {color:#000000}")
        self.setCentralWidget(self.textEdit)

        # File menu actions
        exitAction = QtGui.QAction(QtGui.QIcon("/usr/share/icons/oxygen/32x32/actions/application-exit.png"), "&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(self.close)

        openAction = QtGui.QAction(QtGui.QIcon("/usr/share/icons/oxygen/32x32/actions/document-open.png"), "&Open", self)
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open File")
        openAction.triggered.connect(self.openFile)

        saveAction = QtGui.QAction(QtGui.QIcon("/usr/share/icons/oxygen/32x32/actions/document-save.png"), "&Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("Save File")
        saveAction.triggered.connect(lambda: self.saveFile(self.textEdit.toPlainText()))

        # Edit menu actions
        changeTextColorAction = QtGui.QAction(QtGui.QIcon("/usr/share/icons/oxygen/32x32/actions/format-text-color.png"), "&Text Color", self)
        changeTextColorAction.setStatusTip("Set text color")
        changeTextColorAction.triggered.connect(self.changeTextColor)

        changeFontAction = QtGui.QAction(QtGui.QIcon("/usr/share/icons/oxygen/32x32/actions/character-set.png"), "&Font", self)
        changeFontAction.setStatusTip("Set text font")
        changeFontAction.triggered.connect(self.changeFont)

        # Make the status bar, tool bar, and menu bar
        self.statusBar()
        self.toolbar = self.addToolBar("Exit")
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        editMenu = menubar.addMenu("&Edit")

        # Add items to the toolbar and menus
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(openAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)
        editMenu.addAction(changeTextColorAction)
        editMenu.addAction(changeFontAction)

        # Window drawing options
        self.setWindowTitle("YATE - Yet Another Text Editor™")
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


    def openFile(self):
        open_dialog = lambda: QtGui.QFileDialog.getOpenFileName(self, "Open File", os.path.expanduser("~"))
        with open(open_dialog(), "r") as file_object:
            self.textEdit.setText(file_object.read())
            self.file_path = os.path.abspath(file_object.name)


    def changeTextColor(self):
        color = QtGui.QColorDialog.getColor()
        self.textEdit.setStyleSheet("QTextEdit {color:" + color.name() + "}")


    def changeFont(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.textEdit.setStyleSheet("QTextEdit {font:" + str(font.pointSize()) + "pt " + font.family() +"}")


def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
