#! /usr/bin/python3

import sys
import random
from PyQt4 import QtGui

class MoodLoader(QtGui.QWidget):
    def __init__(self):
        super(MoodLoader, self).__init__()
        self.initUI()


    def center(self):
        """
        A little function to center the program window
        """
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def initUI(self):
        # Make all the layouts
        main_vbox = QtGui.QVBoxLayout()

        # Make all the widgets
        header_image = QtGui.QPixmap("addons-header-bg"+ random.choice(str(123)) + ".gif")
        header_image_label = QtGui.QLabel()
        header_image_label.setPixmap(header_image)


        # Pack everything
        main_vbox.addWidget(header_image_label)
        main_vbox.addStretch()


        self.setLayout(main_vbox)
        self.setWindowTitle("Mood Loader")
        self.resize(800, 600)
        self.center()
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    window = MoodLoader()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
