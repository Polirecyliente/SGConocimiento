
#   Package manager

#T# dpkg and apt commands

#T# install a package with apt install package1
apt install package1

#T# uninstall a package with apt remove package1
apt remove package1

#T# uninstall and remove configuration files with apt purge package1
apt purge package1

#T# check if a package is installed with apt policy package1
apt policy jfsutils

#T# search for a package with apt search packagePatternText
apt search jfsuti*

#T# list packages with apt list, use the --upgradable flag to see upgradable packages
apt list --upgradable

#T# see files inside a package with dpkg-query -L package1
dpkg-query -L jfsutils

#T# get the package that installed a given file with dpkg -S file
dpkg -S $(which ls)

#T# get the packages that contain and will install a given file with
# apt-file search file
#T# but first update the cache with
# apt-file update
apt-file update
apt-file search reiserfsck

#T# set package to be autoremoved with
# apt-mark [auto|manual] package1
apt-mark auto jfsutils

#T# see the different versions available for a package with
# aptitude versions packageName
aptitude versions apache2