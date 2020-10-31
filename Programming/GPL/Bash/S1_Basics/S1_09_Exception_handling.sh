
#   Exception handling

#T# Table of contents

#C# Basic exception handling
#C# The trap command

#T# Beginning of content

#C# Basic exception handling

# |-------------------------------------------------------------
#T# basic exception handling can be done with boolean logic (see S1_03_Operators.sh)

# SYNTAX ( command1 && command2 ) || exception_handler1
#T# command1, command2, up to commandN are the commands that should execute without error, if an error happens then exception_handler1 is called, so it is a command or function

( echo "process1" && cat non_file1 ) || echo "an exception occurred"
#T# the former prints
# process1
# cat: non_file1: No such file or directory
# an exception occurred
# |-------------------------------------------------------------

#C# The trap command

# |-------------------------------------------------------------
#T# exception handling can be approximated in Bash by using the trap command

# SYNTAX trap "command1" signal1 signal2
#T# this assigns command1 as a callback function for when any of signal1, signal2, up to signalN, is sent to the script or program in execution, so it can be said that command1 traps these signals, quoting command1 allows it to have several words

#T# there are several signals that don't originate from Bash but rather from the operating system (see S1_12_System_calls.sh), the signals that come from Bash are, ERR, DEBUG, EXIT, and RETURN

#T# the ERR signal is sent when an error occurs, for example when attempting to open a nonexistent file

#T# the DEBUG signal is sent everytime a command is executed

#T# the EXIT signal is sent when a shell or subshell exits

#T# the RETURN signal is sent whenever there is a return statement from a function

signal_handler1() { echo "the signal was handled"; } # signal_handler1 is the callback function for the trapped signals assigned to it
trap signal_handler1 ERR EXIT DEBUG RETURN
# the signal was handled # this is output when there is an error, or when the current subshell exits

# SYNTAX trap -p signal1
#T# the -p signal1 kwarg pair makes the trap command output the signal handler of signal1
trap -p ERR # trap -- 'signal_handler1' ERR

# SYNTAX trap "" signal1
#T# signal1 is ignored
trap "" EXIT # when a subshell exits there is nothing executed

# SYNTAX trap - signal1
#T# this resets the signal handling for signal1 to its default
trap - ERR # the ERR signal now has no signal handler, and so 'trap - ERR' outputs nothing
# |-------------------------------------------------------------