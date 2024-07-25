pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
presetsdir = join_paths(pkgdatadir, 'jade_gui/presets')

jade_gui_sources = [
    '__init__.py',
    'desktops.py',
    'packages.py'
]
install_data(jade_gui_sources, install_dir: presetsdir)
