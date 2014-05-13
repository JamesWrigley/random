from random import choice
from PyQt4 import QtGui

class MoodLoader(QtGui.QWidget):
    """
    This class contains the GUI for MoodLoader, it's meant to be imported
    and subclassed from a starter file. Note that the starter file must
    implement an '__init__()' method.
    """
    def center(self):
        """
        A little function to center the program window
        """
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def initUI(self):
        ### Make all the layouts ###
        main_vbox = QtGui.QVBoxLayout()
        mods_hbox = QtGui.QHBoxLayout()


        ### Make all the widgets ###
        header_image = QtGui.QPixmap("addons-header-bg"+ choice(str(123)) + ".gif")
        header_image_label = QtGui.QLabel()
        header_image_label.setPixmap(header_image)

        # Settings widgets
        install_mapMod_button = QtGui.QPushButton("Install Map Mod")

        map_mod_frame = QtGui.QFrame(self)
        map_mod_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        map_mod_frame.setLayout(mods_hbox)


        ### Pack everything ###
        mods_hbox.addWidget(install_mapMod_button)
        mods_hbox.addStretch()

        main_vbox.addWidget(header_image_label)
        main_vbox.addWidget(map_mod_frame)
        main_vbox.addStretch()


        self.setLayout(main_vbox)
        self.setWindowTitle("Mood Loader")
        self.resize(800, 600)
        self.center()
        self.show()
