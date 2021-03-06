
#   Basic syntax

#T# Table of contents

#C# Blocks of code
#C# Variables, constants, literals
#C# - Type hints
#C# Escape sequences and escaped chars
#C# Expressions
#C# Function calls
#C# Statements
#C# Multiline statements
#C# Multistatement lines
#C# Metadata

#T# Beginning of content

# |-------------------------------------------------------------
#T# run a Python file /path/to/file1.py in the operating system shell with
# SYNTAX python3 /path/to/file1.py

#T# output variables to stdout with the print function
# SYNTAX print(var1, var2, var3)
#T# the same can be done by simply typing the variable's name in the Python prompt
# SYNTAX var1

#T# get help about a symbol or name (function, attribute, etc.) with the help function, used in a script or in the Python prompt
# SYNTAX help(name1)
help(round)
# |-------------------------------------------------------------

#C# Blocks of code

# |-------------------------------------------------------------
#T# indentation acts as the delimiter (like braces)
if True:
    int1 = 70
# |-------------------------------------------------------------

#C# Variables, constants, literals

# |-------------------------------------------------------------
#T# variables are dynamically typed. Literals are characters, numbers
str1 = 'str'
int1 = 5

#T# variable identifiers can only contain letters, numbers, and the underscore
var_aux1 = 0

#T# strings are created within quotation symbols, each quotation symbol type can be used inside the others as a normal character
str1 = 'sen1word1 sen1""""word2 sen1word3 sen1word4'
str1 = "sen2word1 sen2''''word2 sen2word3 sen2word4"
str1 = """sen3word1 sen3"'"'word2
               sen3word3 sen3word4"""

#C# - Type hints

# |-----
#T# type hints are used when there is no autocompletion for an object that should have, this is because the type of a dynamic type can't be known at compile time

# SYNTAX obj1 = Constructor1() # type: Object_type1
#T# the type hint is written after the comment, the autocompletion of obj1 follows the type Object_type1

var1 = 8 # type: str
# var1. autocompletes as a string
# |-----

# |-------------------------------------------------------------

#C# Escape sequences and escaped chars

# |-------------------------------------------------------------
#T# an special kind of combination of literals are escape sequences and escaped chars, escape sequences mean something particular, e.g. the \n means newline, escaped chars make operators to become literals, e.g. the {{ makes a single curly brace to be taken literally

# SYNTAX \char1
#T# an escape starts with a backslash \ and is followed by char1 which is other character or characters, most commonly char1 is a single character

# SYNTAX {{
# SYNTAX }}
#T# in interpolated strings, duplicating the curly braces escapes them

str1 = f"Line1\n{{Line2}}"
#T# printing str1 gives the following
# Line1
# {Line2}
# |-------------------------------------------------------------

#C# Expressions

# |-------------------------------------------------------------
#T# expressions are evaluated and return a value
int1 = 5 + 3 - 7 # 1
# |-------------------------------------------------------------

#C# Function calls

# |-------------------------------------------------------------
#T# a function call is made with the function name followed by a pair of parentheses that contain the arguments separated by comma

#T# the function name can be separated by whitespace (but not a newline) from the arguments in parentheses

#T# basic output to stdout is done with the print function
print("Hello, Python!")

#T# basic input from stdin is done with the input function
var1 = input                   ("\nPlease enter var1 as input\n")

#T# the arguments to a function contain positional arguments and kwarg pairs

# SYNTAX func1(pos1, pos2, kwarg1 = value1, kwarg2 = value2)
# SYNTAX func1(pos1, pos2, kwargs1)
#T# pos1 and pos2 represent positional arguments so they must be written in that order of positions at the start of the parentheses

#T# kwarg1 = value1, and kwarg2 = value2 are kwarg value pairs that allow naming arguments, these can be written in any order

#T# kwargs1 are the kwarg value pairs, this is a shorthand notation to indicate the kwarg value pairs without writing them one by one

str1 = 'string to print'
print(str1, end = '\n') #| str1 is a positional argument, and the end kwarg is used to set the character at the end of the string

#T# a function signature is a short way to write how to use a function, commonly it contains the return value, the function name, and the arguments, which is the minimum needed
# SYNTAX value1 = func1(arg1, arg2, arg3)
# |-------------------------------------------------------------

#C# Statements

# |-------------------------------------------------------------
#T# a statement is a complete instruction

int1 = 5
#T# int1 = 5 is a statement, the variable int1 is made to point to the value 5

#T# the dot notation is used to access the namespace of an object

# SYNTAX obj1.name1.name2
#T# here the object obj1 has name1 in its namespace, and name1 has name2 in its namespace

int1 = 5
int1 = int1.bit_length() # 3
#T# the bit_length function is accessed using dot notation on an integer

#T# the pass keyword is used to create a no-op statement that does nothing, as a filler
pass
# |-------------------------------------------------------------

#C# Multiline statements

# |-------------------------------------------------------------
#T# a multiline statement is created with a backslash at the end of each line, a list can be continued without a comma at the end of the line
int1 = 5 + 6 + \
       3 + 7     # 21
list1 = ['Mon', 'Wed'
        'Fri', 'Sun']
# |-------------------------------------------------------------

#C# Multistatement lines

# |-------------------------------------------------------------
#T# multiple statements in the same line are separated with a semicolon
int1 = 9; int2 = 7; int3 = 0
# |-------------------------------------------------------------

#C# Metadata

# |-------------------------------------------------------------
#T# the character encoding of a python file can be declared with the `coding` metadata placed at the start of the file, for example:
# coding=utf-8
# |-------------------------------------------------------------