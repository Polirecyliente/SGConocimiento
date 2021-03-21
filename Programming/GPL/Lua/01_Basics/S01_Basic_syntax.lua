--[[
#   Basic syntax
--]]

-- #T# Table of contents

-- #C# Blocks of code
-- #C# Variables, constants, literals
-- #C# Escape sequences and escaped chars
-- #C# Expressions
-- #C# Function calls
-- #C# Statements
-- #C# Multiline statements
-- #C# Multistatement lines

-- #T# Beginning of content

-- # |-------------------------------------------------------------
-- #T# run a Lua file /path/to/file1.lua in a terminal with
-- # SYNTAX lua /path/to/file1.lua

-- #T# output variables to stdout with the print function
-- # SYNTAX print(var1)

-- #T# get the type of a symbol (function, variable, value, etc)
-- # SYNTAX type(var1)
-- # |-------------------------------------------------------------

-- #C# Blocks of code

-- # |-------------------------------------------------------------
-- #T# blocks of code are enclosed with keywords, all of which are ended with the end keyword

-- #T# the basic block of code is enclosed within the do, end keywords
do
    print('function call one')
    print('function call two')
end
-- # |-------------------------------------------------------------

-- #C# Variables, constants, literals

-- # |-------------------------------------------------------------
-- #T# variables are dynamically typed. Literals are characters, numbers
str1 = 'str'
int1 = 5

-- #T# variable identifiers can only contain letters, numbers, and the underscore
var_aux1 = 0

-- #T# strings are created within quotation symbols, each quotation symbol type can be used inside the others as a normal character
str1='Hello       world!"'
str2="second str'ing"
-- # |-------------------------------------------------------------

-- #C# Escape sequences and escaped chars

-- # |-------------------------------------------------------------
-- #T# an special kind of combination of literals are escape sequences and escaped chars, escape sequences mean something particular, e.g. the \n means newline, escaped chars make operators to become literals, e.g. the \$ makes the dollar sign to be taken literally

-- # SYNTAX \char1
-- #T# an escape starts with a backslash \ and is followed by char1 which is other character or characters, most commonly char1 is a single character

-- # SYNTAX %char1
-- #T# the percent sign escapes characters in regex

print("Line1\nLine2")
-- #T# the former prints
-- # Line1
-- # Line2
-- # |-------------------------------------------------------------

-- #C# Expressions

-- # |-------------------------------------------------------------
-- #T# expressions are evaluated and return a value
int1 = 5 + 3 - 7 -- # 1
-- # |-------------------------------------------------------------

-- #C# Function calls

-- # |-------------------------------------------------------------
-- #T# a function call is made with the function name followed by a pair of parentheses that contain the arguments separated by comma

-- #T# basic output to stdout is done with the print function
print("Hello, Lua!", "Second arg") -- # Hello, Lua!    Second arg

-- #T# basic input from stdin is done with the io.read function
print("Please enter var1 as input")
var1 = io.read()

-- #T# when a function call contains only one string or table argument, the call can be made without parentheses
print"No parentheses"

-- #T# the arguments to a function contain positional arguments, kwarg pairs can be approximated with tables
print("pos1", "pos2", "pos3")
-- # |-------------------------------------------------------------

-- #C# Statements

-- # |-------------------------------------------------------------
-- #T# a statement is a complete instruction

int1 = 5
-- #T# int1 = 5 is a statement, the variable int1 is made to point to the value 5
-- # |-------------------------------------------------------------

-- #C# Multiline statements

-- # |-------------------------------------------------------------
-- #T# a multiline statement is created by leaving an incomplete statement, and continuing it in the next line
int1 = 5 + 6 +
       3 + 7   -- # 21
-- # |-------------------------------------------------------------

-- #C# Multistatement lines

-- # |-------------------------------------------------------------
-- #T# multiple statements in the same line are separated with a semicolon
int1 = 9; int2 = 7; int3 = 0
-- # |-------------------------------------------------------------