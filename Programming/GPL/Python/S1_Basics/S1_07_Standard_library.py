
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
#C# Class functions
#C# --- Predicate logic

#T# Beginning of content

#C# Basic functions

# |-------------------------------------------------------------
#T# get input from stdin with the input function, it returns a string which can be cast to any needed type
str1 = input("Enter the input:")

# |--------------------------------------------------\
#T# the map function applies a given function to the elements of an array and returns a map object with the return values, that can be cast as an array

# SYNTAX map(func1, arr1)
#T# the returned map object has the result of applying func1 to each element in arr1

list1 = [-11, 3, -25]
map1 = map(abs, list1)
list2 = list(map1) # [11, 3, 25]
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# the filter function uses a given function to filter the elements of an array and returns a filter object that can be cast as an array

# SYNTAX filter(func1, arr1)
#T# the returned filter object has the elements from arr1 for which func1 returns True

list1 = ['1', '2', 'elem']
filter1 = filter(str.isalpha, list1)
list2 = list(filter1) # ['elem']
# |--------------------------------------------------/

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
x = -5.15
y = 4
#T# the abs function returns the absolute value of a number
flo1 = abs(x) # 5.15

#T# the ceil function returns the ceiling of a number
int1 = math.ceil(x) # -5

#T# the floor function returns the floor of a number
int1 = math.floor(x) # -6

#T# the pi constant approximates the value of pi
flo1 = math.pi # 3.14159...

#T# the e constant approximates the value of e
flo1 = math.e # 2.71828...

#T# the sqrt function returns the square root of a number
flo1 = math.sqrt(y) # 2.0

#T# the pow function raises a number to another
int1 = pow(y, 2) # 16

#T# the exp function raises e to the power of a number
flo1 = math.exp(y) # 54.598...

#T# the log function returns the log of a number in a given base
flo1 = math.log(y, 3) # 1.26...

#T# the log10 function returns the log of a number in base 10
flo1 = math.log10(y) # 0.60...

#T# the max function returns the maximum of the arguments
num1 = max(x, y) # 4

#T# the min function returns the minimum of the arguments
num1 = min(x, y) # -5.15

#T# the modf function returns a tuple with the fractional part and the integer part of a number
tuple1 = math.modf(x) # (-0.15, -5.0); x == -5.15
flo1 = tuple1[0]      # -0.15
int1 = int(tuple1[1]) # -5

#T# the round function rounds a number to a given precision, if the precision is negative it's is rounded to the left of the decimal point
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

str1 = "random string"
#T# the choice function chooses a random element from an array
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

str1 = "Left"
#T# left justify a string, same arguments as in the center function
str1 = str1.ljust(7, ">") # 'Left>>>'

str1 = "Right"
#T# right justify a string, same arguments as in the center function
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
str2 = byte1.decode('unicode-escape') # 'ingA !'
str2 = byte1.decode('ascii')          # 'ingA !'
str2 = byte1.decode('Latin-1')        # 'ingA !'
str2 = byte1.decode('cp1252')         # 'ingA !'
str2 = byte1.decode('big5')           # 'ingA !'
str2 = byte1.decode('iso8859_6')      # 'ingA !'
str2 = byte1.decode('mac_greek')      # 'ingA !'
str2 = byte1.decode('cp424')          # 'ש>קא\x80\x81'

#T# can't decode an utf-8 encoded string in utf-32 unless extra bytes are added
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

# |--------------------------------------------------\
#T# check if a string starts or ends with a given string

# SYNTAX str1.startswith("substr1"[, startN[, endN]])
# SYNTAX str1.endswith("substr2"[, startN[, endN]])
#T# returns True if str1[startN:endN] starts with "substr1", or ends with "substr2" respectively

str1 = "First to Last"
bool1 = str1.startswith("rst", 2)   # True
bool1 = str1.endswith("Las", 0, 12) # True
# |--------------------------------------------------/

#T# get the pos of the first substring found in a string, same arguments as in the startswith function
str1 = "to be found"
int1 = str1.find('fou', 2, -1) # 6

