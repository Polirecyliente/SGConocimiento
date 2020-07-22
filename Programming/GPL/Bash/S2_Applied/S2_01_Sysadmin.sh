
#   Sysadmin

#T# Contents
#T# Essential commands and syntax
#T# Process management
#T# User and group management
#T# Hardware detection
#T# Devices
#T# Fonts

#T# Essential commands and syntax

#T# remove everything but .file with rm !(*.file)
rm !(*.tex|*.bib)

#T# print numbered from the start in file1 up to line up_to_l, but taking only the last N lines
# head -up_to_l file1 | nl -b 'a' | tail -N
head -80 file1 | nl -b 'a' | tail -10

#T# Process management

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

#T# User and group management

#T# see the groups that the current user belongs to with groups userName
groups jul

#T# append user to an existing group with usermod, reboot may be necessary for this to take effect
usermod -a -G audio jul

#T# Hardware detection

#T# list hardware with lshw, the option -short gives a summary
lshw -short

#T# Devices

#T# Check mounted devices in /proc/mounts
cat /proc/mounts
#T# list mounted devices with mount -l
mount -l

#T# Fonts

#T# fonts are stored in /usr/share/fonts/
cd /usr/share/fonts/