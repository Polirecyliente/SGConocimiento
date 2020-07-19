
#   Control flow

#T# Contents
#T# Decision making
#T# Loops

#T# Decision making

val1 = 0

#T# if elif else statement
if val1:
    print("In if")
elif ~val1:
    print("In elif")
    if (val1 == 0):
        print("In nested if")
else:
    print("In else")

print("After statement")

#T# Loops

val1 = 0

#T# while else statement
while (val1 < 80):
    print("In while")
    val1 = val1 + 30
else:
    print(val1, " is the result")

list1 = ['el1',2,'el3']

#T# for in else statement, nested loop, continue, break
for charIt1 in 'S1':
    print("The character is ",charIt1)
    if (charIt1 == '1'): continue
    for elIt1 in list1:
        if (elIt1 == 2): break
        print("In nested loop, The element is ",elIt1)
for idx in range(1,3):
    print("The index is ",idx)
else:
    print("In for's else")

#T# create a list (array) with a for in a list comprehension statement
comprehList1 = [i1*i1 for i1 in range(5) if i1%2 == 0]

#T# pass statement
pass