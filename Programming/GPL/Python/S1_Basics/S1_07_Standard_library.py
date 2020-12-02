
#   Standard library

#T# Table of contents

#C# Basic functions
#C# Math functions
#C# --- Basic math
#C# --- Trigonometry
#C# --- Randon number generation
#C# String functions
#C# --- Alignment
#C# --- Encoding
#C# --- Substring finding
#C# --- Predicate logic
#C# --- Case modification
#C# --- String modification
#C# List functions
#C# Dictionary functions
#C# Datetime functions
#C# --- Datetime parts
#C# --- Timezones
#C# --- Datetime formatting
#C# --- Calendar usage
#C# --- Locales
#C# Class functions
#C# --- Predicate logic
#C# Regex matching
#C# --- Regex functions, methods, and attributes
#C# --- Characters
#C# --- Quantifiers
#C# --- Character classes
#C# --- Groupings
#C# --- Subroutines and conditionals
#C# --- Anchors and boundaries
#C# --- Lookarounds
#C# --- Regex modifiers
#C# Builtin values
#C# --- Constants

#T# Beginning of content

#C# Basic functions

# |-------------------------------------------------------------
#T# get input from stdin with the input function, it returns a string which can be cast to any needed type
str1 = input("Enter the input:")

#T# the map function applies a given function to the elements of an array and returns a map object with the return values, that can be cast as an array

# SYNTAX map(func1, arr1)
#T# the returned map object has the result of applying func1 to each element in arr1

list1 = [-11, 3, -25]
map1 = map(abs, list1)
list2 = list(map1) # [11, 3, 25]

#T# the filter function uses a given function to filter the elements of an array and returns a filter object that can be cast as an array

# SYNTAX filter(func1, arr1)
#T# the returned filter object has the elements from arr1 for which func1 returns True

list1 = ['1', '2', 'elem']
filter1 = filter(str.isalpha, list1)
list2 = list(filter1) # ['elem']

#T# the repr function returns a string representation of its argument, in most cases just surrounding the argument in quotes
str1 = repr(map1) # '<map object at 0x7fd71dea0610>'

#T# the following function func1 is used to show functions used in different scopes, those functions can be used outside as well, no need for func1
def func1():
    int1 = 85

#T# the locals function returns a dictionary of local names paired to their values
    dict1 = locals()  # {'int1': 85}

#T# the vars function returns the __dict__ class attribute of the argument, which is a dictionary that contains the attributes of the argument paired to their values, without argument it acts as the locals function
    dict1 = vars() # {'int1': 85, 'dict1': {...}}
    dict1 = vars(type(int1)) # long dictionary, int1 alone doesn't have the __dict__ attribute, but the return of the type function has it

#T# the globals function returns a dictionary of global names paired to their values
    dict1 = globals() # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f77256c8be0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'S1_07_Standard_library.py', '__cached__': None, 'str1': '<map object at 0x7f77256204f0>', 'list1': ['1', '2', 'elem'], 'map1': <map object at 0x7f77256204f0>, 'list2': ['elem'], 'filter1': <filter object at 0x7f7725620e50>, 'func1': <function func1 at 0x7f77256b91f0>}

#T# the dir function without argument returns a list of local names, and with an argument, it returns a list with the attributes of the argument
    list1 = dir()      # ['dict1', 'int1']
    list1 = dir(dict1) # ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

    return None
# |-------------------------------------------------------------

#C# Math functions

# |-------------------------------------------------------------
#T# math functions are provided in the math module
import math

#C# --- Basic math

# |-----
#T# the abs function returns the absolute value of a number
x = -5.15
flo1 = abs(x) # 5.15

#T# the ceil function returns the ceiling of a number
x = -5.15
int1 = math.ceil(x) # -5

#T# the floor function returns the floor of a number
x = -5.15
int1 = math.floor(x) # -6

#T# the trunc function truncates a number (rounds it towards zero)
x = -2.5
int1 = math.trunc(x) # -2

#T# the pi constant approximates the value of pi
flo1 = math.pi # 3.14159...

#T# the e constant approximates the value of e
flo1 = math.e # 2.71828...

#T# the sum function returns the sum of all elements in an array
list1 = [2, 3, 2]
int1 = sum(list1) # 7

#T# the prod function returns the product of all elements in an array
list1 = [2, 3, 2]
int1 = math.prod(list1) # 12

#T# the sqrt function returns the square root of a number
y = 4
flo1 = math.sqrt(y) # 2.0

#T# the pow function raises a number to another
y = 4
int1 = pow(y, 2) # 16

#T# the exp function raises e to the power of a number
y = 4
flo1 = math.exp(y) # 54.598...

#T# the log function returns the log of a number in a given base
y = 4
flo1 = math.log(y, 3) # 1.26...

#T# the log10 function returns the log of a number in base 10
y = 4
flo1 = math.log10(y) # 0.60...

#T# the max function returns the maximum of the arguments
x = -5.15; y = 4
num1 = max(x, y) # 4

#T# the min function returns the minimum of the arguments
x = -5.15; y = 4
num1 = min(x, y) # -5.15

#T# the modf function returns a tuple with the fractional part and the integer part of a number
x = -5.15
tuple1 = math.modf(x) # (-0.15, -5.0); x == -5.15
flo1 = tuple1[0]      # -0.15
int1 = int(tuple1[1]) # -5

#T# the round function rounds a number to a given precision, if the precision is negative it's is rounded to the left of the decimal point
x = -5.15
flo1 = round(100*x, -1) # -520.0
# |-----

#C# --- Trigonometry

# |-----
#T# the sin function returns the sine of a number in radians
flo1 = math.sin(math.pi/4) # 0.7071... == 1/math.sqrt(2)

#T# the cos function returns the cosine of a number in radians
flo1 = math.cos(math.pi*3/4) # -0.7071... == -1/math.sqrt(2)

#T# the tan function returns the tangent of a number in radians
flo1 = math.tan(math.pi/4) # 1.0 == 1/1

#T# the asin function returns the arc sine in radians of a number
flo1 = math.asin(1/math.sqrt(2)) # 0.7853... == math.pi/4

#T# the acos function returns the arc cosine in radians of a number
flo1 = math.acos(-1) # 3.1415... == math.pi

#T# the atan function returns the arc tangent in radians of a number
flo1 = math.atan(1) # 0.7853 == math.pi/4

#T# the atan2 function returns the arc tangent in radians by taking the triangle legs as arguments
# SYNTAX math.atan2(opposite_leg1, adjacent_leg1)
flo1 = math.atan2(0, -1) # 3.1415... == math.pi

#T# the hypot function returns the hypotenuse given the triangle legs
flo1 = math.hypot(3, 4) # 5.0

#T# the degrees function converts radians into degrees
flo1 = math.degrees(math.pi/4) # 45.0

#T# the radians function converts degrees into radians
flo1 = math.radians(45) # 0.7853 == math.pi/4
# |-----

#C# --- Randon number generation

# |-----
import random

#T# the choice function chooses a random element from an array
str1 = "random string"
str2 = random.choice(str1) # 'd', or another element in str1

#T# the randrange function returns a random number from a range
# SYNTAX random.randrange(iniN, endN, stepN)
#T# the random number is one the numbers starting at iniN, stepping by stepN, and ending at endN - 1
int1 = random.randrange(1, 12, 3) # 7, or another element from the range

#T# the random function generates a random number in the [0, 1) interval
flo1 = random.random() # 0.7156...

#T# the seed function sets the random generation seed
random.seed(2) # None

#T# the uniform function returns an uniform random number
# SYNTAX random.uniform(iniN, endN)
#T# the returned number is in the [iniN, endN) interval
flo1 = random.uniform(3, 5) # 4.4719...
# |-----

# |-------------------------------------------------------------

#C# String functions

# |-------------------------------------------------------------
#T# string functions have several categories to work with strings

#C# --- Alignment

# |-----
#T# center a string with a given padding
# SYNTAX str1.center(width1, char1)
#T# str1 is centered in the width width1, char1 is used to make the padding
str1 = "Cen"
str1 = str1.center(9, "-") # '---Cen---'

#T# left justify a string, same arguments as in the center function
str1 = "Left"
str1 = str1.ljust(7, ">") # 'Left>>>'

#T# right justify a string, same arguments as in the center function
str1 = "Right"
str1 = str1.rjust(8, "<") # '<<<Right'

#T# strip the whitespace, or the given chars at both sides of a string with the strip function
# SYNTAX str1.strip(['chars1'])
#T# strips all chars in 'chars1' from both sides of str1
str1 = 'abb' + "elabele" + 'baa' # 'abbelabelebaa'
str1 = str1.strip('abe') # 'label'

