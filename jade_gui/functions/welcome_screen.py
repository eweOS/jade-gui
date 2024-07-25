# welcome_screen.py

#
# Copyright 2022 user

#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
import urllib.request
from gi.repository import Gtk, GLib, Adw
from gettext import gettext as _
from jade_gui.classes.jade_screen import JadeScreen


@Gtk.Template(resource_path="/moe/ewe/os/jadegui/pages/welcome_screen.ui")
class WelcomeScreen(JadeScreen, Adw.Bin):
    __gtype_name__ = "WelcomeScreen"

    next_button = Gtk.Template.Child()
    no_internet = Gtk.Template.Child()

    def __init__(self, window, next_page, online, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.next_page = next_page
        self.online = online

        self.set_valid(True)

        self.next_button.connect("clicked", next_page)

        self.do_check_internet = True

    def check_internet(self):
        max_tries = 10
        while self.do_check_internet and max_tries > 0:
            try:
                urllib.request.urlopen("https://ping.archlinux.org", timeout=1)
                self.online()
                if not self.next_button.get_sensitive():
                    GLib.idle_add(self.allow_continue, True)

                self.do_check_internet = False
            except:
                max_tries = max_tries - 1
                GLib.idle_add(self.allow_continue, False)
            time.sleep(1)

    def allow_continue(self, allow: bool):
        #still allows installation
        self.set_valid(True)
        #self.next_button.set_sensitive(allow)
        if allow:
            self.next_button.add_css_class("suggested-action")
        else:
            self.next_button.remove_css_class("suggested-action")
        self.no_internet.set_visible(not allow)
        self.next_button.set_visible(True)
