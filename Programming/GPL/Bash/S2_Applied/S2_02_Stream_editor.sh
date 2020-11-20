
#   Stream editor

#T# Table of contents

#C# Basic usage
#C# Printing a match
#C# Substituting a match
#C# Deleting lines
#C# Quit on condition
#C# Skip current line
#C# Read and insert a file
#C# Insert a line
#C# Multiline commands
#C# Hold space commands
#C# Control flow
#C# Examples

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

# SYNTAX sed 'limit1,limit2! command1'
#T# same as before, but this applies command1 to all lines except for those between limit1 and limit2 (the ! acts as a not operator)

echo -e "ab\nac\nad\nae" | sed -n '2,/d/! p' # (see Printing a match)
# ab
# ae

# SYNTAX apply several sed commands between limits
# sed 'limit1,limit2 { command1
# command2 }'
# SYNTAX sed 'limit1,limit2 { command1; command2 }'
#T# both syntaxes are equivalent, this applies command1, command2, up to commandN to each line of the input between limit1 and limit2 (see before), nesting braces allows applying commands to limits within limits

#T# the semicolon ; is the command terminator which allows writing more commands on the same line

#T# each command can have its own limits, depending on the command

echo -e "ab\nabc\nabd" | sed '2,3 { /d/ { s/a/Z1/; s/b/Y2/ } }' # (see Substituting a match)
#T# the former prints
# ab
# abc
# Z1Y2d

# SYNTAX sed -o1 -o2 var2
#T# same as before, with input from stdin, and output to stdout, -o1 represents a flag, -o2 var2 represent a kwarg pair

#T# some of the options of the sed program are
#T#     -e 'command1', this kwarg pair can be repeated up to commandN, each one of the commands is executed in turn as a sed command
#T#     -f "script1", executes all sed commands in the file script1, each command in a separate line or separated by semicolon ;, the hash # is used for comments
#T#     -i.ext1 'commands1' file1, saves the original file1 as file1.ext1, and changes file1 according to commands1
#T#     -n, do not output all lines after processing
#T#     -E, interpret any regex inside command1 with the Extended Regular Expression rules

cat file1 # ab
cat script1 # s/a/Z1/; s/b/Y2/ # (see Substituting a match)
sed -f script1 file1 # Z1Y2

#T# the concept of 'pattern space' means either the current line, or all the lines that have been put together to form the pattern space, the concept of 'hold space' is another pattern space that acts as a buffer or storage for lines of text
# |-------------------------------------------------------------

#C# Printing a match

# |-------------------------------------------------------------
#T# the sed command identified by 'p' is used to print a range of lines

# SYNTAX sed 'limit1,limit2 p'
#T# this prints the lines between limit1 and limit2 (see Basic usage)

echo -e "ab\ncd" | sed -n '2 p' # cd

#T# the sed command identified by 'w' is used to write the output directly to a file

# SYNTAX sed 'limit1,limit2 w file1'
#T# this prints the lines between limit1 and limit2 directly to file1

echo -e "ab\ncd\nef" | sed -E '/[ce]/ w file1'
cat file1
#T# the former prints
# cd
# ef

#T# the sed command identified by '=' is used to print the line number

# SYNTAX sed 'limit1,limit2 ='
#T# this prints the line numbers of the lines between limit1 and limit2

echo -e "ab\nac\nad" | sed -n '2,3 ='
#T# the former prints
# 2
# 3

#T# the sed command identified by 'l' is used the print the current pattern space (the current lines) terminated with a dollar sign $ and with newlines escaped

# SYNTAX sed 'l'
#T# the pattern space (the current lines) is printed

echo "str1" | sed 'l'
#T# the former prints
# str1$
# str1

# |-------------------------------------------------------------

#C# Substituting a match

# |-------------------------------------------------------------
#T# a match found in the input file can be substituted for another in the output file, the sed command to substitute is identified by 's'

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

# SYNTAX sed 's/pattern1/\U&/'
#T# same as before, but the match is converted to uppercase

echo "str1" | sed 's/tr/\U&/' # sTR1

# SYNTAX sed 's/pattern1/\L&/'
#T# same as before, but the match is converted to lowercase

echo "STR1" | sed 's/TR/\L&/' # Str1

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
echo -e "ab\ncd" | sed -nE 's/c/C/ pw file1'
cat file1 # Cd

