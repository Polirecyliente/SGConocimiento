
#   Sysadmin

#T# Table of contents

#C# Desktop environment
#C# Process management
#C# User and group management
#C# Hardware detection
#C# Devices
#C# System libraries
#C# Fonts
#C# Encodings
#C# Internet
#C# --- Package manager
#C# --- Firewall
#C# Languages
#C# --- Latex
#C# --- Python
#C# File system hierarchy management
#C# --- File compression
#C# Root privileges

#T# Beginning of content

#C# Desktop environment

# |-------------------------------------------------------------
# SYNTAX gsettings [get|set] org.gnome.path.to.settings key1 value1
#T# value1 can be for example [true|false], key1 is the aspect or option being modified

gsettings set org.gnome.shell.extensions.dash-to-dock dock-fixed false
#T# this hides the Gnome dock (i.e. the taskbar with opened programs)
# |-------------------------------------------------------------

#C# Process management

# |-------------------------------------------------------------
#T# get the pid of a process with pidof
# pidof program_name1
pidof firefox

#T# get the pid of a running script with pgrep
# pgrep -f script_name1

#T# get a process status with ps pid
ps 187665

#T# get specific ids of a process with the ps command, use the -o kwarg for the type of id, and the -p kwarg for the pid
#T# ppid: process parent id, pgid: process group id
# ps -o [ppid|pgid] -p pid
ps -o ppid -p 187785
ps -o pgid -p 187785

#T# kill a process with kill pid
kill 187785
#T# see the signals that can be sent to the process with
kill -l
#T# send a particular signal_number with kill -signal_number pid
kill -9 187785
kill -SIGKILL 187785

#T# Process status letters meaning
# D -> Uninterruptible sleep (can't be killed without reboot)
# R -> Running or runnable
# S -> Interruptible sleep
# T -> Stopped process
# Z -> Zombie (terminated, but left open by parent)
# modifiers
# < -> high priority
# N -> low priority
# l -> is multithreaded
# + -> is in the foreground process group
# |-------------------------------------------------------------

#C# User and group management

# |-------------------------------------------------------------
#T# see the groups that the current user belongs to with the groups command
groups jul

#T# append user to an existing group with usermod, reboot may be necessary for this to take effect
# SYNTAX 
usermod -a -G audio jul

#T# list the existing users along with their passwd information
nl /etc/passwd

#T# switch user with the su command
su serveruser

#T# get the current user with the whoami command
whoami # jul
# |-------------------------------------------------------------

#C# Hardware detection

# |-------------------------------------------------------------
#T# list hardware with the lshw command, the option -short gives a summary
lshw -short

#T# list pci devices along with their drivers with the lspci command
lspci -k
#T# the -k flag is to show the kernel drivers and kernel modules

#T# list the kernel modules with their status with the lsmod command
lsmod # output too large

#T# get info about a module with the modinfo command
modinfo bluetooth # output too large
# |-------------------------------------------------------------

#C# System libraries

# |-------------------------------------------------------------
#T# print the cache of installed libraries
ldconfig -p
#T# the -p flag is for printing the cache
# |-------------------------------------------------------------

#C# Devices

# |-------------------------------------------------------------
#T# check mounted devices in the /proc/mounts file
cat /proc/mounts # very large output

#T# list mounted devices with the mount command, using the -l flag
mount -l # very large output

#T# check the file of the current terminal with the tty command
tty # /dev/pts/1

#T# check the terminal emulator with the $TERM variable
echo $TERM # xterm-256color
# |-------------------------------------------------------------

#C# Fonts

# |-------------------------------------------------------------
#T# fonts are stored in /usr/share/fonts/
cd /usr/share/fonts/
# |-------------------------------------------------------------

#C# Encodings

# |-------------------------------------------------------------
#T# get the list of encodings knows by the operating system with the -l flag of the iconv program
iconv -l
# |-------------------------------------------------------------

#C# Internet

