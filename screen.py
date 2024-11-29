import dbus
import dbus.mainloop.glib
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

def main():
    loop = GLib.MainLoop()
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    obj = bus.get_object("org.freedesktop.portal.Desktop", "/org/freedesktop/portal/desktop")
    inter = dbus.Interface(obj, "org.freedesktop.portal.Screenshot")
    desktop = inter.Screenshot("", {})

main()
