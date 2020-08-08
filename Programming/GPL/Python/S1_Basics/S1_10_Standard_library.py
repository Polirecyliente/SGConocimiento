
#   Builtin functions

#T# String functions
#T# List functions
#T# Dictionary functions
#T# Datetime functions

import math
x = -5.15
y = 4

#T# basic math functions
print("x is ",x," it's absolute value is ",abs(x))
print("x ceil is ",math.ceil(x))
print("e to the x is ",math.exp(x))
print("the abs val of x as a float is ",math.fabs(x))
print("x floor is ",math.floor(x))
print("y log in base 3 is ",math.log(y,3))
print("y log base 10 is ",math.log10(y))
print("the max of x and y is ",max(x,y))
print("the min of x and y is ",min(x,y))
[floX,intX] = math.modf(x)
print("int part of x is ",intX," deciman part of x is ",floX)
print("x to the y is ",pow(x,y))
print("x rounded to 1 decimal is ",round(x,1))
print("y square root is ",math.sqrt(y))
print("pi constant value is ",math.pi)
print("e constant value is ",math.e)

import random

#T# randon number functions
print("random element from a list: ",random.choice([x,y,intX]))
print("random number in range ",random.randrange(1,12,3))
print("random float between 0 and 1 ",random.random())
print("set the rng seed ",random.seed(2))
list1 = [3,2,9]
random.shuffle(list1)
print("shuffled list is",list1)
print("random float in range ",random.uniform(3,5))

#T# trigonometric functions
print("arc cosine of 0.5 is ",math.acos(0.5))
print("arc sine of 0.5 is ",math.asin(0.5))
print("arc tangent of 2.1 is ",math.atan(2.1))
print("arc tangent of 21 over 10 is ",math.atan2(21,10))
print("cosine of pi/4 is ",math.cos(math.pi/4))
print("sine of pi/4 is ",math.sin(math.pi/4))
print("tangent of pi/4 is ",math.tan(math.pi/4))
print("the hypotenuse with sides 3 and 4 is ",math.hypot(3,4))
print("convert pi/4 radians to degrees ",math.degrees(math.pi/4))
print("convert 45 degrees to radians ",math.radians(45))

def fun1(a1):
    return 2*a1

l1 = [1,3,5,7,9,11]
#T# map (in this context it means apply) a function to an iterable set with map(fun1,iterSet)
l2 = list(map(fun1,l1))

print("list l1 after map is",l2)

#T# String functions

str1 = "partial string ing writt, str2 = 'first string written'"
#T# capitalize the first letter of the string
str1 = str1.capitalize()

#T# center a string str1 in a given width1, padding with char1, with str1.center(width1,char1)
str1 = str1.center(35,"-")

#T# left justify a string, same arguments as in the center function
str1 = str1.ljust(40,">")

#T# right justify a string, same arguments as in the center function
str1 = str1.rjust(42,"<")

#T# count repetitions of substrings, in str1.count("substr"[,startN[,endN]]) the string "substr" is counted in the string slice str1[startN:endN]
int1 = str1.count("--")

#T# encode a string to bytes with the encode function, decode bytes to string with the decode function
byte1 = str1[11:15].encode('utf-8') + b"\x41\x20"
str2 = byte1.decode('utf-16')

#T# a few valid encodings, 'utf-8', 'utf-16', 'utf-32', 'unicode-escape', 'ascii', 'Latin-1', 'cp1252' cp is for code pages, chinese 'big5', arabic 'iso8859_6', greek 'mac_greek', hebrew 'cp424'
str2 = byte1.decode('unicode-escape')
str2 = byte1.decode('ascii')
str2 = byte1.decode('Latin-1')
str2 = byte1.decode('cp1252')
str2 = byte1.decode('big5')
str2 = byte1.decode('iso8859_6')
str2 = byte1.decode('mac_greek')
str2 = byte1.decode('cp424')
#T# can't decode an utf-8 encoded string in utf-32 unless extra bytes are added
# str2 = byte1.decode('utf-32')

