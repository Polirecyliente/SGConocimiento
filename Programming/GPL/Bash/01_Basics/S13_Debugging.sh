
#   Debugging

#T# Table of contents

#C# Basic debugging

#T# Beginning of content

#C# Basic debugging

# |-------------------------------------------------------------
#T# the Bash shell has a few options that can be used for debugging (see S14_Interpreter.sh), the most prominent are -u (errors when expanding unset variables), -v (prints the line read), and -x (prints debug information, for example it shows expansions)

#T# these options can be turned on before a piece of code under debugging, and turned off after said piece
set -uvx
var1=32
echo "code under study, var1 is $var1"
set +uvx
#T# the former prints
# echo "code under study, var1 is $var1"
# + echo 'code under study, var1 is 32'
# code under study, var1 is 32

#T# the LINENO builtin variable stores the curent line number
echo "in line $LINENO" # in line 26

#T# trapping the DEBUG signal (see S09_Exception_handling.sh) executes a signal handler after every command
trap "echo in debug mode" DEBUG

#T# the first char in PS4 (see S14_Interpreter.sh) is repeated for each level of indirection, e.g. for each level in which a command is executed inside another command
echo "lvl1" $(echo "lvl2" $(echo "lvl3"))
#T# the former prints (with the -x shell option turned on)
# +++ echo lvl3
# ++ echo lvl2 lvl3
# + echo lvl1 lvl2 lvl3
# lvl1 lvl2 lvl3
# |-------------------------------------------------------------