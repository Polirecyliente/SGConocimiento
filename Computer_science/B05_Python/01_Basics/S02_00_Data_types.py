
#   Data types

#T# Table of contents

#C# Types in general
#C# Numeric types
#C# String types
#C# - Bytes type
#C# Boolean type
#C# Composite types
#C# - Lists
#C# - Tuples
#C# - Dictionaries
#C# - Sets
#C# Enum type
#C# Null type
#C# Type casting

#T# Beginning of content

#C# Types in general

# |-------------------------------------------------------------
#T# get the type or class of a variable with the type function

# SYNTAX type1 = type(var1)
#T# this returns a type object with the type of var1

int1 = 8
type1 = type(int1) # <class 'int'>
# |-------------------------------------------------------------

#C# Numeric types

# |-------------------------------------------------------------
#T# numerical types are
#T#     integer
#T#     binary, with prefix 0b
#T#     octal, with prefix 0o
#T#     hexa, with prefix 0x or 0X
#T#     float, with suffix EN1 where N1 is an integer, e.g. E-2, E3, or with lowercase 'e'
#T#     complex N1 + N2j where N1, N2 are numbers, j indicates N2 as the imaginary part

#T# the following are particular examples
int1 = 5
int1 = 0b10101 # 21
int1 = 0o11    # 9
int1 = 0x17    # 23
flo1 = 64.51E2 # 6451.0
flo1 = 12.415
complex1 = 5.1 + 3.28j

#T# the digit separator is the underscore
int1 = 10_000 + 2_000 + 50 # 12050 #| the underscores can be placed anywhere in the number, e.g. 1_0_00.3_4_5 is the same as 1000.345
# |-------------------------------------------------------------

#C# String types

# |-------------------------------------------------------------
#T# strings are created inside quotation symbols, single quotes ', double quotes ", and three double quotes """
str1 = 'string one'
str2 = "string two"
str3 = """string three"""

#T# reading elements (characters) from strings
str1 = 'string one'
char1 = str1[3] # 'i'

#T# string concatenation is done with the plus operator
str1 = 'string one'
str2 = "string two"
str3 = str1 + " " + str2 # 'string one string two'

#T# strings created with different quotation symbols can be operated together like normal
str1 = 'string one'
str2 = "string two"
str3 = """string three"""
str4 = str1 + str2 + str3 # 'string onestring twostring three'

#T# escape sequences serve to do in-band signaling

# SYNTAX \char1
#T# char1 is commonly a single char, except for octal values, hex values, unicode chars, etcetera

#T# the escape sequences are
#T#     '\a', alert bell system sound
#T#     '\b', backspace
#T#     '\f', formfeed
#T#     '\r', carriage return
#T#     '\n', newline, the same as \f\r
#T#     '\t', horizontal tab
#T#     '\v', vertical tab
#T#     "\0", null char

#T#     '\\',         literal backslash
#T#     '\'',         single quote
#T#     "\"",         double quote
#T#     '\uNNNN',     unicode character  where NNNN is a 16 bit hex number
#T#     '\UNNNNNNNN', unicode 32 bit hex number
#T#     '\xNN',       hex value
#T#     '\NNN',       octal value

str1 = "Line\\1\'\nLine\"2\a\fForm\vfeed\t\blines\ror \u02A0\U00010346\x6c\0\171"
#T# printing str1 gives the following
# Line\1'
# Line"2
#       Form
# or ʠ𐍆ly   feed lines

#T# a character or char is a string of size 1, but a char can also be obtained from an integer with the chr function
str1 = 'string one'
char1 = str1[0] # 's'
char1 = chr(65) # 'A'

#C# - Bytes type

# |-----
#T# the bytes type is numerical but used extensively in strings

# SYNTAX byte1 = bytes('\NUM', encoding1)
#T# \NUM is a series of escape sequences of hex and octal numbers \xNN and \NNN, encoding1 is a string with an encoding scheme

byte1 = bytes("\x42\103", 'utf-8') # b'BC'
#T# 0x42 is 66 or "B", 0o103 is 67 or "C"
# |-----

# |-------------------------------------------------------------

#C# Boolean type

# |-------------------------------------------------------------
#T# boolean variables have only two possible values, True, False
bool1 = True
bool1 = False
# |-------------------------------------------------------------

#C# Composite types

# |-------------------------------------------------------------
#T# composite types store several values together, each value in an element of the composite type

#C# - Lists

# |-----
#T# lists are created within brackets with elements separated by comma
list1 = [3, 5, 2, "s1"]

#T# declaring, reading from, and writing to lists
list1 = ['elem1', 2, 'elem3']
int1 = list1[1] # 2
list1[1] = 5 # list1 == ['elem1', 5, 'elem3']

#T# a list with a given size can be created with list comprehension
list1 = [[None for it1 in [1, 2, 3]] for it2 in [1, 2]] # [[None, None, None], [None, None, None]]
# |-----

#C# - Tuples

# |-----
#T# tuples are read-only lists, and are created within parentheses with elements separated by comma
tuple1 = (1, 2, "s1", 9, "s2")

