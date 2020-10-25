
#   Composite types

#T# Table of contents

#C# Composite types in general

#T# Beginning of content

#C# Composite types in general

# |-------------------------------------------------------------
#T# the only supported composite types are the one dimensional array, and the one dimensional associative array, their elements can be of any type except for other arrays or associative arrays
arr1=( "elem1" "elem2" "elem3" )
declare -A associative1=( [key1]="value1" [key2]="value2" )

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

#T# get the values of an associative array
declare -A associative1=( [key1]="value1" [key2]="value2" )
echo ${associative1[@]} # value2 value1

#T# get the keys of an associative array (this gets the indices when applied to an array)
declare -A associative1=( [key1]="value1" [key2]="value2" )
echo ${!associative1[@]} # key2 key1
# |-------------------------------------------------------------