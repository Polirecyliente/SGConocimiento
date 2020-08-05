
#   Data types

#T# Table of contents

#T# Numeric types
#T# String types
#T# Boolean type
#T# Composite types
#T# Null type
#T# Type casting

#T# Beginning of content

#T# Numeric types

#T# numerical types are integer, binary 0b, octal 0o, hexa 0x, float E, complex j types. In the following, 0b10101 is 21, 0o11 is 9, 0x17 is 23, 64.51E2 is 6451.0
int1 = 5
int1 = 0b10101
int1 = 0o11
int1 = 0x17
flo1 = 64.51E2
flo1 = 12.415
complex1 = 5.1 + 3.28j

#T# String types

#T# strings are created inside quotation symbols, single quotes, double quotes, and triple double quotes
str1 = 'string one'
str2 = "string two"
str3 = """string three"""

#T# a character is a string of size 1, but a character can also be obtained from an integer with the chr function
char1 = str1[0]
char1 = chr(65)

#T# slice operator [ini_elem:final_elem] to create a slice of the original string, this includes ini_elem, up to before final_elem (excludes final_elem)
str4 = str1[2:5]
#T# [ini_elem:final_elem:stepN] step by stepN elements
str4a = str1[2:8:3]

#T# concat operator + to join strings, repetition operator * to repeat a string after itself a number of times
str4 = str2 + "|" + str1 * 2

#T# strings created with different quotation symbols can be operated together like normal
str4 = str1 + str2 + str3

#T# escape sequences are, literal backslash \\, single quote \', double quote \", bell system sound \a, backspace \b, formfeed \f, carriage return \r, newline \n (\n is the same as \f\r), horizontal tab \t, vertical tab \v, unicode character \uNNNN where NNNN is a 16 bit hex number, unicode 32 bit hex number \UNNNNNNNN, hex value \xNN, octal value \NNN
q1 = "Line\\1\'\nLine\"2\a\fForm\vfeed\t\blines\ror \u02A0\U00010346\x6c\271"

#T# the bytes type is numerical in nature but used extensively in strings, in bytes('\NUM',encoding1) \NUM is a series of escape sequences of hex and octal numbers \xNN and \NNN, encoding1 is a string containing a valid encoding scheme. In the following 0x42 is 66 or "B", 0o103 is 67 or "C"
byte1 = bytes("\x42\103",'utf-8')

#T# Boolean type

#T# boolean variables have only two possible values, True, False
bool1 = True
bool1 = False

#T# Composite types

#T# arrays are called lists, and are created within square brackets with elements separated by comma
arr1 = [3,5,2,"s1"]

#T# lists have the same operators as strings, slice operator [:], concat operator +, repetition operator *
arr2 = arr1[0]
arr2 = arr1[1:3]
arr2 = arr1[0:2] * 3 + arr1

#T# tuples are read-only lists, and are created within parentheses with elements separated by comma
tupl1 = (1,2,"s1",9,"s2")

#T# setting the value of a tuple element gives an error
# tupl1[0] = 3

#T# tuples have the same operators as strings and lists
tupl2 = tupl1[0]
tupl2 = tupl1[1:3]
tupl2 = tupl1[0:2] * 3 + tupl1

#T# tuples can be created without parentheses too
tupl2 = 1,6,5,

#T# dictionaries are python's hash table with key value pairs, and are created within curly braces with pairs separated by comma, and key separated from value with a colon
dict1 = {'Fis':63.2,'Sec':12.1,'Thd':9.8}

#T# set the value associated with a key
dict1['Thd'] = 19.8

#T# get the value associated with a key
valThd = dict1['Thd']

#T# get the keys and values of a dictionary
dict1keys = dict1.keys()
dict1vals = dict1.values()

#T# sets are unordered collections, similar to a list in that it can be changed after creation, and are created within curly braces with elements separated by comma
set1 = {'elem_unord',5,78}

#T# given that sets are unordered, their elements can't be accessed directly, so to modify one element it must be discarded and then added
set1.discard('elem_unord')
set1.add('elem_modif')

#T# frozen sets are sets that can't be changed after creation similar to a tuple, and are created with the same syntax as a set but casted to frozenset
froz1 = frozenset({"elem_unord_froz",12,5,98})

#T# common set operations are union |, intersection &, difference -, symmetric difference
set2 = set1.union(froz1)
set2 = set1 | froz1
set2 = set1.intersection(froz1)
set2 = set1 & froz1
set2 = set1.difference(froz1)
set2 = set1 - froz1
set2 = set1.symmetric_difference(froz1)

set1 = {5}
#T# comparisons between sets 

#T# subsets <, <=
set2 = set1.issubset(froz1)
set2 = set1 < froz1
set2 = set1 <= froz1

#T# supersets >, >=
set2 = set1.issuperset(froz1)
set2 = set1 > froz1
set2 = set1 >= froz1

#T# equal sets ==
set2 = set1 == froz1

#T# Null type

#T# in Python, the null type has the None keyword
str1 = None

#T# Type casting

#T# in Python, type casting can be done with functions named with the wanted type, e.g. int(var1) to cast var1 as an integer

#T# the hexa 0xA4 is 164
str1 = "0xA4"

#T# in int(var1,base1) base1 is the base of var1
int1 = int(str1,16)

flo1 = float(int1/2)

#T# in complex(realN,imN) realN is the real component and imN is the imaginary component
cmp1 = complex(int1,flo1)

#T# casting a dictionary as a list returns only a list of the keys
arr1 = list(dict1)

byte1 = bytes("\x41\x4a",'utf-8')
#T# casting a bytes object as a list returns each byte as a decimal, in the following 0x41 is 65 or "A", 0x4a is 74 or "J"
arr1 = list(byte1)

#T# castings convert the argument to the name sake of the function
str1 = str(cmp1)
tupl1 = tuple(arr1)
set1 = set(arr1)
dict1 = dict(key1=1,key2=2,key3='val3')
froz1 = frozenset(tupl1)

#T# cast from integer to character with the chr function, and from character to integer with the ord function
char1 = chr(0x02A0)
int1 = ord("A")

#T# represent an integer in base 2 with the bin function, in base 8 with the oct function, and in base 16 with the hex function
int1 = bin(21)
int1 = oct(9)
int1 = hex(23)