# |-------------------------------------------------------------
#T# download a file from the internet with wget, the -c flag is to continue downloading a partially downloaded file
wget -c http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda_11.0.2_450.51.05_linux.run

#C# --- Package manager

# |-----
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

# |--------------------------------------------------\
#T# remove a package repository
# SYNTAX apt-add-repository --remove repository_name1
apt-add-repository --remove 'deb http://repos.codelite.org/wx3.1.0/ubuntu/ focal universe'

# SYNTAX if the former doesn't work, remove the repository directly in the file hierarchy, delete the repository entry in the /etc/apt/sources.list, and the repository file in /etc/apt/sources.list.d
#T# e.g. delete the entry 'deb https://repos.codelite.org/wx3.1.3/ubuntu/ focal universe' in /etc/apt/sources.list, and the file codelite-wx3.1.3.list in /etc/apt/sources.list.d
# |--------------------------------------------------/

#T# list the trusted apt keys
apt-key list

#T# see the main architecture supported for running applications
dpkg --print-architecture # amd64

#T# see if i386 programs can be installed, if the output is 'i386'
dpkg --print-foreign-architectures # i386
# |-----

#C# --- Firewall

# |-----
#T# the ufw program serves to manage the firewall, UFW stands for Uncomplicated Firewall, it acts as a wrapper for iptables
ufw status verbose

#T# enable or disable the firewall
# SYNTAX ufw enable|disable

# |--------------------------------------------------\
#T# firewall rules decide whether or not to allow connections, set the default policies which are the rules that apply when there is no rule defined

# SYNTAX ufw default deny|reject|allow incoming|outgoing
#T# this denies, rejects, or allows, incoming or outgoing connections, unless overruled by an explicit rule

#T# the difference between deny and reject is that reject sends and error message to the connecting agent, while deny just ignores the connection attempt

ufw default deny incoming
ufw default allow outgoing
#T# these are normally the default policies for a firewall
# |--------------------------------------------------/

#T# from now on, the deny, reject, and allow arguments will be used for other commands, but their meaning is the same as with the default policies

# |--------------------------------------------------\
#T# create explicit rules to allow or deny different connections

# SYNTAX ufw deny|reject|allow port1|service_name1
#T# port1 is a port number, service_name1 is a string with a service name, they are interchangeable, their equivalencies are set in the /etc/services file

ufw allow 22
ufw allow ssh
#T# both examples are equivalent
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# create rules with port ranges and protocols

# SYNTAX ufw deny|reject|allow port1:port2/[protocol1]
#T# the port range is from the port1 number to the port2 number, protocol1 is the network protocol, such as tcp, udp, and if it's not written is the same as both tcp and udp

ufw reject 5000:6030/tcp
#T# this rejects all IPs connecting to ports 5000 to 6030 using tcp
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# the IP addresses can follow the Classless Inter Domain Routing style (CIDR numbers), CIDR numbers represent IP ranges

#T# an IPv4 address is made up with four 8 bit numbers, separated by dots, for a total of 32 bits, such as 10110010.11001011.11010001.11101111

# SYNTAX byte1.byte2.byte3.byte4/CIDR_number1
#T# the CIDR_number1 number is the amount of bits that do not change in the IP range, starting at the first bit

IP_RANGE1=192.168.255.0/31
#T# as the CIDR number is 31, the first 31 bits of the IP range remain unchanged, so the resulting IP range only has the last bit, the bit 32, varying
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# create rules about specific IPs

# SYNTAX ufw deny|reject|allow from ip1 to ip2 port port1
#T# ip1, ip2 are IP numbers or IP ranges, this sets a rule for a connection from ip1 to ip2 in port port1

ufw allow from 192.168.0.0/24 to 192.168.0.13 port 443
#T# IPs in the range [192.168.0.0, 192.168.0.255] are allowed to connect in port 443, this host is 192.168.0.13
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# create rules about network interfaces

# SYNTAX ufw deny|reject|allow incoming|outgoing on net1 from ip1
#T# net1 is the network interface protected by the rule, ip1 is the connecting IP number or range