#T# strip leading whitespace or given chars at the left of a string with the lstrip function, same arguments as in the strip function
str1 = "     Stripped     "
str1 = str1.lstrip() # 'Stripped     '

#T# strip trailing whitespace or given chars at the right of a string with the rstrip function, same arguments as in the strip function
str1 = "Stripped     "
str1 = str1.rstrip() # 'Stripped'

#T# the zfill function fills a string with zeros up to a given width
# SYNTAX str1.zfill(width1)
#T# str1 is filled up to the width width1, padding with zeros to the left
str1 = "zfilled"
str1 = str1.zfill(10) # '000zfilled'
# |-----

#C# --- Encoding

# |-----
#T# encode a string to bytes with the encode function, decode bytes to string with the decode function
str1 = 'string'
byte1 = str1[3:].encode('utf-8') + b"\x41\x20\x21" # b'ingA !'
str2 = byte1.decode('utf-16')         # '湩䅧℠'

#T# a few valid encodings, 'utf-8', 'utf-16', 'utf-32', 'unicode-escape', 'ascii', 'Latin-1', 'cp1252' cp is for code pages, chinese 'big5', arabic 'iso8859_6', greek 'mac_greek', hebrew 'cp424'
byte1 = b'ingA !'
str2 = byte1.decode('unicode-escape') # 'ingA !'
str2 = byte1.decode('ascii')          # 'ingA !'
str2 = byte1.decode('Latin-1')        # 'ingA !'
str2 = byte1.decode('cp1252')         # 'ingA !'
str2 = byte1.decode('big5')           # 'ingA !'
str2 = byte1.decode('iso8859_6')      # 'ingA !'
str2 = byte1.decode('mac_greek')      # 'ingA !'
str2 = byte1.decode('cp424')          # 'ש>קא\x80\x81'

#T# can't decode an utf-8 encoded string in utf-32 unless extra bytes are added
byte1 = b'ingA !'
str2 = byte1.decode('utf-32') # UnicodeDecodeError: 'utf-32-le' codec can't decode bytes in position 0-3: code point not in range(0x110000)

#T# When encoding with 'unicode-escape' the returned byte object contains the unicode escape sequence \uNNNN or \xNN for non ascii chars
str1 = "ü\u02A0" # 'üʠ'
byte1 = str1.encode('unicode-escape') # b'\\xfc\\u02a0'
# |-----

#C# --- Substring finding

# |-----
#T# count repetitions of substrings
# SYNTAX str1.count("substr"[, startN[, endN]])
#T# "substr" is counted in the string slice str1[startN:endN]
str1 = "in inner innings"
int1 = str1.count("in") # 4

#T# check if a string starts or ends with a given string

# SYNTAX str1.startswith("substr1"[, startN[, endN]])
# SYNTAX str1.endswith("substr2"[, startN[, endN]])
#T# returns True if str1[startN:endN] starts with "substr1", or ends with "substr2" respectively

str1 = "First to Last"
bool1 = str1.startswith("rst", 2)   # True
bool1 = str1.endswith("Las", 0, 12) # True

#T# get the pos of the first substring found in a string, same arguments as in the startswith function
str1 = "to be found"
int1 = str1.find('fou', 2, -1) # 6

#T# do the same as the find function but raise an exception on failure with the index function, same arguments as in the startswith function
str1 = "to be found"
int1 = str1.index('fou') # 6

#T# do a reverse find, in the sense of starting the search at the end of the string, with the functions rfind, and rindex, same arguments as in the startswith function
str1 = "to be found"
int1 = str1.rfind("nd", 3, 45)  # 9
int1 = str1.rindex("nd", 3, 37) # 9
# |-----

#C# --- Predicate logic

# |-----
#T# check if a string is only made of alphabetic chars, no whitespace or numbers allowed
str1 = "test5trin6"
bool1 = str1.isalpha() # False

#T# check if a string is made with numbers, the difference in the following functions is according to unicode definition
str1 = "test5trin6"
bool1 = str1.isdigit()   # False
bool2 = str1.isnumeric() # False
bool3 = str1.isdecimal() # False

#T# check if a string is only made of alphanumeric chars
str1 = "test5trin6"
bool1 = str1.isalnum() # True

#T# check if a string is all whitespace
str1 = "test5trin6"
bool1 = str1.isspace() # False

#T# check if a string is all lowercase
str1 = 'New Te5T'
bool1 = str1.islower() # False

#T# check if a string is in title case, numbers start new words
str1 = 'New Te5T'
bool1 = str1.istitle() # True

#T# check if a string is in upper case
str1 = 'New Te5T'
bool1 = str1.isupper() # False
# |-----

#C# --- Case modification

# |-----
#T# capitalize the first letter of the string
str1 = "case changer"
str1 = str1.capitalize() # 'Case changer'

#T# make all letters uppercase with the upper function
str1 = 'Case changer'
str1 = str1.upper() # 'CASE CHANGER'

#T# make all letters lowercase with the lower function
str1 = 'CASE CHANGER'
str1 = str1.lower() # 'case changer'

#T# make a string title cased with the title function
str1 = 'case changer'
str1 = str1.title() # 'Case Changer'

#T# swap the case of a string with the swapcase function
str1 = 'Case Changer'
str1 = str1.swapcase() # 'cASE cHANGER'
# |-----

#C# --- String modification

# |-----
#T# change the tab size with the expandtabs function
str1 = "With\texpanded\ttabs"
str1 = str1.expandtabs(5) # 'With expanded  tabs'

#T# join the string elements of an array

# SYNTAX "insert1".join(arr1) 
#T# arr1 must be an array of strings, the returned string has "insert1" between each pair of elements in arr1

arr1 = ("elem1", "elem2")
str1 = "-|-".join(arr1) # 'elem1-|-elem2'

#T# split a string into elements of a list

# SYNTAX str1.split("separator1")
#T# str1 is split at each occurrence of the substring "separator1", leaving out said substring

str1 = 'elem1-|-elem2'
list1 = str1.split("-|") # ['elem1', '-elem2']

#T# split around newlines

# SYNTAX str1.splitlines([bool1])
#T# bool1 determines whether or not to keep ends (the newlines), defaults to False

str1 = "line1\nline2 w1\nline3 w1 w2"
list1 = str1.splitlines(True) # ['line1\n', 'line2 w1\n', 'line3 w1 w2']

# |--------------------------------------------------\
#T# create a dictionary with a translation table with the maketrans function, and use it with the translate function

# SYNTAX str.maketrans(str1, str2, str3)
#T# each char in str1 gets translated to str2 (so str1, str2 have the same size), and each char in str3 is translated to None

# SYNTAX str1.translate(dict1)
#T# the chars in str1 get translated according to the translation table in dict1

str1 = "Partial string"
dict1 = str.maketrans("aeiou", "12345", "s") # {97: 49, 101: 50, 105: 51, 111: 52, 117: 53, 115: None}
str1 = str1.translate(dict1) # 'P1rt31l tr3ng'
# |--------------------------------------------------/

#T# replace a substring for another, in a string
# SYNTAX str1.replace("substr1", "replace1", countN)
#T# the first countN occurrences of "substr1" in str1 are replaced by the substring "replace1"
str1 = "t string t"
str1 = str1.replace("t", "67", 2) # '67 s67ring t'
# |-----

# |-------------------------------------------------------------

#C# List functions

# |-------------------------------------------------------------
#T# count the repetitions of an element in a list

# SYNTAX list1.count('elem1')
#T# the repetitions of the element 'elem1' in list1 are counted

list1 = ['a', 5, 'stray_elem', 'a', 'elem5']
int1 = list1.count('a') # 2

#T# get the index of the first occurrence

# SYNTAX list1.index('elem1')
#T# this returns the index of the first occurrence of 'elem1' in list1

list1 = ['a', 5, 'stray_elem', 'a', 'elem5']
int1 = list1.index('elem5') # 4

#T# reverse the order of the elements with the reverse function, it returns None, so it shouldn't be assigned to a var
list1 = ['a', 5, 'stray_elem', 'a', 'elem5']
list1.reverse() # list1 == ['elem5', 'a', 'stray_elem', 5, 'a']

#T# sort elements in a list

# SYNTAX list1.sort([reverse = True|False[, key = func1]])
#T# the default order is ascending, if the reverse kwarg is True then the order is descending, the elements of list1 must be strings

#T# the key kwarg is for the sorting function func1, the result is sorted from smaller to bigger return values of this sorting function, the default is alphabetical order

list1 = ['elem5', 'a', 'stray_elem', '5', 'a']
list1.sort(reverse = True, key = len) # ['stray_elem', 'elem5', 'a', '5', 'a']

