
#   Standard library

#T# Table of contents

#C# Basic functions
#C# Math functions
#C# String functions
#C# Datetime functions
#C# Regex matching
#C# - Characters
#C# - Quantifiers
#C# - Character classes
#C# - Groupings
#C# - Subroutines and conditionals
#C# - Anchors and boundaries
#C# - Lookarounds
#C# - Regex modifiers
#C# Builtin values
#C# - Special parameters

#T# Beginning of content

#C# Basic functions

# |-------------------------------------------------------------
#T# the type command is used to know the type of a command or keyword, so its output is either alias, keyword, function, builtin, file, or not found

# SYNTAX type word1
#T# word1 is the name of the command or keyword whose type is being examined

type man # man is hashed (/usr/bin/man)
#T# in the example the man command is hashed which allows for quicker execution, the hash command is explained in this file too

#T# the compgen command generates completions for different kinds of names

# SYNTAX compgen -o1 str1
#T# -o1 is a flag to indicate the type of name for which completions will be generated, str1 is optional and it contains a string that will be matched by the resulting completions, and only the matching completions are output

#T# -o1 can be one of the following
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

#T# the eval command concatenates its arguments into a single string, and then executes that string in the current shell as if it was written in the shell
int1=5
eval 'echo "string $int1"' "in echo" # string 5 in echo

#T# the exec command replaces the current shell with a command to be executed or with a redirection in the same shell

# SYNTAX exec -o1 -o2 val2 command1 redirection1
#T# everything is optional (if command1 is left out then redirection1 should be there and vice versa) 

#T# command1 is executed and replaces the current shell, destroying the current shell, -o1 represents a flag, -o2 val2 represent a kwarg pair, the -c flag executes command1 in an empty environment, the -a name1 kwarg pair changes the value of $0 for name1 inside command1

#T# if command1 is left out, so redirection1 is alone, then redirection1 applies to the current shell

exec -c -a 'new_shell' rbash 1>file1 #| opens restricted bash, in an empty environment, with the value of $0 being 'new_shell', and all output redirected to file1 in the working directory

# |--------------------------------------------------\
#T# the expr command outputs the result of an expression, this expression can be a boolean expression, or an integer arithmetic expression (but no exponentiation), a regex expression, or a string expression

#T# the syntax is very similar to the rest of Bash, and uses most of the operators in the same way as Bash (see S03_Operators.sh), boolean expressions return 0 for false and 1 for true

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

#T# the hash command is used to manage the hash table of used commands, the hash table contains a field for the used commands paths, and a field for the number of times each command has been called

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

#C# String functions

# |-------------------------------------------------------------
#T# the seq command creates a sequence of numbers, each on its own line, starting at the first argument and ending at the second argument (if there is only one argument then the sequence ends at this one argument)
seq 2 3
#T# the former prints
# 2
# 3
# |-------------------------------------------------------------

#C# Datetime functions

# |-------------------------------------------------------------
#T# the date command is used to get the date and time
date # mar 27 oct 2020 12:11:09 -05 # the last number is the timezone

#T# the output of the date command can be formatted using the format codes from strftime that start with the percent sign %

# SYNTAX date -o1 -o2 val2 +"format_string1"
#T# all arguments are optional, with no arguments the current datetime is output, -o1 represents a flag, -o2 val2 represents a kwarg pair, format_string1 contains the format codes to specify the output of the datetime

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

#C# Regex matching

# |-------------------------------------------------------------
#T# the grep command is used to globally match strings or patterns in the contents of files, and then print these matches

# SYNTAX grep -o1 -o2 val2 'pattern1' file1 file2
#T# about the options, -o1 represents a flag, -o2 val2 represent a kwarg pair, this matches pattern1 in the contents of file1, file2, up to fileN, pattern1 is in single quotes to avoid expansion

#T# grep can also receive input directly via redirection and piping (see S12_System_calls.sh)

