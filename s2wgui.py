#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from s2wapi import ScreenToWebcam
import subprocess

s2w = ScreenToWebcam()

class ResEntry(Gtk.Entry):
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

        self.resolutions = subprocess.check_output("xrandr | grep '*' | awk '{ print $1 }'", shell=True).decode().split()
        self.resSelector = Gtk.ComboBoxText()
        self.resSelector.set_entry_text_column(0)
        for res in self.resolutions:
            self.resSelector.append_text(res)
        self.resSelector.set_active(0)
        self.grid.attach_next_to(self.resSelector, self.inputLabel, Gtk.PositionType.BOTTOM, 1, 1)

        self.textLabel = Gtk.Label(label="")
        self.textLabel.set_justify(Gtk.Justification.FILL)
        self.grid.attach(self.textLabel, 1, 3, 3, 1)

        self.startStopBtn = Gtk.ToggleButton()
        self.startStopBtn.connect("toggled", self.toggleRunning)
        self.grid.attach(self.startStopBtn, 3, 4, 1, 1)

        self.mirrorBtn = Gtk.CheckButton(label="Mirror")
        self.grid.attach(self.mirrorBtn, 1, 4, 1, 1)

        self.settingsWidgets = [self.resSelector, self.mirrorBtn]
        self.setWidgetStates()

    def toggleRunning(self, button):
        if s2w.isRunning():
            if s2w.isInUse():
                self.textLabel.set_label("Unable to remove ScreenToWebcam device.\nClose any program that may be using it and try again.")
            else:
                s2w.stop()
        else:
            heightWidthList = self.resSelector.get_model()[self.resSelector.get_active_iter()][0].split('x')
            print(heightWidthList)
            s2w.start(heightWidthList[0], heightWidthList[1], self.mirrorBtn.get_active())
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

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()