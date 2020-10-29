
#   Sysadmin

#T# Table of contents

#T# Essential commands and syntax
#T# Process management
#T# User and group management
#T# Hardware detection
#T# Devices
#T# System libraries
#T# Fonts
#T# Encodings
#T# Internet
#T# Latex
#T# Files

#T# Beginning of content

#T# Essential commands and syntax

# |-------------------------------------------------------------
#T# remove everything but .file with rm !(*.file), this uses pattern matching (see S1_03_Operators.sh)
rm !(*.tex|*.bib)

#T# print numbered from the start in file1 up to line up_to_l, but taking only the last N lines
# head -up_to_l file1 | nl -b 'a' | tail -N
head -80 file1 | nl -b 'a' | tail -10

#T# make a directory
mkdir -p /tmp/parent_dir1/child_dir1
#T# the p flag creates any parent directories needed, if they don't exist

#T# print the current datetime
date # mar 13 oct 2020 16:52:09 -05
# |-------------------------------------------------------------

#T# Process management

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

#T# User and group management

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

#T# Hardware detection

# |-------------------------------------------------------------
#T# list hardware with the lshw command, the option -short gives a summary
lshw -short

#T# list pci devices along with their drivers with the lspci command
lspci -k
#T# the -k flag is to show the kernel drivers and kernel modules
# |-------------------------------------------------------------

#T# System libraries

# |-------------------------------------------------------------
#T# print the cache of installed libraries
ldconfig -p
#T# the -p flag is for printing the cache
# |-------------------------------------------------------------

#T# Devices

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

#T# Fonts

# |-------------------------------------------------------------
#T# fonts are stored in /usr/share/fonts/
cd /usr/share/fonts/
# |-------------------------------------------------------------

#T# Encodings

# |-------------------------------------------------------------
#T# get the list of encodings knows by the operating system with the -l flag of the iconv program
iconv -l
# |-------------------------------------------------------------

#T# Internet

# |-------------------------------------------------------------
#T# download a file from the internet with wget, the -c flag is to continue downloading a partially downloaded file
wget -c http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda_11.0.2_450.51.05_linux.run
# |-------------------------------------------------------------

#T# Latex

# |-------------------------------------------------------------
#T# see the paths where latex packages can be installed
kpsepath tex

#T# use the tlmgr command (for texlive manager) to install latex packages
# tlmgr install package1
tlmgr install undertilde
# |-------------------------------------------------------------

#T# Files

# |-------------------------------------------------------------
#T# dereference a symbolic link
readlink -f link_file1 # /path/to/original_file1
# |-------------------------------------------------------------