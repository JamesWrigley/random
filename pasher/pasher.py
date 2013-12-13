#! /usr/bin/python3
# A program that hashes files and strings with a user specified cryptographic hash

from gi.repository import Gtk, Pango
from gi.repository import Gio

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Pasher - File and String Hashing")
        self.set_size_request(350, 350)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)

        label = Gtk.Label(label="Pasher")
        label.modify_font(Pango.FontDescription("Inconsolata 40"))
        vbox.pack_start(label, False, True, 30)

        hbox = Gtk.Box()
        vbox.pack_start(hbox, False, True, 0)

        object_choice_menu_button = Gtk.MenuButton()
        object_choice_menu_button.set_size_request(20, 15)
        hbox.pack_start(object_choice_menu_button, False, True, 20)

        object_choice_menu = Gio.Menu()
        object_choice_menu.append("New", "app.new")

        object_choice_menu_button.set_menu_model(object_choice_menu)

#        object_choice = Gtk.Label(label="Choose object type to hash: ")
#        hbox.pack_start(object_choice, True, True, 20)
#
#        object_choice_action_group = Gtk.ActionGroup("choice_actions")
#        self.add(object_choice_action_group)
#
#        uimanager = self.create_ui_manager()
#        uimanager.insert_action_group(object_choice_action_group)



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
