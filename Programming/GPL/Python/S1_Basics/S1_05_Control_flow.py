
#   Control flow

#T# Table of contents

#C# Decision making
#C# --- Conditional statements
#C# Loops
#C# --- for loop
#C# --- while loop
#C# List comprehension

#T# Beginning of content

#C# Decision making

# |-------------------------------------------------------------
#T# decision making is made with the if, elif, and else keywords

#T# in an if conditional statement a condition is checked and if it returns True then the if block is executed, this also happens in an elif conditional statement

#T# in an else conditional statement no condition is checked, but the else requires an if above it, the elif also requires an if above

#T# a colon goes at the end of the line after an if, elif, or else keyword

#C# --- Conditional statements

# |-----
#T# conditional statements are carried out with the following syntax

# SYNTAX if, elif, else conditional statements
# if condition1:
#     statements1
# elif condition2:
#     statements2
# else:
#     statements3
#T# if condition1 returns True then the statements1 are executed, else if condition2 returns True then statements2 are executed, else statements3 are executed. Decision making statements can be nested

int1 = 0
if int1:
    int2 = 1
elif ~int1:
    if (int1 == 0):
        int2 = 2
else:
    int2 = 3
# int2 == 2
# |-----

# |-------------------------------------------------------------

#C# Loops

# |-------------------------------------------------------------
#T# loops are made with the for, and while keywords

#T# in a for loop, the loop is repeated for each element of an iterable, so an iterable has to be given

#T# in a while loop, the loop is repeated as long as the while condition returns True

#T# a colon goes at the end of the line after a for, or while keyword

#C# --- for loop

# |-----
#T# the for loop is made with the following syntax

# SYNTAX for loop
# for elem_i1 in arr1:
#     statements1
#     [continue|break]
# else:
#     statements2
#T# arr1 is an iterable, the loop executes the statements1 for each value in arr1, said value is assigned to the iterator elem_i1 in each iteration. The statements2 execute after the loop

#T# the continue keyword is used to skip the rest of the current iteration and start the next one

#T# the break keyword is used to skip all remaining iterations of the loop that contains the break, this also skips the else part of the loop

int1 = 0
int2 = 0
list1 = ['elem1', 'elem2']
for char_i1 in 's1tr':
    if (char_i1 == '1'): continue
    int1 += 1
    for elem_i2 in list1:
        if (elem_i2 == 'elem1'): break
        int2 += 1 # unreachable code
    if (int1 == 3): break
else:
    print("Unreachable code")
# int1 == 3; int2 == 0

# |--------------------------------------------------\
#T# typical use of the for loop includes the range function

# SYNTAX range(iniN, endN, stepN)
#T# this returns a range object with numbers starting at iniN, stepping by stepN, and ending at endN - 1

range1 = range(1, 12, 3) # this produces the numbers 1, 4, 7, 10
for i1 in range1:
    if i1 == 7:
        break
# |--------------------------------------------------/

# |-----

#C# --- while loop

# |-----
#T# the while loop is made with the following syntax

# SYNTAX while loop
# while condition1:
#     statements1
#     [continue|break]
# else:
#     statements2
#T# the statements1 are executed while condition1 is True, the statements2 are executed at the end of the loop, if there is no break, (for continue, break, int1, see the for loop subsection)

int1 = 0
while (int1 < 80):
    int1 += 30
else:
    int1 += 5
# int1 == 95
# |-----

# |-------------------------------------------------------------

#C# List comprehension

# |-------------------------------------------------------------
#T# create a list with a for using a list comprehension statement
list1 = [i1*i1 for i1 in range(5) if i1%2 == 0] # [0, 4, 16]
# |-------------------------------------------------------------