#T# -o1 and -o2 val2 can be one of the following
#T#     -A int1, print int1 lines after each match
#T#     -B int1, print int1 lines before each match
#T#     -c, output the amount of lines that matched
#T#     -E, interpret pattern1 with the Extended Regular Expression rules
#T#     -i, case insensitive matching
#T#     -m int1, only match up to the first int1 occurrences
#T#     -n, output the line number as well
#T#     -o, output only the match
#T#     -P, use Perl Compatible Regular Expressions to interpret the regex
#T#     -r, grep files recursively
#T#     -v, invert the results (output the non matching lines)
#T#     -z, allow multiline matching, the whole input becomes a single line

#T# the contents of file1 are the following
# first word1 word1 line
# second word1 line
# third word1 line
grep -n "i" file1
#T# the former prints
# 1:first word1 word1 line
# 2:second word1 line
# 3:third word1 lineh
#T# the "i" letter is highlighted
echo "in string1" | grep -n 'i' # 1:in string1 #| the "i" letter is highlighted

#T# the following regex operators and special characters can also be used in other commands that accept patterns, such as the sed program

#T# other regex operators and special characters from PCRE (Perl Compatible Regular Expressions) can be used with the -P flag of the grep command, these may not work in other programs, such as the sed program

#C# - Characters

# |-----
#T# note that to match a dollar sign $ it must be escaped and inside single quotes (because it's an operator in both Bash and regex), such as '\$'

#T# the dot . is used to match any char
echo "str1" | grep -E '.' # str1 # all chars match

#T# to match an operator as a literal char, it must be escaped with a backslash \
echo 'str1.' | grep -E '\.' # .

#T# the escaped char \s matches one whitespace (space, tab, newline)
echo "a b" | grep -E '\sb' #  b

#T# the escaped char \S matches one non whitespace
echo "a bc" | grep -E '\Sc' # bc

#T# the escaped char \w matches one alphanumeric character or an underscore
echo "_a5." | grep -E '\w' # _a5

#T# the escaped char \W matches one non alphanumeric character nor an underscore
echo "_a5." | grep -E '\W' # .

#T# the escaped char \d matches one digit
echo "a5b" | grep -P '\d' # 5

#T# the escaped char \D matches one non digit
echo "5bc" | grep -P '\D' # bc

#T# the escaped char \X matches one unicode char
echo -e "a\u2446b" | grep -P '\w\X' # a⑆

#T# to match a particular unicode char, use either \x{hex1} or the unicode char itself, hex1 is the hexadecimal number of the unicode char being matched, there is no support to match with the char name \N{name1}
echo -e "a⑆b" | grep -P '\x{2446}b' # ⑆b
echo -e "a⑆b" | grep -P 'a⑆'        # a⑆

#T# unicode properties are matched in general with \p{prop1} where prop1 stands for the unicode property being matched, a char with said property will be matched

