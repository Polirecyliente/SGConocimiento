
#   Arrays

#T# Lists

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

#T# Tuples

#T# declaration and accessing
tupl1 = ('tEl1','tElB','tF')
print(tupl1[1:3])

#T# tuple functions

#T# get the size or length of a tuple with the len(tuple1) function
var1 = len(tupl1)
var2 = max(tupl1)

#T# Dictionaries

#T# declaration, updating, and accessing
dict1 = {'key1':5,'key2':'val2'}
dict1['keyNew'] = 'newV'
print(dict1['keyNew'])

#T# clear the whole dictionary with clear()
dict1.clear()
print(dict1)

dict2 = {'key1':7,'key2':'val2'}
#T# dictionary functions
print("dict with str representation:",str(dict2))
print("type of dict var is: ",type(dict2))
dict3 = dict2.copy()
print("new dict: ",dict3)
tupl1 = ('tupK1','valNo')
dict4 = dict.fromkeys(tupl1,8)
print("dict from keys:",dict4)
print("value from key \'key2\'",dict2.get('key2'))
print("dict's items:",dict2.items())
print("dict's keys:",dict2.keys())
print("dict's values:",dict2.values())

#T# append a dictionary to another with dict1.update(dictAppended)
dict2.update(dict4)
print("append a dict to another:",dict2)
dict2.setdefault('noKey','defVal')
print("default value:",dict2['noKey'])

#T# Strings

#T# string declaration, updating, and access
str1 = "first string"
updStr1 = str1 + ' update'
print("pos 3 to 8: ",updStr1[3:9])

#T# membership with in
if ("g" in updStr1):
    print("the string also has a \"g\"")

#T# print escape sequences with raw string prefix "r" or "R"
print(r"\nRaw\tString")

#T# print formatted with %
print("string: %s, digit: %d" %("S1",514))

#T# unicode string with prefix "u"
print(u"gálèät")

#T# string interpolation with prefix "f"
print(f"partial string {updStr1[3:9]}")

#T# string functions
print("capital first".capitalize())
print("centered".center(20))
print("leftJus".ljust(20))
print("rightJus".rjust(20))
print("The t's in the string are ",updStr1.count("t",1,len(updStr1)))
encSt = updStr1.encode('utf8','strict')
print("Encoded string: ",encSt)
print("Decoded string: ",encSt.decode('utf8','strict'))
print("String ends with date? ",updStr1.endswith("date",7,len(updStr1)))
print("String begins with irst?",updStr1.startswith("irst",1,10))
print("With\texpanded\ttabs".expandtabs(18))
print("is \"second\" in string? ",updStr1.find("second",3,len(updStr1)))
print("index of \"str\" is ",updStr1.index("str",3,len(updStr1)))
print("is it purely alphanumeric? ",updStr1.isalnum())
print("is it purely alphabetic? ",updStr1.isalpha())
print("is it purely numeric? ",updStr1.isdigit())
print("is it purely lowercase? ",updStr1.islower())
print("another numeric? ",updStr1.isnumeric())
print("has it only decimal characters? ",updStr1.isdecimal())
print("is it purely whitespace? ",updStr1.isspace())
print("is it titlecased? ",updStr1.istitle())
print("is it purely uppercase? ",updStr1.isupper())
list1 = ['el1',"2",'El3']
print("joined as string ","-|-".join(list1))
print("all uppercase ",updStr1.upper())
print("ALL LOWERCASE ".lower())
print("sWAP cASE!".swapcase())
print("title cased ",updStr1.title())
print(" \t  stripped of leading whitespace".lstrip())
print("stripped of trailing whitespace \t ".rstrip())
print(" \t both ways stripped \t ".strip())
translTab = "".maketrans("aeiou","12345")
print(updStr1.translate(translTab))
print("max alphabetical char is ",max(updStr1))
print("min alphabetical char is ",min(updStr1))
print("replace str: ",updStr1.replace("t","q",2))
print("reverse find: ",updStr1.rfind("second",2,len(updStr1)))
print("reverse index: ",updStr1.rindex("t",3,len(updStr1)))
list2 = updStr1.split(" ")
print("list2 is ",list2)
list3 = "line1\nline2 w1\nl3 w1 w2 w3".splitlines()
print("list3 is ",list3)
print("zero filled".zfill(20))