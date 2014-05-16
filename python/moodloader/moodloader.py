#! /usr/bin/python3

import os
import sys
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
        matching_dirs = []
        matching_dirs = [directory for directory in os.listdir(os.path.expanduser("~")) if ".warzone2100-" in directory]

        if len(matching_dirs) == 1:
            return(os.path.expanduser("~") + "/" + matching_dirs[0])
        else:
            # Else we find the latest version number and append it to the base name
            dir_versions = [float(re.findall(r'\d+\.\d+', foo)[0]) for directory in matching_dirs]
            return(os.path.expanduser("~") + ".warzone2100-" + str(max(dir_versions)))


    def __init__(self):
        ### Create some system variables ###
        config_dir = self.get_config_path()

        super(MoodLoader, self).__init__()
        self.initUI()


def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
