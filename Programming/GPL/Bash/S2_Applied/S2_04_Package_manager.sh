
#   Package manager

#T# dpkg and apt commands

#T# get information about a package, like its name, size, description, version, maintainers, bug report, dependencies, homepage
# apt show package1
apt show qt5-quick-demos

#T# install a package or several
# apt install package1 package2 packageN
apt install vlc

#T# uninstall a package or several
# apt remove package1 package2 packageN
apt remove vlc

#T# uninstall and remove configuration files from a package or several
# apt purge package1 package2 packageN
apt purge vlc

#T# check if a package or several are installed
# apt policy package1 package2 packageN
apt policy jfsutils

#T# search for a package with apt search pattern1
apt search jfsuti*

#T# list packages with apt list, use the --upgradable flag to see upgradable packages
apt list --upgradable

#T# see files inside a package with dpkg-query -L package1
dpkg-query -L jfsutils

#T# get the package that installed a given file with dpkg -S file
dpkg -S $(which ls)

#T# get the packages that contain and will install a given file
# apt-file search file
#T# but first update the cache
# apt-file update
apt-file update
apt-file search reiserfsck

#T# set package to be autoremoved
# apt-mark [auto|manual] package1
apt-mark auto jfsutils

#T# see the different versions available for a package with
# aptitude versions packageName
aptitude versions apache2

#T# install the building dependencies to build a program from source code
# apt build-dep program1
apt build-dep vlc

#T# add a package repository
# apt-add-repository repository_name1
apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main'
apt-add-repository ppa:jonathonf/ffmpeg-4

#T# remove a package repository
# apt-add-repository --remove repository_name1
apt-add-repository --remove 'deb http://repos.codelite.org/wx3.1.0/ubuntu/ focal universe'

#T# list the trusted apt keys
apt-key list

#T# see the main architecture supported for running applications
dpkg --print-architecture # amd64

#T# see if i386 programs can be installed, if the output is 'i386'
dpkg --print-foreign-architectures # i386