#T# the sed command identified by 'y' is used to translate the chars in a string with the chars from another string

# SYNTAX sed 'y/chars1/chars2/'
#T# same rules as before, but this is about two sets of chars, both of which must be the same size, each char in chars1 is replaced by a char in chars2 that is in the same position

echo -e "ab\nac" | sed 'y/abc/ZYX/'
#T# the former prints
# ZY
# ZX
# |-------------------------------------------------------------

#C# Deleting lines

# |-------------------------------------------------------------
#T# the sed command identified by 'd' is used to delete a range of lines

# SYNTAX sed 'limit1,limit2 d'
#T# this deletes the lines between limit1 and limit2 (see Basic usage)

echo -e "ab\nac\nad" | sed '1,2 d' # ad
# |-------------------------------------------------------------

#C# Quit on condition

# |-------------------------------------------------------------
#T# the sed command identified by 'q' is used to quit sed when a given condition is met

# SYNTAX sed 'line1 q'
#T# sed quits when encountering line1, this line1 can be an integer (the line number) or a pattern (the first line that matches said pattern)

echo -e "ab\nac\nad" | sed '/c/ q'
#T# the former prints
# ab
# ac
# |-------------------------------------------------------------

#C# Skip current line

# |-------------------------------------------------------------
#T# the sed command identified by 'n' is used to output the current line and read the next one, effectively skipping the current one

# SYNTAX sed 'line1 n'
#T# line1 is skipped, this line1 can be an integer (the line number), or a pattern (the first line that matches said pattern)

echo -e "ab\nac" | sed '1 n; s/a/Z1/'
#T# the former prints
# ab
# Z1c
# |-------------------------------------------------------------

#C# Read and insert a file

# |-------------------------------------------------------------
#T# the sed command identified by 'r' is used to read a file and then insert it after a given line

# SYNTAX sed 'line1 r file1'
#T# file1 is read and inserted after line1, this line1 can be an integer (the line number), or a pattern (the first line that matches said pattern)

cat file1 # ab
echo -e "str1\nstr2" | sed '1 r file1'
#T# the former prints
# str1
# ab
# str2
# |-------------------------------------------------------------

#C# Insert a line

# |-------------------------------------------------------------
#T# the sed command identified by 'a' is used to insert a line of text after a given line (append the line)

# SYNTAX sed 'line1 a text1'
#T# text1 is inserted after line1, this line1 can be an integer (the line number), or a pattern (the first line that matches said pattern)

echo -e "ab\nac" | sed '1 a ins1'
#T# the former prints
# ab
# ins1
# ac

#T# the sed command identified by 'i' is used to insert a line of text before a given line

# SYNTAX sed 'line1 i text1'
#T# text1 is inserted before line1, this line1 can be an integer (the line number), or a pattern (the first line that matches said pattern)

echo -e "ab\nac" | sed '1 i ins1'
#T# the former prints
# ins1
# ab
# ac

#T# the sed command identified by 'c' is used to change the text from a given line for another

# SYNTAX sed 'limit1,limit2 c text1'
#T# the text in the lines between limit1 and limit2 (see Basic usage) is changed by that of text1, this command acts as a replacement of the entire range for one line

echo -e "ab\nac" | sed '1,2 c new_text1' # new_text1

#T# in the previous syntaxes, if text1 starts with whitespace then said spaces can be retained by putting a backslash \ before the first space
echo -e "ab" | sed '1 c \    str1' #     str1

#T# in the previous syntaxes, if text1 spans several lines, each line must end with a backslash \ to escape the newline (or use \n)
echo -e "ab" | sed '1 { i str1\
str2
}'
#T# the former prints
# str1
# str2
# ab
#T# when using braces, the last brace must appear after a non escaped newline, otherwise the brace becomes part of the text and the ending brace is never found
# |-------------------------------------------------------------

#C# Multiline commands

# |-------------------------------------------------------------
#T# other sed commands can be used to operate over multiple lines, to do this they use the pattern space and the hold space

#T# the sed command identified by 'N' is used to append the next line of input to the current pattern space, thereby increasing the size of the pattern space by one line, and if the next line of input is beyond the last line then sed terminates

# SYNTAX sed 'N'
#T# the next line of input is appended to the pattern space

seq 5 | sed -n '3 q; 1 N; p'
#T# the former prints
# 1
# 2

