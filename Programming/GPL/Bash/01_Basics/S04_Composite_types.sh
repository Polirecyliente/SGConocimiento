
#   Composite types

#T# Table of contents

#C# Composite types in general
#C# Strings
#C# --- String formatting

#T# Beginning of content

#C# Composite types in general

# |-------------------------------------------------------------
#T# the only supported composite types are the one dimensional array, and the one dimensional associative array, their elements can be of any type except for other arrays or associative arrays
arr1=( "elem1" "elem2" "elem3" )
declare -A associative1=( [key1]="value1" [key2]="value2" )

#T# the string is partially treated as a composite type, mainly because its elements can't be accessed directly
str1="string1"

#T# get all the elements of an array separated by IFS
arr1=( "elem1" "elem2" "elem3" )
echo ${arr1[@]} # elem1 elem2 elem3
echo ${arr1[*]} # elem1 elem2 elem3

#T# get all the elements of an array as a single word (string)
arr1=( "elem1" "elem2" "elem3" )
echo "${arr1[*]}" # "elem1 elem2 elem3"

#T# get all the elements of an array as separate words (strings)
arr1=( "elem1" "elem2" "elem3" )
echo "${arr1[@]}" # "elem1" "elem2" "elem3"

#T# get the length of a composite type, the amount of elements it contains, by preceding the variable's name with a hash # when doing an expansion
arr1=( "elem1" "elem2" "elem3" )
declare -A associative1=( [key1]="value1" [key2]="value2" )
echo ${#arr1[@]}         # 3
echo ${#associative1[@]} # 2

#T# append new elements to a composite type with the += operator
str1="string1"
str1+=" appended_string1" # string1 appended_string1
arr1=( "elem1" "elem2" "elem3" )
arr1+=( "appended_elem1" )
echo ${arr1[@]} # elem1 elem2 elem3 appended_elem1

#T# get the values of an associative array
declare -A associative1=( [key1]="value1" [key2]="value2" )
echo ${associative1[@]} # value2 value1

#T# get the keys of an associative array (this gets the indices when applied to an array)
declare -A associative1=( [key1]="value1" [key2]="value2" )
echo ${!associative1[@]} # key2 key1
# |-------------------------------------------------------------

#C# Strings

# |-------------------------------------------------------------
#T# a string can be made so that only its escaped chars (see S02_Data_types.sh) are interpreted (no parameter expansion)

# SYNTAX $'str1\char1str2'
#T# str1 and str2 are substrings, char1 is a single character that is escaped, char1 is interpreted with this syntax

echo $'A\tB' # A	B

#C# --- String formatting

# |-----
#T# the printf command is used to output or store formatted strings

# SYNTAX printf -v var1 "format_string1" "arg1" "arg2"
#T# -v var1 is a kwarg pair that is optional and serves to store the formatted string in var1, format_string1 is the main string that contains both the content of the string and the formatting to apply to arg1, arg2, up to argN

#T# inside format_string1, escaped characters that begin with a backslash \ are interpreted (see S02_Data_types.sh), and also are format specifiers that begin with a percent sign %, these format specifiers dictate the format that arg1, arg2, argN will have

#T# the resulting formatted string is format_string1 but putting arg1, arg2, argN in the places of the format specifiers, if the number N in argN is greater than the number of format specifiers then format_string1 is repeated until all argN strings have been placed in format specifiers, if there are remaining format specifiers they are replaced with 0 for numbers or the empty string "" for strings

# SYNTAX %flag1width1.precision1specifier1
#T# this is the syntax for a format specifier, from these, only specifier1 is obligatory, the rest is optional
#T#     flag1 can be alignment ('-' left inside width1), prefix ('+' numbers with sign, '#' hex numbers with 0x and octal numbers with 0), padding ('0' zero padding inside width1, ' ' space inside width1), style (''' separate a number in its periods of three digits each), these can be combined
#T#     width1 is the minimum size in chars for the affected argument
#T#     .precision1 is the amount of digits after the decimal point, or the maximum size in chars for the affected argument
#T#     specifier1 can be one of the following chars, a, A, b, c, d, e, E, f, g, G, i, o, q, s, u, x, X, or %, there is an example for each

#T# both width1 and precision1 can be changed via placeholders using the asterisk *, and then the actual width1 or precision1 is passed as an argument

printf "ini %a end\n" "13" # ini 0xdp+0 end # %a takes a number and outputs it as a floating point hex, 0xd is the number as stored in memory, p+0 is the power of two multiplier, e.g. if it was p+3 then the number before the p should be multiplied by 2**3 == 8 to get the original number
printf "ini %A end\n" "13" # ini 0XDP+0 end # same as before, but with capital letters
printf "ini %b end\n" "\t" # ini 	 end # %b interprets its arg as an escape sequence
printf "ini %-9c end\n" "abc" # ini a         end # %c takes only the first char of its arg
printf "ini %+'08d end\n" "5420" # ini +005,420 end # %d formats its arg as an integer
printf "ini %.2e end\n" "320.9" # ini 3.21e+02 end # %e takes a number as arg and outputs the number in scientific notation
printf "ini %E end\n" "320.9" # ini 3.209000E+02 end # same as before, but with capital letters
printf "ini % 9.1f end\n" "1.5" # ini       1.5 end # %f takes a floating point arg
printf "ini %g end\n" "32500" # ini 32500 end # %g takes a number and formats it as normal, or in scientific notation, depending on the available space
printf "ini %.2G end\n" "32500" # ini 3.2E+04 end # same as before, but with capital letters
printf "ini %i end\n" "'A" # ini 65 end # %i, same as %d, in here the apostrophe in 'A allows A to be represented as an integer
printf "ini %#o end\n" "9" # ini 011 end # %o takes a number and formats it as an octal number
printf "ini %q end\n" "a b" # ini a\ b end # %q formats its arg to be usable directly by the shell
printf "ini %s end\n" "str1" # ini str1 end # %s takes a string arg
printf "ini %u end\n" "-5" # ini 18446744073709551611 end # %u formats its arg as an unsigned integer
printf "ini %x end\n" "13" # ini d end # %x takes a number and formats it as a hex number
printf "ini %X end\n" "13" # ini D end # same as before, but with capital letters
printf -v var1 "ini %% end\n" # var1 == "ini % end" # %% outputs a percent sign
# |-----

# |-------------------------------------------------------------