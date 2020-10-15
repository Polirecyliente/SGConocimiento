
#   Basic Syntax

#T# Table of contents

#T# Blocks of code
#T# Variables, constants, literals
#T# Escape sequences
#T# Expressions
#T# Function calls
#T# --- Command execution
#T# --- Command substitution
#T# Statements
#T# Multiline statements
#T# Multistatement lines
#T# Command history
#T# --- History expansion

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
#T# escaped characters start with backslash

# |--------------------------------------------------\
#T# the -e flag of echo is to enable the use of escaped characters inside a double quoted string

echo -e "Line1\nLine2"
#T# the former prints
# Line1
# Line2
# |--------------------------------------------------/

# |-------------------------------------------------------------

#T# Expressions

# |-------------------------------------------------------------
#T# expressions are evaluated and return a value

# |--------------------------------------------------\
#T# math expressions are written with this syntax

# SYNTAX num1=$((expr1))
#T# expr1 is the math expression, which is enclosed in the arithmetic expansion $(()), its result is assigned to num1

int1=$((5 + 3 - 1)) # 7
# |--------------------------------------------------/

# |-------------------------------------------------------------

#T# Function calls

# |-------------------------------------------------------------
#T# functions and commands use the same syntax, there are no parentheses, arguments are separated by space

#T# --- Command execution

# |-----
#T# basic output to stdout with the echo command
echo "Hello, Bash!" "Second arg" # Hello, Bash! Second arg

#T# basic input from stdin with the read command
read var1
# |-----

#T# --- Command substitution

# |-----
#T# the result of a command can be converted to a string by using command substitution

# SYNTAX $(command1)
#T# the result that command1 sends to stdout is converted to a string, command1 must be inside $() the command substitution operator

$(echo "str1") # str1: command not found
# |-----

# |-------------------------------------------------------------

#T# Statements

# |-------------------------------------------------------------
#T# a statement is a complete instruction

int1=5
#T# int1=5 is a statement, the variable int1 is made to point to the value 5
# |-------------------------------------------------------------

#T# Multiline statements

# |-------------------------------------------------------------
#T# a multiline statement is created with a backslash at the end of each line
echo "str1" \
"str2" # str1 str2
# |-------------------------------------------------------------

#T# Multistatement lines

# |-------------------------------------------------------------
#T# multiple statements in the same line are separated with a semicolon
int1=9; int2=7; int3=0
# |-------------------------------------------------------------

#T# Command history

# |-------------------------------------------------------------

# |--------------------------------------------------\
#T# the history can be checked with the history command

history
#T# the former prints
#    1  echo "echoed to stdout"
#    2  cat ~/.bash_history 
#    3  git push
#    4  history

#T# or any list of commands executed before and stored in the history
# |--------------------------------------------------/

#T# clear the history with the -c flag of the history command
history -c

#T# --- History expansion

# |-----
#T# commands from the history are expanded with an exclamation mark, known as the bang operator

# |--------------------------------------------------\
#T# any command in the history can be executed again with its number in the history

# SYNTAX additionals1 !int1 additionals2
#T# int1 is the number of the command in the history, additionals1 and additionals2 are any other commands and arguments added before and after the command with number int1

#T# as an example, if the command number 6 is 'echo "repeated string"'
!6 "and more"
#T# then the former prints
# echo "repeated string" "and more"
# repeated string and more

#T# using negative numbers starts counting from the last command in the history
!-1
#T# this executes the last command in the history, this is the same as
!!
#T# to execute the third to last command use
!-3
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# commands in the history can also be expanded with their starting characters

# SYNTAX additionals1 !starting_chars1 additionals2
#T# starting_chars1 is a string with the first characters of the command in the history, if several commands start with the same characters then the last command in the history will be executed

#T# additionals1 and additionals2 are any other commands and arguments added before and after the command that starts with starting_chars1

#T# if the commands 'git pull' and 'git push' are on the history, then executing
!gi
#T# will execute 'git push' as it's the last one in the history
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# appending :p to a history expansion will print it instead of executing it

# SYNTAX !command_id1:p
#T# command_id1 is either an integer with the number of the command in the history, a string with the starting characters of the command in the history, or any other valid history expansion like !!

!!:p # history # if this was the last command in the history
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# history expansion can also be used to reuse arguments from past commands

# SYNTAX command1 !^
#T# this calls command1 with the first argument of the last command in the history

echo !^
#T# if the last command is 'cat str1 str2' then this prints
# echo str1
# str1

# SYNTAX command1 !$
#T# this calls command1 with the last argument of the last command in the history

echo !$
#T# if the last command is 'cat str1 str2' then this prints
# echo str2
# str2

# SYNTAX command1 !*
#T# this calls command1 with all the arguments of the last command in the history

echo !*
#T# if the last command is 'cat str1 str2' then this prints
# echo str1 str2
# str1 str2

# SYNTAX command1 !command_id1:arg_id1
#T# this calls command1 with arguments extracted from the command identified by command_id1 (which can be the number of a command in the history, its starting characters, or any other valid history expansion)

#T# arg_id1 is the identifier of the argument to be extracted, it can be an integer (this means the position number of the argument, first argument is 1, second argument is 2, and so on), or any of the symbols used in the shown syntax, the caret ^ for the first argument, the dollar sign $ for the last argument, and the asterisk * for all the arguments

echo !gi:2
#T# if there is a command 'git pull origin master' in the history then this prints
# echo origin
# origin
# |--------------------------------------------------/

# |-----

# |--------------------------------------------------\
#T# the previous command can be rerun replacing a substring for another, for example in case of a typo

# SYNTAX ^original_substring1^new_substring1
#T# this replaces the first instance of original_substring1 for new_substring1 in the last command

^ir^it
#T# if the last command is 'gir push' then this executes 'git push'
# |--------------------------------------------------/

# |-------------------------------------------------------------