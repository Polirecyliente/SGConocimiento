
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
#C# --- find and xargs commands
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

#T# see the IDs (user ID, group IDs) from a user with the id command
id serveruser # uid=1001(serveruser) gid=1001(serveruser) groups=1001(serveruser),27(sudo),998(bumblebee)

#T# append user to an existing group with usermod, reboot may be necessary for this to take effect

# SYNTAX usermod -o1 -o2 val2 group1 user1
#T# -o1 represents a flag, -o2 val2 represent a kwarg pair, user1 is added to group1

usermod -a -G audio jul #  # the -a flag is to append the user, the -G group1 kwarg pair determines the group in which the user will be appended

#T# list the existing users along with their passwd information
nl /etc/passwd

#T# list the existing groups
nl /etc/group

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
# SYNTAX apt show package1
apt show qt5-quick-demos

#T# install a package or several
# SYNTAX apt install package1 package2 packageN
apt install vlc

#T# uninstall a package or several
# SYNTAX apt remove package1 package2 packageN
apt remove vlc

#T# uninstall and remove configuration files from a package or several
# SYNTAX apt purge package1 package2 packageN
apt purge vlc

#T# simulate the output of apt, to see what would be installed, changed, or uninstalled with the -s flag
apt purge -s vlc

#T# check if a package or several are installed
# SYNTAX apt policy package1 package2 packageN
apt policy jfsutils

#T# search for a package with apt search glob_pattern1
apt search jfsuti*

#T# list packages with apt list, use the --upgradable flag to see upgradable packages, use the --installed flag to see the installed packages
apt list --upgradable

#T# see files inside a package with dpkg-query -L package1
dpkg-query -L jfsutils

#T# get the package that installed a given file with dpkg -S file
dpkg -S $(which ls)

#T# get the packages that contain and will install a given file
# SYNTAX apt-file search file
#T# but first update the cache
# SYNTAX apt-file update
apt-file update
apt-file search reiserfsck

#T# check the dependencies of a package
# SYNTAX apt-rdepends package1
apt-rdepends zerotier-one

#T# check the dependent packages of a package
# SYNTAX apt-rdepends -r package1
apt-rdepends -r dmtracedump

#T# set package to be autoremoved

# SYNTAX apt-mark auto package1
#T# this sets package1 to be removed automatically

# SYNTAX apt-mark manual package1
#T# this sets package1 to be removed manually

apt-mark auto jfsutils

#T# see the different versions available for a package with
# SYNTAX aptitude versions package_name1
aptitude versions apache2

#T# install the building dependencies to build a program from source code
# SYNTAX apt build-dep program1
apt build-dep vlc

#T# add a package repository
# SYNTAX apt-add-repository repository_name1
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

#T# firewall rules decide whether or not to allow connections, set the default policies which are the rules that apply when there is no rule defined

# SYNTAX ufw default deny|reject|allow incoming|outgoing
#T# this denies, rejects, or allows, incoming or outgoing connections, unless overruled by an explicit rule

#T# the difference between deny and reject is that reject sends and error message to the connecting agent, while deny just ignores the connection attempt

ufw default deny incoming
ufw default allow outgoing
#| these are normally the default policies for a firewall

#T# from now on, the deny, reject, and allow arguments will be used for other commands, but their meaning is the same as with the default policies

#T# create explicit rules to allow or deny different connections

# SYNTAX ufw deny|reject|allow port1|service_name1
#T# port1 is a port number, service_name1 is a string with a service name, they are interchangeable, their equivalencies are set in the /etc/services file

ufw allow 22
ufw allow ssh
#T# both examples are equivalent

#T# create rules with port ranges and protocols

# SYNTAX ufw deny|reject|allow port1:port2/[protocol1]
#T# the port range is from the port1 number to the port2 number, protocol1 is the network protocol, such as tcp, udp, and if it's not written is the same as both tcp and udp

ufw reject 5000:6030/tcp
#T# this rejects all IPs connecting to ports 5000 to 6030 using tcp

#T# the IP addresses can follow the Classless Inter Domain Routing style (CIDR numbers), CIDR numbers represent IP ranges

# SYNTAX byte1.byte2.byte3.byte4/CIDR_number1
#T# the CIDR_number1 number is the amount of bits that do not change in the IP range, starting at the first bit

#T# an IPv4 address is made up with four 8 bit numbers, separated by dots, for a total of 32 bits, such as 10110010.11001011.11010001.11101111

IP_RANGE1=192.168.255.0/31 #| as the CIDR number is 31, the first 31 bits of the IP range remain unchanged, so the resulting IP range only has the last bit, the bit 32, varying

#T# create rules about specific IPs

# SYNTAX ufw deny|reject|allow from ip1 to ip2 port port1
#T# ip1, ip2 are IP numbers or IP ranges, this sets a rule for a connection from ip1 to ip2 in port port1

ufw allow from 192.168.0.0/24 to 192.168.0.13 port 443
#T# IPs in the range [192.168.0.0, 192.168.0.255] are allowed to connect in port 443, this host is 192.168.0.13

#T# create rules about network interfaces

