#! /usr/bin/python3
from gi.repository import Gtk, GObject
import hashlib

class WindowMain(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Self Text Entry Test")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)

        hbox = Gtk.Box()
        vbox.pack_start(hbox, True, True, 0)

        self.label = Gtk.Label(label="Enter text to be hashed: ")
        hbox.pack_start(self.label, True, True, 10)

        self.text_entry_widget = Gtk.Entry()
        self.text_entry_widget.connect("activate", self.hash_text)
        hbox.pack_start(self.text_entry_widget, True, True, 0)

        self.hash_button = Gtk.Button(label="Hash Text")
        self.hash_button.props.halign = Gtk.Align.END
        self.hash_button.set_size_request(150, 25)
        self.hash_button.connect("clicked", self.hash_text)
        vbox.pack_start(self.hash_button, False, False, 3)

    def hash_text(self, unknown):
        text_enc = self.text_entry_widget.get_text().encode()
        m = hashlib.sha256()
        m.update(text_enc)
        print(m.hexdigest())

main_window = WindowMain()
main_window.connect("delete-event", Gtk.main_quit)
main_window.show_all()
Gtk.main()
