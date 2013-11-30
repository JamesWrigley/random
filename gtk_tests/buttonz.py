#! /usr/bin/python3

# PyGTK button conglomeration

from gi.repository import Gtk

class HelloWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Button Demo")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)

        self.normal_buttons_label = Gtk.Label(label="Normal Buttons Label")
        vbox.pack_start(self.normal_buttons_label, True, True, 5)

        hbox = Gtk.Box()
        vbox.add(hbox)

        self.click_button = Gtk.Button(label="Click Me")
        self.click_button.connect("clicked", self.click_button_clicked)
        hbox.pack_start(self.click_button, True, True, 4)

        self.open_button = Gtk.Button(label="Open")
        self.open_button.connect("clicked", self.open_button_clicked)
        hbox.pack_start(self.open_button, True, True, 4)

        self.close_button = Gtk.Button(label="Close")
        self.close_button.connect("clicked", self.close_button_clicked)
        hbox.pack_start(self.close_button, True, True, 4)

        label = Gtk.Label(label="Toggle Buttons Label")
        vbox.pack_start(label, True, True, 5)

        hbox = Gtk.Box(spacing=5)
        vbox.pack_start(hbox, True, True, 0)

        self.toggle_button1 = Gtk.ToggleButton(label="Button 1")
        self.toggle_button1.set_active(is_active=True)
        self.toggle_button1.connect("toggled", self.toggle_button1_state)
        hbox.pack_start(self.toggle_button1, True, True, 4)

        self.toggle_button2 = Gtk.ToggleButton(label="Button 2")
        self.toggle_button2.set_active(is_active=False)
        self.toggle_button2.connect("toggled", self.toggle_button2_state)
        hbox.pack_start(self.toggle_button2, True, True, 4)

    def click_button_clicked(self, button):
        print("\"Click Me\" button was clicked")

    def open_button_clicked(self, button):
        print("\"Open\" button was clicked")

    def close_button_clicked(self, button):
        print("\"Close\" button was clicked")

    def toggle_button1_state(self, button):
        print("Button 1 is set to " + str(button.get_active()))

    def toggle_button2_state(self, button):
        print("Button 2 is set to " + str(button.get_active()))

        
win = HelloWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
