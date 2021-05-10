
#   Composite types

#T# Table of contents

#C# Composite types in general
#C# - Basic operators
#C# Strings
#C# - String formatting
#C# - U strings
#C# - R strings
#C# - B strings
#C# - F strings
#C# Lists
#C# Tuples
#C# Dictionaries
#C# Sets
#C# - Comparisons between sets
#C# Multidimensional composite types

#T# Beginning of content

#C# Composite types in general

# |-------------------------------------------------------------
#T# composite types can be mainly lists and tuples, but also dictionaries and sets, if a list or tuple has all elements of the same type then it's called an array, strings are always arrays of characters
str1 = "example string"
list1 = [99, 99, 1, 99, 99, 2, 99, 99, 3, 99]
tuple1 = ('elem1', 2)

#T# get the length of a composite type, the amount of elements it contains, with the len function
list1 = [99, 99, 1, 99, 99, 2, 99, 99, 3, 99]
int1 = len(list1) # 10

#C# - Basic operators

# |-----
#T# the following operators can only be applied to strings, lists, and tuples

# |--------------------------------------------------\
#T# the slice operator is used to create a slice of the original composite type

# SYNTAX arr1[ini_elem1:final_elem1]
#T# this includes ini_elem1, up to before final_elem1 (excludes final_elem1) from arr1

str1 = "example string"
str2 = str1[2:5] # amp

# SYNTAX arr1[ini_elem1:final_elem1:step1]
#T# same as before, but form the slice stepping by step1 elements

list1 = [99, 99, 1, 99, 99, 2, 99, 99, 3, 99]
list2 = list1[2:9:3] # [1, 2, 3]

#T# parts of the slice can be left out, in that case ini_elem1 defaults to 0, final_elem1 defaults to the length of the array, step1 defaults to 1
list1 = [1, 2, 3, 4, 5]
list1[:3]  # [1, 2, 3]
list1[2:]  # [3, 4, 5]
list1[::2] # [1, 3, 5]
list1[:]   # [1, 2, 3, 4, 5]
list1[1:1] # [] #| this starts at index 1 (second element) and ends at element 1 or index 0 (first element), so this list is always empty
# |--------------------------------------------------/

#T# the concatenation operator + is used to concatenate composite types
# SYNTAX arr1 + arr2 + arr3
tuple1 = ('elem1', 2)
tuple2 = tuple1 + ('elem3', 4) # ('elem1', 2, 'elem3', 4)

#T# the repetition operator * is used to repeat a composite type arr1 after itself a number of times N1
# SYNTAX arr1 * N1
tuple1 = ('elem1', 2)
tuple2 = tuple1 * 3 # ('elem1', 2, 'elem1', 2, 'elem1', 2)

#T# when reading from, or writing to a composite type, if the index is negative it is counted right to left, the last element is at index -1, the second to last is at index -2, the nth to last is at -n, and so on
list1 = ['elem1', 2, 'elem3']
str1 = list1[-3] # 'elem1'

#T# when slicing a composite type, if the upper limit is greater than its size, it's ignored, and the same goes for the lower limit in the slice if it's less than the negative size of the composite type
list1 = ['elem1', 2, 'elem3']
list2 = list1[-4:3] # ['elem1', 2, 'elem3']
# |-----

# |-------------------------------------------------------------

#C# Strings

# |-------------------------------------------------------------
#T# membership with in, the string acts as a set of its characters
str1 = "first string"
bool1 = "g" in str1 # True

#C# - String formatting

# |-----
#T# format a string à la printf

# SYNTAX "str1 %fmt_spec1 str2 %fmt_spec2 str3" %(var1, var2)
#T# var1 goes into %fmt_spec1, var2 into %fmt_spec2, and so on

str1 = "string: %s, digit: %d" %("S1", 514) # 'string: S1, digit: 514'

#T# similar format can be done using the format function

# SYNTAX 'str1 {} str2 {} str3'.format(var1, var2)
#T# the format function maps each var to a pair of curly braces in the same position

str1 = 'string: {}, digit: {}'.format("S1", 514) # 'string: S1, digit: 514'
# |-----

#C# - U strings

# |-----
#T# make an unicode string with the prefix "u" or "U", this is the default
str1 = u"gálè\u02A0ät" # 'gálèʠät'
str1 =  "gálè\u02A0ät" # 'gálèʠät'
# |-----

