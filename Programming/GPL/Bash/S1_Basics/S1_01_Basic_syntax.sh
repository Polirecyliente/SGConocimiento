
#   Basic Syntax

#T# Contents
#T# Basic syntax
#T# Variables, constants, literals

#T# run any Bash file /path/to/file1.sh in a terminal with
# bash /path/to/file1.sh

#T# echo (single quotes for literal string)
echo 'Hello World!'

#T# escaped characters start with backslash
echo 'The newline character is \n which is an n escaped with \'

#T# semicolon separates commands in one line
echo 'First line'; echo 'Second line'

#T# Variables, constants, literals

#T# Variable definitions: int, string, command substitition $()
PRICE_PER_APPLE=5
greeting='Hello       world!'
FileWithTimeStamp=/path/to/file_$(/bin/date +%Y-%m-%d).txt

#T# echo (double quotes for interpreted string), escape char, variable substitution ${}, white spaces inside double quotes
echo "The price of an Apple today is: \$${PRICE_PER_APPLE}"
echo ${greeting}" now with spaces: ${greeting}"

#T# echo -e to enable escaped characters inside double quoted string
BIRTHDATE='Jan 1, 2000'
BIRTHDAY=$(date -d "${BIRTHDATE}" +%A)
echo -e "Date: ${BIRTHDATE}\nWeekday: ${BIRTHDAY}"