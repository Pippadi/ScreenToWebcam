#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from screentowebcam import ScreenToWebcam

s2w = ScreenToWebcam()

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Screen to Webcam")
        self.set_default_size(200, 100)
        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.set_border_width(10)

        self.inputLabel = Gtk.Label(label="Dimensions of screen to capture")
        self.inputLabel.set_justify(Gtk.Justification.RIGHT)
        self.grid.add(self.inputLabel)

        self.heightInput = Gtk.Entry()
        self.heightInput.set_text("1920")
        self.grid.attach_next_to(self.heightInput, self.inputLabel, Gtk.PositionType.BOTTOM, 1, 1)

        self.xlabel = Gtk.Label()
        self.xlabel.set_markup(" <big>×</big> ")
        self.grid.attach_next_to(self.xlabel, self.heightInput, Gtk.PositionType.RIGHT, 1, 1)

        self.widthInput = Gtk.Entry()
        self.widthInput.set_text("1080")
        self.grid.attach_next_to(self.widthInput, self.xlabel, Gtk.PositionType.RIGHT, 1, 1)

        self.textLabel = Gtk.Label(label="")
        self.textLabel.set_justify(Gtk.Justification.FILL)
        self.grid.attach_next_to(self.textLabel, self.widthInput, Gtk.PositionType.BOTTOM, 3, 1)

        self.startStopBtn = Gtk.ToggleButton()
        self.startStopBtn.connect("toggled", self.toggleRunning)
        self.grid.attach_next_to(self.startStopBtn, self.textLabel, Gtk.PositionType.BOTTOM, 1, 1)

        self.mirrorBtn = Gtk.CheckButton(label="Mirror")
        self.mirrorBtn.connect("toggled", self.alertForRestart)
        self.grid.attach_next_to(self.mirrorBtn, self.startStopBtn, Gtk.PositionType.LEFT, 1, 1)

        self.setWidgetStates()

    def toggleRunning(self, button):
        print("Clicked")
        if not self.heightAndWidthOkay():
            return
        if s2w.isRunning():
            s2w.stop()
            self.textLabel.set_label("Unable to remove ScreenToWebcam device.\nClose any program that may be using it and try again.")
        else:
            s2w.start(self.heightInput.get_text(), self.widthInput.get_text(), self.mirrorBtn.get_active())
        self.setWidgetStates()

    def setWidgetStates(self):
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
        if (not self.heightInput.get_text().isnumeric()) or (not self.widthInput.get_text().isnumeric()):
            self.textLabel.set_label("The given dimensions to grab are not valid. Please enter valid ones.")
            return False
        else:
            self.textLabel.set_label("")
            return True
    
    def alertForRestart(self, widget):
        if s2w.isRunning():
            self.textLabel.set_label("Stop and start ScreenToWebcam to apply changes.")

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()