#T# do the same as the find function but raise an exception on failure with the index function, same arguments as in the startswith function
int1 = str1.index('fou') # 6

#T# do a reverse find, in the sense of starting the search at the end of the string, with the functions rfind, and rindex, same arguments as in the startswith function
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

# |--------------------------------------------------\
#T# join the string elements of an array

# SYNTAX "insert1".join(arr1) 
#T# arr1 must be an array of strings, the returned string has "insert1" between each pair of elements in arr1

arr1 = ("elem1", "elem2")
str1 = "-|-".join(arr1) # 'elem1-|-elem2'
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# split a string into elements of a list

# SYNTAX str1.split("separator1")
#T# str1 is split at each occurrence of the substring "separator1", leaving out said substring

str1 = 'elem1-|-elem2'
list1 = str1.split("-|") # ['elem1', '-elem2']
# |--------------------------------------------------/

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

# |--------------------------------------------------\
#T# count the repetitions of an element in a list

# SYNTAX list1.count('elem1')
#T# the repetitions of the element 'elem1' in list1 are counted

list1 = ['a', 5, 'stray_elem', 'a', 'elem5']
int1 = list1.count('a') # 2
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# get the index of the first occurrence

# SYNTAX list1.index('elem1')
#T# this returns the index of the first occurrence of 'elem1' in list1

list1 = ['a', 5, 'stray_elem', 'a', 'elem5']
int1 = list1.index('elem5') # 4
# |--------------------------------------------------/

#T# reverse the order of the elements with the reverse function, it returns None, so it shouldn't be assigned to a var
list1 = ['a', 5, 'stray_elem', 'a', 'elem5']
list1.reverse() # list1 == ['elem5', 'a', 'stray_elem', 5, 'a']

# |--------------------------------------------------\
#T# sort elements in a list

# SYNTAX list1.sort([reverse = True|False[, key = func1]])
#T# the default order is ascending, if the reverse kwarg is True then the order is descending, the elements of list1 must be strings

#T# the key kwarg is for the sorting function func1, the result is sorted from smaller to bigger return values of this sorting function, the default is alphabetical order

list1 = ['elem5', 'a', 'stray_elem', '5', 'a']
list1.sort(reverse = True, key = len) # ['stray_elem', 'elem5', 'a', '5', 'a']
# |--------------------------------------------------/

#T# shuffle the elements of a list
list1 = ['elem5', 'a', 'stray_elem', '5', 'a']
random.shuffle(list1) # ['a', 'elem5', '5', 'a', 'stray_elem'] or other
# |-------------------------------------------------------------

#C# Dictionary functions

# |-------------------------------------------------------------

# |--------------------------------------------------\
#T# create a new key value pair in a dictionary only if the key doesn't already exists with the setdefault function

# SYNTAX dict1.setdefault('new_key1', 'new_val1')
#T# the pair 'new_key1', 'new_val1' will be added to dict1 only if 'new_key1' is not in dict1 already

dict1 = {'key1': 85, 'key2': 85}
dict1.setdefault('new_key', 'new_val') # new_val
dict1.setdefault('key2', 'val2') # 85
# |--------------------------------------------------/

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
struct_time1 = time.struct_time(tm_year=2020, tm_mon=8, tm_mday=13, tm_hour=1, tm_min=15, tm_sec=16, tm_wday=3, tm_yday=226, tm_isdst=0)
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
struct_time1 = time.struct_time(tm_year=2020, tm_mon=8, tm_mday=13, tm_hour=1, tm_min=15, tm_sec=16, tm_wday=3, tm_yday=226, tm_isdst=0)
flo2 = calendar.timegm(struct_time1) # 1597281316   == 1597299316 - 18000
# |-----

#C# --- Datetime formatting

# |-----
#T# the asctime function formats a struct_time object as a string
struct_time1 = time.struct_time(tm_year=2020, tm_mon=8, tm_mday=13, tm_hour=1, tm_min=15, tm_sec=16, tm_wday=3, tm_yday=226, tm_isdst=0)
str1 = time.asctime(struct_time1) # 'Thu Aug 13 01:15:16 2020'

