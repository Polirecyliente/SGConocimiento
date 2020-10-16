
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
#T# --- Parameter expansion
#T# Multiline statements
#T# Multistatement lines
#T# Command history
#T# --- History expansion
#T# Interpreter options
#T# Special parameters

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
#T# var1 is the variable to be substituted inside a string, this is also called parameter expansion as explained later in this file

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

#T# --- Parameter expansion

# |-----
#T# variables (called parameters here) can be expanded to get their value or get their value modified by using a word (as it's called here)

#T# parameters are identified because they start with the dollar sign $ when they are being operated with

#T# define a parameter as usual
var1="value one"

# |--------------------------------------------------\
#T# expansion means sustituting the parameter for its value

# SYNTAX $var1
# SYNTAX ${var1}
#T# both syntaxes are equivalent, braces are used when the next character after var1 is not a space, or when needed

echo $var1 # value one

#T# because arguments are separated by spaces, a parameter should be enclosed in double quotes to protect its value' spaces
echo "$var1" # value one # in this case "value one" is the argument, instead of two arguments "value" and "one"
# |--------------------------------------------------/

#T# a null parameter is defined as an empty string
null_var1=""

# |--------------------------------------------------\
#T# a parameter can be unset so it doesn't exist anymore
# SYNTAX unset var1
unset_var1="temp value"
unset unset_var1 # unset_var1 becomes as if it was never defined
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# conditional parameter expansion is done to expand a parameter conditionally, if the parameter doesn't exist then it's expanded to another alternative called a word

# SYNTAX ${var1-alt1}
#T# var1 is the parameter to be expanded, alt1 is the alternative literal string in case var1 doesn't exist, alt1 can also be a parameter expansion, an arithmetic expansion, command substitution etc.

echo ${var1-literal_alt1}
#T# the former prints
# value one    # if var1="value one"
# literal_alt1 # if var1 is unset

# SYNTAX ${var1:-alt1}
#T# same as before, but expanding to alt1 also happens when var1 is null

echo ${var1:-literal_alt1}
#T# the former prints
# value one    # if var1="value one"
# literal_alt1 # if var1 is unset or null

# SYNTAX ${var1=alt1}
#T# same as before, but if var1 is null then it gets assigned the literal string alt1 (unless alt1 is another expansion as said before, in that case var1 is assigned the value of alt1)

echo ${var1=literal_alt1}
#T# the former prints
# value one    # if var1="value one"
# literal_alt1 # if var1 is unset, and now var1="literal_alt1"

# SYNTAX ${var1:=alt1}
#T# same as before, but expanding and assigning to alt1 also happens when var1 is null

echo ${var1:=literal_alt1}
#T# the former prints
# value one    # if var1="value one"
# literal_alt1 # if var1 is unset or null, and now var1="literal_alt1"

# SYNTAX ${var1?alt1}
#T# same as before, but if var1 is unset then alt1 is printed as an error message to stderr

echo ${var1?error_alt1}
#T# the former prints
# value one              # if var1="value one"
# bash: var1: error_alt1 # if var1 is unset

# SYNTAX ${var1:?alt1}
#T# same as before, but expanding to alt1 as an error message also happens when var1 is null

echo ${var1:?error_alt1}
#T# the former prints
# value one              # if var1="value one"
# bash: var1: error_alt1 # if var1 is unset or null

# SYNTAX ${var1+alt1}
#T# same as before, but now var1 is expanded to alt1 when var1 is not unset, note that this doesn't change var1 original value

echo ${var1+literal_alt1}
#T# the former prints
# literal_alt1 # if var1="value one" or any other value
#              # if var1 is unset

# SYNTAX ${var1:+alt1}
#T# same as before, but expanding to alt1 also does not happen when var1 is null

echo ${var1:+literal_alt1}
#T# the former prints
# literal_alt1 # if var1="value one" or any other non null value
#              # if var1 is unset or null
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# substring parameter expansion is done to expand a parameter partially, taking only a substring of the parameter according to an offset or a matching pattern

