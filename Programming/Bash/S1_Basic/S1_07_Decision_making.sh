#!/bin/bash
#   Decision making

#T# if, then, else, elif, fi, NOT !, AND &&, OR ||
expr1=""
expr2="a"
if [[ ${expr1} ]]; then
    echo "Expression is true"
elif [[ !${expr1} ]]; then
    echo "NOT Expression is true"
fi
if [[ ${expr1} && ${expr2} ]]; then
    echo "Both expr1 AND expr2 are true"
elif [[ ${expr1} || ${expr2} ]]; then
    echo "Either expr1 OR expr2 is true"
else
    echo "None is true"
fi

#T# numeric comparisons: -lt, -gt, -le, -ge, -eq, -ne
A=12
B=5
if [[ ${A} -lt ${B} ]]; then
    echo "A is less than B"
elif [[ ${A} -gt ${B} ]]; then
    echo "A is greater than B"
elif [[ ${A} -le ${B} ]]; then
    echo "A is less than or equal to B"
elif [[ ${A} -ge ${B} ]]; then
    echo "A is greater than or equal to B"
elif [[ ${A} -eq ${B} ]]; then
    echo "A is equal to B"
elif [[ ${A} -ne ${B} ]]; then
    echo "A is not equal to B"
else
    echo "this line should never be reached forever"
fi

#T# string comparisons: is empty -z, equal to ==, not equal to !=
if [[ -z ${expr1} || (${expr1} == ${expr2}) ]]; then
    echo "expr1 is empty or both expressions are equal"
elif [[ ${expr1} != ${expr2} ]]; then
    echo "Both expressions are different"
fi

#T# case, in, ), ;;, esac
C="str3"
case ${C} in
    "str1") echo "String 1 selected";;
    "str2") echo "String 2 selected";;
    "str3") echo "String 3 selected";;
esac