#T# shuffle the elements of a list
list1 = ['elem5', 'a', 'stray_elem', '5', 'a']
random.shuffle(list1) # ['a', 'elem5', '5', 'a', 'stray_elem'] or other
# |-------------------------------------------------------------

#C# Dictionary functions

# |-------------------------------------------------------------
#T# create a new key value pair in a dictionary only if the key doesn't already exists with the setdefault function

# SYNTAX dict1.setdefault('new_key1', 'new_val1')
#T# the pair 'new_key1', 'new_val1' will be added to dict1 only if 'new_key1' is not in dict1 already

dict1 = {'key1': 85, 'key2': 85}
dict1.setdefault('new_key', 'new_val') # new_val
dict1.setdefault('key2', 'val2') # 85
# |-------------------------------------------------------------

#C# Datetime functions

# |-------------------------------------------------------------
#T# import the time, calendar modules
import time
import calendar

#C# --- Datetime parts

# |-----
#T# the principal datetime parts are, date, and time, date is mainly the year, month, day, and time is mainly the hour, minute, second

#T# the time.time() function returns a float with the current time in seconds since the UNIX Epoch which is 1 Jan 1970 00:00
flo1 = time.time() # 1597299316.1336622 # or Thu Aug 13 01:15:16 2020

#T# convert the time in seconds to a struct_time object with the date and time from the local region with the localtime function
struct_time1 = time.localtime(flo1) # time.struct_time(tm_year=2020, tm_mon=8, tm_mday=13, tm_hour=1, tm_min=15, tm_sec=16, tm_wday=3, tm_yday=226, tm_isdst=0)

#T# the elements in an struct_time object have self explaining names, when casted as an array, only the values become elements
struct_time1 = time.localtime(flo1) # time.struct_time(tm_year=2020, tm_mon=8, tm_mday=13, tm_hour=1, tm_min=15, tm_sec=16, tm_wday=3, tm_yday=226, tm_isdst=0)
tuple1 = tuple(struct_time1) # (2020, 8, 13, 1, 15, 16, 3, 226, 0)
# |-----

#C# --- Timezones

# |-----
#T# the gmtime function returns an struct_time object with the date and time in gmt
struct_time2 = time.gmtime() # time.struct_time(tm_year=2020, tm_mon=8, tm_mday=13, tm_hour=6, tm_min=10, tm_sec=55, tm_wday=3, tm_yday=226, tm_isdst=0)

#T# the altzone constant is the local difference to UTC in seconds
int1 = time.altzone # 18000
int1 /= 3600 # 5.0

#T# the timezone constant it the local timezone in seconds
int1 = time.timezone # 18000

#T# the mktime function converts a struct_time object in local time into the seconds from Epoch
flo1 = 1597299316.1336622
flo2 = time.mktime(time.localtime(flo1)) # 1597299316.0
flo2 = time.mktime(time.gmtime(flo1))    # 1597317316.0 == 1597299316 + 18000
#          original flo1 for comparison == 1597299316.1336622

#T# the timegm function returns the number of seconds from Epoch in GMT
struct_time1 = time.localtime(flo1) # time.struct_time(tm_year=2020, tm_mon=8, tm_mday=13, tm_hour=1, tm_min=15, tm_sec=16, tm_wday=3, tm_yday=226, tm_isdst=0)
flo2 = calendar.timegm(struct_time1) # 1597281316   == 1597299316 - 18000
# |-----

#C# --- Datetime formatting

# |-----
#T# the asctime function formats a struct_time object as a string
struct_time1 = time.localtime(flo1) # time.struct_time(tm_year=2020, tm_mon=8, tm_mday=13, tm_hour=1, tm_min=15, tm_sec=16, tm_wday=3, tm_yday=226, tm_isdst=0)
str1 = time.asctime(struct_time1) # 'Thu Aug 13 01:15:16 2020'

#T# the ctime function formats the seconds from Epoch in local time as a string
flo1 = 1597299316.1336622
str1 = time.ctime(flo1) # 'Thu Aug 13 01:15:16 2020'

#T# the strftime function converts a struct_time object into a string with a custom format through format codes that start with the percent sign %

# SYNTAX format codes of the strftime function
#T#     %a, locale weekday name abbreviated
#T#     %A, locale weekday name
#T#     %b, locale month name abbreviated
#T#     %B, locale month name
#T#     %c, locale default format
#T#     %C, century number
#T#     %d, day of the month with zero padding
#T#     %D, shorthand for %m/%d/%y
#T#     %e, day of the month
#T#     %F, shorthand for %Y-%m-%d
#T#     %g, year with two digits
#T#     %G, year
#T#     %h, equivalent to %b
#T#     %H, hour in 24 hours format
#T#     %I, hour in 12 hours format
#T#     %j, day of the year
#T#     %k, same as %H, but with space padding
#T#     %l, same as %I, but with space padding
#T#     %m, month number
#T#     %M, minute
#T#     %n, newline char
#T#     %p, AM or PM in a 12 hour clock
#T#     %P, same as %p, but lowercase
#T#     %r, shorthand for %I:%M:%S %p
#T#     %R, shorthand for %H:%M
#T#     %s, seconds from epoch
#T#     %S, second
#T#     %t, tab char
#T#     %T, shorthand for %H:%M:%S
#T#     %u, weekday number, monday is 1
#T#     %U, week of the year, starting monday
#T#     %V, week of the year, ISO 8601
#T#     %w, weekday number, sunday is 0
#T#     %W, week of the year, starting sunday
#T#     %x, shorthand for %m/%d/%y
#T#     %X, shorthand for %H:%M:%S
#T#     %y, year with two digits
#T#     %Y, year
#T#     %z, timezone change
#T#     %Z, timezone name
#T#     %%, escaped char %

struct_time1 = time.localtime(flo1) # time.struct_time(tm_year=2020, tm_mon=8, tm_mday=13, tm_hour=1, tm_min=15, tm_sec=16, tm_wday=3, tm_yday=226, tm_isdst=0)
str1 = time.strftime("%A%B%C %d%t%u %G %h %Hor%I %j %m%M%n%p%S %V %W %w %y %z%%", struct_time1)
#T# printing str1 yields
# ThursdayAugust20 13     4 2020 Aug 06or06 226 0810
# AM55 33 32 4 20 +0000%

#T# the strptime function converts a string in a given format using format codes into an struct_time object

# SYNTAX time.strptime("str_date1", "str_format1")
#T# the string "str_date1" is parsed according to "str_format1"

struct_time2 = time.strptime("Nov 2021 8", "%b %Y %H") # time.struct_time(tm_year=2021, tm_mon=11, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=305, tm_isdst=-1)
# |-----

#C# --- Calendar usage

# |-----
#T# make the calendar for a given month with the calendar.month() function

# SYNTAX calendar.month(year1, month1)
#T# this returns a string with the calendar of month1 from year1

str1 = calendar.month(2020, 2)
#T# printing str1 yields
#    February 2020
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29

#T# make the calendar for a given year with the calendar.calendar() function, this prints similar to the example of calendar.month() but for all months in the year
str1 = calendar.calendar(2020)

#T# check if a given year is leap
bool1 = calendar.isleap(2020) # True

#T# the leapdays function returns the number of leap days in a time interval
# SYNTAX calendar.leapdays(ini_year1, end_year1)
#T# the count of leap days is done between ini_year1, and end_year1
int1 = calendar.leapdays(2020, 2029) # 3

#T# the monthcalendar function returns a list of lists

# SYNTAX list1 = calendar.monthcalendar(year1, month1)
#T# list1 holds the days of month1 from year1, with one inner list for each week of month1

list1 = calendar.monthcalendar(2002, 3) # [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31]]

#T# the monthrange function returns a tuple with the first weekday number, and the number of days in a given month

# SYNTAX tuple1 = calendar.monthrange(year1, month1)
#T# tuple1 contains the first weekday number of month1, and its number of days

tuple1 = calendar.monthrange(1999, 4) # (3, 30)

#T# the weekday function returns the weekday from a given day

# SYNTAX calendar.weekday(year1, month1, day1)
#T# this returns the weekday number of day1 in month1 from year1

int1 = calendar.weekday(1999, 4, 1) # 3
# |-----

#C# --- Locales

# |-----
#T# locales are managed through the locale module
import locale

#T# list the available locales with the locale_alias dictionary
locale.locale_alias # the output is too large to display here

#T# get the current locale in a given category with the getlocale function
locale.getlocale(locale.LC_CTYPE) # ('en_US', 'UTF-8')

#T# change the locale in a given category with the setlocale function
locale.setlocale(locale.LC_TIME, "es_CO.UTF-8")
# |-----

# |-------------------------------------------------------------

