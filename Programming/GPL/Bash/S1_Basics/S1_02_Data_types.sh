
#   Data types

#T# Table of contents

#C# Types in general
#C# Numeric types
#C# String types
#C# --- Heredoc and here string
#C# Composite types
#C# --- Arrays
#C# --- Associative arrays
#C# Null type
#C# The declare command

#T# Beginning of content

#C# Types in general

# |-------------------------------------------------------------
#T# types are not fully supported, the only considered types are strings and numbers, for example there is no boolean type in Bash, see S1_03_Operators.sh and S1_05_Control_flow.sh for the treatment of boolean variables in general and in conditionals

#T# the only caveat, is the declare command, which can be used to set attributes on variables, and these attributes act as the type of the variable
# |-------------------------------------------------------------

#C# Numeric types

# |-------------------------------------------------------------
#T# numerical types are
#T#     integer
#T#     octal, with prefix 0
#T#     hexa, with prefix 0x or 0X
#T#     arbitrary base from 1 to 64, with $((base#number))
#T#     float, substituting the bc command using here string notation

#T# the following are particular examples, numbers in any non decimal base must be enclosed in an arithmetic expansion
int1=5
int1=$(( 011 ))     # 9
int1=$(( 0x17 ))    # 23
int1=$(( 2#10101 )) # 21
flo1=$( bc <<< "12.415" ) # 12.415 # here string is explained later in this file
# |-------------------------------------------------------------

#C# String types

# |-------------------------------------------------------------
#T# strings are created inside quotation symbols, single quotes ' or double quotes "
str1='string one'
str2="string two"

#T# reading elements (characters) from strings is done via substring parameter expansion (see S1_03_Operators.sh)

#T# string concatenation can be done indirectly with parameter expansion (see S1_03_Operators.sh) by expanding two or more string variables separated by space
str1='string one'
str2="string two"
str3=$str1" "$str2 # string one string two

#T# escape sequences serve to do in-band signaling

# SYNTAX \char1
#T# char1 is commonly a single char, except for octal values, hex values, unicode chars, etcetera

#T# the escape sequences are
#T#     "\a", alert bell system sound
#T#     "\b", backspace
#T#     "\f", formfeed
#T#     "\r", carriage return
#T#     "\n", newline, the same as \f\r
#T#     "\t", horizontal tab
#T#     "\v", vertical tab
#T#     "\c", suppress the rest of the string
#T#     "\e", escape char (same as ASCII 033 or Unicode U+001B)
#T#     "\0", null char

#T#     "\\",         literal backslash
#T#     "\"",         double quote
#T#     "\$",         dollar sign
#T#     "\`",         backtick
#T#     "\uNNNN",     unicode character  where NNNN is a 16 bit hex number
#T#     "\UNNNNNNNN", unicode 32 bit hex number
#T#     "\xNN",       hex value
#T#     "\0NNN",      octal value

str1="Line\\1\nLine\"2\a\fForm\vfeed\t\blines\ror \u02A0\U00010346\x6c\$\` \n\cUnreachable"
#T# printing str1 gives the following
# Line\1
# Line"2
#       Form
# or ʠ𐍆l$`  feed lines

#C# --- Heredoc and here string

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

#T# a here string is used like a heredoc but it only sends one string as input to a command

# SYNTAX command1 <<< "string1"
#T# command1 executes using string1 as input, string1 accepts arithmetic expansion, command substitution, parameter expansion, etc.

var1=2
bc <<< "3 + $((1 + 1)) + $(echo 1) + $var1" # 8 # 3 + 2 + 1 + 2
# |-----

# |-------------------------------------------------------------

#C# Composite types

# |-------------------------------------------------------------

#C# --- Arrays

# |-----
#T# arrays in bash can be said to be composite types since they can store any different types of data together

#T# arrays are created within parentheses after the equal sign and separated by space
arr1=( elem1 elem2 elem3 )

#T# declaring, reading from, and writing to arrays
arr1=( elem1 2 'elem three' )
int1=${arr1[1]} # 2
arr1[4]='new elem' # index 3 doesn't need to be assigned, it's null by default
# |-----

#C# --- Associative arrays

# |-----
#T# associative arrays are created using the -A flag of the declare command (see later in this file), the key value pairs go inside parentheses separated by space, each key goes inside brackets and is followed by an equal sign and its associated value
declare -A associative1=( [key1]="value1" [key2]="value2" )

#T# declaring, reading from, and writing to associative arrays
declare -A associative1=( [key1]="value1" [key2]="value2" ) # ( [key2]="value2" [key1]="value1" ) # the order of key value pairs is inverted
str1=${associative1[key2]}  # value2
associative1[key4]="value4" # the new key value pair is appended at the start of the associative array, associative1 == ( [key4]="value4" [key2]="value2" [key1]="value1" )
# |-----

# |-------------------------------------------------------------

#C# Null type

# |-------------------------------------------------------------
#T# the null value is considered to be the empty string
null_var1=""
# |-------------------------------------------------------------

#C# The declare command

# |-------------------------------------------------------------
#T# the declare command is used as a way to set the type of variables by setting attributes to them

#T# the typeset command is an alias for the declare command

# SYNTAX declare -o1 var1
# SYNTAX declare +o1 var1
#T# var1 is assigned the attribute denoted by -o1 which is a flag that indicates a data type, when using +o1 the attribute is removed from var1

#T# the following are the flags of the declare command that assign types to var1, described using the -o1 version
#T#     -a, +a, makes var1 an indexed array
#T#     -A, +A, makes var1 an associative array
#T#     -i, +i, makes var1 an integer
#T#     -l, +l, makes var1 a lowercase string
#T#     -n, +n, makes var1 a reference to another variable
#T#     -r, +r, makes var1 a readonly variable
#T#     -u, +u, makes var1 an uppercase string
#T#     -x, +x, makes var1 an environment variable

declare -a arr1=( "elem1" "elem2" )
declare -A associative1=( [key1]="value1" [key2]="value2" )
declare -i int1=54
declare -l str1="STRING1" # string1
declare -n int_ref1=int1 # 54
declare -r read_only1="read_only_string1"
declare -u str2="string2" # STRING2
declare -x int2=25

#T# the declare command has a few flags that don't actually declare a variable, but that are still useful
#T#     -f, must be used with a function, it shows the function's body
#T#     -F, must be used with a function, it shows the function name and debug information

f1() { : ; } # see S1_06_Functions.sh
declare -f f1
#T# the former prints
# f1 () 
# { 
#     :
# }
declare -F f1 # f1 int1 /path/to/file_of_f1 # int1 and /path/to/file_of_f1 appear when printing debug information (see S1_14_Interpreter.sh), int1 means the number line where f1 is defined inside file_of_f1
# |-------------------------------------------------------------