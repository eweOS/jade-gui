# extrapkg_screen.py

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

from gi.repository import Gtk, Adw
from jade_gui.classes.jade_screen import JadeScreen


@Gtk.Template(resource_path="/moe/ewe/os/jadegui/pages/extrapkg_screen.ui")
class ExtraPkgScreen(JadeScreen, Adw.Bin):
    __gtype_name__ = "ExtraPkgScreen"

    list_package_groups = Gtk.Template.Child()
    chosen_packages= []

    move_to_summary = False

    def __init__(self, window, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.set_valid(True)

    def selected_package(self, widget, row):
        if row is not None:
            if not row.entry in self.chosen_packages:
                self.chosen_packages.append(row.entry)
        else:
            print("extrapkg row is none!")

    def deselected_package(self, widget, row):
        if row is not None:
            if row.entry in self.chosen_packages:
                self.chosen_packages.remove(row.entry)
        else:
            print("extrapkg row is none!")