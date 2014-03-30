#! /usr/bin/python3

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()


    def initUI(self):
        vbox = QtGui.QVBoxLayout()

        self.button = QtGui.QPushButton("Dialog", self)
        self.button.clicked.connect(self.showDialog)

        self.text_edit = QtGui.QTextEdit(self)

        vbox.addWidget(self.button)
        vbox.addWidget(self.text_edit)

        self.setLayout(vbox)
        self.resize(400, 300)
        self.setWindowTitle("Colors!")
        self.center()
        self.show()


    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, "Input Dialog", "Enter your name:")

        if ok:
            self.line_edit.setText(text)


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