# SYNTAX ufw deny|reject|allow incoming|outgoing on net1 from ip1
#T# net1 is the network interface protected by the rule, ip1 is the connecting IP number or range

ufw deny incoming on wlp3s0 from 236.217.38.92
#T# this denies connections from the IP 236.217.38.92 to the wireless network interface identified by wlp3s0

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

#T# install a module or package in a user directory with the --user flag
pip3 install --user sympy
# |-----

# |-------------------------------------------------------------

#C# File system hierarchy management

# |-------------------------------------------------------------
#T# go to the previous directory
cd -

#T# list the current directories in the directory stack, the -v flag can be used to output the index of the entries in the list
dirs -v

#T# push a directory into the directory stack
# SYNTAX pushd dir1
pushd ~/.local/

#T# push a directory without changing the current directory
pushd -n /sbin/

#T# rotate the directory stack by pushing a dir already in the stack, using its index

# SYNTAX pushd +int1
# SYNTAX pushd -int1
#T# int1 is the index, using the plus + sign counts from the start with the first element being 0, using the minus - sign counts from the end with the last element being 0

dirs # /tmp/dir1 /tmp/dir2 /tmp/dir3
pushd +1 # /tmp/dir2 /tmp/dir3 /tmp/dir1
pushd -0 # /tmp/dir1 /tmp/dir2 /tmp/dir3

#T# remove a dir from the directory stack using the popd command, it has the same syntaxes and options as the ones shown for the pushd command
popd +2 # /tmp/dir1 /tmp/dir2 # using the same example as in pushd

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

#C# --- find and xargs commands

# |-----

#T# the find command is used to find files

# SYNTAX find -o1 -o2 val2 /path/to/search1 -option1 -option2 value2 '!' -option3
#T# this searches in /path/to/search1, -o1 represents a flag, -o2 val2 represent a kwarg pair, up to -oN, these must be written before the path

#T# -option1 represents a flag, -option2 value2 represent a kwarg pair, -option1, -option2, -option3, up to -optionN are long options with a single hyphen, they are used as expressions to refine the search

#T# the pairs -option2 value2 in which value2 is a measure of time, or size, are written as a number with a plus or minus sign, e.g. if value2 is in minutes then '+5' means more than 5 minutes ago, '-5' means less than 5 minutes ago, '5' means exactly five minutes ago, it can be a float using comma, for example '6,1', when comparing sizes '+5M' means more than 5 mebibytes and so on

#T# the exclamation mark '!' is used to negate only the option that follows it, the syntax shown finds files where -option3 does not match, the parentheses '(' ')' are used to group expressions of -option1, -option2, up to -optionN, they should be separated with space like this '(' -option2 value2 ')'

#T# globbing patterns such as 'str*' should be quoted

#T# -o1 and -o2 val2 can be one of the following
#T#     -D str1, print debug info according to str1, replace str1 for 'help' to see the different debug options
#T#     -H, only follow symlinks that are directly written or expanded in the arguments to the find command
#T#     -L, follow symlinks
#T#     -Oint1, do search optimization, int1 is the level of optimization between 0 and 3
#T#     -P, do not follow symlinks

