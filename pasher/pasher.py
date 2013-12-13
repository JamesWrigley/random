#! /usr/bin/python3
# A program that hashes files and strings with a user specified cryptographic hash

from gi.repository import Gtk, Pango
import hashlib

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Pasher - File and String Hashing")
        self.set_size_request(350, 350)
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)

        label = Gtk.Label(label="Pasher")
        label.modify_font(Pango.FontDescription("Inconsolata 40"))
        vbox.pack_start(label, False, True, 30)

        hbox = Gtk.Box()
        vbox.pack_start(hbox, False, True, 0)

        object_type_label = Gtk.Label(label="Object type: ")
        hbox.pack_start(object_type_label, True, False, 0)

        # Menu for the user to select the object type
        object_types = [["String/Text"], ["File"]]
        listmodel = Gtk.ListStore(str)
        for i in range(len(object_types)):
            listmodel.append(object_types[i])
        select_object_menu = Gtk.ComboBox(model=listmodel)
        object_menu_cell = Gtk.CellRendererText()
        select_object_menu.pack_start(object_menu_cell, False)
        select_object_menu.add_attribute(object_menu_cell, "text", 0)
        select_object_menu.set_active(0)
        select_object_menu.connect("changed", methods.change_object)
        hbox.pack_start(select_object_menu, True, False, 0)

        string_entry_box = Gtk.Entry()
        string_entry_box.connect("activate", methods.hash_string, string_entry_box.get_text())
        hbox.pack_start(string_entry_box, True, True, 10)

class methods():
    '''
    Method definitions for pasher
    '''

    def change_object(self):
        print("Changed")

    def hash_string(self, text):
        hash_object = hashlib.sha1(text.encode()).hexdigest()
        print(hash_object)
        
'''        dialog = Gtk.Dialog()
        dialog.set_title("Hash Result")
        dialog.set_transient_for(MainWindow())
        dialog.set_modal(True)
        dialog.add_button(button_text="Copy", response_id=Gtk.ResponseType.OK)
        dialog.connect("response", quit())
        dialog_content_area = dialog.get_content_area()
        dialog_content_area_label = Gtk.Label("This is a dialog label")
        dialog_content_area.add(dialog_content_area_label)
        dialog.show_all()
'''

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
