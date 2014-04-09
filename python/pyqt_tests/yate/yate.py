#! /usr/bin/python3
# A text editor

import os
import sys
from PyQt4 import QtGui
from yate_mainWindow import Ui_MainWindow

class YateWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # For the openFile() method
        self.file_path = ""

        # Connect the actions to their methods
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(lambda: self.saveFile(self.ui.textEdit.toPlainText()))
        self.ui.actionText_Color.triggered.connect(self.changeTextColor)
        self.ui.actionFont.triggered.connect(self.changeFont)


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
            self.ui.textEdit.setText(file_object.read())
            self.file_path = os.path.abspath(file_object.name)


    def changeTextColor(self):
        color = QtGui.QColorDialog.getColor()
        self.ui.textEdit.setStyleSheet("QTextEdit {color:" + color.name() + "}")


    def changeFont(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.ui.textEdit.setStyleSheet("QTextEdit {font:" + str(font.pointSize()) + "pt " + font.family() +"}")


def main():
    app = QtGui.QApplication(sys.argv)
    window = YateWindow()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
