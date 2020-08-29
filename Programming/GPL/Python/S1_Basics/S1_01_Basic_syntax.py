
#   Basic syntax

#T# Table of contents

#T# Blocks of code
#T# Variables, constants, literals
#T# --- Type hints
#T# Escape sequences
#T# Expressions
#T# Function calls
#T# Statements
#T# Multiline statements
#T# Multistatement lines

#T# Beginning of content

# |-------------------------------------------------------------
#T# run any Python file /path/to/file1.py in a terminal with
# python3 /path/to/file1.py

#T# output variables to stdout with the print function
# print(var1,var2,var3)
# |-------------------------------------------------------------

#T# Blocks of code

# |-------------------------------------------------------------
#T# indentation acts as the delimiter (like braces)
if True:
    int1 = 70
# |-------------------------------------------------------------

#T# Variables, constants, literals

# |-------------------------------------------------------------
#T# variables are dynamically typed. Literals are characters, numbers
str1 = 'str'
int1 = 5

#T# --- Type hints

# |-----

# |--------------------------------------------------\
#T# type hints are used when there is no autocompletion for an object that should have, this is because the type of a dynamic type can't be known at compile time

# obj1 = Constructor1() # type: Object_type1

#T# the type hint is written after the comment, the autocompletion of obj1 follows the type Object_type1

var1 = 8 # type: str
# var1. autocompletes as a string
# |--------------------------------------------------/

# |-----

#T# quotation types, each quotation symbol can be used inside the others as a normal character
str1 = 'sen1word1 sen1""""word2 sen1word3 sen1word4'
str1 = "sen2word1 sen2''''word2 sen2word3 sen2word4"
str1 = """sen3word1 sen3"'"'word2
               sen3word3 sen3word4"""
# |-------------------------------------------------------------

#T# Escape sequences

# |-------------------------------------------------------------

# |--------------------------------------------------\
#T# an special kind of combination of literals are escape sequences, they mean something particular, e.g. the \n means newline
str1 = "Line1\nLine2"

#T# an escape sequence starts with a backslash and is followed by other character or characters
# |--------------------------------------------------/

# |-------------------------------------------------------------

#T# Expressions

# |-------------------------------------------------------------
#T# expressions are evaluated and return a value
int1 = 5 + 3 - 7
# |-------------------------------------------------------------

#T# Function calls

# |-------------------------------------------------------------
#T# basic output to stdout with the print function
print("Hello, Python!")

# |--------------------------------------------------\
#T# basic input from stdin with the input function
input                   ("\nGive an input to continue the script\n")

#T# the function name can be separated by whitespace (but not a newline) from the args in parentheses
# |--------------------------------------------------/

# |-------------------------------------------------------------

#T# Statements

# |-------------------------------------------------------------
#T# an statement is a complete instruction

int1 = 5
#T# int1 = 5 is an statement, the variable int1 is made to point to the value 5

# |--------------------------------------------------\
#T# the dot notation is used to access the namespace of an object

# obj1.name1.name2

#T# here the object obj1 has name1 in its namespace, and name1 has name2 in its namespace

int1 = int1.bit_length() # 3
#T# the bit_length function is accessed using dot notation on an integer
# |--------------------------------------------------/

#T# the pass keyword is used to create a statement that does nothing, as a filler
pass
# |-------------------------------------------------------------

#T# Multiline statements

# |-------------------------------------------------------------
#T# an expression statement is continued with a backslash at the end, a list can be continued without a comma at the end of the line
int1 = 5 + 6 + \
       3 + 7     # 21
list1 = ['Mon','Wed'
        'Fri','Sun']
# |-------------------------------------------------------------

#T# Multistatement lines

# |-------------------------------------------------------------
#T# multiple statements in the same line are separated with a semicolon
int1 = 9; int2 = 7; int3 = 0
# |-------------------------------------------------------------