pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'jade_gui')
gnome = import('gnome')

gnome.compile_resources('jade_gui',
  'jade_gui.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'jade_gui.in',
  output: 'jade-gui',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

subdir('widgets')
subdir('functions')
subdir('classes')
subdir('locales')
subdir('utils')
subdir('scripts')
subdir('presets')

jade_gui_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'keymaps.py',
  'manualpartitioning.py'
]

install_data(jade_gui_sources, install_dir: moduledir)
