#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from screentowebcam import ScreenToWebcam

s2w = ScreenToWebcam()

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Screen to Webcam")
        self.set_default_size(300, 200)
        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.startStopBtn = Gtk.ToggleButton()
        self.startStopBtn.connect("toggled", self.toggleRunning)
        self.grid.add(self.startStopBtn)

        self.textLabel = Gtk.Label(label="")
        self.grid.attach_next_to(self.textLabel, self.startStopBtn, Gtk.PositionType.BOTTOM, 1, 3)

        self.heightInput = Gtk.Entry()
        self.heightInput.set_text("1920")
        self.grid.attach_next_to(self.heightInput, self.textLabel, Gtk.PositionType.BOTTOM, 1, 1)

        self.xlabel = Gtk.Label(label='x')
        self.grid.attach_next_to(self.xlabel, self.heightInput, Gtk.PositionType.RIGHT, 1, 1)
        self.widthInput = Gtk.Entry()
        self.widthInput.set_text("1080")
        self.grid.attach_next_to(self.widthInput, self.xlabel, Gtk.PositionType.RIGHT, 1, 1)

        self.setWidgetText()

    def toggleRunning(self, button):
        print("Clicked")
        if not self.heightAndWidthOkay():
            return
        if s2w.isRunning():
            s2w.stop()
            self.textLabel.set_label("Unable to remove ScreenToWebcam device. Close any program that may be using it and try again.")
        else:
            s2w.start(self.heightInput.get_text(), self.widthInput.get_text())
        self.setWidgetText()

    def setWidgetText(self):
        if s2w.isRunning():
            self.startStopBtn.set_label("Stop")
            self.heightInput.set_editable(False)
            self.widthInput.set_editable(False)
        else:
            self.startStopBtn.set_label("Start")
            self.textLabel.set_label("")
            self.heightInput.set_editable(True)
            self.widthInput.set_editable(True)
    
    def heightAndWidthOkay(self):
        if (not self.heightInput.get_text().isnumeric()) or (not self.widthInput.get_text().isnumeric):
            self.textLabel.set_label("The given dimensions to grab are not valid. Please enter valid ones.")
            return False
        else:
            self.textLabel.set_label("")
            return True

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()