#C# - R strings

# |-----
#T# include escape sequences in a string without their meaning with the raw string prefix "r" or "R"
str1 = r"\nRaw\tString" # '\\nRaw\\tString'
# |-----

#C# - B strings

# |-----
#T# make a string of bytes with the prefix "b" or "B"

#T# each byte can be represented as 3 octal numbers \NNN or as two hexadecimal numbers \xNN, if the whole number is in the ascii range (less than 128) it will be represented as a character

str1 = b"\101\271\xAC" # b'A\xb9\xac', \101 is 65 or 'A', \271 is 185 or \xb9
#T# a byte as an octal number needs three numbers \NNN, the first N has the first bit ignored, so the first N shouldn't be greater than 3
# |-----

#C# - F strings

# |-----
#T# string interpolation can be made with the prefix "f" or "F", the string interpolation is done inside curly braces

# SYNTAX f'str1 {var1 = } str2 {var2}'
#T# if var1 = val1 then both are printed directly with the self documenting expression {var1 = }, var2 only gets its value val2 printed

str1 = "swords and quotes"
str2 = f"interp: {str1[2:15]}, {str1 = }" # "interp: ords and quot, str1 = 'swords and quotes'"

#T# f strings can have the numbers formatted

# SYNTAX f'{expr1:format1}'
#T# expr1 is a numeric expression, format1 has the form apw.Pt
#T#     a is the alignment, left <, right >
#T#     p is the padding, 0 for zero padding, a space for whitespace padding
#T#     w is the total width of the number, and is an integer
#T#     .P is a number indicating the precision i.e. the amount of numbers after the decimal period
#T#     t is the type, f for float, b for binary, o for octal, x for hex, e for scientific notation

num1 = 6.4
str1 = f'{num1:>08.3f}'     # 0006.400
str1 = f'{num1:< 10.1e}'    # ' 6.4e+00  '
str1 = f'{int(num1):05b}'   # '00110'
str1 = f'{int(num1):< 5o}'  # ' 6   '
str1 = f'{int(num1):x}'     # '6'

#T# escape the curly braces in an f string by duplicating the braces
str1 = f'{{1+2}} = {1+2}' # '{1+2} = 3'
# |-----

# |-------------------------------------------------------------

#C# Lists

# |-------------------------------------------------------------
#T# append an element to a list with the append function
list1 = ['elem1', 2, 'elem3']
list1.append("append_elem") # list1 == ['elem1', 2, 'elem3', 'append_elem']

#T# remove an element from a list with the remove function
list1 = ['elem1', 2, 'elem3', 'append_elem']
list1.remove('elem3') # list1 == ['elem1', 2, 'append_elem']

#T# if a list has repeated elements, and one of them is removed, then the first repetition is removed

#T# extend a list, appending all elements from another

# SYNTAX list1.extend(list2)
#T# the elements from list2 are appended to list1

list1 = ['elem1', 2, "append_elem"]
list2 = ['a', 'b']
list1.extend(list2) # list1 == ['elem1', 2, 'append_elem', 'a', 'b']

#T# insert an element at a given position

# SYNTAX list1.insert(pos1, 'insert_elem1')
#T# the element 'insert_elem1' is inserted at the index pos1 of list1, displacing the following elements to the right

list1 = ['elem1', 2, 'append_elem', 'a', 'b']
list1.insert(4, 'inserted_elem') # list1 == ['elem1', 2, 'append_elem', 'a', 'inserted_elem', 'b']

#T# pop the last element from a list, or the element at a given index

# SYNTAX list1.pop(pos1)
#T# if pos1 is not given then the last element is popped, otherwise the element at index pos1 of list1 is popped and returned

list1 = ['elem1', 2, 'append_elem', 'a', 'inserted_elem', 'b']
list1.pop(-4) # 'append_elem'
# list1 == ['elem1', 2, 'a', 'inserted_elem', 'b']

#T# Copy a list with the `copy` function.

# SYNTAX list2 = list1.copy()

#C# - List comprehension

# |-----
#T# create a list with a for using a list comprehension statement
list1 = [i1*i1 for i1 in range(5) if i1%2 == 0] # [0, 4, 16]