str2 = "ü\u02A0"
#T# When encoding with 'unicode-escape' the returned byte object contains the unicode escape sequence \uNNNN or \xNN for non ascii chars
byte1 = str2.encode('unicode-escape')

#T# check if a string starts or ends with a given string, in str1.startswith("substr"[,startN[,endN]]) returns true if str1[startN:endN] starts with "substr", same arguments for the endswith function
bool1 = str1.startswith("arti",9,18)
bool1 = str1.endswith(" st",9,18)

str2 = "With\texpanded\ttabs"
#T# change the tab size with the expandtabs function
str2 = str2.expandtabs(5)

#T# get the pos of the first substring found in a string, same arguments as in the startswith function, the following returns 3 since 'tial' is at position 3 in 'Partial'
int1 = str1.find('tial',2)

#T# do the same as the find function but raise an exception on failure with the index function, same arguments as in the startswith function
int1 = str1.index('tial')

#T# do a reverse find, in the sense of starting the search at the end of the string, with the functions rfind, and rindex, similarly rindex raises an exception on failure while rfind does not, same arguments as in the startswith function
int1 = str1.rfind("stri",3,45)
int1 = str1.rindex("stri",3,41)

str2 = "test5trin6"
#T# check if a string is only made of alphabetic chars, no whitespace allowed
bool1 = str2.isalpha()

#T# check if a string is made with numbers, the difference in the following functions is according to unicode definition
bool1 = str2.isdigit()
bool1 = str2.isnumeric()
bool1 = str2.isdecimal()

#T# check if a string is only made of alphanumeric chars
bool1 = str2.isalnum()

#T# check if a string is all whitespace
bool1 = str2.isspace()

str2 = 'New Te5T'
#T# check if a string is all lowercase
bool1 = str2.islower()

#T# check if a string is in title case, numbers start new words, the following returns True
bool1 = str2.istitle()

#T# check if a string is in upper case
bool1 = str2.isupper()

#T# join the string elements of an array, in "insert1".join(arr1) arr1 must be an array of strings, the returned string has "insert1" between each pair of elements in arr1
str2 = "-|-".join(("elem1","elem2"))

#T# split a string into elements of an array, in str1.split("separator1") str1 is split at each occurrence of the string "separator1", leaving out "separator1"
list1 = str2.split("-|")

#T# split around newlines, in str1.splitlines(bool1) bool1 determines whether or not each element stores the newline at the end of the element
list1 = "line1\nline2 w1\nline3 w1 w2".splitlines(True)

#T# make all letters uppercase with the upper function
str2 = str2.upper()

#T# make all letters lowercase with the lower function
str2 = str2.lower()

#T# make a string title cased with the title function
str2 = str2.title()

#T# swap the case of a string with the swapcase function
str2 = str2.swapcase()

str2 = 'abba' + str2 + 'baab'
#T# strip the whitespace at both sides of a string with the strip function, use str1.strip('chars1') to strip all chars in 'chars1' from both sides of str1
str2 = str2.strip('abe')

str2 = str2.rjust(20).ljust(25)
#T# strip leading whitespace at the left of a string with the lstrip function, same arguments as in the strip function
str2 = str2.lstrip()

#T# strip trailing whitespace at the right of a string with the rstrip function, same arguments as in the strip function
str2 = str2.rstrip()

#T# create a dictionary with a translation table with the maketrans function, and use it with the translate function. In str.maketrans(str1,str2,str3), each char in str1 gets translated to str2, and each char in str3 is translated to None. In str1.translate(dict1) the chars in str1 get translated according to the translation table in dict1
dict1 = str.maketrans("aeiou","12345","s")
str2 = str1.translate(dict1)

#T# replace a substring for another in a string, in str1.replace("substr1","replace1",countN) the first countN occurrences of "substr1" in str1 are replaced by the string "replace1"
str2 = str2.replace("t","67",2)

