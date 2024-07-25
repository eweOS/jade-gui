# extrapkg.py

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

from gi.repository import Gtk, GLib, Adw
from gettext import gettext as _


@Gtk.Template(resource_path="/moe/ewe/os/jadegui/widgets/extrapkgentry.ui")
class ExtraPkgEntry(Adw.ActionRow):
    __gtype_name__ = "ExtraPkgEntry"

    entry = ""
    entry_group = ""
    select_button = Gtk.Template.Child()

    def __init__(self, window, package, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.set_title(package)
        self.entry = package
        self.select_button.connect("toggled", self.toggled_cb)

    def toggled_cb(self, check_button):
        row = check_button.get_ancestor(Adw.ActionRow)
        listbox = row.get_ancestor(Gtk.ListBox)
        listbox.select_row(row)
        if check_button.props.active:
            self.window.extrapkg_screen.selected_package(self, row)
        else:
            self.window.extrapkg_screen.deselected_package(self, row)

@Gtk.Template(resource_path="/moe/ewe/os/jadegui/widgets/extrapkggroup.ui")
class ExtraPkgGroup(Adw.PreferencesGroup):
    __gtype_name__ = "ExtraPkgGroup"

    list_packages = Gtk.Template.Child()

    def __init__(self, window, title, subtitle, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.set_title(title)
        self.set_description(subtitle)