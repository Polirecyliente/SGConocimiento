
#   Data types

#T# Table of contents

#T# Types in general
#T# Numeric types
#T# String types
#T# --- Bytes type
#T# Boolean type
#T# Composite types
#T# --- Lists
#T# --- Tuples
#T# --- Dictionaries
#T# --- Sets
#T# Enum type
#T# Null type
#T# Type casting

#T# Beginning of content

#T# Types in general

# |-------------------------------------------------------------

# |--------------------------------------------------\
#T# get the type or class of a variable with the type function

# SYNTAX type1 = type(var1)
#T# this returns a type object with the type of var1

int1 = 8
type1 = type(int1) # <class 'int'>
# |--------------------------------------------------/

# |-------------------------------------------------------------

#T# Numeric types

# |-------------------------------------------------------------

# |--------------------------------------------------\
#T# numerical types are
#T#     integer
#T#     binary, with prefix 0b
#T#     octal, with prefix 0o
#T#     hexa, with prefix 0x
#T#     float, with suffix EN1 where N1 is an integer, e.g. E-2, E3
#T#     complex N1 + N2j where N1, N2 are numbers, j indicates N2 as the imaginary part 

#T# the following are particular examples
int1 = 5
int1 = 0b10101 # 21
int1 = 0o11    # 9
int1 = 0x17    # 23
flo1 = 64.51E2 # 6451.0
flo1 = 12.415
complex1 = 5.1 + 3.28j
# |--------------------------------------------------/

# |-------------------------------------------------------------

#T# String types

# |-------------------------------------------------------------
#T# strings are created inside quotation symbols, single quotes, double quotes, and three double quotes
str1 = 'string one'
str2 = "string two"
str3 = """string three"""

#T# reading from strings
str4 = str1[4] # 'n'

#T# a character or char is a string of size 1, but a char can also be obtained from an integer with the chr function
char1 = str1[0] # 's'
char1 = chr(65) # 'A'

# |--------------------------------------------------\
#T# strings created with different quotation symbols can be operated together like normal

str4 = str1 + str2 + str3 # 'string onestring twostring three'
#T# the plus sign concatenates the strings
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# escape sequences are
#T#     '\\' literal backslash
#T#     "\'" single quote
#T#     '\"' double quote
#T#     '\a' bell system sound
#T#     '\b' backspace
#T#     '\f' formfeed
#T#     '\r' carriage return
#T#     '\n' newline, the same as \f\r
#T#     '\t' horizontal tab
#T#     '\v' vertical tab

#T#     '\uNNNN'     unicode character  where NNNN is a 16 bit hex number
#T#     '\UNNNNNNNN' unicode 32 bit hex number
#T#     '\xNN'       hex value
#T#     '\NNN'       octal value

str1 = "Line\\1\'\nLine\"2\a\fForm\vfeed\t\blines\ror \u02A0\U00010346\x6c\271"
#T# printing str1 gives the following
# Line\1'
# Line"2
#       Form
# or ʠ𐍆l¹   feed lines
# |--------------------------------------------------/

#T# --- Bytes type

# |-----

# |--------------------------------------------------\
#T# the bytes type is numerical but used extensively in strings

# SYNTAX byte1 = bytes('\NUM', encoding1)
#T# \NUM is a series of escape sequences of hex and octal numbers \xNN and \NNN, encoding1 is a string with an encoding scheme

byte1 = bytes("\x42\103", 'utf-8') # b'BC'
#T# 0x42 is 66 or "B", 0o103 is 67 or "C"
# |--------------------------------------------------/

# |-----

# |-------------------------------------------------------------

#T# Boolean type

# |-------------------------------------------------------------
#T# boolean variables have only two possible values, True, False
bool1 = True
bool1 = False
# |-------------------------------------------------------------

#T# Composite types

# |-------------------------------------------------------------
#T# arrays store several values together, each value in an element of the array

#T# --- Lists

# |-----
#T# lists are created within brackets with elements separated by comma
list1 = [3, 5, 2, "s1"]

#T# declaring, reading from, and writing to lists
list1 = ['elem1', 2, 'elem3']
int1 = list1[1] # 2
list1[1] = 5
# |-----

#T# --- Tuples

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

#T# --- Dictionaries

