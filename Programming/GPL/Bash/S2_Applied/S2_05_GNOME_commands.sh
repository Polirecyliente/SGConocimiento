
#   GNOME commands

#T# hide the Gnome dock (i.e. the taskbar with opened programs) with
gsettings set org.gnome.shell.extensions.dash-to-dock dock-fixed false

#T# the general syntax is
# gsettings [get|set] org.gnome.path.to.settings key value
#T# where value can be for example [true|false]