#C# Class functions

# |-------------------------------------------------------------
class Class1:
    pass

class Derived1 (Class1):
    pass

obj1 = Class1()

#C# --- Predicate logic

# |-----
#T# check if a class is a subclass of another
bool1 = issubclass(Derived1, Class1) # True

#T# check if an object is an instance of a class
bool1 = isinstance(obj1, Class1) # True
# |-----

# |-------------------------------------------------------------

#C# Regex matching

# |-------------------------------------------------------------
#T# import the regex module to use regular expressions, it supersedes the re module
import regex

#C# --- Regex functions, methods, and attributes

# |-----
#T# compile a regex object with the compile function, this object has access to the rest of regex functions, methods, and attributes shown here, via dot notation
regex_object1 = regex.compile(r'pattern1') # regex.Regex('pattern1', flags=regex.V0)
search1 = regex_object1.search('str1 pattern1 str2') # <regex.Match object; span=(5, 13), match='pattern1'>

#T# match at the start of the string with the match function, if the match fails then None is returned
# SYNTAX match('pattern1', 'str1')
match1 = regex.match(r'a', 'aabbcc') # <regex.Match object; span=(0, 1), match='a'>

#T# match at any place of the string with the search function, if the match fails then None is returned
# SYNTAX search('pattern1', 'str1')
search1 = regex.search(r'(bc)(cd)', 'aabbccdd') # <regex.Match object; span=(3, 7), match='bccd'>

#T# get a list with the regex groups found with the groups function
search1 = regex.search(r'(bc)(cd)', 'aabbccdd') # <regex.Match object; span=(3, 7), match='bccd'>
tuple1 = search1.groups() # ('bc', 'cd')

#T# get a particular group value with the group function

# SYNTAX group(int1)
#T# int1 is the group number

search1 = regex.search(r'(bc)(cd)', 'aabbccdd')
str1 = search1.group(2) # 'cd'

#T# get the starting position of a group with the start function

# SYNTAX start(int1)
#T# int1 is the group number, this returns a position (the start of the string is 0)

search1 = regex.search(r'(bc)(cd)', 'aabbccdd')
int1 = search1.start(2) # 5

#T# get the ending position of a group with the end function

# SYNTAX end(int1)
#T# same as before

search1 = regex.search(r'(bc)(cd)', 'aabbccdd')
int1 = search1.end(2) # 7

#T# get a list with all global matches with the findall function
list1 = regex.findall(r'text', 'strtextstrtextstr') # ['text', 'text']

#T# get a Scanner object that contains all the non overlapping matches as Match objects, and that can be iterated in a for loop with the finditer function
scanner1 = regex.finditer(r'text', 'strtextstrtextstr') # <_regex.Scanner object at 0x22983b0>
list1 = []
for it1 in scanner1: list1.append(it1) # list1 == [<regex.Match object; span=(3, 7), match='text'>, <regex.Match object; span=(10, 14), match='text'>]

#T# get a list without the matches with the split function
list1 = regex.split(r'text', 'strtextstrtextstr') # ['str', 'str', 'str']

#T# substitute matches with a replacement string with the sub function
str1 = regex.sub(r'text', 'TEXT', 'strtextstrtextstr') # 'strTEXTstrTEXTstr'

#T# substitute only up to a given maximum number of occurrences with the count kwarg
str1 = regex.sub(r'text', 'TEXT', 'strtextstrtextstr', count = 1) # 'strTEXTstrtextstr'

#T# substitute with regex groups, using a raw string as the replacement string
str1 = regex.sub(r'(\w+) (\w+)', r'\2 \1', 'str1 str2') # 'str2 str1'

#T# the pattern attribute of a Regex object, contains the pattern that was used to compile the Regex object
regex_object1 = regex.compile('\w*\sPattern1\b') # regex.Regex('\\w*\\sPattern1\x08', flags=regex.V0)
str1 = regex_object1.pattern # '\\w*\\sPattern1\x08'

#T# the groups method of a Match object, returns a tuple where each element is the match of a group
search1 = regex.search(r'(s)(tr)(1)', 'str1') # <regex.Match object; span=(0, 4), match='str1'>
tuple1 = search1.groups() # ('s', 'tr', '1')

#T# the span method of a Match object, returns the start and end positions of a group, or of the match if no group is input as argument
search1 = regex.search(r'(s)(tr)(1)', 'str1') # <regex.Match object; span=(0, 4), match='str1'>
tuple1 = search1.span(1) # (0, 1)

#T# the group method of a Match object, returns the contents of single groups, or the whole match if no group is input as argument
search1 = regex.search(r'(s)(tr)(1)', 'str1') # <regex.Match object; span=(0, 4), match='str1'>
str1 = search1.group(2) # 'tr'

#T# the string property of a Match object, contains the string being analyzed, i.e. the one that the regex is being applied on, the input string
search1 = regex.search(r'(s)(tr)(1)', 'textstr1text') # <regex.Match object; span=(4, 8), match='str1'>
str1 = search1.string # 'textstr1text'
# |-----

#C# --- Characters

# |-----
#T# the dot . is used to match any char
search1 = regex.search(r'.', 'str1') # <regex.Match object; span=(0, 1), match='s'>

#T# to match an operator as a literal char, it must be escaped with a backslash \
search1 = regex.search(r'\.', 'str1.') # <regex.Match object; span=(4, 5), match='.'>

#T# the escaped char \s matches one whitespace (space, tab, newline)
search1 = regex.search(r'\sb', 'a b') # <regex.Match object; span=(1, 3), match=' b'>

#T# the escaped char \S matches one non whitespace
search1 = regex.search(r'\Sc', 'a bc') # <regex.Match object; span=(2, 4), match='bc'>

#T# the escaped char \w matches one alphanumeric character or an underscore
search1 = regex.search(r'\w', '_a5.') # <regex.Match object; span=(0, 1), match='_'>

#T# the escaped char \W matches one non alphanumeric character nor an underscore
search1 = regex.search(r'\W', '_a5.') # <regex.Match object; span=(3, 4), match='.'>

#T# the escaped char \d matches one digit
search1 = regex.search(r'\d', 'a5b') # <regex.Match object; span=(1, 2), match='5'>

#T# the escaped char \D matches one non digit
search1 = regex.search(r'\D', '5bc') # <regex.Match object; span=(1, 2), match='b'>

#T# the escaped char \X matches one unicode char
search1 = regex.search(r'\w\X', 'a\u2446b') # <regex.Match object; span=(0, 2), match='a⑆'>

#T# to match a particular unicode char, use either \uHex1, \UHex1Hex2, the unicode char itself, or \N{name1}, Hex1 and Hex2 are hexadecimal numbers of four digits that represent the unicode char being matched, name1 is the char's name in the Unicode standard
search1 = regex.search(r'\u2446b', 'a⑆b') # <regex.Match object; span=(1, 3), match='⑆b'>
search1 = regex.search(r'\U0001F306', '\U0001F306') # <regex.Match object; span=(0, 1), match='🌆'>
search1 = regex.search(r'a⑆', 'a⑆b') # <regex.Match object; span=(0, 2), match='a⑆'>
search1 = regex.search(r'\N{OCR BRANCH BANK IDENTIFICATION}', 'a⑆b') # <regex.Match object; span=(1, 2), match='⑆'>

#T# unicode properties are matched in general with \p{prop1} where prop1 stands for the unicode property being matched, a char with said property will be matched

