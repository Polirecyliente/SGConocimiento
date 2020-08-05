
#   Arrays

#T# Table of contents

#T# Arrays in general
#T# Strings
#T# Lists
#T# Tuples
#T# Dictionaries
#T# Sets

#T# Beginning of content

#T# Arrays in general

list1 = [3,6,1,2]
#T# get the length of an array, the amount of elements it contains, with the len function
int1 = len(list1)

#T# Strings

#T# string creation, read, write
str1 = "first string"; str2 = 'str2'
str2 = str1 + ' written'

#T# membership with in, the string acts as a set of its characters
bool1 = "g" in str1

#T# include escape sequences in a string without their meaning with the raw string prefix "r" or "R"
str1 = r"\nRaw\tString"

#T# format a string ala printf with "str1 %fmt_spec1 %fmt_spec2" %(var1,var2), where each var goes into the respective position of a format specifier %fmt_spec
str1 = "string: %s, digit: %d" %("S1",514)

#T# similar format can be done with 'str1 {} str2 {}'.format(var1,var2) where the format function maps each var to a pair of curly braces in the same position
str1 = 'string: {}, digit: {}'.format("S1",514)

#T# unicode string with prefix "u" or "U"
str1 = u"gálèät"

#T# string of bytes with prefix "b" or "B", if the byte is represented as an octal number it needs three numbers \NNN and the first has the first bit ignored, so the first number shouldn't be greater than 3
str1 = b"\101\271\x6c"

int1 = 5; int2 = 7
#T# string interpolation with prefix "f" or "F", the string interpolation is done inside curly braces. If var1 = val1, print both directly with the self documenting expression {var1 = }
str1 = f"partial string {str2[9:18]}, {str2 = }"

#T# f strings can be formatted, the syntax is {expr:format1} where format1 can contain apw.P[f|b|o|x] a is the alignment symbol [<|>], p is the padding symbol, w is the width, .P is a number indicating the precision, f for float, b for binary, o for octal, x for hex, e for scientific notation
num1 = 6.4
#T# the following returns 0006.400
str2 = f'{num1:>08.3f}'

#T# Lists

#T# declaring, reading from, and writing to lists
list1 = ['elem1',2,'elem3']
int1 = list1[1]
list1[1] = 5

#T# when reading from a list, if the upper limit in a slice of the list is greater than the size of the list, it's ignored, the list is read up to its last element
str1 = list1[2:538]

#T# append an element to a list with the append function
list1.append("append_elem")

#T# remove an element from a list with the remove function
list1.remove('elem3')

list2 = ['a','b']
#T# extend a list appending all elements from another, in list1.extend(list2) the elements from list2 are appended to list1
list1.extend(list2)

#T# List functions

list1 = ['a', 5, 'append_elem', 'a', 'b']
#T# count the repetitions of an element, in list1.count('elem1') the repetitions of the element 'elem1' are counted in list1
int1 = list1.count('a')
print(int1)

print("Index of \'appEl\'",list1.index('appEl'))
list1.insert(1,'el3')
print(list1)
list1.pop(-4)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)

#T# Tuples

#T# declaration and accessing
tupl1 = ('tEl1','tElB','tF')
print(tupl1[1:3])

#T# tuple functions

#T# get the size or length of a tuple with the len(tuple1) function
var1 = len(tupl1)
var2 = max(tupl1)

#T# Dictionaries

#T# declaration, updating, and accessing
dict1 = {'key1':5,'key2':'val2'}
dict1['keyNew'] = 'newV'
print(dict1['keyNew'])

#T# clear the whole dictionary with clear()
dict1.clear()
print(dict1)

dict2 = {'key1':7,'key2':'val2'}
#T# dictionary functions
print("dict with str representation:",str(dict2))
print("type of dict var is: ",type(dict2))
dict3 = dict2.copy()
print("new dict: ",dict3)
tupl1 = ('tupK1','valNo')
dict4 = dict.fromkeys(tupl1,8)
print("dict from keys:",dict4)
print("value from key \'key2\'",dict2.get('key2'))
print("dict's items:",dict2.items())
print("dict's keys:",dict2.keys())
print("dict's values:",dict2.values())

#T# append a dictionary to another with dict1.update(dictAppended)
dict2.update(dict4)
print("append a dict to another:",dict2)
dict2.setdefault('noKey','defVal')
print("default value:",dict2['noKey'])

#T# Sets