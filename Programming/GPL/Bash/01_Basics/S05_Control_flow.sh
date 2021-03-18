
#   Control flow

#T# Table of contents

#C# Decision making
#C# - Conditional statements
#C# - Switch case statement
#C# Loops
#C# - for loop
#C# - while loop
#C# - until loop
#C# - select loop

#T# Beginning of content

#C# Decision making

# |-------------------------------------------------------------
#T# decision making is made with the if, then, elif, else, and fi keywords, and with the case construct

#T# in an if conditional statement a condition is checked and if it returns 0 then the if block is executed, this also happens in an elif conditional statement

#T# in an else conditional statement no condition is checked, but the else requires an if above it, the elif also requires an if above it, the else block executes when the if and elif blocks do not, and at the end of all this there must be the fi keyword

#T# in a switch case statement the value of a variable is checked and compared to a list of values, if there is a match then the statements associated with the matched value are executed

#C# - Conditional statements

# |-----
#T# conditional statements are carried out with the following syntax

# SYNTAX if, elif, else, conditional statements
# if condition1; then
#     statements1
# elif condition2; then
#     statements2
# else
#     statements3
# fi
#T# if condition1 outputs 0 then the statements1 are executed, else if condition2 outputs 0 then statements2 are executed, else statements3 are executed. Decision making statements can be nested

str1=""
if [[ ${str1} ]]; then
    str2="one"
elif [[ ! ${str1} ]]; then
    if [[ -z ${str1} ]]; then
        str2="two"
    fi
else
    str2="three"
fi
# str2 == "two"

#T# conditional statements can be made into a one liner
str1=a
if [[ ${str1} == 'a' ]]; then echo "in a one liner"; elif [[ ${str1} == 'b' ]]; then echo "in str1 = b"; else echo "in else"; fi # in a one liner
# |-----

#C# - Switch case statement

# |-----
#T# the switch case statement is carried out with the following syntax

# SYNTAX case statement
# case $var1 in
#     "value1") statements1;;
#     "value2") statements2;;
#     "value3") statements3;&
#     "value4") statements4;;&
#     "value5") statements5;;
#     *) default_statements1;;
# esac
#T# the value of var1 is taken and compared to the list of values, value1, value2, value3, up to valueN, if the value of var1 matches any of these values, for example value2, then the statements associated with that value are executed, in this case statements2

#T# the last case is the default case, represented with the asterisk *, the default_statements1 execute when no case value matches the value of var1

#T# each statement can be terminated with a different operator, there are three of them, ;;, ;;&, and ;&

#T# a statement ended in ;; makes Bash end the case statement, in the syntax example, if value1 matches then only statements1 execute

#T# a statement ended in ;;& makes Bash try to match the value of var1 with the following values again, if another match is found then its statement is executed and its ending operator is followed, in the syntax example, if value4 matches then default_statements1 is also executed

#T# a statement ended in ;& will continue executing the following statements until a ;; or ;;& is found, if ;; is found then Bash ends the case statement there, if ;;& is found then the value of var1 is matched again with the following values, in the syntax example, if value3 is matched then statements3, statements4, and default_statements1 are executed

C="str2"
case ${C} in
    "str1") echo "String 1 matched";;
    "str2") echo "String 2 matched";&
    "str3") echo "String 3 matched";;&
    "str2") echo "String 2 matched again";;
esac
#T# the former prints
# String 2 matched
# String 3 matched
# String 2 matched again
# |-----

# |-------------------------------------------------------------

#C# Loops

# |-------------------------------------------------------------
#T# loops are made with the for, while, and until constructs

#T# in a for loop, the loop is repeated for each element of an array

#T# in a while loop, the loop is repeated as long as the while condition outputs 0

#T# in an until loop, the loop is repeated as long as the until condition outputs 1

#C# - for loop

# |-----
#T# the for loop is made with the following syntax

# SYNTAX for loop
# for elem_i1 in ${arr1[@]}; do
#     statements1
#     [continue int1|break int1]
# done
#T# arr1 is an array that becomes expanded, the loop executes the statements1 for each value in arr1, said value is assigned to the iterator elem_i1 in each iteration

#T# the continue keyword is used to skip the rest of the current iteration and start the next one of the affected loop (see about int1)

#T# the break keyword is used to skip all remaining iterations of the loop affected by the break (see about int1)

#T# about int1, when omitted it's the same as int1 == 1, if int1 == 1 then the loop that is affected (breaks or continues) is the current loop, int == 2 the affected loop is the loop outside the current loop, and so on

for file_it1 in $(ls); do
    echo "File is: ${file_it1}"
    if [[ "${file_it1}" == "file1" ]]; then
        break
    else
        continue
    fi
done

#T# there is another syntax of the for loop

# SYNTAX for loop with arithmetic expansion
# for (( statement_ini1; expression1; statement_end1 )); do
#     statements1
#     [continue int1|break int1]
# done
#T# the loop will repeat statements1 as long as expression1 evaluates to true, statement_ini1 is executed only once at the start of the loop, statement_end1 is executed at the end of each loop iteration

#T# the idea is that through the execution of statement_end1 at the end of each iteration, eventually expression1 becomes false, and the loop ends

#T# same as before about continue, break, and int1

for (( it1 = 2; it1 <= 5; it1++ )); do
    echo "iter $it1"
done
#T# the former prints
# iter 2
# iter 3
# iter 4
# iter 5
# |-----

#C# - while loop

# |-----
#T# the while loop is made with the following syntax

# SYNTAX while loop
# while condition1; do
#     statements1
#     [continue int1|break int1]
# done
#T# the statements1 are executed while condition1 outputs 0, (for the continue, break keywords, and for int1, see the for loop subsection)

int1=4
while [[ ${int1} -gt 0 ]]; do
    if [[ ${int1} -eq 2 ]]; then
        (( "int1" -= 1))
        continue
    fi
    (( "int1" -= 1))
done
# int1 == 0
# |-----

#C# - until loop

# |-----
#T# the until loop is made with the following syntax

# SYNTAX until loop
# until condition1; do
#     statements1
#     [continue int1|break int1]
# done
#T# the statements1 are executed as long as condition1 outputs 1, until condition1 outputs 0, (for the continue, break keywords, and for int1, see the for loop subsection)

int1=4
until [[ ${int1} -ge 12 ]]; do
    (( "int1" += 1))
    if [[ ${int1} -eq 9 ]]; then
        break
    fi
done
# int1 == 9
# |-----

#C# - select loop

# |-----
#T# in true fashion, a select loop can be seen as a decision making statement, but given that it loops indefinitely until receiving a selection, the select loop is clasified under the loops section, and also because that reduces confusion due to its namesake

#T# the select loop is made with the following syntax

# SYNTAX select loop
# select var1 in ${arr1[@]}; do
#     statements1
#     [break int1]
# done
#T# a looping prompt is entered, the user must input a number, since an incremental number (starting at 1) is assigned to each element in arr1

#T# the element selected from arr1 is stored in var1, and the input number is stored in a special variable called 'REPLY'

#T# after inputting the number, statements1 execute, and the prompt reappears for another input, until a break statement is found (for break, int1, see the for loop subsection)

PS3="Select one option using numbers: "
#T# PS3 stands for Prompt String 3, this is the prompt for the selection (see the file titled CLI arguments)
while [[ : ]]; do
    select var1 in "opt1" "opt2" "opt3"; do
        break 2
    done
done
echo $var1  # opt3 # assuming option three was selected
echo $REPLY # 3    # assuming option three was selected
# |-----

# |-------------------------------------------------------------
