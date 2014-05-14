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
        mods_labels_hbox = QtGui.QHBoxLayout()

        map_mods_vbox = QtGui.QVBoxLayout()
        cam_mods_vbox = QtGui.QVBoxLayout()
        global_mods_vbox = QtGui.QVBoxLayout()


        ### Make all the widgets ###
        header_image = QtGui.QPixmap("addons-header-bg"+ choice(str(123)) + ".gif")
        header_image_label = QtGui.QLabel()
        header_image_label.setPixmap(header_image)

        # Map mod widgets
        map_mod_label = QtGui.QLabel("Map Mods")
        install_map_mod_button = QtGui.QPushButton("Install Map Mod")
        map_mod_frame = QtGui.QFrame()
        map_mod_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        map_mod_frame.setLayout(map_mods_vbox)

        # Campaign mod widgets
        cam_mod_label = QtGui.QLabel("Campaign Mods")
        install_cam_mod_button = QtGui.QPushButton("Install Campaign Mod")
        cam_mod_frame = QtGui.QFrame()
        cam_mod_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        cam_mod_frame.setLayout(cam_mods_vbox)

        # Global mod widgets
        global_mod_label = QtGui.QLabel("Global Mods")
        install_global_mod_button = QtGui.QPushButton("Install Global Mod")
        global_mod_frame = QtGui.QFrame()
        global_mod_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        global_mod_frame.setLayout(global_mods_vbox)


        ### Pack everything ###
        mods_labels_hbox.addWidget(map_mod_label)
        mods_labels_hbox.addWidget(cam_mod_label)
        mods_labels_hbox.addWidget(global_mod_label)

        map_mods_vbox.addWidget(install_map_mod_button)
        cam_mods_vbox.addWidget(install_cam_mod_button)
        global_mods_vbox.addWidget(install_global_mod_button)

        mods_hbox.addWidget(map_mod_frame)
        mods_hbox.addWidget(cam_mod_frame)
        mods_hbox.addWidget(global_mod_frame)

        main_vbox.addWidget(header_image_label)
        main_vbox.addLayout(mods_labels_hbox)
        main_vbox.addLayout(mods_hbox)
        main_vbox.addStretch()


        self.setLayout(main_vbox)
        self.setWindowTitle("Mood Loader")
        self.resize(800, 600)
        self.center()
        self.show()