#T# unicode categories are matched with \p{categ1}, categ1 can be one of the following
#T#     L, matches a letter char, such as 's'
#T#     Ll, matches a lowercase letter char, such as 's'
#T#     Lu, matches an uppercase letter char, such as 'S'
#T#     Lt, matches a titlecase letter char, such as 'ǅ' \u01C5
#T#     L&, matches a lowercase, uppercase, or titlecase letter char, such as 'ǅ'
#T#     Lm, matches a modifier letter char, such as 'ʱ' \u02B1
#T#     Lo, matches a type other letter char, such as 'ƻ' \u01BB
#T#     M, matches a combining mark char (like diacritics), such as the breve in 'ă' a\u0306
#T#     Mc, matches an spacing combining mark char, such as 'ೄ' \u0CC4
#T#     Me, matches an enclosing mark char, such as 'a꙲' a\uA672
#T#     Mn, matches a nonspacing mark char, such as 'ả' a\u0309
#T#     N, matches a numeric char, such as '୬' \u0B6C
#T#     Nd, matches a decimal digit char, such as '߈' \u07C8
#T#     Nl, matches a number letter char, such as 'ↈ' \u2188
#T#     No, matches a type other number char, such as '௲' \u0BF2
#T#     P, matches a punctuation char, such as '⸗' \u2E17
#T#     Pc, matches a punctuation connector char, such as '﹏' \uFE4F
#T#     Pd, matches a punctuation dash char, such as '⸻' \u2E3B
#T#     Pe, matches a punctuation close char, such as '⟧' \u27E7
#T#     Pf, matches a punctuation final quote char, such as '»' \u00BB
#T#     Pi, matches a punctuation initial quote char, such as '⸄' \u2E04
#T#     Ps, matches a punctuation open char, such as '⁅' \u2045
#T#     Po, matches a type other punctuation char, such as '¶' \u00B6
#T#     S, matches a symbol char, such as '⌨' \u2328"
#T#     Sc, matches a symbol currency char, such as '֏' \u058F
#T#     Sk, matches a symbol modifier char, such as '˧' \u02E7
#T#     Sm, matches a symbol math char, such as '؆' \u0606
#T#     So, matches a type other symbol char, such as '۩' \u06E9
#T#     Z, matches a separator char, such as \u205F
#T#     Zl, matches a separator line char, such as \u2028
#T#     Zp, matches a separator paragraph char, such as \u2029
#T#     Zs, matches a separator space char, such as ' ' \u0020
#T#     C, matches a control char, such as \uFFF9
#T#     Cf, matches a format control char, such as \u2060
#T#     Co, matches a private use control char, such as \uE000
#T#     Cc, matches a type other control char, such as \u008A
echo "str1" | grep -P '\p{L}'        # str
echo -e "\u01C5" | grep -P '\p{Lt}'  # ǅ
echo -e "\u02B1" | grep -P '\p{Lm}'  # ʱ
echo -e "\u01BB" | grep -P '\p{Lo}'  # ƻ
echo -e "a\u0306" | grep -P 'a\p{M}' # ă
echo -e "\u0B6C" | grep -P '\p{N}'   # ୬
echo -e "\u2E17" | grep -P '\p{P}'   # ⸗
echo -e "\u2328" | grep -P '\p{S}'   # ⌨
echo -e "\u205F" | grep -P '\p{Z}'   #  
echo -e "\uFFF9" | grep -P '\p{C}'   #  

#T# unicode scripts are matched with \p{script1}, the possible values of script1 are the following (each name represents a script, 'Common' is for chars common to many scripts, 'Inherited' is for chars that inherit their script from a char they accompany, like nonspacing diacritics do): Arabic, Armenian, Avestan, Balinese, Bamum, Bassa_Vah, Batak, Bengali, Bopomofo, Brahmi, Braille, Buginese, Buhid, Canadian_Aboriginal, Carian, Caucasian_Albanian, Chakma, Cham, Cherokee, Common, Coptic, Cuneiform, Cypriot, Cyrillic, Deseret, Devanagari, Duployan, Egyptian_Hieroglyphs, Elbasan, Ethiopic, Georgian, Glagolitic, Gothic, Grantha, Greek, Gujarati, Gurmukhi, Han, Hangul, Hanunoo, Hebrew, Hiragana, Imperial_Aramaic, Inherited, Inscriptional_Pahlavi, Inscriptional_Parthian, Javanese, Kaithi, Kannada, Katakana, Kayah_Li, Kharoshthi, Khmer, Khojki, Khudawadi, Lao, Latin, Lepcha, Limbu, Linear_A, Linear_B, Lisu, Lycian, Lydian, Mahajani, Malayalam, Manichaean, Meetei_Mayek, Mende_Kikakui, Meroitic_Cursive, Meroitic_Hieroglyphs, Miao, Modi, Mongolian, Mro, Myanmar, Nabataean, New_Tai_Lue, Nko, Ogham, Ol_Chiki, Old_Italic, Old_North_Arabian, Old_Permic, Old_Persian, Old_South_Arabian, Old_Turkic, Oriya, Osmanya, Pahawh_Hmong, Palmyrene, Pau_Cin_Hau, Phags_Pa, Phoenician, Psalter_Pahlavi, Rejang, Runic, Samaritan, Saurashtra, Sharada, Shavian, Siddham, Sinhala, Sora_Sompeng, Sundanese, Syloti_Nagri, Syriac, Tagalog, Tagbanwa, Tai_Le, Tai_Tham, Tai_Viet, Takri, Tamil, Telugu, Thaana, Thai, Tibetan, Tifinagh, Tirhuta, Ugaritic, Vai, Warang_Citi, Yi
echo "5" | grep -P '\p{Common}'          # 5
echo -e "\u060B" | grep -P '\p{Arabic}'  # ؋
echo -e "\u1C12" | grep -P '\p{Lepcha}'  # ᰒ
echo -e "\u07D2" | grep -P '\p{Nko}'     # ߒ
echo -e "\u0F12" | grep -P '\p{Tibetan}' # ༒

