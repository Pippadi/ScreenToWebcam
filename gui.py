#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from screentowebcam import ScreenToWebcam

s2w = ScreenToWebcam()

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Screen to Webcam")
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        self.startStopBtn = Gtk.ToggleButton()
        self.startStopBtn.connect("clicked", self.toggleRunning)
        self.box.pack_start(self.startStopBtn, True, True, 0)

        self.textLabel = Gtk.Label(label="")
        self.box.pack_end(self.textLabel, True, True, 10)

        self.setWidgetText()

    def toggleRunning(self, button):
        print("Clicked")
        if s2w.isRunning():
            s2w.stop()
            self.textLabel.set_label("Unable to remove ScreenToWebcam device. Close any program that may be using it and try again.")
        else:
            s2w.start()
        self.setWidgetText()

    def setWidgetText(self):
        if s2w.isRunning():
            self.startStopBtn.set_label("Stop")
            self.startStopBtn.set_active(True)
        else:
            self.startStopBtn.set_label("Start")
            self.textLabel.set_label("")
            self.startStopBtn.set_active(False)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()