# SYNTAX ${var1:offset1}
# SYNTAX ${var1:offset1:length1}
#T# var1 is the parameter to be expanded, offset1 and length1 are integers, this extracts a substring from var1, starting at the character in the position offset1, and extracting a total of length1 characters

#T# offset1 and length1 can be negative integers, if they are then they must be enclosed in parentheses to avoid forming the :- operator, if offset1 is negative then the first character is counted from the end of the parameter value, if length1 is negative then the last length1 characters are removed

var1=str1str2str3
echo ${var1:4}         # str2str3
echo ${var1:(-8)}      # str2str3
echo ${var1:3:4}       # 1str
echo ${var1:(-5):(-1)} # 2str

# SYNTAX ${var1#pattern1}
# SYNTAX ${var1##pattern1}
#T# this removes the substring that has to start from the left of var1 and matches pattern1, using double hash ## makes a greedy match

#T# pattern1 accepts globbing, the asterisk * matches 0 or more characters, the question mark ? matches 0 or 1 character, brackets [] are used for character classes which includes negation with the caret ^

var1="apple pie"
echo ${var1#?p}           # ple pie
echo ${var1##*p}          # ie
echo ${var1#[a-z][^a-h]p} # le pie

# SYNTAX ${var1%pattern1}
# SYNTAX ${var1%%pattern1}
#T# same as before, but the removed substring has to start at the right of var1 and match pattern1, using double %% makes a greedy match

var1="apple pie"
echo ${var1%p*}  # apple
echo ${var1%%p*} # a
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# substring substitution is done to make substring replacements and then expand the changed parameter

# SYNTAX ${var1/pattern1/replace_string1}
# SYNTAX ${var1//pattern1/replace_string1}
#T# var1 is the parameter whose value is the string where the replacement will take place, pattern1 is the pattern to be matched, replace_string1 replaces the matched substring

#T# if only one slash / is used between var1 and pattern1 then only the first match is replaced, with double slash // all matches are replaced

#T# pattern1 accepts globbing, the asterisk * matches 0 or more characters, the question mark ? matches 0 or 1 character, brackets [] are used for character classes which includes negation with the caret ^

var1="apple pie"
echo ${var1/ /_}  # apple_pie
echo ${var1/p/n}  # anple pie
echo ${var1//p/b} # abble bie
# |--------------------------------------------------/

# |-----

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

#T# Interpreter options

# |-------------------------------------------------------------
#T# the interpreter can have several options set at the start and changed during execution

# SYNTAX set -o1
# SYNTAX set +o1
#T# the set command is used to set the value of flags that modify the options of the interpreter, o1 is the flag being set, using -o1 activates the flag, using +o1 turns off the flag

#T# there are several flags used for different options, the following lists describes each flag when turned on
#T#     -C, +C, impedes bash from overwriting files
#T#     -f, +f, disable globbing
#T#     -x, +x, print debug information
#T#     -e, +e, quit the interpreter on error
#T#     -v, +v, print each line read
#T#     -H, +H, enable history expansion
#T#     -m, -M, enable job control, to manage background and foreground processes

#T# the -i flag means the shell is interactive, the -s flag makes bash read commands from stdin

set -x
set +x
# |-------------------------------------------------------------

#T# Special parameters

# |-------------------------------------------------------------
#T# the special parameters are variables whose name can't be manually assigned values, they are used to store special values

#T# process related parameters are the $$, $! parameters
echo $$ # 389217 # prints the PID of the current terminal
echo $! # 406952 # prints the PID of the last process sent to be a background process, if any

#T# the $? parameter stores the exit status of the last command
echo $? # 0 # zero usually means correct execution

#T# the $0 parameter stores the name of the script or command that expanded its value
echo $0 # bash

#T# the $_ parameter stores a string with the last argument of the last command
echo $_ # third # if the last command was 'echo first second third'

#T# the $- parameter stores the interpreter options
echo $- # himBHs

#T# there are a few more special parameters that deal with positional parameters which are treated in the section about command line arguments, see S1_08_CLI_args.sh
# |-------------------------------------------------------------