str2 = "zfilled_string"
#T# make a string str1 fill a given width1, padding with zeros at the left of str1, with str1.zfill(width1)
str2 = str2.zfill(20)

#T# List functions

list1 = ['a', 5, 'append_elem', 'a', 'elem5']
#T# count the repetitions of an element, in list1.count('elem1') the repetitions of the element 'elem1' are counted in list1
int1 = list1.count('a')

#T# get the index of the first occurrence, in list1.index('elem1') the returned value is the index of the first occurrence of 'elem1' in list1
int1 = list1.index('elem5')

#T# reverse the order of the elements with the reverse function, it returns None, so it shouldn't be assigned to a var
list1.reverse()

list1[3] = str(list1[3])
#T# sort elements in a list, in list1.sort([reverse = True|False[, key=fun1]]), the default order is ascending, if the reverse kwarg is True then the order is descending, the key kwarg is for the sorting function fun1, the result is sorted from smaller to bigger return values of this sorting function, the default is alphabetical order
list1.sort(reverse=True,key=len)

#T# Dictionary functions

dict1 = {'key1': 85, 'key2': 85}
#T# create a new key value pair in a dictionary only if the key doesn't already exists with the setdefault function
# dict1.setdefault('new_key1','new_val1')
#T# the pair 'new_key1', 'new_val1' will be added to dict1 only if 'new_key1' is not in dict1 already
dict1.setdefault('new_key','new_val') # new_val
dict1.setdefault('key2','val2') # 85

#T# Datetime functions

#T# import the time module
import time

#T# get current seconds with time.time()
currSec = time.time()

#T# gmtime() as a time structure
print("time structure of 9 values:",time.gmtime())

#T# local time with localtime()
print("The local time is",time.localtime(currSec))

#T# formatted time with asctime()
print("Formated time is",time.asctime(time.localtime(currSec)))

#T# import the calendar module
import calendar

#T# make the calendar for a given month with calendar.month()
cal1 = calendar.month(2020,2)
print("Calendar for Feb 2020 is\n",cal1)

#T# local difference to UTC in seconds with altzone
print("hours to UTC",time.altzone/3600)

#T# seconds from start of exection with clock()
print("seconds from start",time.clock())

#T# format time with ctime()
print("Formatted too",time.ctime(currSec))

#T# get seconds from epoch with mktime()
print("seconds from epoch:",time.mktime(time.localtime(currSec)))

#T# suspend execution with sleep()
time.sleep(0.3)
print("after sleep()")

var1 = time.localtime()
#T# custom format date with strftime()
print("Formatted date with %:",time.strftime(
    "%A%B%C %d%t%u %G %h %Hor%I %j %m%M%n%p%S %V %W %w %y %z%%",var1))

#T# string to time structure with strptime()
print("time structure from string:",time.strptime("Nov 2021 8","%b %Y %H"))

#T# get the timezone with timezone
print("Timezone here:",time.timezone)

#T# get the timezone name with tzname
print("Timezone name:",time.tzname)

#T# know if leap year with isleap()
print("is 2020 a leap year?",calendar.isleap(2020))

#T# make a year's calendar with calendar()
print(calendar.calendar(2020))

#T# get the first weekday with firstweekday()
print("first day of the week is",calendar.firstweekday())

#T# get number of leap days between years with leapdays()
print("leap days ",calendar.leapdays(2020,2021))

#T# get lists with day of the week inside month with monthcalendar()
print("lists with weekdays",calendar.monthcalendar(2002,3))

#T# get first day's weekday of a month and total days in the month with monthrange()
print("first weekday, days in month",calendar.monthrange(1999,4))

#T# get number of seconds from epoch with timegm()
print("other seconds from epoch",calendar.timegm(time.gmtime(time.time())))

#T# get weekday with weekday()
print("weekday is",calendar.weekday(2600,3,21))