#T# there is no support to match chars by their unicode block with \p{block1}

#T# the escaped char \t matches one tab char (this also works in the sed program)
echo "ab    c" | grep -P '\tc' #     c

#T# the escaped char \r matches one carriage return (this also works in the sed program)
echo -e "ab\rc" # cb
echo -e "ab\rc" | grep -P '\rc' # c

#T# the escaped char \n matches one newline, use the -z flag
echo -e "str1\nstr2" | grep -zP 'r1\nst' # r1\nst

#T# the escaped char \N matches a non newline
echo -e "ab\ncd" | grep -P '\Nc' #  # no match

#T# the escaped char \h matches an horizontal whitespace (space, tab)
echo -e "a b    c" | grep -P '\hb\hc' #  b    c

#T# the escaped char \H matches a non horizontal whitespace
echo -e "a b  c" | grep -P '\Hc' #  # no match

#T# the escaped chars \Q and \E escape any characters inside them, e.g. \Q.*\E matches a literal dot . followed by a literal asterisk *
echo "a.+?" | grep -P '\Qa.+?\E' # a.+?

#T# the escaped char \K removes the part of the match that is to its left
echo -e "str1\nstr2" | grep -zP 'str1\n\Kstr2' # str2 #| without \K both lines are matched, i.e. str1\nstr2, but with \K str1\n is removed from the match

#T# comments are introduced with (?# comment1)
echo -e "str1" | grep -P '(?# initial comment)str(?# a number comes next)1' # str1
# |-----

#C# - Quantifiers

# |-----
#T# the question mark ? is used as a quantifier to match 0 or 1 of the preceding char
echo "str1" | grep -E 'r?1' # r1

#T# the asterisk * is used as a quantifier to match 0 or more of the preceding char
echo "st1" | grep -E 'r*1' # 1

#T# the plus sign + is used as a quantifier to match 1 or more of the preceding char
echo "strrr1" | grep -E 'r+1' # rrr1

#T# the syntax {int1} is used as a quantifier to match the preceding char int1 times
echo "strrrr1" | grep -E 'r{2}1' # rr1

#T# the syntax {int1,int2} is used as a quantifier to match the preceding char between int1 and int2 times (as many times as possible), so int2 >= int1, if int2 is omitted then match any amount greater than or equal to int1
echo "strrrrr1" | grep -E 'r{1,3}1' # rrr1
echo "strrrrr1" | grep -E 'r{1,}1' # rrrrr1

# |--------------------------------------------------\
#T# lazy (non greedy) quantifiers are created with a question mark ? after the operator, it only works well for the asterisk * quantifier
echo "12345" | grep -P '[0-9]*?' #  # no match

#T# the lazy quantifier *? can be emulated in programs where there is no lazy quantifiers, such as sed

# SYNTAX [^c1]*c1
#T# in here 'c1' is any single character, this syntax matches zero or more non 'c1' characters followed by a 'c1', exactly as .*?c1 using the lazy quantifier
# |--------------------------------------------------/

#T# possessive quantifiers add a plus + at the end of the other quantifiers, they are greedy without backtracking, so that after a match fails, it is not checked if less chars would make it succeed, works as *+, ++, {}+
echo "abcdeF" | grep -Po '\w{1,7}+F' # no match #| 'abcdeF' would be matched without the possessive quantifier
# |-----

#C# - Character classes

# |-----
#T# the syntax [char1char2charN] is called a character class, and used to match any single one of the characters, char1, char2, up to charN
echo "strr1" | grep -E '[trs]1' # r1

