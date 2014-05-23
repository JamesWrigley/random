#! /usr/bin/python3

import re
import os
import sys
import shutil
from PyQt4 import QtGui
from moodloader_ui import MoodLoader

class MainWindow(MoodLoader):
    """
    Subclass the GUI for the main window. We implement '__init__()' here, and
    also set up connections for the widgets.
    """

    def get_config_path(self):
        """
        Get the path of the config folder of the latest version of WZ on the
        users computer.
        """
        matching_dir_versions = [float(re.findall(r'\d+\.\d+', directory)[0])
                                 for directory in os.listdir(os.path.expanduser("~"))
                                 if re.match(".warzone2100-\d+\.\d+", directory)]

        if len(matching_dir_versions) >= 1:
            return(os.path.expanduser("~") + "/.warzone2100-" + str(max(matching_dir_versions)))
        else:
            self.statusbar.showMessage("No config folder found!")
            return("")


    def __init__(self):
        ### Create some system variables ###
        self.config_dir = self.get_config_path()


        super(MoodLoader, self).__init__()
        self.initUI()

        ### Set up connections ###
        self.install_map_mod_button.clicked.connect(lambda: self.install_mod("/maps"))
        self.install_cam_mod_button.clicked.connect(lambda: self.install_mod("/campaign"))
        self.install_global_mod_button.clicked.connect(lambda: self.install_mod("/global"))


    def install_mod(self, mod_type):
        """
        Install a map to the /.warzone2100-xx/maps folder.
        Note that even the name of the argument is 'mod_type', it's actually
        the folder name the map is to be installed into (i.e. '/maps' for a map mod).
        """
        mod_path = QtGui.QFileDialog.getOpenFileName(self, "Select Mod", os.path.expanduser("~"), "WZ Mods (*.wz);; All files (*.*)")

        if mod_path and os.path.isdir(mod_path):
            shutil.copy(mod_path, self.config_dir + mod_type)
            self.statusbar.showMessage("Map installed!")
        elif not mod_path:
            return
        elif not os.path.isdir(mod_path):
            os.mkdir(self.config_dir + mod_type)
            self.statusbar.showMessage("Created " + self.config_dir + mod_type + " and installed mod.")


def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
