--[[
#   Data types
--]]

-- #T# Table of contents

-- #C# Types in general
-- #C# Numeric types
-- #C# String types
-- #C# Boolean type
-- #C# Composite types
-- #C# Null type
-- #C# Type casting

-- #T# Beginning of content

-- #C# Types in general

-- # |-------------------------------------------------------------
-- #T# get the type of a symbol with the type function

-- # SYNTAX str1 = type(var1)
-- #T# this returns a string str1 with the type of var1

int1 = 8
str1 = type(int1) -- # number
-- # |-------------------------------------------------------------

-- #C# Numeric types

-- # |-------------------------------------------------------------
-- #T# numerical types are
-- #T#     integer
-- #T#     hexa, with prefix 0x or 0X
-- #T#     float, with suffix EN1 where N1 is an integer, e.g. E-2, E3, or with lowercase 'e'

-- #T# the following are particular examples
int1 = 5
int1 = 0x17    -- # 23
flo1 = 64.51E2 -- # 6451.0
flo1 = 12.415
-- # |-------------------------------------------------------------

-- #C# String types

-- # |-------------------------------------------------------------
-- #T# strings are created inside quotation symbols, single quotes ' or double quotes "
str1 = 'string one'
str2 = "string two"

-- #T# reading elements (characters) from strings is done with the string.sub function
str1 = 'string one'
char1 = string.sub(str1, 4, 4) -- # i

-- #T# string concatenation is done with the dot dot operator
str1 = 'string one'
str2 = "string two"
str3 = str1 .. " " .. str2 -- # string one string two

-- #T# escape sequences serve to do in-band signaling

-- # SYNTAX \char1
-- #T# char1 is commonly a single char, except for octal values, hex values, unicode chars, etcetera

-- #T# the escape sequences are
-- #T#     "\a", alert bell system sound
-- #T#     "\b", backspace
-- #T#     "\f", formfeed
-- #T#     "\r", carriage return
-- #T#     "\n", newline, the same as \f\r
-- #T#     "\t", horizontal tab
-- #T#     "\v", vertical tab
-- #T#     "\0", null char

-- #T#     "\\",    literal backslash
-- #T#     '\'',    single quote
-- #T#     "\"",    double quote
-- #T#     "\xNN",  hex value
-- #T#     "\0NNN", octal value

str1="Line\\1\nLine\"2\a\fForm\vfeed\t\blines\ror \x6c\0a"
-- #T# printing str1 gives the following
-- # Line\1
-- # Line"2
-- #      Form
-- # or la    feed lines
-- # |-------------------------------------------------------------

-- #C# Boolean type

-- # |-------------------------------------------------------------
-- #T# boolean variables have only two possible values, true, false
bool1 = true
bool1 = false

-- #T# only the values false and nil return a false value, any other value returns a true value, i.e. numbers, strings, the number zero, the empty string
-- # |-------------------------------------------------------------

-- #C# Composite types

-- # |-------------------------------------------------------------
-- #T# composite types store several values together, each value in an element of the composite type

-- #T# tables are the only composite type, they are created with curly braces
table1 = {}

-- #T# as associative arrays, tables contain key value pairs

-- # SYNTAX table1 = {key1 = value1, key2 = value2}
-- #T# keys must not be strings, nor numbers, but rather identifiers, values can be numbers, strings, variables, other tables, functions, etcetera

table1 = {key1 = 'value1', key2 = 2}

-- # SYNTAX table1["key1"] = 'new_value1'
-- #T# this syntax sets the value in key1 to 'new_value1'

table1["key1"] = 'new_value1'

-- # SYNTAX table1.key1 = 'new_value1'
-- #T# same as before

table1.key1 = 'new_value1'

-- #T# declaring, reading from, and writing to tables
table1 = {key1 = 'value1', key2 = 2}
int1 = table1.key2 -- # 2
table1["new_key1"] = 'new_value1' -- #| the key new_key1 is created
-- # |-------------------------------------------------------------

-- #C# Null type

-- # |-------------------------------------------------------------
-- #T# the nil keyword has the null value
var1 = nil
-- # |-------------------------------------------------------------

-- #C# Type casting

-- # |-------------------------------------------------------------
-- #T# type casting can be done with functions named 'totype1', where type1 is the resulting type after casting

-- #T# cast to a number with the tonumber function
str1 = '5'
int1 = tonumber(str1) -- # 5

-- #T# cast to a string with the tostring function
int1 = 39
str1 = tostring(int1) -- # 39
-- # |-------------------------------------------------------------