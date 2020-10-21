
#   Basic Syntax

#T# Table of contents

#T# Blocks of code
#T# Variables, constants, literals
#T# Escape sequences
#T# Expressions
#T# Function calls
#T# --- Command execution
#T# Statements
#T# Multiline statements
#T# Multistatement lines

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

#T# define variables with the equal sign, no spaces are allowed before or after the equal sign (because spaces separate arguments)
int1=5

#T# strings are created within quotation symbols, each quotation symbol type can be used inside the others as a normal character, quotation symbols preserve the whitespace of the string
str1='Hello       world!"'
str2="second str'ing"

# |--------------------------------------------------\
#T# double quotes are used for interpolated strings (single quotes create raw, literal strings), variable substitution is made with

# SYNTAX ${var1}
#T# var1 is the variable to be substituted inside a string, this is also called parameter expansion and uses the braces operator as explained in S1_03_Operators.sh

str2="string ${int1} interpolation" # string 5 interpolation
# |--------------------------------------------------/

# |-------------------------------------------------------------

#T# Escape sequences

# |-------------------------------------------------------------
#T# escaped characters start with backslash

#T# the -e flag of echo is to enable the use of escaped characters inside a double quoted string

echo -e "Line1\nLine2"
#T# the former prints
# Line1
# Line2
# |-------------------------------------------------------------

#T# Expressions

# |-------------------------------------------------------------
#T# expressions are evaluated and return a value

#T# math expressions are written with this syntax

# SYNTAX num1=$((expr1))
#T# expr1 is the math expression, its result is assigned to num1, for the $(()) operator see S1_03_Operators.sh, specifically arithmetic expansion

int1=$((5 + 3 - 1)) # 7
# |-------------------------------------------------------------

#T# Function calls

# |-------------------------------------------------------------
#T# functions and commands use the same syntax, there are no parentheses, arguments are separated by space, arguments without quotation are taken to be strings

#T# --- Command execution

# |-----
#T# basic output to stdout with the echo command
echo "Hello, Bash!" "Second arg" # Hello, Bash! Second arg

#T# basic input from stdin with the read command
echo "Please enter var1 as input"
read var1
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