#T# unicode categories are matched with \p{categ1}, categ1 can be one of the following
#T#     L, matches a letter char, such as 's'
#T#     Ll, matches a lowercase letter char, such as 's'
#T#     Lu, matches an uppercase letter char, such as 'S'
#T#     Lt, matches a titlecase letter char, such as 'ǅ' \u01C5
#T#     L&, matches a lowercase, uppercase, or titlecase letter char, such as 'ǅ'
#T#     Lm, matches a modifier letter char, such as 'ʱ' \u02B1
#T#     Lo, matches a type other letter char, such as 'ƻ' \u01BB
#T#     M, matches a combining mark char (like diacritics), such as the breve in 'ă' a\u0306
#T#     Mc, matches an spacing combining mark char, such as 'ೄ' \u0CC4
#T#     Me, matches an enclosing mark char, such as 'a꙲' a\uA672
#T#     Mn, matches a nonspacing mark char, such as 'ả' a\u0309
#T#     N, matches a numeric char, such as '୬' \u0B6C
#T#     Nd, matches a decimal digit char, such as '߈' \u07C8
#T#     Nl, matches a number letter char, such as 'ↈ' \u2188
#T#     No, matches a type other number char, such as '௲' \u0BF2
#T#     P, matches a punctuation char, such as '⸗' \u2E17
#T#     Pc, matches a punctuation connector char, such as '﹏' \uFE4F
#T#     Pd, matches a punctuation dash char, such as '⸻' \u2E3B
#T#     Pe, matches a punctuation close char, such as '⟧' \u27E7
#T#     Pf, matches a punctuation final quote char, such as '»' \u00BB
#T#     Pi, matches a punctuation initial quote char, such as '⸄' \u2E04
#T#     Ps, matches a punctuation open char, such as '⁅' \u2045
#T#     Po, matches a type other punctuation char, such as '¶' \u00B6
#T#     S, matches a symbol char, such as '⌨' \u2328"
#T#     Sc, matches a symbol currency char, such as '֏' \u058F
#T#     Sk, matches a symbol modifier char, such as '˧' \u02E7
#T#     Sm, matches a symbol math char, such as '؆' \u0606
#T#     So, matches a type other symbol char, such as '۩' \u06E9
#T#     Z, matches a separator char, such as \u205F
#T#     Zl, matches a separator line char, such as \u2028
#T#     Zp, matches a separator paragraph char, such as \u2029
#T#     Zs, matches a separator space char, such as ' ' \u0020
#T#     C, matches a control char, such as \uFFF9
#T#     Cf, matches a format control char, such as \u2060
#T#     Co, matches a private use control char, such as \uE000
#T#     Cc, matches a type other control char, such as \u008A
search1 = regex.search(r'\p{L}', 'str1') # <regex.Match object; span=(0, 1), match='s'>
search1 = regex.search(r'\p{Lt}', '\u01C5') # <regex.Match object; span=(0, 1), match='ǅ'>
search1 = regex.search(r'\p{Lm}', '\u02B1') # <regex.Match object; span=(0, 1), match='ʱ'>
search1 = regex.search(r'\p{Lo}', '\u01BB') # <regex.Match object; span=(0, 1), match='ƻ'>
search1 = regex.search(r'a\p{M}', 'a\u0306') # <regex.Match object; span=(0, 2), match='ă'>
search1 = regex.search(r'\p{N}', '\u0B6C') # <regex.Match object; span=(0, 1), match='୬'>
search1 = regex.search(r'\p{P}', '\u2E17') # <regex.Match object; span=(0, 1), match='⸗'>
search1 = regex.search(r'\p{S}', '\u2328') # <regex.Match object; span=(0, 1), match='⌨'>
search1 = regex.search(r'\p{Z}', '\u205F') # <regex.Match object; span=(0, 1), match='\u205f'>
search1 = regex.search(r'\p{C}', '\uFFF9') # <regex.Match object; span=(0, 1), match='\ufff9'>

#T# unicode scripts are matched with \p{script1}, the possible values of script1 are the following (each name represents a script, 'Common' is for chars common to many scripts, 'Inherited' is for chars that inherit their script from a char they accompany, like nonspacing diacritics do): Adlam, Ahom, Anatolian_Hieroglyphs, Arabic, Armenian, Avestan, Balinese, Bamum, Bassa_Vah, Batak, Bengali, Bhaiksuki, Bopomofo, Brahmi, Braille, Buginese, Buhid, Canadian_Aboriginal, Carian, Caucasian_Albanian, Chakma, Cham, Cherokee, Chorasmian, Common, Coptic, Cuneiform, Cypriot, Cyrillic, Deseret, Devanagari, Dives_Akuru, Dogra, Duployan, Egyptian_Hieroglyphs, Elbasan, Elymaic, Ethiopic, Georgian, Glagolitic, Gothic, Grantha, Greek, Gujarati, Gunjala_Gondi, Gurmukhi, Han, Hangul, Hanifi_Rohingya, Hanunoo, Hatran, Hebrew, Hiragana, Imperial_Aramaic, Inherited, Inscriptional_Pahlavi, Inscriptional_Parthian, Javanese, Kaithi, Kannada, Katakana, Kayah_Li, Kharoshthi, Khitan_Small_Script, Khmer, Khojki, Khudawadi, Lao, Latin, Lepcha, Limbu, Linear_A, Linear_B, Lisu, Lycian, Lydian, Mahajani, Makasar, Malayalam, Mandaic, Manichaean, Marchen, Masaram_Gondi, Medefaidrin, Meetei_Mayek, Mende_Kikakui, Meroitic_Cursive, Meroitic_Hieroglyphs, Miao, Modi, Mongolian, Mro, Multani, Myanmar, Nabataean, Nandinagari, New_Tai_Lue, Newa, Nko, Nushu, Nyiakeng_Puachue_Hmong, Ogham, Ol_Chiki, Old_Hungarian, Old_Italic, Old_North_Arabian, Old_Permic, Old_Persian, Old_Sogdian, Old_South_Arabian, Old_Turkic, Oriya, Osage, Osmanya, Pahawh_Hmong, Palmyrene, Pau_Cin_Hau, Phags_Pa, Phoenician, Psalter_Pahlavi, Rejang, Runic, Samaritan, Saurashtra, Sharada, Shavian, Siddham, Sinhala, Sogdian, Sora_Sompeng, Soyombo, Sundanese, Sutton_SignWriting, Syloti_Nagri, Syriac, Tagalog, Tagbanwa, Tai_Le, Tai_Tham, Tai_Viet, Takri, Tamil, Tangut, Telugu, Thaana, Thai, Tibetan, Tifinagh, Tirhuta, Ugaritic, Vai, Wancho, Warang_Citi, Yezidi, Yi, Zanabazar_Square
search1 = regex.search(r'\p{Common}', '5') # <regex.Match object; span=(0, 1), match='5'>
search1 = regex.search(r'\p{Adlam}', "\U0001E904") # <regex.Match object; span=(0, 1), match='𞤄'>
search1 = regex.search(r'\p{Arabic}', "\u060B") # <regex.Match object; span=(0, 1), match='؋'>
search1 = regex.search(r'\p{Lepcha}', "\u1C12") # <regex.Match object; span=(0, 1), match='ᰒ'>
search1 = regex.search(r'\p{Nko}', "\u07D2") # <regex.Match object; span=(0, 1), match='ߒ'>
search1 = regex.search(r'\p{Tibetan}', "\u0F12") # <regex.Match object; span=(0, 1), match='༒'>

