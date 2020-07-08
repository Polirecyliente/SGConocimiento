#!/usr/bin/python3
#   Datetime

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