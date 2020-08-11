
#   Basic syntax

#T# Table of contents

#T# Blocks of code
#T# Variables, constants, literals
#T# Escape sequences
#T# Expressions
#T# Function calls
#T# Statements
#T# Multiline statements
#T# Multistatement lines

#T# Beginning of content

#T# run any Python file /path/to/file1.py in a terminal with
# python3 /path/to/file1.py

#T# output variables to stdout with the print function
# print(var1,var2,var3)

#T# Blocks of code

#T# indentation acts as the delimiter (like braces)
if True:
    i1 = 70

#T# Variables, constants, literals

#T# variables are dinamically typed. Literals are characters, numbers
i1 = 'str'
i1 = 5

#T# quotation types, each quotation symbol can be used inside the others as a normal character
q1 = 'sen1word1 sen1""""word2 sen1word3 sen1word4'
q2 = "sen2word1 sen2''''word2 sen2word3 sen2word4"
q3 = """sen3word1 sen3"'"'word2
               sen3word3 sen3word4"""

#T# Escape sequences

#T# an special kind of combination of literals are escape sequences, they mean something particular, e.g. the \n means newline
q1 = "Line1\nLine2"
#T# an escape sequence starts with a backslash and is followed by other character or characters

#T# Expressions

#T# expressions are evaluated and return a value
expr1 = 5 + 3 - 7

#T# Function calls

#T# basic output to stdout with the print function
print("Hello, Python!")

#T# basic input from stdin with the input function
input                   ("\nGive an input to continue the script\n")
#T# the function name can be separated by whitespace, but not a newline, from the args in parentheses

#T# Statements

#T# an statement is a complete instruction
int1 = 5
#T# int1 = 5 is a statement, the variable int1 is made to point to the value 5

#T# use the pass keyword to create a statement that does nothing, as a filler
pass

#T# Multiline statements

#T# an expression statement is continued with a backslash at the end, a list can be continued without a comma at the end of the line
varT = 5 + 6 + \
       3 + 7
days = ['Mon','Wed'
        'Fri','Sun']

#T# Multistatement lines

#T# multiple statements in the same line are separated with a semicolon
x1 = 9; x2 = 7; x3 = 0