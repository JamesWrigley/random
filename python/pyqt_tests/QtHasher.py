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

    algo_list = {"MD5":hashlib.md5, "SHA-1":hashlib.sha1, "SHA-224":hashlib.sha224,
                 "SHA-256":hashlib.sha256, "SHA-384":hashlib.sha384, "SHA-512":hashlib.sha512}
    hash_algo = hashlib.sha1
    title_font = QtGui.QFont("Inconsolata", 40)

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
            self.hash_algo()


    def initUI(self):
        # Widgets
        self.lineEdit_input = QtGui.QLineEdit(self)
        hash_button = QtGui.QPushButton("Hash")
        object_type_comboBox = QtGui.QComboBox(self)
        algos_comboBox = QtGui.QComboBox(self)
        title_label = QtGui.QLabel("QtHasher")

        # Set title font
        title_label.setFont(self.title_font)

        # Add items to algos_comboBox, and set default algorithm to SHA-1
        algos_comboBox.addItems(["MD5", "SHA-1", "SHA-224", "SHA-256", "SHA-384", "SHA-512"])
        algos_comboBox.setCurrentIndex(1)

        # Add items to object_type_comboBox
        object_type_comboBox.addItems(["String/Text", "File"])

        # Connect button to function
        self.hash_algo = lambda: hasher(self.lineEdit_input.text(), self.algo_list[algos_comboBox.currentText()])
        hash_button.clicked.connect(self.hash_algo)

        # Make the layouts
        main_vbox = QtGui.QVBoxLayout()  # Holds all the other layouts
        upper_hbox = QtGui.QHBoxLayout() # Holds lineEdit_input and the hash object combo box
        lower_hbox = QtGui.QHBoxLayout() # Holds the hash button and algos_comboBox

        # Packing
        main_vbox.addWidget(title_label, 0, QtCore.Qt.AlignHCenter)
        main_vbox.addSpacing(20)
        upper_hbox.addWidget(object_type_comboBox)
        upper_hbox.addWidget(self.lineEdit_input)

        lower_hbox.addStretch()
        lower_hbox.addWidget(algos_comboBox)
        lower_hbox.addWidget(hash_button)
        main_vbox.addLayout(upper_hbox)
        main_vbox.addLayout(lower_hbox)


        self.setLayout(main_vbox)
        self.setWindowTitle("QtHasher")
        self.resize(320, 200)
        self.center()
        self.show()



def hasher(text, algorithm):
    """
    Returns the hash of the users input
    """
    hash_value = algorithm(text.encode()).hexdigest()
    print(hash_value)


# Code to actually start the program
app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
