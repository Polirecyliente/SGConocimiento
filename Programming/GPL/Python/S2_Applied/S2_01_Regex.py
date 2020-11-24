
#C# Regex matching

# |-------------------------------------------------------------
#T# import the re module to use regular expressions
import re

#C# --- Regex functions

# |-----
#T# match at the start of the string with the match function
# SYNTAX match('pattern1', 'str1')
match1 = re.match('a', 'aabbcc') # <re.Match object; span=(0, 1), match='a'>

#T# match at any place of the string with the search function
# SYNTAX search('pattern1', 'str1')
search1 = re.search('(bc)(cd)', 'aabbccdd') # <re.Match object; span=(3, 7), match='bccd'>

#T# get a list with the regex groups found with the groups function
search1 = re.search('(bc)(cd)', 'aabbccdd')
tuple1 = search1.groups() # ('bc', 'cd')

#T# get a particular group value with the group function

# SYNTAX group(int1)
#T# int1 is the group number

search1 = re.search('(bc)(cd)', 'aabbccdd')
str1 = search1.group(2) # 'cd'

#T# get the starting position of a group with the start function

# SYNTAX start(int1)
#T# int1 is the group number, this returns a position (the start of the string is 0)

search1 = re.search('(bc)(cd)', 'aabbccdd')
int1 = search1.start(2) # 5

#T# get a list with all global matches with the findall function
list1 = re.findall('text', 'strtextstrtextstr') # ['text', 'text']

#T# get a list without the matches with the split function
list1 = re.split('text', 'strtextstrtextstr') # ['str', 'str', 'str']

#T# substitute matches with a replacement string with the sub function
str1 = re.sub('text', 'TEXT', 'strtextstrtextstr') # 'strTEXTstrTEXTstr'
# |-----

#C# --- Characters

# |-----
#T# the dot . is used to match any char
search1 = re.search('.', 'str1') # <re.Match object; span=(0, 1), match='s'>

#T# to match an operator as a literal char, it must be escaped with a backslash \
search1 = re.search('\.', 'str1.') # <re.Match object; span=(4, 5), match='.'>

#T# the escaped char \s matches one whitespace (space, tab, newline)
search1 = re.search('\sb', 'a b') # <re.Match object; span=(1, 3), match=' b'>

#T# the escaped char \S matches one non whitespace
search1 = re.search('\Sc', 'a bc') # <re.Match object; span=(2, 4), match='bc'>

#T# the escaped char \w matches one alphanumeric character or an underscore
search1 = re.search('\w', '_a5.') # <re.Match object; span=(0, 1), match='_'>

#T# the escaped char \W matches one non alphanumeric character nor an underscore
search1 = re.search('\W', '_a5.') # <re.Match object; span=(3, 4), match='.'>

#T# the escaped char \d matches one digit
search1 = re.search('\d', 'a5b') # <re.Match object; span=(1, 2), match='5'>

#T# the escaped char \D matches one non digit
search1 = re.search('\D', '5bc') # <re.Match object; span=(1, 2), match='b'>

#T# the escaped char \t matches one tab char
search1 = re.search('\tc', 'ab    c') # <re.Match object; span=(2, 4), match='\tc'>




# |-----

#C# --- Quantifiers

# |-----


#T# the asterisk * is used as a quantifier to match 0 or more of the preceding char
search1 = re.search('r*1', 'st1') # <re.Match object; span=(2, 3), match='1'>

#T# the plus sign + is used as a quantifier to match 1 or more of the preceding char
search1 = re.search('r+1', 'strrr1') # <re.Match object; span=(2, 6), match='rrr1'>

#T# the syntax {int1} is used as a quantifier to match the preceding char int1 times
search1 = re.search('r{2}1', 'strrrr1') # <re.Match object; span=(4, 7), match='rr1'>



# |-----

#C# --- Character classes

# |-----
#T# the syntax [char1char2charN] is called a character class, and used to match any single one of the characters, char1, char2, up to charN
search1 = re.search('[trs]1', 'strr1') # <re.Match object; span=(3, 5), match='r1'>

# |-----

#C# --- Groupings

# |-----
#T# the parentheses () are used to capture a group of chars, and treat this group the same as treating a single char
search1 = re.search('(tr)+1', 'strtr1') # <re.Match object; span=(1, 6), match='trtr1'>


#T# the vertical bar | is used for alternation (to match either one of the patterns separated with the vertical bar)
search1 = re.search('st|tr1', 'str1') # <re.Match object; span=(0, 2), match='st'>



# |-----

#C# --- Anchors and boundaries

# |-----
#T# the caret ^ (outside a character class) matches the following chars as an anchor at the start of the line
search1 = re.search('^str', 'str1') # <re.Match object; span=(0, 3), match='str'>

#T# the escaped char \A does the same as the caret ^, it anchors the match at the beginning of the line
search1 = re.search()

echo "str1" | grep -P '\Astr' # str

#T# the dollar sign $ matches the preceding chars as an anchor at the end of the line
search1 = re.search('tr1$', 'str1') # <re.Match object; span=(1, 4), match='tr1'>



# |-----

#C# --- Lookarounds

# |-----
# |-----

# |-------------------------------------------------------------