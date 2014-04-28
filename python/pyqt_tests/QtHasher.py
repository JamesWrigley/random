#! /usr/bin/python3

"""
QtHasher

A program that outputs a cryptographic hash given input from the user.
Input can be plaintext or a file.
"""

import sys
import hashlib
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        
    def center(self):
        """
        A little function to center the program window
        """
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def keyPressEvent(self, event):
        """
        Reimplementation of the event handler to hash the input when the return
        key is pressed
        """
        if event.key() == QtCore.Qt.Key_Return:
            hasher(self.lineEdit_input.text())


    def initUI(self):
        # Widgets
        self.lineEdit_input = QtGui.QLineEdit(self)
        hash_button = QtGui.QPushButton("Hash")

        # Make connections
        hash_button.clicked.connect(lambda: hasher(self.lineEdit_input.text()))
        self.connect(self.lineEdit_input, QtCore.SIGNAL("enterPressed"), lambda: hasher(self.lineEdit_input.text()))

        # Make the layouts
        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()

        # Packing
        hbox.addStretch(1)
        hbox.addWidget(hash_button)
        vbox.addWidget(self.lineEdit_input)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle("QtHasher")
        self.center()
        self.show()


hash_algo = hashlib.sha1

def hasher(text):
    """
    Returns the hash
    """
    hashed_text = hash_algo(text.encode()).hexdigest()
    print(hashed_text)


# Code to actually start the program
app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
