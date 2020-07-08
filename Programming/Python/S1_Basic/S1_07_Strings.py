#!/usr/bin/python3
#   Strings

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