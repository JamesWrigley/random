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

        game_options_vbox = QtGui.QVBoxLayout()
        game_options_hbox = QtGui.QHBoxLayout()


        ### Stylesheet for the mod QGroupBox's ###
        mods_stylesheet = "QGroupBox {border: 2px solid gray; font-family: Inconsolata; font-size: 21px; margin-top: .5em;} QGroupBox::title {subcontrol-origin: margin; subcontrol-position: top center; padding:0 10px;}"


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
        cam_mod_gbox = QtGui.QGroupBox("Campaign Mods")
        cam_mod_gbox.setStyleSheet(mods_stylesheet)
        cam_mod_gbox.setLayout(cam_mods_vbox)

        # Global mod widgets
        install_global_mod_button = QtGui.QPushButton("Install Global Mod")
        run_global_mod_button = QtGui.QPushButton("Run Global Mod")
        global_mod_gbox = QtGui.QGroupBox("Global Mods")
        global_mod_gbox.setStyleSheet(mods_stylesheet)
        global_mod_gbox.setLayout(global_mods_vbox)

        # Game options
        fullscreen_rb = QtGui.QRadioButton("Fullscreen")
        windowed_rb = QtGui.QRadioButton("Windowed")
        shadows_on_rb = QtGui.QRadioButton("Shadows On")
        shadows_off_rb = QtGui.QRadioButton("Shadows Off")
        shaders_on_rb = QtGui.QRadioButton("Shaders On")
        shaders_off_rb = QtGui.QRadioButton("Shaders Off")

        windowing_button_group = QtGui.QButtonGroup(game_options_hbox)
        shadows_button_group = QtGui.QButtonGroup(game_options_hbox)
        shaders_button_group = QtGui.QButtonGroup(game_options_hbox)

        windowing_button_group.addButton(fullscreen_rb)
        windowing_button_group.addButton(windowed_rb)
        shadows_button_group.addButton(shadows_on_rb)
        shadows_button_group.addButton(shadows_off_rb)
        shaders_button_group.addButton(shaders_on_rb)
        shaders_button_group.addButton(shaders_off_rb)

        game_options_gbox = QtGui.QGroupBox("Game Options")
        game_options_gbox.setStyleSheet(mods_stylesheet)
        game_options_gbox.setLayout(game_options_hbox)


        ### Pack everything ###

        # Pack mod buttons into their vbox's
        map_mods_vbox.insertSpacing(0, 10)
        map_mods_vbox.addWidget(install_map_mod_button)
        map_mods_vbox.addWidget(run_map_mod_button)

        cam_mods_vbox.insertSpacing(0, 10)
        cam_mods_vbox.addWidget(install_cam_mod_button)
        cam_mods_vbox.addWidget(run_cam_mod_button)
        
        global_mods_vbox.insertSpacing(0, 10)
        global_mods_vbox.addWidget(install_global_mod_button)
        global_mods_vbox.addWidget(run_global_mod_button)

        # Pack game options radio buttons
        game_options_hbox.addWidget(fullscreen_rb)
        game_options_hbox.addWidget(windowed_rb)
        game_options_hbox.addWidget(shadows_on_rb)
        game_options_hbox.addWidget(shadows_off_rb)
        game_options_hbox.addWidget(shaders_on_rb)
        game_options_hbox.addWidget(shaders_off_rb)

        # Pack group boxes into the main 'mods_hbox'
        mods_hbox.addWidget(map_mod_gbox)
        mods_hbox.addWidget(cam_mod_gbox)
        mods_hbox.addWidget(global_mod_gbox)

        # Pack everything into 'main_vbox'
        main_vbox.addWidget(header_image_label)
        main_vbox.addLayout(mods_hbox)
        main_vbox.insertSpacing(2, 50)
        main_vbox.addWidget(game_options_gbox)
        main_vbox.addStretch()


        self.setLayout(main_vbox)
        self.setWindowTitle("Warzone 2100 Mood Loader")
        self.resize(800, 600)
        self.center()
        self.show()