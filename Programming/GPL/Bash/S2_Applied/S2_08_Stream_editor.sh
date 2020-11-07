
#   Stream editor

#T# Table of contents

#C# Basic usage
#C# Substitution of expressions

#T# Beginning of content

# |-------------------------------------------------------------
#T# the sed program is a flexible stream editor
# |-------------------------------------------------------------

#C# Basic usage
# |-------------------------------------------------------------
#T# sed is used as a command in the shell of the operating system

# SYNTAX sed 'command1' 0<file1 1>new_file1
#T# sed takes input from file1, executes command1 over each line, and sends its output to new_file1, command1 is inside sigle quotes to avoid shell expansions

# SYNTAX sed -o1 -o2 var2
#T# same as before, with input from stdin, and output to stdout, -o1 represents a flag, -o2 var2 represent a kwarg pair

#T# some of the options of the sed program are
#T#     -n, do not output all lines after processing
#T#     -E, interpret any regex inside command1 with the Extended Regular Expression rules
# |-------------------------------------------------------------

#C# Printing a match

# |-------------------------------------------------------------
#T# a match found in the input can be printed to the output of the command

# SYNTAX sed '/pattern1/p'
#T# this prints the lines in which a match to pattern1 was found, the input is stdin, and the output is stdout

echo -e "ab\ncd\nef" | sed -nE '/[ce]/p'
#T# the former prints
# cd
# ef

# SYNTAX sed '/pattern1/w file1'
#T# this prints the output directly to file1
echo -e "ab\ncd\nef" | sed -E '/[ce]/w file1'
cat file1
#T# the former prints
# cd
# ef
# |-------------------------------------------------------------

#C# Substitution of expressions

# |-------------------------------------------------------------
#T# an expression found in the input file can be substituted for another in the output file

# SYNTAX sed 's/pattern1/replace1/' 0<file1 1>new_file1
#T# the first occurrence of pattern1 in each line from file1 is substituted with replace1, the result is output to new_file1, pattern1 can be regex

#T# the slash / is a delimiter character, but it can be any other character, even a letter, the / is just a convention

#T# the contents of file1 are the following
# first word1 word1 line
# second word1 line
# third word1 line
sed 's/word1/substituted/' 0<file1 1>new_file1
cat new_file1
#T# the former prints
# first substituted word1 line
# second substituted line
# third substituted line

# SYNTAX sed 's/pattern1/substr1&substr2/' 0<file1 1>new_file1
#T# same as before, but replace the match with substr1 before it, and substr2 after it, the ampersand & is replaced with the match (it can be repeated)
echo "start541end" | sed -E 's/[0-9]+/| & |/' # start| 541 |end

# SYNTAX sed 's/pattern1/replace1/g'
#T# same as before, but the char 'g' that appears at the end is a regex modifier (also known as a regex flag), this 'g' makes the substitution to be global, i.e. to change all instances of pattern1 for replace1
echo "word1 second_word end" | sed -E 's/\w+/subs/' # subs subs subs

# SYNTAX sed 's/pattern1/replace1/int1'
#T# same as before, but the number int1 is used as a regex modifier, in such a way that only the occurrence int1 of pattern1 is replaced with replace1, if used with the g regex modifier, the remaining occurrences are replaced as well
echo "str1str2str3str4" | sed -E 's/str/NEW/3g' # str1str2NEW3NEW4

# SYNTAX sed 's/pattern1/replace1/I'
#T# same as before, but the I regex modifier matches pattern1 case insensitive
echo "Str1" | sed -E 's/str/NEW/I' # NEW1

#T# when mixing 'p', 'w', etc. (see Printing a match), with regex modifiers, the w must be the last one
echo -e "ab\ncd" | sed -E 's/c/C/pw file1'
cat file1 # Cd
# |-------------------------------------------------------------