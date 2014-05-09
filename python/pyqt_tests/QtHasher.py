#! /usr/bin/python3

"""
QtHasher

A program that outputs a cryptographic hash given input from the user.
Input can be plaintext or a file.
"""

import sys
import hashlib
from os.path import expanduser
from PyQt4 import QtGui, QtCore



class dialog_box(QtGui.QDialog):
    def __init__(self, parent=None):
        super(dialog_box, self).__init__(parent)

    def show_dialog(self, hash_value):
        dialog_window = QtGui.QMessageBox()
        dialog_window.setText(hash_value)
        ret = dialog_window.exec_()


class MainWindow(QtGui.QWidget):
    # Declare some class variables, their names should make their purpose clear
    algo_list = {"MD5":hashlib.md5, "SHA-1":hashlib.sha1, "SHA-224":hashlib.sha224,
                 "SHA-256":hashlib.sha256, "SHA-384":hashlib.sha384, "SHA-512":hashlib.sha512}
    hasher_call = hashlib.sha1
    title_font = QtGui.QFont("Inconsolata", 40)
    is_objType_string = True


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
            self.hasher_call()


    def change_object_type(self):
        """
        Changes the 'is_objType_string' bool when called
        """
        if self.object_type_comboBox.currentText() == "String/Text":
            is_objType_string = True
            self.lineEdit_input.setText("")
            self.lineEdit_input.setReadOnly(False)
            self.open_file_button.setEnabled(False)
        elif self.object_type_comboBox.currentText() == "File":
            is_objType_string = False
            self.lineEdit_input.setText("")
            self.lineEdit_input.setReadOnly(True)
            self.open_file_button.setEnabled(True)


    def hasher_call(self):
        """
        This calls hasher() with the users input and displays it in a dialog box.
        Not quite finished.
        """
        hash_value = hasher(self.lineEdit_input.text(),
                            self.algo_list[self.algos_comboBox.currentText()],
                            self.is_objType_string)

        hash_dialog = dialog_box()
        hash_dialog.show_dialog(hash_value)


    def initUI(self):
        # Widgets, sorted by order of appearance
        title_label = QtGui.QLabel("QtHasher")
        object_type_label = QtGui.QLabel("Object type:")
        self.object_type_comboBox = QtGui.QComboBox(self)
        self.lineEdit_input = QtGui.QLineEdit(self)
        self.algos_comboBox = QtGui.QComboBox(self)
        self.open_file_button = QtGui.QPushButton("Open File")
        hash_button = QtGui.QPushButton("Hash")

        # Set title font
        title_label.setFont(self.title_font)

        # Add items to self.algos_comboBox, and set default algorithm to SHA-1
        self.algos_comboBox.addItems(["MD5", "SHA-1", "SHA-224", "SHA-256", "SHA-384", "SHA-512"])
        self.algos_comboBox.setCurrentIndex(1)

        # Add items to self.object_type_comboBox
        self.object_type_comboBox.addItems(["String/Text", "File"])

        # Connect 'hash_button' to 'self.hasher_call'
        hash_button.clicked.connect(self.hasher_call)
        
        # Call 'self.change_object_type' when the combo box is changed
        QtCore.QObject.connect(self.object_type_comboBox, QtCore.SIGNAL("activated(int)"), self.change_object_type)

        # Set the QLineEdit widget to display the return of an open file dialog,
        # and visually disable the open file button
        self.open_file_button.clicked.connect(lambda: self.lineEdit_input.setText(
            QtGui.QFileDialog.getOpenFileName(self, "Open File", expanduser("~"))))
        self.open_file_button.setEnabled(False)

        # Make the layouts
        main_vbox = QtGui.QVBoxLayout()  # Holds all the other layouts
        upper_hbox = QtGui.QHBoxLayout() # Holds lineEdit_input and the hash object combo box
        lower_hbox = QtGui.QHBoxLayout() # Holds the hash button and self.algos_comboBox

        # Packing
        main_vbox.addWidget(title_label, 0, QtCore.Qt.AlignHCenter)
        main_vbox.addSpacing(20)
        upper_hbox.addWidget(object_type_label)
        upper_hbox.addWidget(self.object_type_comboBox)
        upper_hbox.addWidget(self.lineEdit_input)

        lower_hbox.insertStretch(1)
        lower_hbox.addWidget(self.algos_comboBox)
        lower_hbox.addWidget(self.open_file_button)
        lower_hbox.addWidget(hash_button)
        main_vbox.addLayout(upper_hbox)
        main_vbox.addLayout(lower_hbox)


        self.setLayout(main_vbox)
        self.setWindowTitle("QtHasher")
        # Bit of a hack, but setting this size lines up the combo boxes properly
        self.resize(375, 220)
        self.center()
        self.show()



def hasher(text, algorithm, is_object_string):
    """
    Returns the hash of the users input. 'object_type' is the index of the
    'self.algos_comboBox', so if it's 0 then the type is string, and if it's 1 it's
    a file.
    """

    # The actual hashing step
    if is_object_string:
        hash_value = algorithm(text.encode()).hexdigest()
        return hash_value
    elif not is_object_string:
        blocksize = 65536
        algorithm_instance = algorithm()

        with open(text, 'rb') as file_object:
            buffer = file_object.read(blocksize)
            while len(buffer) > 0:
                algorithm_instance.update(buffer)
                buffer = file_object.read(blocksize)
        hash_value = algorithm_instance.hexdigest()
        return hash_value




# Code to actually start the program
app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
