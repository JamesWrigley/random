#! /usr/bin/python3
from gi.repository import Gtk

class box_window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="GTK3 Box Container Test")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.hello_button = Gtk.Button(label="Button No.1, Hello")
        self.hello_button.connect("clicked", self.on_hello_button_clicked)
        self.box.pack_start(self.hello_button, True, True, 0)

        self.farewell_button = Gtk.Button(label='Say bye')
        self.farewell_button.connect("clicked", self.on_farewell_button_clicked)
        self.box.pack_start(self.farewell_button, True, True, 0)

    def on_hello_button_clicked(self, widget):
        print("'lo there")

    def on_farewell_button_clicked(self, widget):
        print("Adieu, farewell")

window = box_window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
