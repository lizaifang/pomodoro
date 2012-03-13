#!/usr/bin/python
import gtk
import gobject
import pynotify

class StatusIcon:
    def __init__(self):
        self.statusicon = gtk.StatusIcon()
        #self.statusicon.set_from_stock(gtk.STOCK_HOME)
        self.statusicon.set_from_file('tomato.png')
        self.statusicon.connect("popup-menu", self.right_click_event)
        self.statusicon.connect("activate", self.show_about_dialog)
        tag = gobject.timeout_add(5000, self.show_time)
        #gobject.source_remove(tag)

    def show_time(self):
        cur_time = gobject.get_current_time()
        print(cur_time)

    def right_click_event(self, icon, button, time):
        menu = gtk.Menu()

        about = gtk.MenuItem("About")
        quit = gtk.MenuItem("Quit")
        about.connect("activate", self.show_about_dialog)
        quit.connect("activate", gtk.main_quit)
        menu.append(about)
        menu.append(quit)
        menu.show_all()
        menu.popup(None, None, gtk.status_icon_position_menu, button, time, self.statusicon)
        
    def show_about_dialog(self, widget):
        about_dialog = gtk.AboutDialog()

        about_dialog.set_destroy_with_parent(True)
        about_dialog.set_name("StatusIcon Example")
        about_dialog.set_version("1.0")
        about_dialog.set_authors(["Andrew Steele"])
        about_dialog.run()
        about_dialog.destroy()

if __name__ == '__main__':
    StatusIcon()
    gtk.main()
