#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from screentowebcam import ScreenToWebcam

s2w = ScreenToWebcam()

class resEntry(Gtk.Entry):
    def __init__(self, text):
        Gtk.Entry.__init__(self)
        self.set_width_chars(6)
        self.set_text(text)

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Screen to Webcam")
        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.set_border_width(10)

        self.inputLabel = Gtk.Label(label="Dimensions to capture")
        self.inputLabel.set_justify(Gtk.Justification.LEFT)
        self.grid.attach(self.inputLabel, 1, 1, 3, 1)

        self.heightInput = resEntry("1920")
        self.grid.attach_next_to(self.heightInput, self.inputLabel, Gtk.PositionType.BOTTOM, 1, 1)

        self.xlabel = Gtk.Label()
        self.xlabel.set_markup(" <big>×</big> ")
        self.grid.attach_next_to(self.xlabel, self.heightInput, Gtk.PositionType.RIGHT, 1, 1)

        self.widthInput = resEntry("1080")
        self.grid.attach_next_to(self.widthInput, self.xlabel, Gtk.PositionType.RIGHT, 1, 1)

        self.textLabel = Gtk.Label(label="")
        self.textLabel.set_justify(Gtk.Justification.FILL)
        self.grid.attach(self.textLabel, 1, 3, 3, 1)

        self.startStopBtn = Gtk.ToggleButton()
        self.startStopBtn.connect("toggled", self.toggleRunning)
        self.grid.attach(self.startStopBtn, 3, 4, 1, 1)

        self.mirrorBtn = Gtk.CheckButton(label="Mirror")
        self.grid.attach(self.mirrorBtn, 1, 4, 1, 1)

        self.settingsWidgets = [self.heightInput, self.widthInput, self.mirrorBtn]
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
            self.setSettingsWidgetsEnabled(False)
        else:
            self.startStopBtn.set_label("Start")
            self.textLabel.set_label("")
            self.setSettingsWidgetsEnabled(True)
    
    def setSettingsWidgetsEnabled(self, enabled):
        for sw in self.settingsWidgets:
            sw.set_sensitive(enabled)

    def heightAndWidthOkay(self):
        if (not self.heightInput.get_text().isnumeric()) or (not self.widthInput.get_text().isnumeric()):
            self.textLabel.set_label("The given dimensions to grab are not valid. Please enter valid ones.")
            return False
        else:
            self.textLabel.set_label("")
            return True

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()