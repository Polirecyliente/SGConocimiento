
#   Standard library

#T# Table of contents

#C# Basic functions
#C# Math functions
#C# Datetime functions

#T# Beginning of content

#C# Basic functions

# |-------------------------------------------------------------

# |--------------------------------------------------\
#T# the type command is used to know the type of a command or keyword, so its output is either alias, keyword, function, builtin, file, or not found

#T# an alias is a shell word that executes another command or keyword, a keyword is a shell word that has its own semantic meaning for Bash, a function is a command created in Bash, a builtin is a command that comes with Bash, a file is an external command that resides in the file hierarchy

# SYNTAX type word1
#T# word1 is the name of the command or keyword whose type is being examined

type man # man is hashed (/usr/bin/man)
#T# in the example the man command is hashed which allows for quicker execution, the hash command is explained in this file too
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# the compgen command generates completions for different kinds of names

# SYNTAX compgen -o1 str1
#T# -o1 is a flag to indicate the type of name for which completions will be generated, str1 is optional and it contains a string that will be matched by the resulting completions, and only the matching completions are output

#T# -o1 con be one of several values
#T#     -a, generates completions of aliases
#T#     -b, generates completions of builtin commands
#T#     -c, generates completions of commands
#T#     -d, generates completions of directories
#T#     -e, generates completions of exported shell variables (parameters)
#T#     -f, generates completions of files and directories
#T#     -g, generates completions of groups in the operating system
#T#     -j, generates completions of jobs under the current shell
#T#     -k, generates completions of keywords
#T#     -s, generates completions of services
#T#     -u, generates completions of users in the operating system
#T#     -v, generates completions of shell variables

compgen -b tr
#T# the former prints
# trap
# true
# |--------------------------------------------------/

#T# the eval command concatenates its arguments into a single string, and then executes that string in the current shell as if it was written in the shell
int1=5
eval 'echo "string $int1"' "in echo" # string 5 in echo

# |--------------------------------------------------\
#T# the exec command replaces the current shell with a command to be executed or with a redirection in the same shell

# SYNTAX exec -o1 -o2 var2 command1 redirection1
#T# everything is optional (if command1 is left out then redirection1 should be there and vice versa) 

#T# command1 is executed and replaces the current shell, destroying the current shell, -o1 represents a flag, -o2 var2 represent a kwarg pair, the -c flag executes command1 in an empty environment, the -a name1 kwarg pair changes the value of $0 for name1 inside command1

#T# if command1 is left out, so redirection1 is alone, then redirection1 applies to the current shell

exec -c -a 'new_shell' rbash 1>file1 # opens restricted bash, in an empty environment, with the value of $0 being 'new_shell', and all output redirected to file1 in the working directory
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# the expr command outputs the result of an expression, this expression can be a boolean expression, or an integer arithmetic expression (but no exponentiation), a regex expression, or a string expression

#T# the syntax is very similar to the rest of Bash, and uses most of the operators in the same way as Bash (see S1_03_Operators.sh), boolean expressions return 0 for false and 1 for true

# SYNTAX expr "token1" "token2" "token3"
#T# token1, token2, token3, etc., are evaluated as an expression, it's important to quote the tokens so that the shell operators don't act as shell operators but as operators that are part of the expression

#T# there can be more than three tokens, tokens can be numbers, strings, or operators, parentheses can be used as tokens to set the order of operations, token1 can specify a command, this is only for regex and string expressions, in that case token1 can be 'match', 'substr', 'index', and 'length'

#T# the following are examples of boolean expressions
expr "s1" "==" "s2" # 0 # equality operation
expr "s1" "!=" "s2" # 1 # not equal operation
expr "5"  ">"  "3"  # 1 # greater than operation
expr "2"  "<"  "7"  # 1 # less than operation
expr "5"  ">=" "5"  # 1 # greater than or equal operation
expr "7"  "<=" "7"  # 1 # less than or equal operation

