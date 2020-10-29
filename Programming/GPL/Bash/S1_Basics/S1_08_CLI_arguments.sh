
#   CLI arguments

#T# Table of contents

#C# Special parameters
#C# Command prompts

#T# Beginning of content

# |-------------------------------------------------------------
#T# CLI stands for Command Line Interface

#T# execute this file with command line arguments: str2 5.4 -oCount -oCount
# |-------------------------------------------------------------

#C# Special parameters

# |-------------------------------------------------------------
#T# the positional parameters have already been explored in the section about functions (see S1_06_Functions.sh), those apply here as well in the exact same way, $0 for the name of the script or program in execution, $1 for the first argument passed to the CLI, $2 for the second argument passed to the CLI, and so on
echo "arg1 $1, arg2 $2, script name $0" # arg1 str2, arg2 5.4, script name S1_08_CLI_arguments.sh

#T# the following special parameters (variables) are used in parsing CLI arguments, but they can be used the same for function arguments

#T# the $# parameter stores the number of arguments passed in the CLI, or to the function
echo $# # 4

#T# the $*, $@ parameters both store the passed arguments in an array, the difference is that when quoted inside double quotes, "$*" is expanded to the list of arguments as a single string, and "$@" is expanded to the list of arguments as separate strings
for it1 in "$*"; do echo "$it1"; done
for it1 in "$@"; do echo "$it1"; done
# |-------------------------------------------------------------

#C# Command prompts

# |-------------------------------------------------------------
#T# there are 4 default prompts in Bash, denoted by PS1, PS2, PS3, and PS4, PS stands for Prompt String, since each of them is a string that makes up the prompt

#T# PS1 is commonly 'user@host:/path/to/current/dir$ ', and appears as the default prompt in Bash
#T# PS2 is simply '>', and appears when a partial command is entered, e.g. when typing 'echo "str' PS2 appears to complete the echo command
#T# PS3 is '', and appears as the prompt for the select loop (see S1_05_Control_flow.sh)
#T# PS4 is '+', and appears as a debugging prompt

#T# each of these prompt strings can be modified via the values of the variables $PS1, $PS2, $PS3, and $PS4
echo $PS1 # \[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$
echo $PS2 # >
echo $PS3 #
echo $PS4 # +

#T# several escape sequences can be put into the prompt strings to be intepreted as special values
#T#     \a, alert bell system sound
#T#     \d, current date as 'weekday_name_abbreviated month_name_abbreviated day_of_the_month' (the same as '%a %b %d', using format codes (see S1_07_Standard_library.sh))
#T#     \D{format1}, current date using format1 as a string with format codes, e.g. PS1="\D{%Y}" gives '1998' as the prompt if 1998 is the year
#T#     \e, escape char, the same as typing \033 or \x1B
#T#     \h, current host machine, up to the first dot .
#T#     \H, current host full name
#T#     \j, amount of jobs under the shell
#T#     \l, terminal device name, can be checked with the tty command
#T#     \n, newline
#T#     \r, carriage return
#T#     \s, current shell
#T#     \t, time in 24 hour format
#T#     \T, time in 12 hour format
#T#     \@, time with AM or PM
#T#     \A, time in 24 hour format without seconds
#T#     \u, current user
#T#     \v, shell version
#T#     \V, shell version with bug fixing version
#T#     \w, working directory
#T#     \W, like \w, but only shows the name of the last dir in the path
#T#     \!, command number in the history
#T#     \#, command number in the current session
#T#     \$, puts a hash # when the user is root, otherwise a dollar sign $
#T#     \nnn, prints the octal nnn as an ascii char
#T#     \\, one backslash
#T#     \[, begins a control sequence (e.g. an ANSI escape sequence)
#T#     \], ends a control sequence (e.g. an ANSI escape sequence)
#T#     $'\char1' use a normal escape sequence, \char1 is any of the normal escape sequences in Bash (see S1_02_Data_types.sh), this allows using \u to insert an Unicode char instead of the current user

# |--------------------------------------------------\
#T# command prompts can be customized using ANSI escape sequences, these allow modifying the title of the terminal, the prompt string (e.g. its color), the cursor position, among other features

#T# ANSI escape sequences begin with the escape character, there are a number of ways to write the escape character, all of them equivalent, '\e', '\033', '\x1B', in the following the \e form is used

# SYNTAX \e[int1J
#T# this clears the screen, the specific way to clean the screen is dictated by int1, which can be 0 (clear after the cursor), 1 (clear before the cursor), or 2 (clear the whole screen)
echo -e "\e[1J" # clears the screen before the cursor

# SYNTAX \e]0;string1\a
#T# this sets string1 as the title of the terminal
echo -e "\e]0;New Title1\a" # sets 'New Title1' as the title of the terminal

# SYNTAX \e[int1A
#T# moves the cursor up by int1 lines
echo -e "\e[6Atext1" # the cursor is moved up 6 lines, 'text1' is placed in column 1

# SYNTAX \e[int1B
#T# moves the cursor down by int1 lines
echo -e "\e[4Btext1" # the cursor is moved down 6 lines, 'text1' is placed in column 1

# SYNTAX \e[int1C
#T# moves the cursor forward by int1 columns
echo -e "\e[5Ctext1" # the cursor is moved forward 5 columns, 'text1' is placed after column 5

# SYNTAX \e[int1D
#T# moves the cursor back by int1 columns
echo -e "\e[5C\e[3Dtext1" # the cursor is moved forward 5 columns and then back 3 columns, 'text1' is placed after column 2 (5 - 3 == 2)

# SYNTAX \e[int1E
#T# moves the cursor down by int1 lines, and places the cursor in column 1
echo -e "\e[5Etext1" # the cursor goes down 5 new lines, 'text1' is placed in column1

# SYNTAX \e[int1F
#T# moves the cursor up by int1 lines, and places the cursor in column 1
echo -e "\e[3Ftext1" # the cursor goes up 3 lines back, 'text1' is placed in column1

# SYNTAX 

# |--------------------------------------------------/

# |-------------------------------------------------------------