#T# List comprehension can be used to create multidimensional arrays
list1 = [[['a', 'b'], ['c', 'd'], ['e', 'f']], [['g', 'h'], ['i', 'j'], ['k', 'l']]]

list2 = = [[[list1[it1][it2][it3] for it1 in [0, 1]] for it2 in [0, 2]] for it3 in [0, 1]]
# [[['a', 'g'], ['e', 'k']], [['b', 'h'], ['f', 'l']]]
#T# The new multidimensional array is built from the innermost list and then outwards, so `it1` varies first, then `it2`, and then `it3`. Initially `it1, it2, it3 = [0, 0, 0]`, then `it1, it2, it3 = [1, 0, 0]`, `it1, it2, it3 = [0, 2, 0]`, `it1, it2, it3 = [1, 2, 0]`, `it1, it2, it3 = [0, 0, 1]`, `it1, it2, it3 = [1, 0, 1]`, `it1, it2, it3 = [0, 2, 1]`, and lastly `it1, it2, it3 = [1, 2, 1]`.

#T# Each dimension of the list has as many elements as its iterator, if `it2` had three elements then its corresponding list would have three elements.

#T# The iterators can be placed in any order, for example:

list1 = [[['a', 'b'], ['c', 'd'], ['e', 'f']], [['g', 'h'], ['i', 'j'], ['k', 'l']]]
list2 = [[[list1[it1][it2][it3] for it2 in [0, 2]] for it3 in [0, 1]] for it1 in [0]]
# [[['a', 'e'], ['b', 'f']]]
# |-----

# |-------------------------------------------------------------

#C# Tuples

# |-------------------------------------------------------------
#T# as read only variables, tuples have fewer functions than lists

#T# count the amount of occurrences of an element in a tuple

# SYNTAX tuple1.count('elem1')
#T# the returned value is the amout of times 'elem1' is in tuple1

tuple1 = (0, 7, 'repeated_elem', 12, 'repeated_elem', 1, 1, 'repeated_elem')
int1 = tuple1.count('repeated_elem') # 3

#T# get the index of the first occurrence of an element

# SYNTAX tuple1.index('elem1')
#T# the returned value is the index of the first occurrence of 'elem1' in tuple1

tuple1 = (0, 7, 'repeated_elem', 12, 'repeated_elem', 1, 1, 'repeated_elem')
int1 = tuple1.index('repeated_elem') # 2

#T# unpack a tuple with the tuple unpack operator *

# SYNTAX elem_var1, elem_vari, *unpack_tuple1, elem_varj, elem_varN = tuple1
#T# unpack_tuple1 has every element in tuple1 except for the elements corresponding to the suffixes of elem_var1, elem_vari, elem_varj, elem_varN

tuple1 = (1, 7, 'elem', 12, 'last_elem')
elem1, *unpack_tuple1, elemN = tuple1 # unpack_tuple1 == [7, 'elem', 12]

#T# an unpacked tuple can be passed as an argument, to pass each element as a separate arg
tuple1 = (1, 7, 'elem', 12, 'last_elem')
str1 = "Elements {} {}, and {}".format(*tuple1) # Elements 1 7, and elem
# |-------------------------------------------------------------

#C# Dictionaries

# |-------------------------------------------------------------
#T# append a new key value pair directly to a dictionary
dict1 = {'key1': 2, 'key2': 'val2'}
dict1['new_key'] = 'new_value' # dict1 == {'key1': 2, 'key2': 'val2', 'new_key': 'new_value'}

#T# get the value associated with a key

# SYNTAX dict1.get('key1')
#T# this returns the value of 'key1' in dict1

dict1 = {'key1': 2, 'key2': 'val2'}
str1 = dict1.get('key2') # 'val2'

#T# clear the whole dictionary with the clear function
dict1 = {'key1': 2, 'key2': 'val2'}
dict1.clear() # dict1 == {}

#T# copy a dictionary's contents (overwriting another) with the copy function
dict1 = {'key1': 7, 'key2': 'val2'}
dict2 = {'dict2_key': 'dict2_val'}
dict2 = dict1.copy() # {'key1': 7, 'key2': 'val2'}

#T# create a dictionary from an iterable (tuples, lists)

# SYNTAX dict.fromkeys(arr1, 'val1')
#T# use the values in arr1 as the keys, and assign to each key the value 'val1'