expr "s1" "|" "s2" # s1 # or operation, an operand is false with 0 or null ""
expr  ""  "|" "s2" # s2
expr  ""  "|"  ""  # 0
expr "s1" "&" "s2" # s1 # and operation, same rules as the or operation
expr  ""  "&" "s2" # 0

#T# the following are examples of integer arithmetic expressions
expr "7" "+" "5" # 12 # addition operation
expr "7" "-" "5" #  2 # subtraction operation
expr "5" "*" "3" # 15 # multiplication operation
expr "5" "/" "3" #  1 # division rounded towards zero operation
expr "5" "%" "3" #  2 # modulo operation

#T# the following are examples of regex and string expressions
int1=3; int2=5; str1="xpr"
expr "example string" ":" "\w*ple\s" # 8 # colon operator to match the first string to the regex pattern in the second string, the output is the number of matched chars
expr "match" "example string" "\w*ple\s" # 8 # same as before
expr "substr" "example string" "$int1" "$int2" # ample # returns a substring from "example string" starting at char int1, and with a length of int2 chars
expr "index" "example string" "$str1" # 2 # returns the index of the first char found in "example string" from the chars in str1
expr "length" "example string" # 14 # returns the length of "example string"
# |--------------------------------------------------/

#T# the alias command is used for the creation of aliases, when typing an alias in the shell, the alias is expanded to another string, and that string is executed
alias e1="echo 'this' 'string never changes'"
e1 # this string never changes

#T# the builtin command allows the execution of a builtin command, even if there is another command of the same name that takes precedence
echo() { builtin "echo" "ubiquitous string"; }
echo "arg1" "arg2" # ubiquitous string

#T# the command command acts similar to the builtin command
echo() { command "echo" "newly ubiquitous"; }
echo "arg1" "arg2" "arg3" # newly ubiquitous

# |--------------------------------------------------\
#T# the enable command is used to enable or disable builtin commands

# SYNTAX enable command1
#T# this enables command1

# SYNTAX enable -n command1
#T# this disables command1

enable -n typeset
typeset -i int1=5 # typeset: command not found

enable typeset
typeset -i int1=5
echo $int1 # 5
# |--------------------------------------------------/

#T# the which command outputs the path to its argument if it's an executable on the operating system path
which bash # /bin/bash

# |--------------------------------------------------\
#T# the hash command is used to manage the hash table of used commands

#T# the hash table contains a field for the used commands paths, and a field for the number of times each command has been called

# SYNTAX hash -o1 command1
#T# -o1 is a flag or kwarg option to indicate the action to be done about the hash table, command1 is the command that will be affected in the hash table, omitting -o1 and command1 outputs the hash table

#T# the following are a few values of the -o1 flag or kwarg option
#T#     -d command1, deletes the entry of command1 in the hash table
#T#     -r, deletes all entries of the hash table
#T#     -l, lists the entries of the hash table
#T#     -t command1, outputs the path of command1
#T#     command1, hashes command1 and adds it to the hash table

hash which
hash man
hash
#T# the former prints
# hits	command
#    0	/usr/bin/which
#    0	/usr/bin/man
hash -d which # the which command's entry is deleted from the hash table
# |--------------------------------------------------/

#T# the time keyword is used to measure the time of execution of a command or set of commands, it measures the execution time of it's arguments
time ping duckduckgo.com
#T# the former prints
# real	0m2,531s # time from start to finish
# user	0m0,000s # time in user space used by the command or its children
# sys	0m0,003s # time in kernel mode used by system calls from the command
# |-------------------------------------------------------------

#C# Math functions

# |-------------------------------------------------------------
#T# a lot of math functions are done with the bc command (the basic calculator), it can be used interactively by calling it with the -i flag, the -l flag loads the standard math library needed to access math functions, the 'scale' internal variable of bc is used to set the truncated amount of decimals in the result of a division

#T# in bc (interactive or in a script), any variable's value can be printed to stdout just by typing its name into the bc command, operators are mostly the same as in Bash, a difference is that the power operator is the caret ^

