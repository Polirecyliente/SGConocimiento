
#   Expansions, subshells

#T# Parameter expansions

echo "One time substitution"
#T# substitute only in one expression (no assignment) with ${parameter:-word} if parameter is null
echo ${var1:-defValTemp1}
echo ${var1}

echo "Permanent substitution"
#T# assign permanently if parameter is null with ${parameter:=word}
echo ${var1:=defVal1}
echo ${var1}

echo "Substring expansion"
var1=str1str2str3
#T# substring expansion with ${parameter:offset:length}
echo ${var1:1:8}

echo "Unsetting variable"
#T# unset a variable to make it null with unset var1
unset var1
echo ${var1}

echo "Error if null"
#T# return error with "word" if parameter is null with ${parameter:?word}
${var1:?errStr1}

#T# Subshells

#T# commands inside parentheses are executed in a subshell
(
    cd ..
    echo "In subshell"
)

#T# Command substitution

#T# command substitution $()
FileWithTimeStamp=/path/to/file_$(/bin/date +%Y-%m-%d).txt