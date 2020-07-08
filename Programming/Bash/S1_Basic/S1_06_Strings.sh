#!/bin/bash
#   Strings

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