#!/bin/bash
#   Variables

#T# Variable definitions: int, string, command substitition $()
PRICE_PER_APPLE=5
greeting='Hello       world!'
FileWithTimeStamp=/tmp/my-dir/file_$(/bin/date +%Y-%m-%d).txt

#T# echo (double quotes for interpreted string), escape char, variable substitution ${}, white spaces inside double quotes
echo "The price of an Apple today is: \$HK ${PRICE_PER_APPLE}"
echo ${greeting}" now with spaces: ${greeting}"

#T# echo -e to enable escaped characters inside double quoted string
BIRTHDATE='Jan 1, 2000'
BIRTHDAY=$(date -d "${BIRTHDATE}" +%A)
echo -e "Date: ${BIRTHDATE}\nWeekday: ${BIRTHDAY}"