#T# -option1, -option3, and -option2 value2 can be one of the following
#T#     -a, and operator, returns true (as -true) if the left and right side of it are true
#T#     -amin time1, finds files and dirs accessed time1 minutes ago, see up for the time1 notation
#T#     -anewer file1, finds files and dirs accessed after file1
#T#     -atime time1, finds files and dirs accessed time1 days ago, see up for the time1 notation
#T#     -cmin time1, finds files and dirs changed time1 minutes ago, see up for the time1 notation
#T#     -cnewer file1, finds files and dirs changed after file1
#T#     -ctime time1, finds files and dirs changed time1 days ago, see up for the time1 notation
#T#     -depth, in each dir, process first the files and last the dir
#T#     -delete, deletes found files, should be used at the end of the command, because it deletes all files that were found before its place in the command
#T#     -empty, finds empty files and dirs
#T#     -exec command1 '{}' \;, executes command1, placing each found file in the placeholder '{}' and terminating the command with \;
#T#     -exec command1 '{}' +, same as before, but append the found files one after the other separated by space, so that command1 uses them as arguments
#T#     -execdir command1, like -exec in both syntaxes, but command1 is run from the subdir that contains the found file
#T#     -executable, finds executable files and dirs
#T#     -false, false value for boolean expression
#T#     -fprint file1, prints the output directly to file1
#T#     -fstype fs1, finds files with the filesystem type fs1
#T#     -gid int1, finds files and dirs whose group id is int1
#T#     -group str1, finds files and dirs whose group name is str1
#T#     -ilname file1, finds the symlinks to file1, case insensitive
#T#     -iname file1, finds files and dirs with the name file1, case insensitive
#T#     -inum int1, finds the file whose inode is int1
#T#     -ipath path1, like -iname, but find the whole path1, not only the last file or dir name, so, not only the basename
#T#     -iregex 'pattern1', finds files and dirs matching pattern1, it must be quoted
#T#     -links int1, finds files with int1 hard links
#T#     -lname file1, finds the symlinks to file1
#T#     -maxdepth int1, finds files and dirs at a dir depth of maximum int1
#T#     -mindepth int1, finds files and dirs at a dir depth of minimum int1
#T#     -mmin time1, finds files and dirs modified time1 minutes ago, see up for the time1 notation
#T#     -mount, do not descend into directories from other filesystems and partitions
#T#     -mtime time1, finds files and dirs modified time1 days ago, see up for the time1 notation
#T#     -name file1, finds files and dirs with the name file1
#T#     -newer file1, finds files and dirs modified after file1
#T#     -nogroup, finds files and dirs whose group is not registered in /etc/group
#T#     -nouser, finds files and dirs whose user is not registered in /etc/passwd
#T#     -o, or operator, returns true (as -true) if the left or right side of it are true
#T#     -ok command1, like -exec in both syntaxes, but ask for confirmation before executing any command
#T#     -okdir command1, like -execdir, but ask for confirmation before executing any command
#T#     -path path1, like -name, but find the whole path1, not only the last file or dir name, so, not only the basename
#T#     -perm int1, finds files and dirs that have their permission bits set as the octal number int1, int1 has up to 4 digits
#T#     -perm str1, finds files and dirs that have their permissions as str1, the format of str1 is 'ugo=rwx,ugo=rwx,ugo=rwx' any single char can be deleted, except for '=', they mean, u user, g group, o other, r read, w write, x execute
#T#     -readable, finds readable files and dirs
#T#     -regex 'pattern1', finds files and dirs matching pattern1, it must be quoted
#T#     -print, prints each found file and dir separated by newline
#T#     -print0, prints each found file and dir separated by a null char
#T#     -prune, prunes found matches, so it should be used with -o -print, to print the files and dirs that were not found, -prune also prevents descending into dirs found to the left (before it in the command)
#T#     -quit, quits the command
#T#     -samefile file1, finds any file that is the same as file1, so hard links, and soft links (using the -L flag)
#T#     -size size1, size1 has three parts, sign, number, letter, see up for the size1 notation which explains sign and number, the letters are, 'c' for bytes, 'w' for words (two bytes), 'b' for 512 bytes, 'k' for kibibytes, 'M' for mebibytes, 'G' for gibibytes
#T#     -true, true value for boolean expression
#T#     -type type1, finds files of type1, type1 can have the values, 'b' for block files, 'c' for char files, 'd' for dirs, 'f' for files, 'l' for symlinks, 'p' for pipes, 's' for sockets
#T#     -uid int1, finds files and dirs whose user id is int1
#T#     -user str1, finds files and dirs whose username is str1
#T#     -writable, finds writable files and dirs

find -H . link1 #| finds files and dirs and dereferences link1 to check if it is a file or dir
find . -amin -5 #| finds files accessed less than 5 minutes ago
find . -ctime +2 #| finds files modified more than 2 days ago
find . -execdir pwd \; #| prints the dir of each found file and dir
find . '!' -executable '!' -readable #| finds files that are non executable and non readable, kwarg options can be used after the '!' too
find . '(' -fstype ext4 ')' #| finds files with an ext4 filesystem
find . -gid 1000 #| finds files whose group id is 1000
find . -inum 52300562 # ./file1 # if 52300562 is the inode of file1
find . -path './dir1*' #| finds files that contain the path ./dir1* after globbing
find . -name dir* -prune #| does not descend into dirs that start with 'dir' in the name
find . -regex '..[A-z]+[0-9]*' #| finds files with the given regex pattern

#T# the xargs command is used as an improved -exec action from the find command, xargs applies a command (echo by default) over a set of arguments, separated by space or newline

# SYNTAX xargs -o1 -o2 val2 command1 args1
#T# some of these parts can be optional depending on the context, -o1 represents a flag, -o2 val2 represent a kwarg pair, command1 args1 is the command and the arguments (separated by space) that will be applied to the input of the xargs command

#T# -o1 and -o2 val2 can be one of the following
#T#     -0, use the null char to identify separated inputs
#T#     -a file1, use file1 contents as the input of the xargs command
#T#     -d char1, use char1 to identify separated inputs
#T#     -E char1, use char1 as the EOF (end of file) char, char1 must appear alone in its own line
#T#     -I str1, use str1 as the placeholder for each of the inputs, str1 is replaced by each input in turn, so str1 is used in args1 to represent the inputs
#T#     -P int1, open int1 processes in parallel, this allows multiprocessing
#T#     -p, prompt to ask for confirmation before executing any command
#T#     -t, verbose output, it shows the commands being executed

find . -print0 | xargs -0 echo #| prints the found files and dirs
xargs -d A -a files.txt grep -n 'key' #| prints the files written inside files.txt separated by 'A', that contain 'key', i.e. if in files.txt is the line file1Afile2Afile3A then file1, file2, and file3 are printed if the contain 'key'
find . -name 'file*' | xargs -I str1 mv str1 str1_new #| finds any files and dirs whose name starts with 'file', and appends '_new' to their name
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