#T# unicode blocks are matched with \p{block1}, the possible values of block1 are the following: InAdlam, InAegean_Numbers, InAhom, InAlchemical_Symbols, InAlphabetic_Presentation_Forms, InAnatolian_Hieroglyphs, InAncient_Greek_Musical_Notation, InAncient_Greek_Numbers, InAncient_Symbols, InArabic, InArabic_Extended-A, InArabic_Mathematical_Alphabetic_Symbols, InArabic_Presentation_Forms-A, InArabic_Presentation_Forms-B, InArabic_Supplement, InArmenian, InArrows, InAvestan, InBalinese, InBamum, InBamum_Supplement, InBasic_Latin, InBassa_Vah, InBatak, InBengali, InBhaiksuki, InBlock_Elements, InBopomofo, InBopomofo_Extended, InBox_Drawing, InBrahmi, InBraille_Patterns, InBuginese, InBuhid, InByzantine_Musical_Symbols, InCarian, InCaucasian_Albanian, InChakma, InCham, InCherokee, InCherokee_Supplement, InChess_Symbols, InChorasmian, InCJK_Compatibility, InCJK_Compatibility_Forms, InCJK_Compatibility_Ideographs, InCJK_Compatibility_Ideographs_Supplement, InCJK_Radicals_Supplement, InCJK_Strokes, InCJK_Symbols_and_Punctuation, InCJK_Unified_Ideographs, InCJK_Unified_Ideographs_Extension_A, InCJK_Unified_Ideographs_Extension_B, InCJK_Unified_Ideographs_Extension_C, InCJK_Unified_Ideographs_Extension_D, InCJK_Unified_Ideographs_Extension_E, InCJK_Unified_Ideographs_Extension_F, InCJK_Unified_Ideographs_Extension_G, InCombining_Diacritical_Marks, InCombining_Diacritical_Marks_Extended, InCombining_Diacritical_Marks_for_Symbols, InCombining_Diacritical_Marks_Supplement, InCombining_Half_Marks, InCommon_Indic_Number_Forms, InControl_Pictures, InCoptic, InCoptic_Epact_Numbers, InCounting_Rod_Numerals, InCuneiform, InCuneiform_Numbers_and_Punctuation, InCurrency_Symbols, InCypriot_Syllabary, InCyrillic, InCyrillic_Extended-A, InCyrillic_Extended-B, InCyrillic_Extended-C, InCyrillic_Supplement, InDeseret, InDevanagari, InDevanagari_Extended, InDingbats, InDives_Akuru, InDogra, InDomino_Tiles, InDuployan, InEarly_Dynastic_Cuneiform, InEgyptian_Hieroglyphs, InEgyptian_Hieroglyph_Format_Controls, InElbasan, InElymaic, InEmoticons, InEnclosed_Alphanumeric_Supplement, InEnclosed_Alphanumerics, InEnclosed_CJK_Letters_and_Months, InEnclosed_Ideographic_Supplement, InEthiopic, InEthiopic_Extended, InEthiopic_Extended-A, InEthiopic_Supplement, InGeneral_Punctuation, InGeometric_Shapes, InGeometric_Shapes_Extended, InGeorgian, InGeorgian_Extended, InGeorgian_Supplement, InGlagolitic, InGlagolitic_Supplement, InGothic, InGrantha, InGreek_and_Coptic, InGreek_Extended, InGujarati, InGunjala_Gondi, InGurmukhi, InHalfwidth_and_Fullwidth_Forms, InHangul_Compatibility_Jamo, InHangul_Jamo, InHangul_Jamo_Extended-A, InHangul_Jamo_Extended-B, InHangul_Syllables, InHanifi_Rohingya, InHanunoo, InHatran, InHebrew, InHigh_Private_Use_Surrogates, InHigh_Surrogates, InHiragana, InIdeographic_Description_Characters, InIdeographic_Symbols_and_Punctuation, InImperial_Aramaic, InIndic_Siyaq_Numbers, InInscriptional_Pahlavi, InInscriptional_Parthian, InIPA_Extensions, InJavanese, InKaithi, InKana_Extended-A, InKana_Supplement, InKanbun, InKangxi_Radicals, InKannada, InKatakana, InKatakana_Phonetic_Extensions, InKayah_Li, InKharoshthi, InKhitan_Small_Script, InKhmer, InKhmer_Symbols, InKhojki, InKhudawadi, InLao, InLatin-1_Supplement, InLatin_Extended-A, InLatin_Extended-B, InLatin_Extended-C, InLatin_Extended-D, InLatin_Extended-E, InLatin_Extended_Additional, InLepcha, InLetterlike_Symbols, InLimbu, InLinear_A, InLinear_B_Ideograms, InLinear_B_Syllabary, InLisu, InLisu_Supplement, InLow_Surrogates, InLycian, InLydian, InMahajani, InMahjong_Tiles, InMakasar, InMalayalam, InMandaic, InManichaean, InMarchen, InMasaram_Gondi, InMathematical_Alphanumeric_Symbols, InMathematical_Operators, InMayan_Numerals, InMedefaidrin, InMeetei_Mayek, InMeetei_Mayek_Extensions, InMende_Kikakui, InMeroitic_Cursive, InMeroitic_Hieroglyphs, InMiao, InMiscellaneous_Mathematical_Symbols-A, InMiscellaneous_Mathematical_Symbols-B, InMiscellaneous_Symbols, InMiscellaneous_Symbols_and_Arrows, InMiscellaneous_Symbols_and_Pictographs, InMiscellaneous_Technical, InModi, InModifier_Tone_Letters, InMongolian, InMongolian_Supplement, InMro, InMultani, InMusical_Symbols, InMyanmar, InMyanmar_Extended-A, InMyanmar_Extended-B, InNabataean, InNandinagari, InNew_Tai_Lue, InNewa, InNKo, InNumber_Forms, InNushu, InNyiakeng_Puachue_Hmong, InOgham, InOl_Chiki, InOld_Hungarian, InOld_Italic, InOld_North_Arabian, InOld_Permic, InOld_Persian, InOld_Sogdian, InOld_South_Arabian, InOld_Turkic, InOptical_Character_Recognition, InOriya, InOrnamental_Dingbats, InOsage, InOsmanya, InOttoman_Siyaq_Numbers, InPahawh_Hmong, InPalmyrene, InPau_Cin_Hau, InPhags-pa, InPhaistos_Disc, InPhoenician, InPhonetic_Extensions, InPhonetic_Extensions_Supplement, InPlaying_Cards, InPrivate_Use_Area, InPsalter_Pahlavi, InRejang, InRumi_Numeral_Symbols, InRunic, InSamaritan, InSaurashtra, InSharada, InShavian, InShorthand_Format_Controls, InSiddham, InSinhala, InSinhala_Archaic_Numbers, InSmall_Form_Variants, InSmall_Kana_Extension, InSogdian, InSora_Sompeng, InSoyombo, InSpacing_Modifier_Letters, InSpecials, InSundanese, InSundanese_Supplement, InSuperscripts_and_Subscripts, InSupplemental_Arrows-A, InSupplemental_Arrows-B, InSupplemental_Arrows-C, InSupplemental_Mathematical_Operators, InSupplemental_Punctuation, InSupplemental_Symbols_and_Pictographs, InSupplementary_Private_Use_Area-A, InSupplementary_Private_Use_Area-B, InSutton_SignWriting, InSyloti_Nagri, InSymbols_and_Pictographs_Extended-A, InSymbols_for_Legacy_Computing, InSyriac, InSyriac_Supplement, InTagalog, InTagbanwa, InTags, InTai_Le, InTai_Tham, InTai_Viet, InTai_Xuan_Jing_Symbols, InTakri, InTamil, InTamil_Supplement, InTangut, InTangut_Components, InTangut_Supplement, InTelugu, InThaana, InThai, InTibetan, InTifinagh, InTirhuta, InTransport_and_Map_Symbols, InUgaritic, InUnified_Canadian_Aboriginal_Syllabics, InUnified_Canadian_Aboriginal_Syllabics_Extended, InVai, InVariation_Selectors, InVariation_Selectors_Supplement, InVedic_Extensions, InVertical_Forms, InWancho, InWarang_Citi, InYezidi, InYi_Radicals, InYi_Syllables, InYijing_Hexagram_Symbols, InZanabazar_Square
search1 = regex.search(r'\p{InBasic_Latin}', '&') # <regex.Match object; span=(0, 1), match='&'>
search1 = regex.search(r'\p{InLatin-1_Supplement}', '\u00A7') # <regex.Match object; span=(0, 1), match='§'>
search1 = regex.search(r'\p{InGurmukhi}', '\u0A07') # <regex.Match object; span=(0, 1), match='ਇ'>
search1 = regex.search(r'\p{InMusical_Symbols}', '\U0001D121') # <regex.Match object; span=(0, 1), match='𝄡'>

#T# the escaped char \t matches one tab char
search1 = regex.search(r'\tc', 'ab    c') # <regex.Match object; span=(2, 4), match='\tc'>

#T# the escaped char \r matches one carriage return (this also works in the sed program)
print('ab\rc') # cb
search1 = regex.search(r'\rc', 'ab\rc') # <regex.Match object; span=(2, 4), match='\rc'>

#T# the escaped char \n matches one newline
search1 = regex.search(r'r1\nst', 'str1\nstr2') # <regex.Match object; span=(2, 7), match='r1\nst'>

#T# there is no support for the escaped char \N to match a non newline, it can be replaced with [^\n]
search1 = regex.search(r'[^\n]c', 'ab\ncd') # None

#T# there is no support for the escaped char \h to match an horizontal whitespace (space, tab), it can be approximated by [^\S\n] but a few vertical spaces can be matched this way
search1 = regex.search(r'[^\S\n]b[^\S\n]c', 'a b    c') # <regex.Match object; span=(1, 5), match=' b\tc'>

#T# there is no support for the escaped char \H to match a non horizontal whitespace

#T# the escaped chars \Q and \E escape any characters inside them, but in Python they are not used, the escape function is used instead
search1 = regex.search(regex.escape(r'a.+?'), 'a.+?') # <regex.Match object; span=(0, 4), match='a.+?'>

#T# the escaped char \K removes the part of the match that is to its left
search1 = regex.search(r'str1\n\Kstr2', 'str1\nstr2') # <regex.Match object; span=(5, 9), match='str2'>

#T# comments are introduced with (?# comment1)
search1 = regex.search(r'(?# initial comment)str(?# a number comes next)1', 'str1') # <regex.Match object; span=(0, 4), match='str1'>
# |-----

#C# --- Quantifiers

# |-----
#T# the question mark ? is used as a quantifier to match 0 or 1 of the preceding char
search1 = regex.search(r'r?1', 'str1') # <regex.Match object; span=(2, 4), match='r1'>

#T# the asterisk * is used as a quantifier to match 0 or more of the preceding char
search1 = regex.search(r'r*1', 'st1') # <regex.Match object; span=(2, 3), match='1'>

