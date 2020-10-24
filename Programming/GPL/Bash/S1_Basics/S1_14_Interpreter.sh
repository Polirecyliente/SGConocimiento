
#   Interpreter

#T# Table of contents

#C# Interpreter customization
#C# --- Interpreter options
#C# --- Shell options

#T# Beginning of content

#C# Interpreter customization

# |-------------------------------------------------------------

#C# --- Interpreter options

# |-----
#T# the interpreter can have several options set at the start and changed during execution

# SYNTAX set -o1
# SYNTAX set +o1
#T# the set command is used to set the value of flags that modify the options of the interpreter, o1 is the flag being set, using -o1 activates the flag, using +o1 turns off the flag

#T# there are several flags used for different options, the following list describes each flag when turned on
#T#     -a, +a, automatically export created or newly modified variables
#T#     -b, +b, print a message when a job is killed
#T#     -e, +e, exit the interpreter on error
#T#     -f, +f, disable globbing
#T#     -h, +h, executed commands are placed in a hash table for quicker access, for an explanation on this hash table see S1_06_Functions.sh
#T#     -k, +k, arguments that contain variables use the same variables of the calling environment, var1=$var1 uses $var1 from the calling environment
#T#     -m, +m, enable job control, to manage background and foreground processes
#T#     -n, +n, read commands but do not execute them, used executing 'bash -n script1.sh' prints the syntax errors in script1.sh
#T#     -o arg1, +o arg1, activates the flag arg1, the names of the flags can be seen executing 'set --help'
#T#     -t, +t, exit the interpreter after executing one command
#T#     -u, +u, print error when calling an unset variable
#T#     -v, +v, print each line read
#T#     -x, +x, print debug information
#T#     -B, +B, perform brace expansion, for an explanation on brace expansion see S1_03_Operators.sh
#T#     -C, +C, impede bash from overwriting files
#T#     -E, +E, the ERR trap can be activated by shell functions, for an explanation on traps see S1_09_Exception_handling.sh
#T#     -H, +H, enable history expansion, for an explanation on history expansion see S1_03_Operators.sh
#T#     -P, +P, follow symbolic links, e.g. if dir1 has a symlink link1, and -P is on, then executing 'cd link1' makes the pwd be dir1 and not link1
#T#     -T, +T, the DEBUG and RETURN traps can be activated by shell functions, for an explanation on traps see S1_09_Exception_handling.sh

#T# the -i flag means the shell is interactive, the -s flag makes bash read commands from stdin

set -x
set +x
# |-----

#C# --- Shell options

# |-----
#T# shell options are modified with the shopt command

# SYNTAX shopt -s option1
#T# the shell option option1 is turned on

# SYNTAX shopt -u option1
#T# the shell option option1 is turned off

#T# the following list is the list of shell options
#T#     extglob, allows the use of an extended set of operators for globbing (see S1_03_Operators.sh)

shopt -s extglob
shopt -u extglob
# |-----

# |-------------------------------------------------------------










# export keyword for environment variables in an interpreter session