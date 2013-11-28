#! /usr/bin/python3
from gi.repository import Gtk, GObject

class WindowMain(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Self Text Entry Test")