tuple1 = ('key1', 'key2')
dict1 = dict.fromkeys(tuple1, 85) # {'key1': 85, 'key2': 85}

#T# get a dict_items object from a dictionary, as a list of tuples, each tuple corresponding to a key value pair of the dictionary
dict1 = {'key1': 85, 'key2': 85}
dict_items1 = dict1.items() # dict_items([('key1', 85), ('key2', 85)])

#T# update a dictionary with another, new keys are appended

# SYNTAX dict1.update(dict2)
#T# the key value pairs from dict1 are updated with those of dict2

dict1 = {'key1': 85, 'key2': 85}
dict2 = {'appended_key1': 80, 'key2': 'val2'}
dict1.update(dict2) # dict1 == {'key1': 85, 'key2': 'val2', 'appended_key1': 80}

#T# unpack a dictionary 

# SYNTAX dict1 = {**dict2, **dictN}
#T# the dictionary unpack operator ** unpacks the key value pairs of a dictionary, this can only be done into another dictionary, or as an argument

dict1 = {'initial1':'ini_value1'}
dict2 = {'unpacked1':15}
dict3 = {**dict1, **dict2} # {'initial1': 'ini_value1', 'unpacked1': 15}

#T# unpacking a dictionary in an argument, passes each key value pair as a kwarg value pair
dict1 = {'base':7}
int1 = int('10', **dict1) # 7
# |-------------------------------------------------------------

#C# Sets

# |-------------------------------------------------------------
#T# common set operations are
#T#     | union
#T#     & intersection
#T#     - difference
#T#     symmetric difference

set1 = {'elem', 5}
froz1 = frozenset({"elem_froz", 62, 88, 5})
set2 = set1.union(froz1)                # {5, 'elem', 'elem_froz', 88, 62}
set2 = set1 | froz1                     # {5, 'elem', 'elem_froz', 88, 62}
set2 = set1.intersection(froz1)         # {5}
set2 = set1 & froz1                     # {5}
set2 = set1.difference(froz1)           # {'elem'}
set2 = set1 - froz1                     # {'elem'}
set2 = set1.symmetric_difference(froz1) # {'elem', 'elem_froz', 88, 62}

#C# - Comparisons between sets

# |-----
#T# subsets <, <=
set1 = {5}
froz1 = frozenset({"elem_froz", 62, 88, 5})
bool1 = set1.issubset(froz1) # True
bool1 = set1 < froz1         # True
bool1 = set1 <= froz1        # True

#T# supersets >, >=
set1 = {5}
froz1 = frozenset({"elem_froz", 62, 88, 5})
bool1 = set1.issuperset(froz1) # False
bool1 = set1 > froz1           # False
bool1 = set1 >= froz1          # False

#T# equal sets ==
set1 = {5}
froz1 = frozenset({"elem_froz", 62, 88, 5})
bool1 = set1 == froz1 # False
# |-----

# |-------------------------------------------------------------

#C# Multidimensional composite types

# |-------------------------------------------------------------
#T# create multidimensional composite types by creating them inside one another, access an element from a multidimensional composite type by index
multi_arr1 = [(1, 2), [['a.1', 'a.2'], ['b.1', 'b.2', 'b.3']], {'k1':'v1'}]
str1 = multi_arr1[1][1][2] # 'b.3'

#T# multidimensional arrays can be sliced too
arr1 = [[[1, 2], [3, 4]], [[5, 6], [7, 8, 9, 10], [11]]]
int1 = arr1[1][0:2][1][1:3][1] # 9
#| this takes index 1 of arr1 which is [[5, 6], [7, 8, 9, 10], [11]], then slice 0:2 of that is [[5, 6], [7, 8, 9, 10]], then index 1 of that is [7, 8, 9, 10], then slice 1:3 of that is [8, 9], and finally index 1 of that is 9

#T# multidimensional arrays are iterated with a nested loop for each dimension (see the file titled Control flow)

arr1 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
for dim1 in arr1:
    dim1
#T# the former prints
# [[1, 2, 3], [4, 5, 6]]
# [[7, 8, 9], [10, 11, 12]]

for dim1 in arr1:
    for dim2 in dim1:
        for dim3 in dim2:
            dim3
#T# the former prints
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# |-------------------------------------------------------------