# |-----
#T# dictionaries are Python's hash table with key value pairs, and are created within curly braces with pairs separated by comma, and key separated from value with a colon

#T# declaring, reading from, and writing to dictionaries
dict1 = {'key1': 5, 'key2': 'val2'}
int1 = dict1['key1'] # 5
dict1['key1'] = 2

dict1 = {'Fis': 63.2, 'Sec': 12.1, 'Thd': 19.8}
#T# get the keys and values of a dictionary
dict1keys = dict1.keys()   # dict_keys(['Fis', 'Sec', 'Thd'])
dict1vals = dict1.values() # dict_values([63.2, 12.1, 19.8])
# |-----

#T# --- Sets

# |-----
#T# sets are unordered collections, similar to a list in that they can be changed after creation, and are created within curly braces with elements separated by comma
set1 = {'elem_unord', 5, 78}

#T# given that sets are unordered, their elements can't be accessed directly, so to modify one element it must be discarded and then added
set1.discard('elem_unord')
set1.add('elem_modif')

#T# frozen sets are sets that can't be changed after creation similar to a tuple, and are created with the same syntax as a set but casted to frozenset
froz1 = frozenset({"elem_unord_froz", 12, 5, 98})
# |-----

# |-------------------------------------------------------------

#T# Enum type

# |-------------------------------------------------------------
#T# enums or enumerations map names to constant values

# |--------------------------------------------------\
#T# creating an enum requires inheriting from the Enum class
from enum import Enum

# SYNTAX definition of an enum
# class enum1(Enum):
#     elem1 = val1
#     elem2 = val2
#     elem3 = val3
#T# the enum maps elemN to valN. In the example, enum1 maps elem1 to val1

class enum1(Enum):
    elem1 = 1
    elem2 = 'two'
# |--------------------------------------------------/

#T# the value attribute of an enum element has the value of the element
int1 = enum1.elem1.value # 1
str1 = enum1.elem2.value # two
# |-------------------------------------------------------------

#T# Null type

# |-------------------------------------------------------------
#T# the null type has the None keyword
str1 = None
# |-------------------------------------------------------------

#T# Type casting

# |-------------------------------------------------------------
#T# type casting can be done with functions named after the wanted type, e.g. str(var1) casts var1 as a string

# |--------------------------------------------------\
#T# cast from int to int base 10

# SYNTAX int(int1)
#T# this returns int1 in base 10

int1 = int(0o12) # 10
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# cast from string to int base 10

# SYNTAX int(str1, base1)
#T# base1 is the base of str1, it can be from 2 to 36, in base 36 the number 35 is represented with a 'z', in base 35 the number 34 is 'y', and so on

str1 = "0xA4" # 0xA4 is 164
int1 = int(str1, 16) # 164
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# cast pairs of numbers as complex numbers

# SYNTAX complex(realN, imN)
#T# realN is the real component, imN is the imaginary component

flo1 = float(int1/2) # 82.0
cmp1 = complex(int1, flo1) # (164+82j)
# |--------------------------------------------------/

byte1 = bytes("\x41\x4a", 'utf-8') # b'AJ'
#T# casting a bytes object as a list returns each byte as a decimal, in the following 0x41 is 65 or "A", 0x4a is 74 or "J"
list1 = list(byte1) # [65, 74]

#T# represent an integer in base 2 with the bin function, in base 8 with the oct function, and in base 16 with the hex function
int1 = bin(21) # 0b10101
int1 = oct(9)  # 0o11
int1 = hex(23) # 0x17

#T# cast from integer to char with the chr function, and from char to integer with the ord function
char1 = chr(0x02A0) # 'ʠ'
int1 = ord("A")     # 65

#T# casting a dictionary as a list returns only a list of the keys
list1 = list(dict1) # ['Fis', 'Sec', 'Thd']

#T# other castings
str1 = str(cmp1) # '(164+82j)'
tuple1 = tuple(list1) # (65, 74)
set1 = set(list1)     # {65, 74}
dict1 = dict(key1 = 1, key2 = 2, key3 = 'val3') # {'key1': 1, 'key2': 2, 'key3': 'val3'}
froz1 = frozenset(tuple1) # frozenset({65, 74})
# |-------------------------------------------------------------