#T# the s function returns the sine of a number in radians
var1=$(bc -l <<< "scale = 5; s(3.14159/2)") # 1.00000

#T# the c function returns the cosine of a number in radians
var1=$(bc -l <<< "scale = 5; c(0)") # 1.00000

#T# the a function returns the arctangent of a number
var1=$(bc -l <<< "scale = 5; a(1)") # .78539 # same as pi/4

#T# get the pi constant with the a function
var1=$(bc -l <<< "a(1) * 4") # 3.14159265358979323844 # approximates pi

#T# the l function returns the natural logarithm of a number
var1=$(bc -l <<< "scale = 5; l(1)") # 0

#T# the e function returns the e constant raised to the power of a number
var1=$(bc -l <<< "e(1)") # 2.71828182845904523536 # approximates e

#T# the j function returns the Bessel function of order int1 evaluated in a given number
var1=$(bc -l <<< "scale = 5; j(1, 8.2)") # .25799

#T# the sqrt function returns the square root of a number
var1=$(bc -l <<< "scale = 5; sqrt(2)") # 1.41421

#T# the length function returns the amount of significant digits in a number
var1=$(bc -l <<< "length(253.45)") # 5

#T# generate a random number between int1 and int2 using the $RANDOM variable, (( int1 + $RANDOM % int2 ))
(( var1 = 5 + $RANDOM % 22 )) # var1 == 11 # the number is between 5 and 27
# |-------------------------------------------------------------

#C# Datetime functions

# |-------------------------------------------------------------
#T# the date command is used to get the date and time
date # mar 27 oct 2020 12:11:09 -05 # the last number is the timezone

#T# the output of the date command can be formatted using format codes that start with the percent sign %

# SYNTAX date -o1 -o2 var2 +"format_string1"
#T# all arguments are optional, with no arguments the current datetime is output, -o1 represents a flag, -o2 var2 represents a kwarg pair, format_string1 contains the format codes to specify the output of the datetime

#T# the -u flag outputs the date in UTC (Universal Time Coordinated), the -d date1 kwarg pair outputs date1 instead of the current date (the date1 arg is written as "year-month-day hour:minute:second"), the -r file1 kwarg pair outputs the last modification time of file1

date -u -d "1998-10-21 20:42" +"%x and %X" # 21/10/98 and 20:42:00

#T# the following are the format codes that can be used in the date command
#T#     %a, locale weekday name abbreviated
#T#     %A, locale weekday name
#T#     %b, locale month name abbreviated
#T#     %B, locale month name
#T#     %c, locale default format
#T#     %C, century number
#T#     %d, day of the month with zero padding
#T#     %D, shorthand for %m/%d/%y
#T#     %e, day of the month
#T#     %F, shorthand for %Y-%m-%d
#T#     %g, year with two digits
#T#     %G, year
#T#     %h, equivalent to %b
#T#     %H, hour in 24 hours format
#T#     %I, hour in 12 hours format
#T#     %j, day of the year
#T#     %k, same as %H, but with space padding
#T#     %l, same as %I, but with space padding
#T#     %m, month number
#T#     %M, minute
#T#     %n, newline char
#T#     %p, AM or PM in a 12 hour clock
#T#     %P, same as %p, but lowercase
#T#     %r, shorthand for %I:%M:%S %p
#T#     %R, shorthand for %H:%M
#T#     %s, seconds from epoch
#T#     %S, second
#T#     %t, tab char
#T#     %T, shorthand for %H:%M:%S
#T#     %u, weekday number, monday is 1
#T#     %U, week of the year, starting monday
#T#     %V, week of the year, ISO 8601
#T#     %w, weekday number, sunday is 0
#T#     %W, week of the year, starting sunday
#T#     %x, shorthand for %m/%d/%y
#T#     %X, shorthand for %H:%M:%S
#T#     %y, year with two digits
#T#     %Y, year
#T#     %z, timezone change
#T#     %Z, timezone name
#T#     %%, escaped char %
# |-------------------------------------------------------------