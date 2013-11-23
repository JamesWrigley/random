#! /usr/bin/python3
from gi.repository import Gtk

class test_window(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title="GTK3 Grid Container Test")

        window_grid = Gtk.Grid()
        self.add(window_grid)

        buttonA = Gtk.Button(label="This be buttonA")
        buttonB = Gtk.Button(label="This be the second button")
        buttonC = Gtk.Button(label="Button 3")
        buttonD = Gtk.Button(label="Button the fourth")
        buttonE = Gtk.Button(label="Eth button")
        buttonF = Gtk.Button(label="I need to come up with better names")

        window_grid.add(buttonA)
        window_grid.attach(buttonB, 1, 0, 2, 1)
        window_grid.attach_next_to(buttonC, buttonA, Gtk.PositionType.BOTTOM, 1, 2)
        window_grid.attach_next_to(buttonD, buttonC, Gtk.PositionType.RIGHT, 2, 1)
        window_grid.attach(buttonE, 1, 2, 1, 1)
        window_grid.attach_next_to(buttonF, buttonE, Gtk.PositionType.RIGHT, 1, 1)

        
window = test_window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
