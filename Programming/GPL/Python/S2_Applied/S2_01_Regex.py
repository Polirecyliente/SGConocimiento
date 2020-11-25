
#C# Regex matching

# |-------------------------------------------------------------
#T# import the regex module to use regular expressions, it supersedes the re module
import regex

#C# --- Regex functions, methods, and attributes

# |-----
#T# compile a regex object with the compile function, this object has access to the rest of regex functions, methods, and attributes shown here
regex_object1 = regex.compile(r'pattern1') # regex.Regex('pattern1', flags=regex.V0)

#T# match at the start of the string with the match function, if the match fails then None is returned
# SYNTAX match('pattern1', 'str1')
match1 = regex.match(r'a', 'aabbcc') # <regex.Match object; span=(0, 1), match='a'>

#T# match at any place of the string with the search function, if the match fails then None is returned
# SYNTAX search('pattern1', 'str1')
search1 = regex.search(r'(bc)(cd)', 'aabbccdd') # <regex.Match object; span=(3, 7), match='bccd'>

#T# get a list with the regex groups found with the groups function
search1 = regex.search(r'(bc)(cd)', 'aabbccdd') # <regex.Match object; span=(3, 7), match='bccd'>
tuple1 = search1.groups() # ('bc', 'cd')

#T# get a particular group value with the group function

# SYNTAX group(int1)
#T# int1 is the group number

search1 = regex.search(r'(bc)(cd)', 'aabbccdd')
str1 = search1.group(2) # 'cd'

#T# get the starting position of a group with the start function

# SYNTAX start(int1)
#T# int1 is the group number, this returns a position (the start of the string is 0)

search1 = regex.search(r'(bc)(cd)', 'aabbccdd')
int1 = search1.start(2) # 5

#T# get a list with all global matches with the findall function
list1 = regex.findall(r'text', 'strtextstrtextstr') # ['text', 'text']

#T# get a list without the matches with the split function
list1 = regex.split(r'text', 'strtextstrtextstr') # ['str', 'str', 'str']

#T# substitute matches with a replacement string with the sub function
str1 = regex.sub(r'text', 'TEXT', 'strtextstrtextstr') # 'strTEXTstrTEXTstr'

#T# the Match objects have a few properties and methods

#T# the groups method returns a tuple where each element is the match of a group
search1 = regex.search(r'(s)(tr)(1)', 'str1') # <regex.Match object; span=(0, 4), match='str1'>
tuple1 = search1.groups() # ('s', 'tr', '1')

#T# the span method returns the start and end positions of a group, or of the match if no group is input as argument
search1 = regex.search(r'(s)(tr)(1)', 'str1') # <regex.Match object; span=(0, 4), match='str1'>
tuple1 = search1.span(1) # (0, 1)

#T# the group method returns the contents of single groups, or the whole match if no group is input as argument
search1 = regex.search(r'(s)(tr)(1)', 'str1') # <regex.Match object; span=(0, 4), match='str1'>
str1 = search1.group(2) # 'tr'

#T# the string property contains the string being analyzed, i.e. the one that the regex is being applied on, the input string
search1 = regex.search(r'(s)(tr)(1)', 'textstr1text') # <regex.Match object; span=(4, 8), match='str1'>
str1 = search1.string # 'textstr1text'
# |-----

#C# --- Characters

# |-----
#T# the dot . is used to match any char
search1 = regex.search(r'.', 'str1') # <regex.Match object; span=(0, 1), match='s'>

#T# to match an operator as a literal char, it must be escaped with a backslash \
search1 = regex.search(r'\.', 'str1.') # <regex.Match object; span=(4, 5), match='.'>

#T# the escaped char \s matches one whitespace (space, tab, newline)
search1 = regex.search(r'\sb', 'a b') # <regex.Match object; span=(1, 3), match=' b'>

#T# the escaped char \S matches one non whitespace
search1 = regex.search(r'\Sc', 'a bc') # <regex.Match object; span=(2, 4), match='bc'>

#T# the escaped char \w matches one alphanumeric character or an underscore
search1 = regex.search(r'\w', '_a5.') # <regex.Match object; span=(0, 1), match='_'>

#T# the escaped char \W matches one non alphanumeric character nor an underscore
search1 = regex.search(r'\W', '_a5.') # <regex.Match object; span=(3, 4), match='.'>

#T# the escaped char \d matches one digit
search1 = regex.search(r'\d', 'a5b') # <regex.Match object; span=(1, 2), match='5'>

#T# the escaped char \D matches one non digit
search1 = regex.search(r'\D', '5bc') # <regex.Match object; span=(1, 2), match='b'>

#T# the escaped char \X matches one unicode char
search1 = regex.search(r'\w\X', 'a\u2446b') # <regex.Match object; span=(0, 2), match='a⑆'>

#T# the escaped char \t matches one tab char
search1 = regex.search(r'\tc', 'ab    c') # <regex.Match object; span=(2, 4), match='\tc'>

#T# the escaped char \r matches one carriage return (this also works in the sed program)
print('ab\rc') # cb
search1 = regex.search(r'\rc', 'ab\rc') # <regex.Match object; span=(2, 4), match='\rc'>

#T# the escaped char \n matches one newline
search1 = regex.search(r'r1\nst', 'str1\nstr2') # <regex.Match object; span=(2, 7), match='r1\nst'>