#T# the ctime function formats the seconds from Epoch in local time as a string
flo1 = 1597299316.1336622
str1 = time.ctime(flo1) # 'Thu Aug 13 01:15:16 2020'

# |--------------------------------------------------\
#T# the strftime function converts a struct_time object into a string with a custom format through format codes that start with %

# SYNTAX format codes of the strftime function
#T#     %a weekday name abbreviated
#T#     %A weekday name
#T#     %b month name abbreviated
#T#     %B month name
#T#     %c default format
#T#     %C century number
#T#     %d day of the month with zero padding
#T#     %D shorthand for %m/%d/%y
#T#     %e day of the month
#T#     %g year with two digits
#T#     %G year
#T#     %h equivalent to %b
#T#     %H 24 hour clock
#T#     %I 12 hour clock
#T#     %j day of the year
#T#     %m month number
#T#     %M minute
#T#     %n newline char
#T#     %p AM or PM in a 12 hour clock 
#T#     %r shorthand for %I:%M:%S %p
#T#     %R shorthand for %H:%M
#T#     %S second
#T#     %t tab char
#T#     %T shorthand for %H:%M:%S
#T#     %u weekday number, monday is 1
#T#     %U week of the year, starting monday
#T#     %V week of the year, ISO 8601
#T#     %W week of the year, starting sunday
#T#     %w weekday number, sunday is 0
#T#     %x shorthand for %m/%d/%y
#T#     %X shorthand for %H:%M:%S
#T#     %y year with two digits
#T#     %Y year
#T#     %z timezone change
#T#     %Z timezone name
#T#     %% escaped char %

struct_time1 = time.struct_time(tm_year=2020, tm_mon=8, tm_mday=13, tm_hour=1, tm_min=15, tm_sec=16, tm_wday=3, tm_yday=226, tm_isdst=0)
str1 = time.strftime("%A%B%C %d%t%u %G %h %Hor%I %j %m%M%n%p%S %V %W %w %y %z%%", struct_time1)
#T# printing str1 yields
# ThursdayAugust20 13     4 2020 Aug 06or06 226 0810
# AM55 33 32 4 20 +0000%
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# the strptime function converts a string in a given format using format codes into an struct_time object

# SYNTAX time.strptime("str_date1", "str_format1")
#T# the string "str_date1" is parsed according to "str_format1"

struct_time2 = time.strptime("Nov 2021 8", "%b %Y %H") # time.struct_time(tm_year=2021, tm_mon=11, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=305, tm_isdst=-1)
# |--------------------------------------------------/

# |-----

#C# --- Calendar usage

# |-----

# |--------------------------------------------------\
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
# |--------------------------------------------------/

#T# make the calendar for a given year with the calendar.calendar() function, this prints similar to the example of calendar.month() but for all months in the year
str1 = calendar.calendar(2020)

#T# check if a given year is leap
bool1 = calendar.isleap(2020) # True

#T# the leapdays function returns the number of leap days in a time interval
# SYNTAX calendar.leapdays(ini_year1, end_year1)
#T# the count of leap days is done between ini_year1, and end_year1
int1 = calendar.leapdays(2020, 2029) # 3

# |--------------------------------------------------\
#T# the monthcalendar function returns a list of lists

# SYNTAX list1 = calendar.monthcalendar(year1, month1)
#T# list1 holds the days of month1 from year1, with one inner list for each week of month1

list1 = calendar.monthcalendar(2002, 3) # [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31]]
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# the monthrange function returns a tuple with the first weekday number, and the number of days in a given month

# SYNTAX tuple1 = calendar.monthrange(year1, month1)
#T# tuple1 contains the first weekday number of month1, and its number of days

tuple1 = calendar.monthrange(1999, 4) # (3, 30)
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# the weekday function returns the weekday from a given day

# SYNTAX calendar.weekday(year1, month1, day1)
#T# this returns the weekday number of day1 in month1 from year1

int1 = calendar.weekday(1999, 4, 1) # 3
# |--------------------------------------------------/

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