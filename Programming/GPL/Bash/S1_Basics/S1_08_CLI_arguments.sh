
#   CLI arguments

#T# Table of contents

#C# Special parameters
#C# The getopt command

#T# Beginning of content

# |-------------------------------------------------------------
#T# CLI stands for Command Line Interface

#T# execute this file with command line arguments: str2 5.4 -oCount -oCount
# |-------------------------------------------------------------

#C# Special parameters

# |-------------------------------------------------------------
#T# the positional parameters have already been explored in the section about functions (see S1_06_Functions.sh), those apply here as well in the exact same way, $0 for the name of the script or program in execution, $1 for the first argument passed to the CLI, $2 for the second argument passed to the CLI, and so on
echo "arg1 $1, arg2 $2, script name $0" # arg1 str2, arg2 5.4, script name S1_08_CLI_arguments.sh

#T# the following special parameters (variables) are used in parsing CLI arguments, but they can be used the same for function arguments

#T# the $# parameter stores the number of arguments passed in the CLI, or to the function
echo $# # 4

#T# the $*, $@ parameters both store the passed arguments in an array, the difference is that when quoted inside double quotes, "$*" is expanded to the list of arguments as a single string, and "$@" is expanded to the list of arguments as separate strings
for it1 in "$*"; do echo "$it1"; done # str2 5.4 -oCount -oCount
for it1 in "$@"; do echo "$it1"; done
#T# the former prints
# str2
# 5.4
# -oCount
# -oCount

# |--------------------------------------------------\
#T# the shift command is used to shift the positional parameters to the left, reducing their number

# SYNTAX shift int1
#T# int1 is the number of times the positional parameters are shifted to the left (it's optional, if left out it defaults to 1), it varies between 1 and the number of arguments (positional parameters)

echo $1 # str2
shift 2
echo $1 # -oCount # corresponds to the original third argument
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# the set command allows the modification of the positional parameters

# SYNTAX set -- new_arg1 new_arg2 new_arg3
#T# the new values of the positional parameters are new_arg1, new_arg2, new_arg3, up to new_argN, this always deletes all positional parameters, and puts the new ones

set -- "new_arg"
echo $1 # new_arg
echo $2 # ""
# |--------------------------------------------------/

# |-------------------------------------------------------------

#C# The getopt command

# |-------------------------------------------------------------
#T# the getopt command is used to parse the CLI arguments

# SYNTAX getopt -o1 arg1 -o "short_names1" -l "long_names1" -- "$@"
#T# -o1 arg1 is an option (kwarg pair), or a flag (when arg1 is left out), short_names1 contains a string of characters that will be recognized as short names, and long_names1 contains a list of strings separated by comma that holds the long names that will be recognized as options

#T# in both short_names1 and long_names1, a name can end with a colon to indicate that the name is a kwarg and not a flag

#T# with "$@" all positional parameters are passed to the getopt command, (an smaller subset can be passed too), and the output of the getopt command is a string with the parsed arguments, if there are no errors from the user

#T# -o1 arg1 can have two values of significance, the -a flag is used to allow using long names with only one hyphen, so with the -a flag --name1 is as valid as -name1, and the kwarg -n script_name1 is used to output errors from script_name1 instead of doing it from getopt itself

set -- "pos1" -acvalc "pos2" -bname valb --dname " the last "
parsed_args1=$(getopt -a -n "CLI_arguments" -o "ab:c:d:" -l "aname,bname:,cname:,dname:" -- "$@")
echo $parsed_args1 # -a -c 'valc' --bname 'valb' --dname ' the last ' -- 'pos1' 'pos2'
# |-------------------------------------------------------------