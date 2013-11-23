#! /usr/bin/python3
from gi.repository import Gtk

class LabelWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Label test")

        hbox = Gtk.Box(spacing=10)
        hbox.set_homogenous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogenous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right.set_homogenous(False)

        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        label = Gtk.Label("This here be your average label.")
        vbox_left.pack_start(label, True, True, 0)

        label = Gtk.Label()
        label.set_text("This is a left-justified labelesque \nwith multiple lines.")
        label.set_justify(Gtk.Justification.LEFT)
        vbox_left.pack_start(label, True, True, 0)

        label = Gtk.Label("This is an example of a line-wrapped label. It's "
                          "not allowed to take up the enter width it has, "
                          "but automatically wraps the words to fit.\n"
                          "		Bad spacing here, but it supoorts multiple"
                          "paragraphs correctly and takes the spaces"
                          "verbatim       from the              user.")
        label.set_line_wrap(True)
        vbox_right.pack_start(label, True, True, 0)

        label = Gtk.Label("This is an example of a line-wrapped, filled label. "
                          "It should be taking "
                          "up the entire              width allocated to it.   "
                          "Here be another sentence to prove "
                          "my point. And Yet Another Sentence. "
                          "Laurem cum ipsa."
                          "		This be a new paragraph.\n"
                          "		And here's another, longer, better "
                          "paragraph. I need to come up with better examples "
                          "for these things.")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        vbox_right.pack_start(label, True, True, 0)

        label = Gtk.Label()
        label.set_markup("Text can be <small>small</small>, <big>big</big>, "
                         "<b>bold</b>, <i>in italics</i> and point to places "
                         "places in the <a href=\"vimeo.com/jamesnz\" title=\"Moar info\">internetz</a> as well.")
        label.set_line_wrap(True)
        vbox_left.pack_start(label, True, True, 0)

        label =  Gtk.Label.new_with_mnemonic("_Press Alt + P to select the button "
                                             "to the right")
        vbox_left.pack_start(label, True, True, 0)
        label.set_selectable(True)

        button = Gtk.Button(label="Click at thine own risk")
        label.set_mnemonic_widget(button)
        vbox_right.pack_start(button, True, True, 0)
        
label_window = LabelLabel_windowdow()
label_window.connect("delete-event", Gtk.main_quit)
label_window.show_all()
Gtk.main()