#T# the plus sign + is used as a quantifier to match 1 or more of the preceding char
search1 = regex.search(r'r+1', 'strrr1') # <regex.Match object; span=(2, 6), match='rrr1'>

#T# the syntax {int1} is used as a quantifier to match the preceding char int1 times
search1 = regex.search(r'r{2}1', 'strrrr1') # <regex.Match object; span=(4, 7), match='rr1'>

#T# the syntax {int1,int2} is used as a quantifier to match the preceding char between int1 and int2 times (as many times as possible), so int2 >= int1, if int2 is omitted then match any amount greater than or equal to int1
search1 = regex.search('r{1,3}1', 'strrrrr1') # <regex.Match object; span=(4, 8), match='rrr1'>
search1 = regex.search(r'r{1,}1', 'strrrrr1') # <regex.Match object; span=(2, 8), match='rrrrr1'>

#T# lazy (non greedy) quantifiers are created with a question mark ? after the operator, works as ??, *?, +?
search1 = regex.search(r'[0-9][0-9]??', '12345') # <regex.Match object; span=(0, 1), match='1'>
search1 = regex.search(r'[0-9]*?', '12345') # <regex.Match object; span=(0, 0), match=''>
search1 = regex.search(r'[0-9]+?', '12345') # <regex.Match object; span=(0, 1), match='1'>

#T# possessive quantifiers add a plus + at the end of the other quantifiers, they are greedy without backtracking, so that after a match fails, it is not checked if less chars would make it succeed, works as *+, ++, {}+
search1 = regex.search(r'a*+', 'aaa') # <regex.Match object; span=(0, 3), match='aaa'>
search1 = regex.search(r'\w++b', 'aaaab') # None #| 'aaaab' would be matched without the possessive quantifier
search1 = regex.search(r'\w{1,7}+F', 'abcdeF') # None #| 'abcdeF' would be matched without the possessive quantifier
# |-----

#C# --- Character classes

# |-----
#T# the syntax [char1char2charN] is called a character class, and used to match any single one of the characters, char1, char2, up to charN
search1 = regex.search(r'[trs]1', 'strr1') # <regex.Match object; span=(3, 5), match='r1'>

#T# using a caret ^ at the start of a character class, negates it
search1 = regex.search(r'[^trs]1', 'strr1') # None

#T# using a dash - between two characters inside a character class, matches any single one character in the range of said two characters
search1 = regex.search(r'[3-u]1', 'strr1') # <regex.Match object; span=(3, 5), match='r1'>

#T# a character class can be one of the POSIX character clases, these are made with a word within colons and a pair of brackets which don't count as the character class brackets
#T#     [:alnum:],  matches one alphanumeric char
#T#     [:alpha:],  matches one alphabetic char
#T#     [:blank:],  matches one space or tab
#T#     [:cntrl:],  matches one control char, like a vertical tab
#T#     [:digit:],  matches one digit
#T#     [:graph:],  matches one visible char
#T#     [:lower:],  matches one lowercase char
#T#     [:print:],  matches one visible char or space
#T#     [:punct:],  matches one punctuation char
#T#     [:space:],  matches one space char
#T#     [:upper:],  matches one uppercase char
#T#     [:xdigit:], matches one hexadecimal digit
search1 = regex.search(r'[[:alnum:]]', 'str1') # <regex.Match object; span=(0, 1), match='s'>

#T# in Python, set operations using nested sets are possible, || for union, && for intersection, -- for difference, ~~ for symmetric difference
search1 = regex.search(r'[[a-z] -- [aeiou]]', 'abc', flags = regex.V1) # <regex.Match object; span=(1, 2), match='b'> #| [a-z] set minus [aeiou] set
search1 = regex.search(r'[[0-7] || [d-h]]', 't5', flags = regex.V1) # <regex.Match object; span=(1, 2), match='5'> #| [0-7] set union [d-h] set
search1 = regex.search(r'[[0-7] && [d-h]]', 't5', flags = regex.V1) # None #| [0-7] set intersected with [d-h] set
search1 = regex.search(r'[[a-p] ~~ [h-z]]', 'mb', flags = regex.V1) # <regex.Match object; span=(1, 2), match='b'> #| [a-p] symmetric difference with [h-z] set
# |-----

#C# --- Groupings

# |-----
#T# the parentheses () are used to capture a group of chars, and treat this group the same as treating a single char
search1 = regex.search(r'(tr)+1', 'strtr1') # <regex.Match object; span=(1, 6), match='trtr1'>

#T# the escaped numbers \1, \2, etc., are used to match (backreference) a captured group, \1 matches the first group, \2 the second, and so on
search1 = regex.search(r'(st)(r1)A\1\2', 'str1Astr1') # <regex.Match object; span=(0, 9), match='str1Astr1'>

#T# a group number from 10 onwards can be backreferenced with \g<int1> where int1 is the group number, this avoids ambiguity
search1 = regex.search(r'(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)\g<11>', 'abcdefghijkk', flags = regex.V1) # <regex.Match object; span=(0, 12), match='abcdefghijkk'>

#T# nested groups are possible as (group1(group2)), they are numbered in order of appearance, so \1 matches group1group2, \2 matches group2
search1 = regex.search(r'(a(b)) \1', 'ab ab') # <regex.Match object; span=(0, 5), match='ab ab'>
search1 = regex.search(r'(a(b)) a\2', 'ab ab') # <regex.Match object; span=(0, 5), match='ab ab'>

#T# named groups are created with (?<group_name1>pattern1) or (?P<group_name1>pattern1) and are matched again (as a backreference) with \g<group_name1> or (?P=group_name1)
search1 = regex.search(r'(?P<group1>ab) \g<group1>', 'ab ab') # <regex.Match object; span=(0, 5), match='ab ab'>
search1 = regex.search(r'(?<group1>ab) \g<group1>', 'ab ab') # <regex.Match object; span=(0, 5), match='ab ab'>
search1 = regex.search(r'(?P<group1>ab) (?P=group1)', 'ab ab') # <regex.Match object; span=(0, 5), match='ab ab'>

#T# subscripting repeated groups as in (\w)+, is done with the subf function, the syntax is {int1[int2]} int1 is for the group number, int2 is for the subscript
str1 = regex.subf(r'(\w)+', '{1[0]} {1[1]} {1[2]} {1[-1]}', 'str1') # 's t r 1'

#T# the vertical bar | is used for alternation (to match either one of the patterns separated with the vertical bar)
search1 = regex.search(r'st|tr1', 'str1') # <regex.Match object; span=(0, 2), match='st'>

#T# the syntax (?:pattern1) is used to create a non capturing group for pattern1, this means that the match of pattern1 can't be recalled with a backreference like \1, because it doesn't create a group
search1 = regex.search(r'(?:tr)(ab)\1', 'strabab') # <regex.Match object; span=(1, 7), match='trabab'>

#T# the syntax (?>pattern1|pattern2) up to patternN creates an atomic group, this means there is no backtracking, i.e. the match is fixed with the first pattern found from this group, and if it fails there is no checking the remaining patterns, in this sense pattern1 has more priority than pattern2 and so on
search1 = regex.search(r'(?>prio|priorshi)p', 'priorship') # no match #| given that the first pattern 'prio' is matched, the second one 'priorshi' will never be matched due to the atomic group, without '?>' the whole 'priorship' is matched

#T# the syntax (?|(pattern1)|pattern2|(pattern3)(pattern4)) creates a brach reset group, in it, the group numbering resets, this means that if pattern3 is matched then it's group number 1 and pattern4 is group 2, if pattern1 is matched then it's group 1, and if pattern2 is matched there are no groups created
search1 = regex.search(r'(?|A(\d+)|B(\d+)) \1', 'B12 12') # <regex.Match object; span=(0, 6), match='B12 12'>
# |-----

#C# --- Subroutines and conditionals

# |-----
#T# subroutines are a way to reuse regex patterns already created, instead of writing them again

#T# the basic subroutine reuses the numbered groups, a subroutine (?int1) matches the pattern of the numbered group int1
search1 = regex.search(r'(\w\w\w\d) (?1)', 'str1 str2') # <regex.Match object; span=(0, 9), match='str1 str2'>

#T# a named subroutine is the same as before, but using a named group, the named subroutine (?&group_name1) matches the pattern of a named group group_name1
search1 = regex.search(r'(?<group1>str\d) (?&group1)', 'str1 str2') # <regex.Match object; span=(0, 9), match='str1 str2'>

#T# there is no support for relative subroutines

#T# regex patterns can have recursion with (?R), the whole pattern is put in place of (?R), so the ? quantifier should accompany it, as (?R)? to ensure the recursion can end when it doesn't match anymore
search1 = regex.search(r'\w\d(?R)?', 'a1b2') # <regex.Match object; span=(0, 4), match='a1b2'>
search1 = regex.search(r'\w(?R)?\d', 'ab12') # <regex.Match object; span=(0, 4), match='ab12'> #| when used at the start '(?R)?pattern1' Python gives a MemoryError

