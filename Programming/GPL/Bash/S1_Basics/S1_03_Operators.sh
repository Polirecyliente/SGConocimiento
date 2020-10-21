
#   Operators

#T# Table of contents

#T# Expansions
#T# --- Brace expansion
#T# --- Tilde expansion
#T# --- Parameter (variable) expansion
#T# --- Command substitution
#T# --- Arithmetic expansion
#T# --- Word splitting
#T# --- Pathname expansion
#T# Arithmetic operators
#T# Relational operators
#T# Assignment operators
#T# Bitwise operators
#T# Ternary operator
#T# Logical operators
#T# Membership operators
#T# Identity operators

#T# Beginning of content

#T# Expansions

# |-------------------------------------------------------------
#T# expansions are used to replace tokens into characters depending on the value of the tokens, expansion operators serve to recognize the tokens to replace (called expand here)

#T# there are several kinds of expansion, and so they are done in a given order, the following sections are written in this order, the tokens expand in this order

#T# --- Brace expansion

# |-----
#T# brace expansion is used to create strings in a combinatorial manner, with N sets of strings, each enclosed in braces, and each of size n_i, the total amount of created strings is the product of all the n_i from all the N sets

#T# each set of strings goes inside braces, with elements separated with comma (no spaces in between), except when there is only one string in the set, in that case the set of one element goes without braces and no commas

# SYNTAX "set1_elem1"{"set2_elem1","set2_elem2"}"set3_elem1"
#T# each of the strings is an element of a set of strings, there can be more sets and more elements in each set, and as set1_elem1 is the string element 1 of set 1, in general setI_elemi is the string element i of the set I

echo "s1"{"s2","s3"}"sm"{"s4","s5","s6"} # s1s2sms4 s1s2sms5 s1s2sms6 s1s3sms4 s1s3sms5 s1s3sms6
# |-----

#T# --- Tilde expansion

# |-----
#T# tilde expansion expands a tilde by replacing it for a user's home directory

# SYNTAX ~
#T# a tilde alone is expanded to the current user's home directory

echo ~/dir1 # /home/user1/dir1 # if such user and directory exist

# SYNTAX ~user1
#T# this expands to the user1 home directory

echo ~other_user1/dir1 # /home/other_user1/dir1 # if such user and directory exist
# |-----

#T# --- Parameter (variable) expansion

# |-----
#T# variables (called parameters here) can be expanded to get their value, or get their value with modification

#T# parameters are identified because they start with the dollar sign $ and followed by their name, with optional braces enclosing the name

#T# define a parameter as usual
var1="value one"

# |--------------------------------------------------\
#T# expansion means substituting the parameter for its value

# SYNTAX $var1
# SYNTAX ${var1}
#T# both syntaxes are equivalent, braces are used when the next character after var1 is not a space, or when needed

echo $var1 # value one

#T# because arguments are separated by spaces, a parameter should be enclosed in double quotes to protect its value' spaces
echo "$var1" # value one # in this case "value one" is the argument, instead of two arguments "value" and "one"
# |--------------------------------------------------/

#T# a null parameter is defined as an empty string
null_var1=""

# |--------------------------------------------------\
#T# a parameter can be unset so it doesn't exist anymore
# SYNTAX unset var1
unset_var1="temp value"
unset unset_var1 # unset_var1 becomes as if it was never defined
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# a variable's length in bytes can be expanded

# SYNTAX ${#var1}
#T# var1 is the variable (parameter) whose lenght in bytes (according to the locale) is the result of the expansion

