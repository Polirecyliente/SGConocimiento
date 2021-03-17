
#   Basic Syntax

#T# Table of contents

#C# Blocks of code
#C# Variables, constants, literals
#C# Escape sequences and escaped chars
#C# Expressions
#C# Function calls
#C# - Command execution
#C# Statements
#C# Multiline statements
#C# Multistatement lines

#T# Beginning of content

# |-------------------------------------------------------------
#T# run a Bash file /path/to/file1.sh in a terminal with
# SYNTAX bash /path/to/file1.sh

#T# output variables to stdout with the echo command
# SYNTAX echo "$var1 $var2 $var3"

#T# get help about a symbol or name (function, command, etc.) in a few ways

# SYNTAX help builtin_command1
#T# this prints help about builtin_command1

# SYNTAX man command1
#T# this prints the manual pages of command1

# SYNTAX type symbol1
#T# this prints the type of symbol1 which can be a function, command, etc.
# |-------------------------------------------------------------

#C# Blocks of code

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
# |-------------------------------------------------------------

#C# Variables, constants, literals

# |-------------------------------------------------------------
#T# variables are dynamically typed. Literals are characters, numbers

#T# define variables with the equal sign, no spaces are allowed before or after the equal sign (because spaces separate arguments)
str1='str'
int1=5

#T# variable identifiers can only contain letters, numbers, and the underscore
var_aux1=0

#T# strings are created within quotation symbols, each quotation symbol type can be used inside the others as a normal character
str1='Hello       world!"'
str2="second str'ing"
# |-------------------------------------------------------------

#C# Escape sequences and escaped chars

# |-------------------------------------------------------------
#T# an special kind of combination of literals are escape sequences and escaped chars, escape sequences mean something particular, e.g. the \n means newline, escaped chars make operators to become literals, e.g. the \$ makes the dollar sign to be taken literally

# SYNTAX \char1
#T# an escape starts with a backslash \ and is followed by char1 which is other character or characters, most commonly char1 is a single character

echo -e "Line1\n\$Line2" #| the -e flag is to enable the use of escaped characters inside a double quoted string
#T# the former prints
# Line1
# $Line2
# |-------------------------------------------------------------

#C# Expressions

# |-------------------------------------------------------------
#T# expressions are evaluated and return a value

#T# math expressions are written with this syntax

# SYNTAX num1=$(( expr1 ))
#T# expr1 is the math expression, its result is assigned to num1, for the $(()) operator see the file titled Operators, specifically arithmetic expansion

int1=$(( 5 + 3 - 1 )) # 7
# |-------------------------------------------------------------

#C# Function calls

# |-------------------------------------------------------------
#T# a function call is made with the function name followed by a space, and then the arguments separated by space

#T# functions and commands use the same syntax, arguments without quotation are taken to be strings

#C# - Command execution

# |-----
#T# basic output to stdout is done with the echo command
echo "Hello, Bash!" "Second arg" # Hello, Bash! Second arg

#T# basic input from stdin is done with the read command
echo "Please enter var1 as input"
read var1

#T# bash has several commands that are builtin, such as echo, read, commands can receive arguments, there are three types of arguments, flags, options (kwarg pairs), and positional parameters

# SYNTAX command1 -f --option1 value1 -- positional1
# SYNTAX command1 --flag1 -o=value1 positional1
# SYNTAX command1 -f -ovalue1 positional1
# SYNTAX command1 -fovalue1 positional1
#T# the former syntaxes are equivalent, command1 is the command to be executed

#T# -f is a flag, it can also have a long name such as --flag1, a flag is a binary variable, it can be turned on by its presence after the command, or turned off by its absence after the command

#T# --option1 value1 is a key value pair, it can also be called a kwarg pair, --option1 can have a short name such as -o, value1 can be separated by space, by an equal sign =, or not separated from -o

#T# positional1 is a positional parameter, the double dash -- is used to separate flags and options from positional parameters, to avoid ambiguity when there are positional parameters that start with a hyphen, e.g. '-pos1'

#T# flags can be put in a single hyphen, the last one can be an option, e.g. -fgovalue1, if g is another flag

#T# when an application is big, it can be composed of several different but related commands, in this case the command name is separated from the application name by space, as if the command was an argument (it's not), e.g. git pull, git add, git commit, etc.

read -s -p prompt1 -- var1 #| -s is a flag to read silently (without showing the read chars), -p prompt1 are a kwarg pair (an option) to display prompt1 as the prompt, and var1 is a positional parameter separated from the rest with a double dash --, var1 stores the value received by the read command from stdin
# |-----

# |-------------------------------------------------------------

#C# Statements

# |-------------------------------------------------------------
#T# a statement is a complete instruction

int1=5
#T# int1=5 is a statement, the variable int1 is made to point to the value 5

#T# the colon : operator is used to create a no-op statement that does nothing, as a filler
:

#T# in Bash, an alias is a shell word that executes another command or keyword, a keyword is a shell word that has its own semantic meaning for Bash, a function is a command created in Bash, a builtin is a command that comes with Bash, a file is an external command that resides in the file hierarchy
# |-------------------------------------------------------------

#C# Multiline statements

# |-------------------------------------------------------------
#T# a multiline statement is created with a backslash at the end of each line
echo "str1" \
"str2" # str1 str2
# |-------------------------------------------------------------

#C# Multistatement lines

# |-------------------------------------------------------------
#T# multiple statements in the same line are separated with a semicolon
echo 'First line'; echo 'Second line'; int1=9; int2=7; int3=0

#T# assignment statements can also be separated with space
var1=value1 var2=value2
# |-------------------------------------------------------------