#T# there is no support for regex code capsules

#T# conditionals allow matching patterns according to an if-then-else conditional, the basic form is (?(if1)(then_patterns1)|(else_patterns1)) note the plural in patterns as each can be several patterns separated by alternation |, if1 is either a lookaround or a group (named or numbered)
search1 = regex.search(r'(?(?=\d+)(123|456)|(abc|def))', '12345') # <regex.Match object; span=(0, 3), match='123'>
search1 = regex.search(r'(\d)(?(1)(2)|(b))', '12345') # <regex.Match object; span=(0, 2), match='12'>
search1 = regex.search(r'(?<group1>\d{2})(?(group1)(34)|(cd))', '12345') # <regex.Match object; span=(0, 4), match='1234'>
# |-----

#C# --- Anchors and boundaries

# |-----
#T# the caret ^ (outside a character class) matches the following chars as an anchor at the start of the line
search1 = regex.search(r'^str', 'str1') # <regex.Match object; span=(0, 3), match='str'>

#T# the escaped char \A matches the beginning of the first line
search1 = regex.search(r'\Astr\d', 'str1\nstr2') # <regex.Match object; span=(0, 4), match='str1'> #| this can only match 'str1', so the pattern '\Astr2' fails

#T# the dollar sign $ matches the preceding chars as an anchor at the end of the line
search1 = regex.search(r'tr1$', 'str1') # <regex.Match object; span=(1, 4), match='tr1'>

#T# the escaped char \Z matches the end of the last line
search1 = regex.search(r'str\d\Z', 'str1\nstr2') # <regex.Match object; span=(5, 9), match='str2'> #| this can only match 'str2', so the pattern 'str1\Z' fails

#T# the escaped char \m matches at the start of a word
search1 = regex.search(r'\mcd', 'ab cd') # <regex.Match object; span=(3, 5), match='cd'>

#T# the escaped char \M matches at the end of a word
search1 = regex.search(r'ab\M', 'ab cd') # <regex.Match object; span=(0, 2), match='ab'>

#T# the escaped char \b matches at a word boundary
search1 = regex.search(r'\bcd', 'ab cd') # <regex.Match object; span=(3, 5), match='cd'>

#T# the escaped char \B matches at a non word boundary
search1 = regex.search(r'\Bcd', 'ab cd') # None

#T# the escaped char \G matches at beginning of the first line or at the end position of the last match, so several matches must be allowed to see the effect
list1 = regex.findall(r'\G\w\d', 'a1b2c3 d4e5f6') # ['a1', 'b2', 'c3']
# |-----

#C# --- Lookarounds

# |-----
#T# the syntax (?=pattern1) is used to create a positive lookahead with pattern1, so pattern1 must appear ahead when finding a match, because pattern1 is not matched
search1 = regex.search(r'r(?=[0-2])\d', 'str1') # <regex.Match object; span=(2, 4), match='r1'> #| only matches r0, r1, or r2

#T# the syntax (?<=pattern1) is used to create a positive lookbehind with pattern1, so pattern1 must appear behind when finding a match, pattern1 is not matched
search1 = regex.search(r'(?<=st)r1', 'str1') # <regex.Match object; span=(2, 4), match='r1'>

#T# the syntax (?!pattern1) is used to create a negative lookahead with pattern1, so pattern1 can't appear ahead when finding a match, because pattern1 is not matched
search1 = regex.search(r'r1(?!00)\d\d', 'str101') # <regex.Match object; span=(2, 6), match='r101'> #| doesn't match in str100

#T# the syntax (?<!pattern1) is used to create a negative lookbehind with pattern1, so pattern1 can't appear behind when finding a match, pattern1 is not matched
search1 = regex.search(r'(?<!st)r1', 'str1') # None
# |-----

#C# --- Regex modifiers

# |-----
#T# regular regex modifiers are passed via the flags kwarg of the regex functions from the regex module, several modifiers can be passed together using the vertical bar operator |, e.g. regex.I | regex.U passes both modifiers

#T# the continuation modifier is not needed in Python, instead, functions like the findall function are used
list1 = regex.findall(r'\G\w\d', 'a1b2c3 d4e5f6') # ['a1', 'b2', 'c3']

#T# the global modifier has no inline version, in Python it is used through functions like the findall function and the finditer function, whereas the match function and the search function do not match globally
scanner1 = regex.finditer(r'text', 'strtextstrtextstr')
list1 = []
for it1 in scanner1: list1.append(it1) # [<regex.Match object; span=(3, 7), match='text'>, <regex.Match object; span=(10, 14), match='text'>]

#T# use the regular case insensitive modifier with the regex.I constant as value for the flags kwarg, this matches lowercase and uppercase letters the same
search1 = regex.search(r'STR1', 'str1', flags = regex.I) # <regex.Match object; span=(0, 4), match='str1'>

#T# use the inline case insensitive modifier (?i), turn it off with (?-i)
search1 = regex.search(r'(?i)ST(?-i)R1', 'stR1', flags = regex.V1) # <regex.Match object; span=(0, 4), match='stR1'>

#T# use the regular multiline modifier with the regex.M constant as value for the flags kwarg, this makes the caret ^ and the dollar sign $ match at the start and end of intermediate lines (all lines actually)
search1 = regex.search(r'^str2$', 'str1\nstr2\nstr3', flags = regex.M) # <regex.Match object; span=(5, 9), match='str2'>

#T# use the inline multiline modifier (?m) with the -z flag, turn it off with (?-m)
search1 = regex.search(r'(?m)^str2$', 'str1\nstr2\nstr3') # <regex.Match object; span=(5, 9), match='str2'>

#T# use the regular dotall modifier with the regex.S constant as value for the flags kwarg, this makes the dot . also match a newline
search1 = regex.search(r'in.*en', 'begin\nend', flags = regex.S) # <regex.Match object; span=(3, 8), match='in\nen'>

#T# use the inline dotall modifier (?s), turn it off with (?-s)
search1 = regex.search(r'(?s)in.*en', 'begin\nend') # <regex.Match object; span=(3, 8), match='in\nen'>

#T# there is no support for the ungreedy modifier

#T# use the regular extended modifier with the regex.X constant as value for the flags kwarg, this ignores whitespace that is not escaped or outside a character class
search1 = regex.search(r'st    r1\ st r2', 'str1 str2', flags = regex.X) # <regex.Match object; span=(0, 9), match='str1 str2'>

#T# use the inline extended modifier (?x), turn it off with (?-x)
search1 = regex.search(r'(?x)st    r1\ st r2', 'str1 str2') # <regex.Match object; span=(0, 9), match='str1 str2'>

#T# there is no support for the extra modifier that throws an error when escaping a character that has no special meaning

#T# use the regular ascii modifier with the regex.A constant as value for the flags kwarg, this makes characters like \w, \s, \d, and similar, to match only ascii chars
list1 = regex.findall(r'\w', 'áüo', flags = regex.A) # ['o']

#T# use the inline ascii modifier (?a), it can't be turned off and must be placed at the start of the pattern
list1 = regex.findall(r'(?a)\w', 'áüo') # ['o']

#T# use the regular unicode modifier with the regex.U constant as value for the flags kwarg, this makes characters like \w, \s, \d, and similar, to match unicode chars, this is the default behavior
list1 = regex.findall(r'\w', 'áüo', flags = regex.U) # ['á', 'ü', 'o']

#T# use the inline unicode modifier (?u), it can't be turned off and must be placed at the start of the pattern
list1 = regex.findall(r'(?u)\w', 'áüo') # ['á', 'ü', 'o']

#T# turn on or off several inline modifiers together, e.g. (?ix-m)
search1 = regex.search(r'(?ix-m)S  T  R1', 'str1', flags = regex.V1) # <regex.Match object; span=(0, 4), match='str1'>

#T# all former inline modifiers shown can be introduced exclusively for the pattern inside the same parentheses of the inline modifier, i.e. (?s:pattern1), (?-s:pattern1) only affects pattern1
search1 = regex.search(r'(?i:STR)1 (?-i:STR)2', 'str1 STR2') # <regex.Match object; span=(0, 9), match='str1 STR2'>
# |-----

# |-------------------------------------------------------------

#C# Builtin values

# |-------------------------------------------------------------

#C# --- Constants

# |-----
#T# the ellipsis ... constant is used to allow for extra functionality in third party libraries, particularly in array notation
... # Ellipsis
# |-----

# |-------------------------------------------------------------