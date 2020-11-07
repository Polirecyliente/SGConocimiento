
#   Stream editor

#T# Table of contents

#C# Basic usage
#C# Printing a match
#C# Substituting a match
#C# Deleting lines

#T# Beginning of content

# |-------------------------------------------------------------
#T# the sed program is a flexible stream editor
# |-------------------------------------------------------------

#C# Basic usage
# |-------------------------------------------------------------
#T# sed is used as a command in the shell of the operating system

# SYNTAX sed 'command1' 0<file1 1>new_file1
#T# sed takes input from file1, executes command1 over each line, and sends its output to new_file1, command1 is inside sigle quotes to avoid shell expansions

sed 's/a/Z1/' 0<file1 1>new_file1 # (see Substituting a match)
cat file1     # ab
cat new_file1 # Z1b

# SYNTAX sed 'command1' file1 file2
#T# this syntax is used when there are several input files, the output is the result of applying command1 to the files in turn, file1, file2, up to fileN

cat file1 # ab
cat file2 # cd
sed 's/a/Z1/' file1 file2 # (see Substituting a match)
#T# the former prints
# Z1b
# cd

# SYNTAX sed '\delim1pattern1delim1 command1'
#T# this applies command1 but only to the lines in which pattern1 matches, delim1 is the delimiter of the pattern, the first delim1 is escaped with a backslash unless delim1 is the slash /

echo -e "ab\nac" | sed '/b/ s/a/Z1/' # (see Substituting a match)
#T# the former prints
# Z1b
# ac

# SYNTAX sed 'int1,int2 command1'
#T# this applies command1 but only to the lines in the range of int1 and int2, int2 can be replaced with a dollar sign $ to signify the last line

echo -e "ab\nac\nad" | sed '2,$ s/a/Z1/' # (see Substituting a match)
#T# the former prints
# ab
# Z1c
# Z1d

# SYNTAX sed 'limit1,limit2 command1'
#T# this is a more general syntax that combines the previous two, limit1 and limit2 can be patterns or integers, this applies command1 between limit1 and limit2, if limit1 and limit2 are patterns then command1 starts to apply when limit1 is matched and stops applying when limit2 is matched

echo -e "ab\nac\nad\nae" | sed '2,/d/ s/a/Z1/' # (see Substituting a match)
#T# the former prints
# ab
# Z1c
# Z1d
# ae

# SYNTAX sed -o1 -o2 var2
#T# same as before, with input from stdin, and output to stdout, -o1 represents a flag, -o2 var2 represent a kwarg pair

#T# some of the options of the sed program are
#T#     -e 'command1', this kwarg pair can be repeated up to commandN, each one of the commands is executed in turn as a sed command
#T#     -f "script1", executes all sed commands in the file script1, each command in a separate line, the hash # is used for comments
#T#     -n, do not output all lines after processing
#T#     -E, interpret any regex inside command1 with the Extended Regular Expression rules

cat file1 # ab
cat script1 # s/a/Z1/ # (see Substituting a match)
sed -f script1 file1 # Z1b
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

#C# Substituting a match

# |-------------------------------------------------------------
#T# an match found in the input file can be substituted for another in the output file

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

#C# Deleting lines

# |-------------------------------------------------------------
#T# 

# |-------------------------------------------------------------