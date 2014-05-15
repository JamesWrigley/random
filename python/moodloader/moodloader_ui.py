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

        map_mods_vbox = QtGui.QVBoxLayout()
        cam_mods_vbox = QtGui.QVBoxLayout()
        global_mods_vbox = QtGui.QVBoxLayout()

        run_options_hbox = QtGui.QHBoxLayout()


        ### Stylesheets ###
        mods_stylesheet = "QGroupBox {border: 2px solid gray; margin-top: .5em;} QGroupBox::title {subcontrol-origin: margin; subcontrol-position: top center; padding:0 10px;}"


        ### Make all the widgets ###

        # Header image is randomly chosen, 'choice()' is from the random module
        header_image = QtGui.QPixmap("addons-header-bg"+ choice(str(123)) + ".gif")
        header_image_label = QtGui.QLabel()
        header_image_label.setPixmap(header_image)

        # Map mod widgets
        install_map_mod_button = QtGui.QPushButton("Install Map Mod")
        run_map_mod_button = QtGui.QPushButton("Run Map Mod")
        map_mod_gbox = QtGui.QGroupBox("Map Mods")
        map_mod_gbox.setStyleSheet(mods_stylesheet)
        map_mod_gbox.setLayout(map_mods_vbox)

        # Campaign mod widgets
        install_cam_mod_button = QtGui.QPushButton("Install Campaign Mod")
        run_cam_mod_button = QtGui.QPushButton("Run Campaign Mod")
        cam_mod_gbox = QtGui.QFrame()
        cam_mod_gbox.setFrameShape(QtGui.QFrame.StyledPanel)
        cam_mod_gbox.setLayout(cam_mods_vbox)

        # Global mod widgets
        install_global_mod_button = QtGui.QPushButton("Install Global Mod")
        run_global_mod_button = QtGui.QPushButton("Run Global Mod")
        global_mod_gbox = QtGui.QGroupBox("Global Mods")
        global_mod_gbox.setStyleSheet(mods_stylesheet)
        global_mod_gbox.setLayout(global_mods_vbox)

        # Radio buttons for the WZ running options
        fullscreen_rb = QtGui.QRadioButton()
        windowed_rb = QtGui.QRadioButton()
        shadows_on_fb = QtGui.QRadioButton()
        shadows_off_fb = QtGui.QRadioButton()
        shaders_on_rb = QtGui.QRadioButton()
        shadows_off_fb = QtGui.QRadioButton()


        ### Pack everything ###

        # Pack buttons
        map_mods_vbox.addWidget(install_map_mod_button)
        map_mods_vbox.addWidget(run_map_mod_button)
        cam_mods_vbox.addWidget(install_cam_mod_button)
        cam_mods_vbox.addWidget(run_cam_mod_button)
        global_mods_vbox.addWidget(install_global_mod_button)
        global_mods_vbox.addWidget(run_global_mod_button)

        # Pack frames
        mods_hbox.addWidget(map_mod_gbox)
        mods_hbox.addWidget(cam_mod_gbox)
        mods_hbox.addWidget(global_mod_gbox)

        # Pack everything into 'main_vbox'
        main_vbox.addWidget(header_image_label)
        main_vbox.addLayout(mods_hbox)
        main_vbox.addStretch()


        self.setLayout(main_vbox)
        self.setWindowTitle("Warzone 2100 Mood Loader")
        self.resize(800, 600)
        self.center()
        self.show()