#T# the sed command identified by 'D' is used to delete only the first line of the pattern space

# SYNTAX sed 'D'
#T# only the first line of the pattern space is deleted

seq 2 | sed 'N; D' # 2

#T# the sed command identified by 'P' is used to print only the first line of the pattern space

# SYNTAX sed 'P'
#T# only the first line of the pattern space is printed

seq 2 | sed -n 'N; P' # 1
# |-------------------------------------------------------------

#C# Hold space commands

# |-------------------------------------------------------------
#T# the hold space is used to hold lines of text, the text in this hold space is manipulated with the use of sed commands

#T# the sed command identified by 'x' is used to exchange the hold space with the current pattern space

# SYNTAX sed 'x'
#T# in each line, the current pattern space is exchanged with the hold space, initially the hold space only has a blank line

echo -e "str1\nstr2\nstr3" | sed 'x'
#T# the former prints
# 
# str1
# str2

#T# the sed command identified by 'h' is used to put the pattern space into the hold space, overwriting it

# SYNTAX sed 'h'
#T# the current pattern space is copied into the hold space

echo -e "str1\nstr2" | sed -n 'h; $ {x; p}' # str2

#T# the sed command identified by 'H' is used to append the pattern space at the end of the hold space

# SYNTAX sed 'H'
#T# the pattern space is appended at the end of the hold space

echo -e "str1\nstr2" | sed -n 'H; $ {x; p}'
#T# the former prints
# 
# str1
# str2

#T# the sed command identified by 'g' is used to put the hold space into the pattern space, overwriting it

# SYNTAX sed 'g'
#T# the hold space is copied into the pattern space

echo -e "str1\nstr2" | sed '1 h; g'
#T# the former prints
# str1
# str1

#T# the sed command identified by 'G' is used to append the hold space at the end of the pattern space

# SYNTAX sed 'G'
#T# the hold space is appended at the end of the pattern space

echo "str1" | sed -n 'G; p'
#T# the former prints
# str1
# 
# |-------------------------------------------------------------

#C# Control flow

# |-------------------------------------------------------------
#T# in sed the control flow is of goto type, in the sense that the commands for control flow continue execution after a label

#T# the sed command identified by 'b' is used to make an unconditional jump to a label

# SYNTAX sed 'commands1; :label1; commands2; b label1; commands3'
#T# the label is defined in :label1, and the sed command identified by 'b' is used to jump to the label1 location, this can be done inside any amount of commands, up to commandsN, and the label definition can be written after the jump

echo -e "str1\nstr2\nstr3" | sed -n ':lbl1; l; N; p; b lbl1' # the 'N' breaks the infinite loop
#T# the former prints
# str1$
# str1
# str2
# str1\nstr2$
# str1
# str2
# str3
# str1\nstr2\nstr3$

echo -e "str1\nstr2\nstr3" | sed -n 'b lbl1; l; N; p; :lbl1; l' # the commands in the middle are skipped
#T# the former prints
# str1$
# str2$
# str3$

# SYNTAX sed 'b; commands1'
#T# when used alone, the sed command identified by 'b' jumps to the end of the commands, skipping over commands1 and starting at the next input line

echo -e "str1" | sed 'b; l' # str1 # without skipping this would also print 'str1$'

#T# the sed command identified by 't' is used to make a conditional jump to a label, the condition being that the last substitution did modify the pattern space

# SYNTAX sed ':label1; commands1; s/pattern1/replace1/; t label1'
#T# same as before, what's relevant here is that before 't label1' any substitution command is successful, if so then the execution jumps to :label1, also as before, the label definition can be written after the jump

echo -e "str1" | sed -n 's/t/T/; t lbl1; p; p; :lbl1; l' # sTr1$

#T# in the previous syntaxes, if :label1 is repeated several times then the jump is made to the last one
# |-------------------------------------------------------------

#C# Examples

# |-------------------------------------------------------------
#T# the following process a table of Unicode chars and through substitution rearranges the columns and puts the vertical bar | as a separator to use the result as a Markdown table
sed -Ene 's/^U\+([^ ]*) \t(.*) \(U\+\1\) \t(.).*/| \&\#x\1\; | \3 | \2/ p' unicode_buffer.txt > out_buffer.txt
# |-------------------------------------------------------------