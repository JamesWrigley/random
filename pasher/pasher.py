#! /usr/bin/python3
# A program that hashes files and strings with a user specified cryptographic hash
# (I know, stupid name...)

from gi.repository import Gtk, Gdk, Pango
import hashlib

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Pasher - File and String Hashing")
        self.set_size_request(350, 200)
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)

        main_label = Gtk.Label(label="Pasher")
        main_label.modify_font(Pango.FontDescription("Inconsolata 40"))
        vbox.pack_start(main_label, False, True, 30)

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
        select_object_menu.connect("changed", change_object, select_object_menu, self)
        hbox.pack_start(select_object_menu, True, False, 2)

        self.string_entry_box = Gtk.Entry()
        self.string_entry_box.connect("activate", hasher, self.string_entry_box, self)
        hbox.pack_start(self.string_entry_box, True, True, 0)

        hbox = Gtk.Box()
        vbox.pack_start(hbox, False, True, 2)

        self.hash_button = Gtk.Button(label="Hash")
        self.hash_button.connect("clicked", hasher, self.string_entry_box, self)
        hbox.pack_end(self.hash_button, False, False, 0)

        self.file_button = Gtk.Button(label="Open File")
        self.file_button.connect("clicked", choose_file, self)
        self.file_button.set_sensitive(False)
        hbox.pack_end(self.file_button, False, False, 0)

        algo_menu_hbox = Gtk.Box()
        vbox.pack_start(algo_menu_hbox, False, False, 0)

        # Menu for the user to select the hash algorithm
        object_types = []
        for i in hashlib.algorithms_available:
            object_types.append([i])
        listmodel = Gtk.ListStore(str)
        for i in range(len(object_types)):
            listmodel.append(object_types[i])
        select_object_menu = Gtk.ComboBox(model=listmodel)
        object_menu_cell = Gtk.CellRendererText()
        select_object_menu.pack_start(object_menu_cell, False)
        select_object_menu.add_attribute(object_menu_cell, "text", 0)
        select_object_menu.set_active(0)
        select_object_menu.connect("changed", hasher, self.string_entry_box, select_object_menu, self)
        algo_menu_hbox.pack_start(select_object_menu, False, False, 2)
        

current_object_type = "String/Text"

def copy_to_clipboard(self, button, hashed_text):
    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD).set_text(hashed_text, -1)

def change_object(self, combo, window_instance):
    tree_iter = combo.get_active_iter()
    model = combo.get_model()
    current_object_type = model.get_value(tree_iter, 0)
    
    if current_object_type == "File":
        window_instance.string_entry_box.set_text("")
        window_instance.string_entry_box.set_editable(False)
        window_instance.file_button.set_sensitive(True)
    else:
        window_instance.string_entry_box.set_editable(True)
        window_instance.file_button.set_sensitive(False)

def choose_file(button, window_instance):
    dialog = Gtk.FileChooserDialog("Please choose a file", window_instance, Gtk.FileChooserAction.OPEN,
                                   (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                   Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        window_instance.string_entry_box.set_text(dialog.get_filename())

    dialog.destroy()

def hasher(entry_box, combo, window_instance):
    text = entry_box.get_text()

    tree_iter = combo.get_active_iter()
    model = combo.get_model()
    hash_algo = model.get_value(tree_iter, 0)

    if current_object_type == "File":
        blocksize = 65536
        hash_algo = model.get_value(tree_iter, 0).hashlib.sha1()

        with open(file_path, 'rb') as file:
            buffer = file.read(blocksize)
            while len(buffer) > 0:
                hash_algo.update(buffer)
                buffer = file.read(blocksize)
        hashed_text = hash_algo.hexdigest()
    elif current_object_type =="String/Text":
        hashed_text = hashlib.sha1(text.encode()).hexdigest()

    if len(text) > 40:
        text = "..." + text[-37:]
    
    dialog = Gtk.Dialog()
    dialog.set_size_request(400, 100)
    dialog.set_title("Hash Result")
    dialog.set_transient_for(window_instance)
    dialog.set_modal(True)
    dialog.add_button("Copy to clipboard", Gtk.ResponseType.YES)
    dialog.connect("response", copy_to_clipboard, hashed_text)
    dialog_content_area = dialog.get_content_area()
    dialog_content_area_label = Gtk.Label(label="Hash of " + '"' + text + '"' + ":")
    dialog_content_area.add(dialog_content_area_label)
    hashed_text_label = Gtk.Label(label=hashed_text)
    dialog_content_area.pack_start(hashed_text_label, True, True, 0)
    dialog.show_all()



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
