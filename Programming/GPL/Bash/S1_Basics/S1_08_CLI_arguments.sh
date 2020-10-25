
#   CLI arguments

#T# Table of contents

#C# 

#T# Beginning of content

#T# Positional parameters: First argument $1, second argument $2, Script calling name $0
echo -e "First argument is: $1\nSecond argument is: $2\nScript name is: $0"

#T# Number of arguments $#, String with all args concatenated $@
argsNum=$#
echo -e "The number of args is: ${argsNum}\nThe args are: $@"

#T# $*, these can be used in functions as well
#T# PS1, PS2 prompts, and their escaped characters
