
#   Control flow

#T# Table of contents

#T# Decision making

#T# if, elif, else keywords

#T# Loops

#T# for loop
#T# while loop

#T# List comprehension

#T# Beginning of content

#T# Decision making

#T# decision making is made with the if, elif, and else keywords. In an if conditional statement a condition is checked and if it returns True then the if block will be executed. In an elif conditional statement a condition is also checked. In an else conditional statement no condition is checked, but the else requires an if above it, the elif also requires an if above

#T# a colon goes at the end of the line after an if, elif, or else keyword

#T# if, elif, else keywords

int1 = 0
#T# if elif else syntax
# if condition1:
#     statements1
# elif condition2:
#     statements2
# else:
#     statements3
#T# if condition1 returns True then the statements1 are executed, else if condition2 returns True then statements2 are executed, else statements3 are executed
if int1:
    int2 = 1
elif ~int1:
#T# decision making statements can be nested
    if (int1 == 0):
        int2 = 2
else:
    int2 = 3
# int2 == 2

#T# Loops

#T# loops are made with the for, and while keywords. In a for, the loop is repeated for each element of an iterable, so an iterable has to be given. In a while, the loop is repeated as long as the while condition returns True

#T# a colon goes at the end of the line after a for, or while keyword

#T# for loop

int1 = 0
int2 = 0
list1 = ['elem1',2]
#T# for, else syntax, and nested loops
# for elem_i1 in arr1:
#     statements1
# else:
#     statements2
#T# arr1 is an iterable, the loop executes the statements1 for each value in arr1, said value is assigned to the iterator elem_i1 in each iteration. The statements2 execute after the loop 
for char_i1 in 's1tr':
#T# use the continue keyword to skip the rest of the current iteration and start the next one
    if (char_i1 == '1'): continue
    int1 += 1
    for elem_i2 in list1:
#T# use the break keyword to skip all remaining iterations of the loop that contains the break
        if (elem_i2 == 'elem1'): break
        int2 += 1
#T# int1 == 3; int2 == 0

#T# typical use of the for loop includes the range function
# range(iniN,endN,stepN)
#T# this returns a range object with numbers starting at iniN, stepping by stepN, and ending at endN - 1
range1 = range(1,12,3) # this produces the numbers 1, 4, 7, 10

for i1 in range1:
    if i1 == 7:
        break
#T# the break also skips the else part of the loop, the else part only executes at the end of the loop if there is no break
else:
    print("Unreachable code")

#T# while loop

int1 = 0
#T# while syntax
# while condition1:
#     statements1
# else:
#     statements2
#T# the statements1 are executed while condition1 is True, the statements2 are executed at the end of the loop, and if there is no break
while (int1 < 80):
    int1 += 30
else:
    int1 += 5
#T# int1 == 95

#T# List comprehension

#T# create a list with a for using a list comprehension statement
list1 = [i1*i1 for i1 in range(5) if i1%2 == 0] # [0, 4, 16]