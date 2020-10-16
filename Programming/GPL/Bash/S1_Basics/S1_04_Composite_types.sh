
#   Composite types

#T# Array initialization, length of array #Arr[@], all elements Arr[@]
Arr1=( elem1 elem2 elem3 "elem 4" )
Arr2[3]=el3
echo -e "Length of Arr1: ${#Arr1[@]}\nElement3 in Arr2: ${Arr2[3]}"
echo "Elements in Arr1: ${Arr1[@]}"

#T# Strings

#T# expr index, string length #string, string extraction ${string:ini:len}
STRING="STR1"
INDEX1=$(expr index "${STRING}" "T_CHAR")
echo -e "String measures: ${#STRING}\n${STRING:${INDEX1}:2}"

#T# string replacement /, replace all //, replace at start #, at end %
origStr="to be or not to be"
replace1=${origStr/be/be $(date)}
replaceAll=${origStr//be/eat}
replaceAtStart=${origStr/#"to be"/begin}
replaceAtEnd=${origStr/%be/end}