ufw deny incoming on wlp3s0 from 236.217.38.92
#T# this denies connections from the IP 236.217.38.92 to the wireless network interface identified by wlp3s0
# |--------------------------------------------------/

#T# list the available firewall rules by number
ufw status numbered

#T# delete a rule by number
ufw delete 2

#T# reset the firewall rules to default settings
ufw reset
# |-----

# |-------------------------------------------------------------

#C# Languages

# |-------------------------------------------------------------

#C# --- Latex

# |-----
#T# see the paths where latex packages can be installed
kpsepath tex

#T# use the tlmgr command (for texlive manager) to install latex packages
# tlmgr install package1
tlmgr install undertilde
# |-----

#C# --- Python

# |-----
#T# get help and documentation about a module with the pydoc program
# pydoc module1
pydoc itertools

#T# show information about a module with the pip3 program
# pip3 show module1
#T# if it returns nothing the package is not installed
pip3 show alabaster

#T# if the installation of a module gets timeout errors in the download, it may be fixed with the --default-timeout=1000 option
pip3 install --default-timeout=1000 matplotlib
# |-----

# |-------------------------------------------------------------

#C# File system hierarchy management

# |-------------------------------------------------------------
#T# dereference a symbolic link
readlink -f link_file1 # /path/to/original_file1

#T# remove everything but .file with rm !(*.file), this uses pattern matching (see S1_03_Operators.sh)
rm !(*.tex|*.bib)

#T# print numbered from the start in file1 up to line up_to_l, but taking only the last N lines
# head -up_to_l file1 | nl -b 'a' | tail -N
head -80 file1 | nl -b 'a' | tail -10

#T# make a directory
mkdir -p /tmp/parent_dir1/child_dir1
#T# the p flag creates any parent directories needed, if they don't exist

#C# --- File compression

# |-----
#T# tar, zip, and unzip commands

cd ~/PolirecylBases/tutos/Bash/Section2/
#T# create a tar file from file1 with tar cf tarName.tar file1
tar cvvf tarDebug.tar Section2_2.sh
#T# compress to a fileName.zip with zip fileName file1 file2
zip sections Section2_2.sh Section2_3.sh
#T# compress a dir recursively to a zip with the -r flag
zip -r sectionsRecurs dir1/

#T# list the file contents of a tar file with tar tf tarName.tar
tar tf tarDebug.tar
#T# list the contents of a zip file with unzip -l zipFile.zip
unzip -l zipFile.zip

#T# extract the files from a tar file with tar xf tarName.tar
tar xf tarDebug.tar
#T# unzip to a dir with unzip -d newDir file.zip
unzip -d newDir file.zip
#T# untar to a dir with tar xf tarName.tar -C dirName
tar xf tarDebug.tar -C dirName

#T# you can have verbose output adding v to the options, e.g. 
# tar xvf tarName.tar ; tar cvf tarName.tar file1

#T# for tar, a single hyphen - means read from stdin, it's used to decompress a tar in stdin, e.g. 
# xz -cd file.tar.xz | tar xf -
cat tarDebug.tar | tar xf -

#T# extract the files from a gzip file with tar xzf file.tar.gz
tar xzf file.tar.gz

#T# extract the files from a bzip2 file with tar xjf file.tar.bz2
tar xjf file.tar.bz2

#T# decompress a .tar.xz file leaving it as .tar with
xz -d compressed_file1.tar.xz
# |-----

# |-------------------------------------------------------------

#C# Root privileges

# |-------------------------------------------------------------
#T# the sudo command grants root privileges

# SYNTAX sudo -o1 command1
#T# command1 is executed with root privileges, -o1 represents a flag

#T# command1 is optional, the -s flag without command1 starts a shell session with the shell found in the SHELL environment variable, and with root as the user

sudo echo "str1" # str1
sudo -s # starts a shell session with the root user
# |-------------------------------------------------------------