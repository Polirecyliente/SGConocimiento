
#   Data types

#T# Table of contents

#T# Types in general
#T# Numeric types
#T# String types
#T# --- Heredoc and here string
#T# Boolean type
#T# Composite types
#T# --- Lists
#T# --- Tuples
#T# --- Dictionaries
#T# --- Sets
#T# Enum type
#T# Null type
#T# Type casting

#T# Beginning of content

#T# Types in general

# |-------------------------------------------------------------
#T# types are not fully supported, the only considered types are strings and numbers
# |-------------------------------------------------------------

#T# Numeric types

# |-------------------------------------------------------------
#T# numerical types are
#T#     integer
#T#     octal, with prefix 0
#T#     hexa, with prefix 0x or 0X
#T#     arbitrary base from 1 to 64, with $((base#number))
#T#     float, substituting the bc command using here string notation

#T# the following are particular examples, numbers in any non decimal base must be enclosed in an arithmetic expansion
int1=5
int1=$((011))     # 9
int1=$((0x17))    # 23
int1=$((2#10101)) # 21
flo1=$(bc <<< "12.415") # 12.415 # here string is explained later in this file
# |-------------------------------------------------------------

#T# String types

# |-------------------------------------------------------------
#T# strings are created inside quotation symbols, single quotes ' or double quotes "
str1='string one'
str2="string two"

#T# reading elements (characters) from strings is done via substring parameter expansion (see S1_03_Operators.sh)

#T# string concatenation can be done indirectly with parameter expansion (see S1_03_Operators.sh) by expanding two or more string variables separated by space
str3=$str1" "$str2 # string one string two

# |--------------------------------------------------\
#T# escape sequences are
#T#     '\\' 
#T#     "\'" 

# |--------------------------------------------------/

#T# --- Heredoc and here string

# |-----

# |--------------------------------------------------\
#T# a heredoc is used to pass several lines of input to a command

# SYNTAX command1 << delimiter1
# SYNTAX line1
# SYNTAX lineN
# SYNTAX delimiter1
#T# the former lines of syntax go together, command1 is the command that will receive the lines of input, delimiter1 is any arbitrary word that is used to start and end the heredoc, line1 up to lineN are the lines of input to be passed to command1, these lines can't be equal to delimiter1

#T# arithmetic expansion, command substitution, parameter expansion, etc are interpolated inside the heredoc

var1="all done"
cat << delimiter1
first line of input $((3 + 2)) $(pwd)
second line of input $var1
delimiter1
#T# the cat command is used because it prints the lines of input, so the former prints
# first line of input 5 /path/to/current/dir
# second line of input all done

# SYNTAX command1 << "delimiter1"
# SYNTAX line1
# SYNTAX lineN
# SYNTAX delimiter1
#T# same as before, but with this syntax there is no arithmetic expansion, command substitution, parameter expansion, etc., so characters are parsed verbatim

var1="value1"
cat << "delimiter1"
text $var1 text
delimiter1
#T# the former prints
# text $var1 text

# SYNTAX command1 <<- delimiter1
# SYNTAX line1
# SYNTAX lineN
# SYNTAX delimiter1
#T# same as before, but with this syntax all the tab characters at the start of each line, from line1 to lineN, are trimmed

cat <<- delimiter1
    first line
        second line
delimiter1
#T# the former prints
# first line
# second line
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# a here string is used like a heredoc but it only sends one string as input to a command

# SYNTAX command1 <<< "string1"
#T# command1 executes using string1 as input, string1 accepts arithmetic expansion, command substitution, parameter expansion, etc.

var1=2
bc <<< "3 + $((1 + 1)) + $(echo 1) + $var1" # 8 # 3 + 2 + 1 + 2
# |--------------------------------------------------/

# |-----

# |-------------------------------------------------------------