var1="ʠüña"
echo ${#var1} # 4
LC_ALL=C      # changing the locale
echo ${#var1} # 7
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# the case of the string value of a parameter (variable) can be modified

# SYNTAX ${var1^pattern_single1}
#T# var1 is the parameter whose case is being changed, pattern_single1 is a single character, pattern_single1 can be nothing, it can be a char, or it can be a character class with several chars

#T# this syntax makes uppercase the first char in var1 if it matches pattern_single1

var1="choqolada"
echo ${var1^[aqc]} # Choqolada

# SYNTAX ${var1^^pattern_single1}
#T# same as before, but make uppercase all chars in var1 that match pattern_single1

var1="choqolada"
echo ${var1^^[!aqc]} # cHOqOLaDa

# SYNTAX ${var1,pattern_single1}
#T# same as before, but make lowercase the first char in var1 if it matches pattern_single1

var1="CHOQOLADA"
echo ${var1,C} # cHOQOLADA

# SYNTAX ${var1,,pattern_single1}
#T# same as before, but make lowercase all chars in var1 that match pattern_single1
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# conditional parameter expansion is done to expand a parameter conditionally, if the parameter doesn't exist then it's expanded to another alternative called a word

# SYNTAX ${var1-alt1}
#T# var1 is the parameter to be expanded, alt1 is the alternative literal string in case var1 doesn't exist, alt1 can also be a parameter expansion, an arithmetic expansion, command substitution etc.

echo ${var1-literal_alt1}
#T# the former prints
# value one    # if var1="value one"
# literal_alt1 # if var1 is unset

# SYNTAX ${var1:-alt1}
#T# same as before, but expanding to alt1 also happens when var1 is null

echo ${var1:-literal_alt1}
#T# the former prints
# value one    # if var1="value one"
# literal_alt1 # if var1 is unset or null

# SYNTAX ${var1=alt1}
#T# same as before, but if var1 is null then it gets assigned the literal string alt1 (unless alt1 is another expansion as said before, in that case var1 is assigned the value of alt1)

echo ${var1=literal_alt1}
#T# the former prints
# value one    # if var1="value one"
# literal_alt1 # if var1 is unset, and now var1="literal_alt1"

# SYNTAX ${var1:=alt1}
#T# same as before, but expanding and assigning to alt1 also happens when var1 is null

echo ${var1:=literal_alt1}
#T# the former prints
# value one    # if var1="value one"
# literal_alt1 # if var1 is unset or null, and now var1="literal_alt1"

# SYNTAX ${var1?alt1}
#T# same as before, but if var1 is unset then alt1 is printed as an error message to stderr

echo ${var1?error_alt1}
#T# the former prints
# value one              # if var1="value one"
# bash: var1: error_alt1 # if var1 is unset

# SYNTAX ${var1:?alt1}
#T# same as before, but expanding to alt1 as an error message also happens when var1 is null

echo ${var1:?error_alt1}
#T# the former prints
# value one              # if var1="value one"
# bash: var1: error_alt1 # if var1 is unset or null

# SYNTAX ${var1+alt1}
#T# same as before, but now var1 is expanded to alt1 when var1 is not unset, note that this doesn't change var1 original value

echo ${var1+literal_alt1}
#T# the former prints
# literal_alt1 # if var1="value one" or any other value
#              # if var1 is unset

# SYNTAX ${var1:+alt1}
#T# same as before, but expanding to alt1 also does not happen when var1 is null

echo ${var1:+literal_alt1}
#T# the former prints
# literal_alt1 # if var1="value one" or any other non null value
#              # if var1 is unset or null
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# substring parameter expansion is done to expand a parameter partially, taking only a substring of the parameter according to an offset or a matching pattern

# SYNTAX ${var1:offset1}
# SYNTAX ${var1:offset1:length1}
#T# var1 is the parameter to be expanded, offset1 and length1 are integers, this extracts a substring from var1, starting at the character in the position offset1, and extracting a total of length1 characters

#T# offset1 and length1 can be negative integers, if they are then they must be enclosed in parentheses to avoid forming the :- operator, if offset1 is negative then the first character is counted from the end of the parameter value, if length1 is negative then the last length1 characters are removed

var1=str1str2str3
echo ${var1:4}         # str2str3
echo ${var1:(-8)}      # str2str3
echo ${var1:3:4}       # 1str
echo ${var1:(-5):(-1)} # 2str

# SYNTAX ${var1#pattern1}
# SYNTAX ${var1##pattern1}
#T# this removes the substring that has to start from the left of var1 and matches pattern1, using double hash ## makes a greedy match

#T# pattern1 accepts globbing (see Pathname expansion subsection in the Expansions section)

var1="apple pie"
echo ${var1#?p}           # ple pie
echo ${var1##*p}          # ie
echo ${var1#[a-z][^a-h]p} # le pie

# SYNTAX ${var1%pattern1}
# SYNTAX ${var1%%pattern1}
#T# same as before, but the removed substring has to start at the right of var1 and match pattern1, using double %% makes a greedy match

var1="apple pie"
echo ${var1%p*}  # apple
echo ${var1%%p*} # a
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# substring substitution is done to make substring replacements and then expand the changed parameter

# SYNTAX ${var1/pattern1/replace_string1}
# SYNTAX ${var1//pattern1/replace_string1}
#T# var1 is the parameter whose value is the string where the replacement will take place, pattern1 is the pattern to be matched, replace_string1 replaces the matched substring

#T# if only one slash / is used between var1 and pattern1 then only the first match is replaced, with double slash // all matches are replaced

#T# pattern1 accepts globbing (see Pathname expansion subsection in the Expansions section)

var1="apple pie"
echo ${var1/ /_}  # apple_pie
echo ${var1/p/n}  # anple pie
echo ${var1//p/b} # abble bie

# SYNTAX ${var1/#pattern1/replace_string1}
# SYNTAX ${var1/%pattern1/replace_string1}
#T# same as before, but when using hash # the pattern is matched only at the left of var1, and when using percent sign % the pattern is matched at the right of var1

var1="apple pie"
echo ${var1/#app/abs} # absle pie
echo ${var1/%pie/bye} # apple bye
# |--------------------------------------------------/

# |-----

#T# --- Command substitution

# |-----
#T# command substitution allows using the output of commands as arguments for other commands

# SYNTAX command1 $(command2)
# SYNTAX command1 `command2`
#T# the output of command2 is used as argument for the command1

echo "Bash exec file is in "$(which bash) # Bash exec file is in /bin/bash
echo "Bash exec file is in "`which bash`  # Bash exec file is in /bin/bash
# |-----

#T# --- Arithmetic expansion

# |-----
#T# arithmetic expansion is done to do arithmetic calculations

# SYNTAX $(( expression1 ))
#T# expression1 is any arithmetic expression consisting of integers (for floating point numbers, bc or similar commands can be used), the list of math operations is shown later in this file

int1=$((7 - 2 + 1)) # 6
int2=$((int1 + 5))  # 11 # int1 must not be expanded with dollar sign $

# |--------------------------------------------------\
#T# the let command can be used to do the same as arithmetic expansions

# SYNTAX let "expression1"
#T# expression1 is any arithmetic expression consisting of integers, it must contains at least one variable

let "var1 = 5 + 2" # var1 == 7
# |--------------------------------------------------/

# |-----

#T# --- Word splitting

# |-----
#T# word splitting is done to split words where an IFS (Internal Field Separator) character is found, this is done only outside double quotes ", so strings inside double quotes are not word splitted

#T# the default value of the IFS consist of space, tab, and newline

#T# words are tokens that can be passed as arguments to commands, a string with substrings separated by the IFS will create one such token or word per each substring when word splitted

# SYNTAX IFSsubstring1IFSsubstring2IFS
# SYNTAX  substring1 substring2 "sub string 3" 
#T# The IFS at the start and end of the string are ignored, all substrings, substring1, substring2, etc., are converted into separate tokens, these can be used as arguments by commands

cat file1 file2 "file name 3" # this outputs the contents of file1, file2, and "file name 3", if such files exist
# |-----

#T# --- Pathname expansion

# |-----
#T# pathname expansion is done with globbing (also called filename expansion), the following syntaxes of this section can be used anywhere where globbing is accepted in Bash

# SYNTAX substring1*substring2
#T# the asterisk * operator is expanded to the filenames of the working directory that start with substring1 and end with substring2

echo * # Drawing Math Programming Science # or others, according to the working directory
echo D*g # Drawing

# SYNTAX substring1?substring2
#T# the question mark ? operator is expanded to any single character of the filenames of the working directory, this single character must be preceded by substring1 and followed by substring2

echo ???? # Math
echo M??h # Math

# SYNTAX substring1[chars1]substring2
#T# the brackets [] operator encloses a character class made of the characters in chars1, it matches one and only one of the characters in chars1, preceded by substring1 and followed by substring2

#T# a character range is allowed with the hyphen -, e.g. [c-h] matches one char between 'c' and 'h' according to the collation set

#T# the caret ^ and the exclamation mark ! are used to negate the character class (match a char that is not in the character class), this negation sign must be placed at the start of the character class

#T# to match a hyphen or other special char, they can be escaped with backslash

#T# a character class can be one of the POSIX character clases, these are made with a word within colons and a pair of brackets which don't count as the character class brackets
#T#     [:alnum:],  matches one alphanumeric char
#T#     [:alpha:],  matches one alphabetic char
#T#     [:blank:],  matches one space or tab
#T#     [:cntrl:],  matches one control char, like a vertical tab
#T#     [:digit:],  matches one digit
#T#     [:graph:],  matches one visible char
#T#     [:lower:],  matches one lowercase char
#T#     [:print:],  matches one visible char or space
#T#     [:punct:],  matches one punctuation char
#T#     [:space:],  matches one space char
#T#     [:upper:],  matches one uppercase char
#T#     [:xdigit:], matches one hexadecimal digit

echo F[a9i]le1     # File1 # if such file exists in the working directory
echo F[k-p]le2     # Fmle2 # if such file exists
echo F[^i][!o]3    # Fae3  # if such file exists
echo [[:xdigit:]]* # A     # if such file exists

# SYNTAX */*/pattern1
#T# pattern1 can be any matching pattern, the series of '*/' can be longer and it means that pattern1 will be matched in a subdirectory, for the case of '*/*/' pattern1 will be matched in all subsubdirectories (in a depth level of 2)

echo */*/*/File1 # dir1/subdir1/subsubdir1/File1 # if such file exists under the working directory

#T# for the following syntax, an extended set of operators for globbing is required, this feature is turned on with the extglob option of the shopt command (see S1_08_CLI.sh)

# SYNTAX operator1(pattern1|pattern2|pattern3)
#T# there can be more than 3 patterns separated by vertical bar |, operator1 can be any of '?', '*', '+', '@', or '!', all patterns, pattern1, pattern2, pattern3, etcetera, are matching patterns, this syntax matches any of the patterns inside parentheses according to operator1

#T# the use of the operators is
#T#     ?, matches 0 or 1 time any of the patterns
#T#     *, matches 0 or more times any of the patterns
#T#     +, matches 1 or more times any of the patterns
#T#     @, matches 1 time any of the patterns
#T#     !, matches the negation of the patterns, so anything that doesn't match any of the patterns

echo ?(F1|F2)        # F2      # if such file exists in the working directory
echo *(F[[:digit:]]) # F1F2 F2 # if such files exist
echo +(FA|FB|FC)     # FAFBFC  # if such files exist
echo @(F[A-Z])       # FB FC   # if such files exist
echo !(F[A-Z])       # F1F2 F2 # if such files exist
# |-----

# |-------------------------------------------------------------

#T# Arithmetic operators

# |-------------------------------------------------------------
#T# these operators can be used in an arithmetic expansion, and so they can be used in expressions with the let command, when used inside an arithmetic expansion, the dollar sign $ can be omitted to avoid expanding the result if it's not going to be used as argument or output

# SYNTAX (( var3 = var1 + var2 ))
# SYNTAX let "var3 = var1 + var2"
#T# this adds var1 and var2, and stores the result in var3

var1=5; var2=3
(( var3 = var1 + var2 )) # var3 == 8
let "var3 = var1 + var2" # var3 == 8

# SYNTAX (( var3 = var1 - var2 ))
# SYNTAX let "var3 = var1 - var2"
#T# this subtracts var2 from var1, and stores the result in var3

var1=5; var2=3
(( var3 = var1 - var2 )) # var3 == 2
let "var3 = var1 - var2" # var3 == 2

# SYNTAX (( var3 = var1*var2 ))
# SYNTAX let "var3 = var1*var2"
#T# this multiplies var1 by var2, and stores the result in var3

var1=5; var2=3
(( var3 = var1*var2 )) # var3 == 15
let "var3 = var1*var2" # var3 == 15

# SYNTAX (( var3 = var1/var2 ))
# SYNTAX let "var3 = var1/var2"
#T# this divides var1 by var2, and stores the result in var3, since Bash doesn't support floating point arithmetics, the result is the nearest integer to zero

var1=5; var2=3
(( var3 = var1/var2 )) # var3 == 1
let "var3 = var1/var2" # var3 == 1

# SYNTAX (( var3 = var1 % var2 ))
# SYNTAX let "var3 = var1 % var2"
#T# this does the modulo operation, which calculates the remainder of var1 divided by var2, and stores the result in var3

var1=5; var2=3
(( var3 = var1 % var2 )) # var3 == 2
let "var3 = var1 % var2" # var3 == 2

# SYNTAX (( var3 = var1**var2 ))
# SYNTAX let "var3 = var1**var2"
#T# this elevates var1 to the power of var2, and stores the result in var3

var1=5; var2=3
(( var3 = var1**var2 )) # var3 == 125
let "var3 = var1**var2" # var3 == 125
# |-------------------------------------------------------------

#T# Relational operators
#T# Assignment operators

# |-------------------------------------------------------------
#T# assignment operators with let "var = 4"
let "A = 2"
echo "A value is: $A"
let "A += 3"
echo "A value is: $A"
let "A -= 4"
echo "A value is: $A"
let "A *= 8"
echo "A value is: $A"
let "A /= 2"
echo "A value is: $A"
# |-------------------------------------------------------------

#T# Bitwise operators
#T# Ternary operator
#T# Logical operators
#T# Membership operators
#T# Identity operators













# |--------------------------------------------------\
#T# the dot command, and its synonym the source command, are used for executing a script in the same shell environment, normally scripts are executed in a subshell

# SYNTAX . script1.sh
# SYNTAX source script1.sh
#T# both syntaxes are equivalent, the commands in script1 are executed in the same shell environment that called it

. S1_08_CLI_args.sh      # executes this script in the same shell
source S1_08_CLI_args.sh # executes this script in the same shell
# |--------------------------------------------------/


#T# variable indirection, indirect expansion


#T# Command history

# |-------------------------------------------------------------

# |--------------------------------------------------\
#T# the history can be checked with the history command

history
#T# the former prints
#    1  echo "echoed to stdout"
#    2  cat ~/.bash_history 
#    3  git push
#    4  history

#T# or any list of commands executed before and stored in the history
# |--------------------------------------------------/

#T# clear the history with the -c flag of the history command
history -c

#T# --- History expansion

# |-----
#T# commands from the history are expanded with an exclamation mark, known as the bang operator

# |--------------------------------------------------\
#T# any command in the history can be executed again with its number in the history

# SYNTAX additionals1 !int1 additionals2
#T# int1 is the number of the command in the history, additionals1 and additionals2 are any other commands and arguments added before and after the command with number int1

#T# as an example, if the command number 6 is 'echo "repeated string"'
!6 "and more"
#T# then the former prints
# echo "repeated string" "and more"
# repeated string and more

#T# using negative numbers starts counting from the last command in the history
!-1
#T# this executes the last command in the history, this is the same as
!!
#T# to execute the third to last command use
!-3
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# commands in the history can also be expanded with their starting characters

# SYNTAX additionals1 !starting_chars1 additionals2
#T# starting_chars1 is a string with the first characters of the command in the history, if several commands start with the same characters then the last command in the history will be executed

#T# additionals1 and additionals2 are any other commands and arguments added before and after the command that starts with starting_chars1

#T# if the commands 'git pull' and 'git push' are on the history, then executing
!gi
#T# will execute 'git push' as it's the last one in the history
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# appending :p to a history expansion will print it instead of executing it

# SYNTAX !command_id1:p
#T# command_id1 is either an integer with the number of the command in the history, a string with the starting characters of the command in the history, or any other valid history expansion like !!

!!:p # history # if this was the last command in the history
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# history expansion can also be used to reuse arguments from past commands

# SYNTAX command1 !^
#T# this calls command1 with the first argument of the last command in the history

echo !^
#T# if the last command is 'cat str1 str2' then this prints
# echo str1
# str1

# SYNTAX command1 !$
#T# this calls command1 with the last argument of the last command in the history

echo !$
#T# if the last command is 'cat str1 str2' then this prints
# echo str2
# str2

# SYNTAX command1 !*
#T# this calls command1 with all the arguments of the last command in the history

echo !*
#T# if the last command is 'cat str1 str2' then this prints
# echo str1 str2
# str1 str2

# SYNTAX command1 !command_id1:arg_id1
#T# this calls command1 with arguments extracted from the command identified by command_id1 (which can be the number of a command in the history, its starting characters, or any other valid history expansion)

#T# arg_id1 is the identifier of the argument to be extracted, it can be an integer (this means the position number of the argument, first argument is 1, second argument is 2, and so on), or any of the symbols used in the shown syntax, the caret ^ for the first argument, the dollar sign $ for the last argument, and the asterisk * for all the arguments

echo !gi:2
#T# if there is a command 'git pull origin master' in the history then this prints
# echo origin
# origin
# |--------------------------------------------------/

# |-----

# |--------------------------------------------------\
#T# the previous command can be rerun replacing a substring for another, for example in case of a typo

# SYNTAX ^original_substring1^new_substring1
#T# this replaces the first instance of original_substring1 for new_substring1 in the last command

^ir^it
#T# if the last command is 'gir push' then this executes 'git push'
# |--------------------------------------------------/

# |-------------------------------------------------------------


#T# Special parameters

# |-------------------------------------------------------------
#T# the special parameters are variables whose name can't be manually assigned values, they are used to store special values

#T# process related parameters are the $$, $! parameters
echo $$ # 389217 # prints the PID of the current terminal
echo $! # 406952 # prints the PID of the last process sent to be a background process, if any

#T# the $? parameter stores the exit status of the last command
echo $? # 0 # zero usually means correct execution

#T# the $0 parameter stores the name of the script or command that expanded its value
echo $0 # bash

#T# the $_ parameter stores a string with the last argument of the last command
echo $_ # third # if the last command was 'echo first second third'

#T# the $- parameter stores the interpreter options
echo $- # himBHs

#T# there are a few more special parameters that deal with positional parameters which are treated in the section about command line arguments, see S1_08_CLI_args.sh
# |-------------------------------------------------------------