#T# using a caret ^ at the start of a character class, negates it
echo "strr1" | grep -E '[^trs]1' #  # no match

#T# using a dash - between two characters inside a character class, matches any single one character in the range of said two characters
echo "strr1" | grep -E '[3-H]1' # r1

#T# a character class can be one of the POSIX character clases, these are made with a word within colons and a pair of brackets which don't count as the character class brackets
#T#     [:alnum:],  matches one alphanumeric char
#T#     [:alpha:],  matches one alphabetic char
#T#     [:blank:],  matches one space or tab
#T#     [:cntrl:],  matches one control char, like a vertical tab
#T#     [:digit:],  matches one digit
#T#     [:graph:],  matches one visible char
#T#     [:lower:],  matches one lowercase char
#T#     [:print:],  matches one visible char or space
#T#     [:punct:],  matches one punctuation char
#T#     [:space:],  matches one space char
#T#     [:upper:],  matches one uppercase char
#T#     [:xdigit:], matches one hexadecimal digit
echo "str1" | grep '[[:alnum:]]' # str1
# |-----

#C# - Groupings

# |-----
#T# the parentheses () are used to capture a group of chars, and treat this group the same as treating a single char
echo "strtr1" | grep -E '(tr)+1' # trtr1

#T# the escaped numbers \1, \2, etc., are used to match (backreference) a captured group, \1 matches the first group, \2 the second, and so on
echo "str1Astr1" | grep -E '(st)(r1)A\1\2' # str1Astr1

#T# a group number from 10 onwards can be backreferenced with \g<int1> or \g{int1} where int1 is the group number, this avoids ambiguity
echo "abcdefghijkk" | grep -P '(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)\g<11>' # abcdefghijkk
echo "abcdefghijkk" | grep -P '(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)\g{11}' # abcdefghijkk

#T# nested groups are possible as (group1(group2)), they are numbered in order of appearance, so \1 matches group1group2, \2 matches group2
echo "ab ab" | grep -P '(a(b)) \1'  # ab ab
echo "ab ab" | grep -P '(a(b)) a\2' # ab ab

#T# named groups are created with (?<group_name1>pattern1) or (?P<group_name1>pattern1) and are matched again (as a backreference) with \k<group_name1>
echo "ab ab" | grep -P '(?P<group1>ab) \k<group1>' # ab ab
echo "ab ab" | grep -P '(?<group1>ab) \k<group1>' # ab ab

#T# there is no support for subscripting repeated groups, e.g. in (\w)+ the group stores only the last match, in this case the last letter

#T# the vertical bar | is used for alternation (to match either one of the patterns separated with the vertical bar)
echo "str1" | grep -E 'st|tr1' # st

#T# the syntax (?:pattern1) is used to create a non capturing group for pattern1, this means that the match of pattern1 can't be recalled with a backreference like \1, because it doesn't create a group
echo "strabab" | grep -P '(?:tr)(ab)\1' # trabab

#T# the syntax (?>pattern1|pattern2) up to patternN creates an atomic group, this means there is no backtracking, i.e. the match is fixed with the first pattern found from this group, and if it fails there is no checking the remaining patterns, in this sense pattern1 has more priority than pattern2 and so on
echo "priorship" | grep -P '(?>prio|priorshi)p' # no match #| given that the first pattern 'prio' is matched, the second one 'priorshi' will never be matched due to the atomic group, without '?>' the whole 'priorship' is matched

#T# the syntax (?|(pattern1)|pattern2|(pattern3)(pattern4)) creates a brach reset group, in it, the group numbering resets, this means that if pattern3 is matched then it's group number 1 and pattern4 is group 2, if pattern1 is matched then it's group 1, and if pattern2 is matched there are no groups created
echo "B12 12" | grep -P '(?|A(\d+)|B(\d+)) \1' # B12 12
# |-----

#C# - Subroutines and conditionals

# |-----
#T# subroutines are a way to reuse regex patterns already created, instead of writing them again

#T# the basic subroutine reuses the numbered groups, a subroutine (?int1) matches the pattern of the numbered group int1
echo "str1 str2" | grep -P '(\w\w\w\d) (?1)' # str1 str2 #| (?1) matches the pattern of the first group '\w\w\w\d'