#T# there is no support for the escaped char \N to match a non newline, it can be replaced with [^\n]
search1 = regex.search(r'[^\n]c', 'ab\ncd') # None

#T# there is no support for the escaped char \h to match an horizontal whitespace (space, tab), it can be approximated by [^\S\n] but a few vertical spaces can be matched this way
search1 = regex.search(r'[^\S\n]b[^\S\n]c', 'a b    c') # <regex.Match object; span=(1, 5), match=' b\tc'>

#T# there is no support for the escaped char \H to match a non horizontal whitespace

#T# the escaped chars \Q and \E escape any characters inside them, but in Python they are not used, the escape function is used instead
search1 = regex.search(regex.escape(r'a.+?'), 'a.+?') # <regex.Match object; span=(0, 4), match='a.+?'>

#T# the escaped char \K removes the part of the match that is to its left
search1 = regex.search(r'str1\n\Kstr2', 'str1\nstr2') # <regex.Match object; span=(5, 9), match='str2'>

#T# comments are introduced with (?# comment1)
search1 = regex.search(r'(?# initial comment)str(?# a number comes next)1', 'str1') # <regex.Match object; span=(0, 4), match='str1'>
# |-----

#C# --- Quantifiers

# |-----
#T# the question mark ? is used as a quantifier to match 0 or 1 of the preceding char
search1 = regex.search(r'r?1', 'str1') # <regex.Match object; span=(2, 4), match='r1'>

#T# the asterisk * is used as a quantifier to match 0 or more of the preceding char
search1 = regex.search(r'r*1', 'st1') # <regex.Match object; span=(2, 3), match='1'>

#T# the plus sign + is used as a quantifier to match 1 or more of the preceding char
search1 = regex.search(r'r+1', 'strrr1') # <regex.Match object; span=(2, 6), match='rrr1'>

#T# the syntax {int1} is used as a quantifier to match the preceding char int1 times
search1 = regex.search(r'r{2}1', 'strrrr1') # <regex.Match object; span=(4, 7), match='rr1'>

#T# the syntax {int1,int2} is used as a quantifier to match the preceding char between int1 and int2 times (as many times as possible), so int2 >= int1, if int2 is omitted then match any amount greater than or equal to int1
search1 = regex.search('r{1,3}1', 'strrrrr1') # <regex.Match object; span=(4, 8), match='rrr1'>
search1 = regex.search(r'r{1,}1', 'strrrrr1') # <regex.Match object; span=(2, 8), match='rrrrr1'>

#T# lazy (non greedy) quantifiers are created with a question mark ? after the operator, works as ??, *?, +?
search1 = regex.search(r'[0-9][0-9]??', '12345') # <regex.Match object; span=(0, 1), match='1'>
search1 = regex.search(r'[0-9]*?', '12345') # <regex.Match object; span=(0, 0), match=''>
search1 = regex.search(r'[0-9]+?', '12345') # <regex.Match object; span=(0, 1), match='1'>

#T# possessive quantifiers add a plus + at the end of the other quantifiers, they are greedy without backtracking, so that after a match fails, it is not checked if less chars would make it succeed, works as *+, ++, {}+
search1 = regex.search(r'a*+', 'aaa') # <regex.Match object; span=(0, 3), match='aaa'>
search1 = regex.search(r'\w++b', 'aaaab') # None #| 'aaaab' would be matched without the possessive quantifier
search1 = regex.search(r'\w{1,7}+F', 'abcdeF') # None #| 'abcdeF' would be matched without the possessive quantifier
# |-----

#C# --- Character classes

# |-----
#T# the syntax [char1char2charN] is called a character class, and used to match any single one of the characters, char1, char2, up to charN
search1 = regex.search(r'[trs]1', 'strr1') # <regex.Match object; span=(3, 5), match='r1'>


# TODO set operations with character classes

# |-----

#C# --- Groupings

# |-----
#T# the parentheses () are used to capture a group of chars, and treat this group the same as treating a single char
search1 = regex.search(r'(tr)+1', 'strtr1') # <regex.Match object; span=(1, 6), match='trtr1'>


#T# the vertical bar | is used for alternation (to match either one of the patterns separated with the vertical bar)
search1 = regex.search(r'st|tr1', 'str1') # <regex.Match object; span=(0, 2), match='st'>



# |-----

#C# --- Subroutines and conditionals

# |-----

# |-----

#C# --- Anchors and boundaries

# |-----
#T# the caret ^ (outside a character class) matches the following chars as an anchor at the start of the line
search1 = regex.search(r'^str', 'str1') # <regex.Match object; span=(0, 3), match='str'>

#T# the escaped char \A does the same as the caret ^, it anchors the match at the beginning of the line
search1 = regex.search()

# echo "str1" | grep -P '\Astr' # str

#T# the dollar sign $ matches the preceding chars as an anchor at the end of the line
search1 = regex.search(r'tr1$', 'str1') # <regex.Match object; span=(1, 4), match='tr1'>



# |-----

#C# --- Lookarounds

# |-----
# |-----

#C# --- Regex modifiers

# |-----
#T# regular regex modifiers are passed via the flags kwarg of the regex functions from the re module


# |-----

# |-------------------------------------------------------------