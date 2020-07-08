#!/usr/bin/python3
#   Lists

#T# declaring, updating, and accessing list
list1 = ['el1',2,'El3']
list1[1] = 5
print(list1[1:3])

#T# append to list with append()
list1.append("appEl")
list2 = list1
print(list2)

#T# remove from list with remove()
list1.remove('El3')
print(list1)

list3 = ['a','b']
#T# list functions
print("Repetitions of \'el1\'",list1.count('el1'))
list1.extend(list3)
print(list1)
print("Index of \'appEl\'",list1.index('appEl'))
list1.insert(1,'el3')
print(list1)
list1.pop(-4)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)