#T# declaring, and reading from tuples
tuple1 = ('tuple_elem1', 'tuple_elem2', 'tuple_elem3')
str1 = tuple1[2] # 'tuple_elem3'

#T# setting the value of a tuple element gives an error
# tuple1[0] = 3 # "TypeError: 'tuple' object does not support item assignment"

#T# tuples can be created without parentheses too
tuple2 = 1, 6, 5,
# |-----

#C# - Dictionaries

# |-----
#T# dictionaries are Python's hash table with key value pairs, and are created within curly braces with pairs separated by comma, and key separated from value with a colon

#T# declaring, reading from, and writing to dictionaries
dict1 = {'key1': 5, 'key2': 'val2'}
int1 = dict1['key1'] # 5
dict1['key1'] = 2 # dict1 == {'key1': 2, 'key2': 'val2'}

#T# get the keys and values of a dictionary
dict1 = {'Fis': 63.2, 'Sec': 12.1, 'Thd': 19.8}
dict1keys = dict1.keys()   # dict_keys(['Fis', 'Sec', 'Thd'])
dict1vals = dict1.values() # dict_values([63.2, 12.1, 19.8])
# |-----

#C# - Sets

# |-----
#T# sets are unordered collections, similar to a list in that they can be changed after creation, and are created within curly braces with elements separated by comma
set1 = {'elem_unord', 5, 78}

#T# given that sets are unordered, their elements can't be accessed directly, so to modify one element it must be discarded and then added
set1.discard('elem_unord')
set1.add('elem_modif')
# set1 == {'elem_modif', 5, 78}

#T# frozen sets are sets that can't be changed after creation similar to a tuple, and are created with the same syntax as a set but casted to frozenset
froz1 = frozenset({"elem_unord_froz", 12, 5, 98})
# |-----

# |-------------------------------------------------------------

#C# Enum type

# |-------------------------------------------------------------
#T# enums or enumerations map names to constant values

#T# creating an enum requires inheriting from the Enum class
from enum import Enum

#T# an enum is defined as follows

# SYNTAX definition of an enum
# class enum1(Enum):
#     elem1 = val1
#     elem2 = val2
#     elem3 = val3
#T# the enum maps elemN to valN. In the example, enum1 maps elem1 to val1

class enum1(Enum):
    elem1 = 1
    elem2 = 'two'

#T# the value attribute of an enum element has the value of the element
#T# see the enum1 definition up from here
int1 = enum1.elem1.value # 1
str1 = enum1.elem2.value # two
# |-------------------------------------------------------------

#C# Null type

# |-------------------------------------------------------------
#T# the None keyword has the null value
var1 = None
# |-------------------------------------------------------------

#C# Type casting

# |-------------------------------------------------------------
#T# type casting can be done with functions named after the wanted type, e.g. str(var1) casts var1 as a string

#T# cast from int to int base 10

# SYNTAX int(int1)
#T# this returns int1 in base 10

int1 = int(0o12) # 10

#T# cast from string to int base 10

# SYNTAX int(str1, base1)
#T# base1 is the base of str1, it can be from 2 to 36, in base 36 the number 35 is represented with a 'z', in base 35 the number 34 is 'y', and so on

str1 = "0xA4" # 0xA4 is 164
int1 = int(str1, 16) # 164

#T# the bool function casts its argument as a boolean value
bool1 = bool(5)   # True
bool1 = bool(0)   # False
bool1 = bool('a') # True

#T# cast pairs of numbers as complex numbers

# SYNTAX complex(realN, imN)
#T# realN is the real component, imN is the imaginary component

int1 = 164
flo1 = float(int1/2) # 82.0
cmp1 = complex(int1, flo1) # (164+82j)

#T# casting a bytes object as a list returns each byte as a decimal, in the following 0x41 is 65 or "A", 0x4a is 74 or "J"
byte1 = bytes("\x41\x4a", 'utf-8') # b'AJ'
list1 = list(byte1) # [65, 74] # 0x41 == 64, 0x4A == 74

#T# represent an integer in base 2 with the bin function, in base 8 with the oct function, and in base 16 with the hex function
int1 = bin(21) # 0b10101
int1 = oct(9)  # 0o11
int1 = hex(23) # 0x17

#T# cast from integer to char with the chr function, and from char to integer with the ord function
char1 = chr(0x02A0) # 'ʠ'
int1 = ord("A")     # 65

#T# casting a dictionary as a list returns only a list of the keys
dict1 = {'Fis': 63.2, 'Sec': 12.1, 'Thd': 19.8}
list1 = list(dict1) # ['Fis', 'Sec', 'Thd']

#T# other castings
cmp1 = complex(164, 82.0)
list1 = [65, 74]
str1 = str(cmp1) # '(164+82j)'
tuple1 = tuple(list1) # (65, 74)
set1 = set(list1)     # {65, 74}
dict1 = dict(key1 = 1, key2 = 2, key3 = 'val3') # {'key1': 1, 'key2': 2, 'key3': 'val3'}
tuple1 = (65, 74)
froz1 = frozenset(tuple1) # frozenset({65, 74})
# |-------------------------------------------------------------