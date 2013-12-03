#! /usr/bin/python3

# A truly disgusting PyGTK button conglomeration, will try and clean this
# up sometime

from gi.repository import Gtk

class HelloWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Button Demo")
        self.set_size_request(250, 250)

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

        hbox = Gtk.Box()
        vbox.pack_start(hbox, True, True, 10)

        label = Gtk.Label(label="Enable the check box?")
        hbox.pack_start(label, True, True, 5)

        self.check_button = Gtk.CheckButton()
        self.check_button.connect("toggled", self.check_button_toggle)
        hbox.pack_start(self.check_button, True, True, 0)

        label = Gtk.Label(label="Select your choice of radio buttons:")
        vbox.pack_start(label, True, True, 0)


        hbox = Gtk.Box()
        vbox.pack_start(hbox, True, True, 0)

        self.radio_button1 = Gtk.RadioButton.new_with_label_from_widget(None, "Button One")
        self.radio_button1.connect("toggled", self.radio_button_toggle, "1")    
        hbox.pack_start(self.radio_button1, False, False, 0)

        self.radio_button2 = Gtk.RadioButton.new_with_label_from_widget(self.radio_button1, "Button Two")
        self.radio_button2.connect("toggled", self.radio_button_toggle, "2")
        hbox.pack_start(self.radio_button2, False, False, 0)

        self.radio_button3 = Gtk.RadioButton.new_with_label_from_widget(self.radio_button1, "Button Three")
        self.radio_button3.connect("toggled", self.radio_button_toggle, "3")
        hbox.pack_start(self.radio_button3, False, False, 0)

        link = Gtk.LinkButton("https://github.com/JamesWrigley", "Bad Code Example")
        vbox.pack_start(link, False, False, 0)

        label = Gtk.Label(label="SpinButton Demonstration")
        vbox.pack_start(label, True, True, 15)

        hbox = Gtk.Box()
        vbox.pack_start(hbox, True, True, 0)

        self.adjustment = Gtk.Adjustment(4, 0, 100, 2, 10, 0)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_adjustment(self.adjustment)
        self.spinbutton.set_digits(2)
        hbox.pack_start(self.spinbutton, True, True, 0)

        self.check_numeric = Gtk.CheckButton("Numeric")
        self.check_numeric.connect("toggled", self.on_numeric_toggled)
        hbox.pack_start(self.check_numeric, True, True, 0)

        self.check_valid = Gtk.CheckButton("If Valid")
        self.check_valid.connect("toggled", self.check_valid_toggled)
        hbox.pack_start(self.check_valid, True, True, 0)


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

    def check_button_toggle(self, button):
        print("Check button is set to" + str(button.get_active()))

    def radio_button_toggle(self, button, name):
        if button.get_active() == True:
            print("Button " + name + " is now active")

    def on_numeric_toggled(self, button):
        self.spinbutton.set_numeric(button.get_active())

    def check_valid_toggled(self, button):
        if button.get_active():
            policy = Gtk.SpinButtonUpdatePolicy.IF_VALID
        else:
            policy = Gtk.SpinButtonUpdatePolicy.ALWAYS
        self.spinbutton.set_update_policy(policy)

        
win = HelloWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
