
#   Builtin functions

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

#T# Datetime

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