#! /usr/bin/python3
from gi.repository import Gtk, GObject
import hashlib

class WindowMain(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Self Text Entry Test")

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(hbox)

        self.label = Gtk.Label(label="Enter text to be hashed: ")
        hbox.pack_start(self.label, True, True, 10)

        self.text_entry_widget = Gtk.Entry()
        hbox.pack_start(self.text_entry_widget, True, True, 0)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        self.get_text_button = Gtk.Button(label="Hash")
        self.get_text_button.connect("clicked", self.hash_text(self.text_entry_widget.get_text))
        vbox.pack_start(self.get_text_button, True, True, 0)

    def hash_text(self, text):
        print(hashlib.sha256(text.encode()).hexdigest())

main_window = WindowMain()
main_window.connect("delete-event", Gtk.main_quit)
main_window.show_all()
Gtk.main()