#T# a named subroutine is the same as before, but using a named group, the named subroutine (?&group_name1) matches the pattern of a named group group_name1
echo "str1 str2" | grep -P '(?<group1>str\d) (?&group1)' # str1 str2

#T# there are relative subroutines, the syntax (?-int1) matches the pattern of the int1 group to the left, (?+int1) matches the pattern of the int1 group to the right
echo "a b 1 2" | grep -P '(\w) (?-1) (?+1) (\d)' # a b 1 2

#T# regex patterns can have recursion with (?R), the whole pattern is put in place of (?R), so the ? quantifier should accompany it, as (?R)? to ensure the recursion can end when it doesn't match anymore
echo "a1b2" | grep -P '\w\d(?R)?' # a1b2
echo "ab12" | grep -P '\w(?R)?\d' # ab12
#| when used at the start '(?R)?pattern1' grep gives an error, "grep: recursive call could loop indefinitely"

#T# there is no support for regex code capsules

#T# conditionals allow matching patterns according to an if-then-else conditional, the basic form is (?(if1)(then_patterns1)|(else_patterns1)) note the plural in patterns as each can be several patterns separated by alternation |, if1 is either a lookaround or a group (named or numbered)
echo "12345" | grep -P '(?(?=\d+)(123|456)|(abc|def))'        # 123
echo "12345" | grep -P '(\d)(?(1)(2)|(b))'                    # 12
echo "12345" | grep -P '(?<group1>\d{2})(?(group1)(34)|(cd))' # 1234
# |-----

#C# - Anchors and boundaries

# |-----
#T# the caret ^ (outside a character class) matches the following chars as an anchor at the start of the line
echo "str1" | grep -E '^str' # str

#T# the escaped char \A matches the beginning of the first line, use it with the -z flag to see the effect
echo -e "str1\nstr2" | grep -zP '\Astr\d' # str1

#T# the dollar sign $ matches the preceding chars as an anchor at the end of the line
echo "str1" | grep -E 'tr1$' # tr1

#T# the escaped char \Z matches the end of the last line, use it with the -z flag to see the effect
echo -e "str1\nstr2" | grep -zP 'str\d\Z' # str2

#T# the escaped char \< matches at the start of a word
echo "ab cd" | grep -E '\<cd' # cd

#T# the escaped char \> matches at the end of a word
echo "ab cd" | grep -E 'ab\>' # ab

#T# the escaped char \b matches at a word boundary
echo "ab cd" | grep -E '\bcd' # cd

#T# the escaped char \B matches at a non word boundary
echo "ab cd" | grep -E '\Bcd' #  # no match

#T# there is no support for the match anchor \G
# |-----

#C# - Lookarounds

# |-----
#T# the syntax (?=pattern1) is used to create a positive lookahead with pattern1, so pattern1 must appear ahead when finding a match, because pattern1 is not matched
echo "str1" | grep -P 'r(?=[0-2])\d' # r1 #| only matches r0, r1, or r2

#T# the syntax (?<=pattern1) is used to create a positive lookbehind with pattern1, so pattern1 must appear behind when finding a match, pattern1 is not matched
echo "str1" | grep -P '(?<=st)r1' # r1

#T# the syntax (?!pattern1) is used to create a negative lookahead with pattern1, so pattern1 can't appear ahead when finding a match, because pattern1 is not matched
echo "str101" | grep -P 'r1(?!00)\d\d' # r101 #| doesn't match in str100
#| use single quotes to avoid history expansion with !

#T# the syntax (?<!pattern1) is used to create a negative lookbehind with pattern1, so pattern1 can't appear behind when finding a match, pattern1 is not matched
echo "str1" | grep -P '(?<!st)r1' #  # no match
# |-----

#C# - Regex modifiers

# |-----
#T# grep only supports a few regular regex modifiers, to use inline modifiers the -P flag must be used

#T# there is no support for the continuation modifier

