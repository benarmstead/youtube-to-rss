"GTK program to take a youtube channel URL and convert it to the channels youtube RSS feed link."

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import get_rss_link as get_link

class MainWindow(Gtk.Window):
    "Main and only window for the program"
    def __init__(self):
        "Initialises display"
        super().__init__()
        self.display()

    def display(self):
        "Sets up the display to take an input and output the RSS URL"

        #Sets some defaults for window
        self.set_icon_from_file("icon.png")
        self.set_default_size(615, 100)
        self.set_border_width(5)

        #Creates list box to put elements in
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)

        #Sets title
        self.set_title("Youtube --> RSS")

        #Header message
        self.message = Gtk.Label()
        self.message.set_markup("<b>Youtube --> RSS</b>\n\nEnter the channel link below, which you wish to generate the RSS link for.")
        self.message.set_line_wrap(True)

        #Gets channel link from user
        entry = Gtk.Entry()
        entry.connect("activate", self.print_link)

        #Sets up label for RSS link
        self.print_rss = Gtk.Label()

        #Adds all items to display
        self.add(listbox)
        listbox.add(self.message)
        listbox.add(entry)
        listbox.add(self.print_rss)

        self.connect("destroy", Gtk.main_quit)


    def print_link(self, link):
        "Prints the generated RSS link to the screen"
        #Converts the link and prints it
        link = get_link.convert_link(link.get_text())
        self.print_rss.set_markup("<a href=\"" + link + "\"" + "title=\"RSS Link\">" + link + "</a>")
        self.print_rss.set_selectable(True)
        self.print_rss.set_line_wrap(True)

#Initialises window

def __init__():
    "Creates the MainWindow and starts the program"
    win = MainWindow()
    win.show_all()
    Gtk.main()

__init__()
