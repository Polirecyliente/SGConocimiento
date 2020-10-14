
#   Basic Syntax

#T# Table of contents

#T# Blocks of code
#T# Variables, constants, literals
#T# Escape sequences

#T# Beginning of content

# |-------------------------------------------------------------
#T# run any Bash file /path/to/file1.sh in a terminal with
# SYNTAX bash /path/to/file1.sh

#T# output variables to stdout with the echo command
# SYNTAX echo "$var1 $var2 $var3"
# |-------------------------------------------------------------

#T# Blocks of code

# |-------------------------------------------------------------
#T# blocks of code are delimited by either braces of parentheses

#T# the braces execute the block in the same shell environment
{
    echo "command one"
    echo "command two"
}

#T# the parentheses execute the block in a subshell
(
    echo "command one"
    echo "command two"
)

#T# semicolon separates commands in one line
echo 'First line'; echo 'Second line'
# |-------------------------------------------------------------

#T# Variables, constants, literals

# |-------------------------------------------------------------
#T# variables are dynamically typed. Literals are characters, numbers

#T# define variables with the equal sign, no spaces are allowed before or after the equal sign
int1=5

#T# strings are created within quotation symbols, each quotation symbol type can be used inside the others as a normal character
str1='Hello       world!"'
str2="second str'ing"

# |--------------------------------------------------\
#T# double quotes are used for interpolated strings, variable substitution is made with

# SYNTAX ${var1}
#T# var1 is the variable to be substituted inside a string

str2="string ${int1} interpolation" # string 5 interpolation
# |--------------------------------------------------/

# |-------------------------------------------------------------

#T# Escape sequences

# |-------------------------------------------------------------
#T# echo -e to enable escaped characters inside double quoted string, escaped characters start with backslash
BIRTHDATE='Jan 1, 2000'
BIRTHDAY=$(date -d "${BIRTHDATE}" +%A)
echo -e "Date: ${BIRTHDATE}\nWeekday: ${BIRTHDAY}"
# |-------------------------------------------------------------