#T# the global modifier has no inline version, grep has the global modifier by default, use the -m int1 kwarg, the -o flag, and pipe it to head -1 to avoid it (this prints only the first match of the pattern)
echo "str1" | grep -P '\w' # str1
echo "str1" | grep -P -m 1 -o '\w' | head -1 # s

#T# use the case insensitive modifier with the -i flag, this matches lowercase and uppercase letters the same
echo "str1" | grep -i 'STR1' # str1

#T# use the inline case insensitive modifier (?i), turn it off with (?-i)
echo "stR1" | grep -P '(?i)ST(?-i)R1' # stR1

#T# use the multiline modifier directly, by default grep uses this modifier, this makes the caret ^ and the dollar sign $ match at the start and end of intermediate lines (all lines actually)
echo -e "str1\nstr2\nstr3" | grep '^str2$' # str2

#T# use the inline multiline modifier (?m) with the -z flag, turn it off with (?-m)
echo -e "str1\nstr2\nstr3" | grep -zP '(?m)^str2$' # str2

#T# use the dotall modifier with the -z flag, this makes the dot . also match a newline
echo -e "begin\nend" | grep -z 'in.*en' # in\nen

#T# use the inline dotall modifier (?s) with the -z flag, turn it off with (?-s)
echo -e "begin\nend" | grep -zP '(?s)in.*en' # in\nen

#T# there is no support for the regular ungreedy modifier, only for the inline one

#T# use the inline ungreedy modifier (?U), turn it off with (?-U), this makes quantifiers lazy by default
echo "abcde" | grep -P '(?U)\w*' #  # no match

#T# there is no support for the regular extended modifier, there is however, support for the inline version

#T# use the inline extended modifier (?x), turn it off with (?-x), this ignores whitespace that is not escaped or outside a character class
echo -e "str1 str2" | grep -P '(?x)st    r1\ st r2' # str1 str2

#T# there is no support for the extra modifier, but there is for the inline version

#T# use the inline extra modifier (?X), turn it off with (?-X), this throws an error when escaping a character that has no special meaning
echo -e "str1ystr2" | grep -P '(?X)str1\ystr2' # grep: unrecognized character follows \ #| without (?X) this would match "str1ystr2"

#T# there is no support for the ascii modifier (?a), nor for the unicode modifier (?u), \w matches ascii letters
echo -e "áüo" | grep -P '\w' # o

#T# turn on or off several inline modifiers together, e.g. (?ix-m)
echo "str1" | grep -P '(?ix-m)S  T  R1' # str1

#T# all former inline modifiers shown can be introduced exclusively for the pattern inside the same parentheses of the inline modifier, i.e. (?s:pattern1), (?-s:pattern1) only affects pattern1
echo "str1 STR2" | grep -P '(?i:STR)1 (?-i:STR)2' # str1 STR2
# |-----

# |-------------------------------------------------------------

#C# Builtin values

# |-------------------------------------------------------------

#C# - Special parameters

# |-----
#T# the special parameters are variables whose name can't be manually assigned values, they are used to store special values

#T# process related parameters are the $$, $! parameters
echo $$ # 389217 # prints the PID of the current terminal
echo $! # 406952 # prints the PID of the last process sent to be a background process, if any

#T# the $? parameter stores the exit status of the last command
echo $? # 0 # zero usually means correct execution

#T# the $0 parameter stores the name of the script or command that expanded its value
echo $0 # bash

#T# the $_ parameter stores a string with the last argument of the last command
echo $_ # third # if the last command was 'echo first second third'

#T# the $- parameter stores the interpreter options
echo $- # himBHs

#T# the $int1 parameter stores the value of argument int1 passed to the CLI, to a function, or to a script, see S08_CLI_args.sh
echo $1 # str1 #| if 'str1' is the first argument passed to the CLI
echo $2 # str2

#T# the $# parameter stores the number of arguments passed to the CLI, to a function, or to a script, see S08_CLI_args.sh
echo $# # 5 #| if there are 5 arguments

#T# the $*, $@ parameters store the passed arguments in an array, for their difference see S08_CLI_args.sh
echo $* # str1 str2
echo $@ # str1 str2
# |-----

# |-------------------------------------------------------------
