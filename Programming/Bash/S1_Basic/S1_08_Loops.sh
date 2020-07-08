#!/bin/bash
#   Loops

#T# for, in, do, done
for fileL in $(ls); do
    echo "File is: ${fileL}"
done

#T# while, do, done; continue
COUNT=4
Arr1=(str1 str2 str3 str4)
while [[ ${COUNT} -gt 0 ]]; do
    if [[ ${COUNT} -eq 2 ]]; then
        COUNT=$((${COUNT} - 1))
        continue
    fi
    echo "Current element is: ${Arr1[${COUNT} - 1]}"
    COUNT=$((${COUNT} - 1))
done

#T# until, do, done; break
until [[ ${COUNT} -ge 12 ]]; do
    COUNT=$((${COUNT} + 1))
    echo "Value of COUNT is: ${COUNT}"
    if [[ ${COUNT} -eq 5 ]]; then
        break
    fi
done