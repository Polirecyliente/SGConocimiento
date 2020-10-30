
#   CLI arguments

#T# Table of contents

#C# Special parameters


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
for it1 in "$*"; do echo "$it1"; done
for it1 in "$@"; do echo "$it1"; done

#T#
# |-------------------------------------------------------------


# set command to set args, shift command