
#   Regex

#T# import the regex module
import re

#T# match at the start of the string with match('regexStr', 'textStr')
match1 = re.match('a', 'aabbcc')

#T# match at any place of the string with search('regexStr', 'textStr')
search1 = re.search('(bc)(cd)', 'aabbccdd')

#T# get a list with regex groups found with groups()
print(search1.groups())

#T# get a particular group value with group(groupNum)
print(search1.group(2))

#T# get the starting position of a group with start(groupNum)
print(search1.start(2))