
#   Interpreter

#T# Table of contents

#C# Interpreter customization
#C# --- Interpreter options
#C# --- Shell options
#C# --- Command prompts
#C# --- ANSI escape sequences
#C# Shell session

#T# Beginning of content

#C# Interpreter customization

# |-------------------------------------------------------------

#C# --- Interpreter options

# |-----
#T# the interpreter can have several options changed during execution

# SYNTAX set -o1
# SYNTAX set +o1
#T# the set command is used to set the value of flags that modify the options of the interpreter, o1 is the flag being set, using -o1 activates the flag, using +o1 turns off the flag

#T# there are several flags used for different options, the following list describes each flag when turned on
#T#     -a, +a, automatically export created or newly modified variables
#T#     -b, +b, print a message when a job is killed
#T#     -e, +e, exit the interpreter on error
#T#     -f, +f, disable globbing
#T#     -h, +h, executed commands are placed in a hash table for quicker access, for an explanation on this hash table see S06_Functions.sh
#T#     -k, +k, arguments that contain variables use the same variables of the calling environment, var1=$var1 uses $var1 from the calling environment
#T#     -m, +m, enable job control, to manage background and foreground processes
#T#     -n, +n, read commands but do not execute them, used executing 'bash -n script1.sh' prints the syntax errors in script1.sh
#T#     -o arg1, +o arg1, activates the shell option arg1, the names of the shell options can be seen executing 'set --help'
#T#     -t, +t, exit the interpreter after executing one command
#T#     -u, +u, print error when calling an unset variable
#T#     -v, +v, print each line read
#T#     -x, +x, print debug information
#T#     -B, +B, perform brace expansion (see S03_Operators.sh)
#T#     -C, +C, impede bash from overwriting files
#T#     -E, +E, the ERR trap can be activated by shell functions (see S09_Exception_handling.sh)
#T#     -H, +H, enable history expansion (see S03_Operators.sh)
#T#     -P, +P, follow symbolic links, e.g. if dir1 has a symlink link1, and -P is on, then executing 'cd link1' makes the pwd be dir1 and not link1
#T#     -T, +T, the DEBUG and RETURN traps can be activated by shell functions (see S09_Exception_handling.sh)

#T# the -i flag means the shell is interactive, the -s flag makes bash read commands from stdin

#T# some of the shell options that can be turned on with the -o arg1 kwarg pair of the set command are the following
#T#     -o pipefail, makes a pipeline of commands have the exit status of the last command to fail

set -x
set +x

#T# other interpreter options are used when starting Bash

# SYNTAX bash -o1 -o2 val2
#T# this should be executed from the operating system shell, such as Bash itself, -o1 represents a flag, and -o2 val2 represent a kwarg pair

#T# the following are some of these options
#T#     -c "command_string1", makes Bash execute command_string1, any strings following command_string1 are taken as positional paratemers for the shell, i.e. $0, $1, etc.
#T#     -s, allows writing the positional parameters for an interactive session, any argument that is positional is not interpreted as a file name, but as a positional parameter

bash -c 'echo str1 "$0" "$1"' "name1" "name2" # str1 name1 name2
# |-----

#C# --- Shell options

# |-----
#T# shell options are modified with the shopt command

# SYNTAX shopt -s option1
#T# the shell option option1 is turned on

# SYNTAX shopt -u option1
#T# the shell option option1 is turned off

#T# the following list is the list of shell options
#T#     extglob, allows the use of an extended set of operators for globbing (see S03_Operators.sh)
#T#     lastpipe, the last command in a pipeline executes in the current shell (see S12_System_calls.sh), job control must be turned off with 'set +m'
#T#     nullglob, if the filename expansion * returns no files, then do not return a literal asterisk *, e.g. doing 'ls *' in an empty dir tries to list a file named '*', unless nullglob is set in which case nothing is listed

shopt -s extglob
shopt -u extglob

# SYNTAX shopt -p option1
#T# prints option1 and its status, on (-s) or off (-u), option1 is optional and leaving it out prints all options and their status
# |-----

#C# --- Command prompts

# |-----
#T# there are 4 default prompts in Bash, denoted by PS1, PS2, PS3, and PS4, PS stands for Prompt String, since each of them is a string that makes up the prompt

#T# PS1 is commonly 'user@host:/path/to/current/dir$ ', and appears as the default prompt in Bash
#T# PS2 is simply '>', and appears when a partial command is entered, e.g. when typing 'echo "str' PS2 appears to complete the echo command
#T# PS3 is '', and appears as the prompt for the select loop (see S05_Control_flow.sh)
#T# PS4 is '+', and appears as a debugging prompt

#T# each of these prompt strings can be modified via the values of the variables $PS1, $PS2, $PS3, and $PS4
echo $PS1 # \[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$
echo $PS2 # >
echo $PS3 #
echo $PS4 # +

#T# several escape sequences can be put into the prompt strings to be intepreted as special values
#T#     \a, alert bell system sound
#T#     \d, current date as 'weekday_name_abbreviated month_name_abbreviated day_of_the_month' (the same as '%a %b %d', using format codes (see S07_Standard_library.sh))
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
#T#     $'\char1' use a normal escape sequence, \char1 is any of the normal escape sequences in Bash (see S02_Data_types.sh), this allows using \u to insert an Unicode char instead of the current user
# |-----

#C# --- ANSI escape sequences

# |-----
#T# the terminal can be customized using ANSI escape sequences, these allow modifying the title of the terminal, the prompt string (e.g. its color), the cursor position, among other features

#T# ANSI escape sequences begin with the escape character, there are a number of ways to write the escape character, all of them equivalent, '\e', '\033', '\x1B'

#T# to start one of these sequences, a CSI (Control Sequence Introducer) is used, the CSI in Bash is a escape char followed by an opening bracket, i.e. \033[, in the following the \e[ form is used

#T# in Bash, the escape sequence must be enclosed in escaped brackets \[ \], this is to avoid behaviors where the escape sequence changes the cursor position or the prompt, e.g. PS1='\[\e[33mP>\e[0m\]' creates a prompt 'P>' of orange color

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

# SYNTAX \e[int1G
#T# moves the cursor to the column int1
echo -e "\e[3Gtext1" # the cursor is moved to column 3, 'text1' is placed in column 3

# SYNTAX \e[int1;int2H
# SYNTAX \e[int1;int2f
#T# moves the cursor to line int1 and column int2, both syntaxes are equivalent
echo -e "\e[4;9Htext1" # the cursor is moved to line 4 column 9, 'text1' is placed in line 4 column 9

# SYNTAX \e[int1J
#T# this clears the screen, the specific way to clean the screen is dictated by int1, which can be 0 (clear after the cursor), 1 (clear before the cursor), 2 (clear the whole screen), or 3 (clear outside the current screen)
echo -e "\e[1J" # clears the screen before the cursor

# SYNTAX \e[int1K
#T# clears part of the current line, depending on int1, which can be 0 (clear after the cursor), 1 (clear before the cursor), 2 (clear the whole line)
echo -e "\e[4G\e[2A\e[0K" # the cursor goes to column 4, then up two lines, and any text after the cursor is cleared

# SYNTAX \e[int1S
#T# scrolls the screen up by int1 lines, adding new lines if necessary
echo -e "\e[3Stext1" # the screen goes up 3 lines, even if the cursor was at the bottom of the terminal, 'text1' is placed in column 1

# SYNTAX \e[int1T
#T# scrolls the screen down by int1 lines, clearing the bottom lines out of the screen
echo -e "\e[3Ttext1" # the screen goes down 3 lines, any lines that would be below the terminal are cleared, 'text1' is placed in column 1

# SYNTAX \e[6n
#T# types the cursor position into the prompt, as ^[[int1;int2R where int1 is the line number, and int2 is the column number, of the current cursor position, 
echo -e "\e[6n"; sleep 0.1 # given that this string starts with '^[' which is the escape char, to see the actual numbers, the sleep command stops the execution for a short moment, to allow priting the string verbatim

# SYNTAX \e[s
#T# saves the current cursor position
echo -e "\e[4;7H\e[s" # the cursor is moved to line 4 column 7, then that position is saved

# SYNTAX \e[u
#T# restores the saved cursor position
echo -e "\e[utext1" # 'text1' is placed in line 4 column 7 of the current screen (even if the screen has moved up or down), if that was the saved cursor position

# SYNTAX \e[?25l
#T# hides the cursor
echo -e "\e[?25l" # the cursor is hidden

# SYNTAX \e[?25h
#T# shows the cursor
echo -e "\e[?25h" # the cursor reappears, if it was hidden before

#T# the following is the syntax for the SGR (Select Graphic Rendition, or Set Graphics Rendition), an SGR consists of a CSI (\e[) followed by arguments separated by semicolon, and ending with a letter 'm'

# SYNTAX \e[0m
#T# reset graphics
echo -e "\e[0mtext1" # 'text1' is displayed with normal graphics from the terminal

# SYNTAX \e[1m
#T# bold text
echo -e "\e[1mtext1" # 'text1' is displayed with a bold font weight

# SYNTAX \e[2m
#T# light or faint text
echo -e "\e[2mtext1" # 'text1' is displayed with a light font weight

# SYNTAX \e[22m
#T# bold or faint off
echo -e "\e[1mtext1\e[22mtext2" # 'text1' appears with bold weight, and 'text2' is displayed with a normal font weight

# SYNTAX \e[3m
#T# italic text
echo -e "\e[3mtext1" # 'text1' is displayed with an italic font

# SYNTAX \e[23m
#T# italic off
echo -e "\e[3mtext1\e[23mtext2" # 'text1' appears in italic, and 'text2' is displayed with a normal font

# SYNTAX \e[4m
#T# underlined text
echo -e "\e[4mtext1" # 'text1' is displayed with an underlined font

# SYNTAX \e[21m
#T# double underlined text
echo -e "\e[21mtext1" # 'text1' is displayed with a double underlined font

# SYNTAX \e[24m
#T# underline off
echo -e "\e[21mtext1\e[24mtext2" # 'text1' appears with a double underline, and 'text2' is displayed with a normal font

# SYNTAX \e[53m
#T# overlined text
echo -e "\e[53mtext1" # 'text1' is displayed with an overlined font

# SYNTAX \e[55m
#T# overline off
echo -e "\e[53mtext1\e[55mtext2" # 'text1' appears with an overline, and 'text2' is displayed with a normal font

# SYNTAX \e[5m
# SYNTAX \e[6m
#T# slow blink text
echo -e "\e[5mtext1" # 'text1' blinks in a slow rate

# SYNTAX \e[25m
#T# blink off
echo -e "\e[6mtext1\e[25mtext2" # 'text1' blinks, and 'text2' is displayed with a normal font

# SYNTAX \e[7m
#T# swap foreground and background colors
echo -e "\e[7mtext1" # 'text1' appears with swapped foreground and background colors

# SYNTAX \e[27m
#T# swap colors off
echo -e "\e[7mtext1\e[27mtext2" # 'text1' appears with swapped colors, and 'text2' is displayed with a normal font

# SYNTAX \e[8m
#T# concealed text
echo -e "\e[8mtext1" # 'text1' is invisible

# SYNTAX \e[28m
#T# concealed off
echo -e "\e[8mtext1\e[28mtext2" # 'text1' is invisible, and 'text2' is displayed with a normal font

# SYNTAX \e[9m
#T# strikethrough text
echo -e "\e[9mtext1" # 'text1' is displayed with an strikethrough font

# SYNTAX \e[29m
#T# strikethrough off
echo -e "\e[9mtext1\e[29mtext2" # 'text1' is strikethrough, and 'text2' is displayed with a normal font

# SYNTAX \e[30m
#T# black text
echo -e "\e[30mtext1" # 'text1' is displayed in black color

# SYNTAX \e[90m
#T# gray text
echo -e "\e[90mtext1" # 'text1' is displayed in gray color

# SYNTAX \e[31m
#T# red text
echo -e "\e[31mtext1" # 'text1' is displayed in red color

# SYNTAX \e[91m
#T# bright red text
echo -e "\e[91mtext1" # 'text1' is displayed in bright red color

# SYNTAX \e[32m
#T# green text
echo -e "\e[32mtext1" # 'text1' is displayed in green color

# SYNTAX \e[92m
#T# bright green text
echo -e "\e[92mtext1" # 'text1' is displayed in bright green color

# SYNTAX \e[33m
#T# yellow (or orange) text
echo -e "\e[33mtext1" # 'text1' is displayed in yellow color

# SYNTAX \e[93m
#T# bright yellow text
echo -e "\e[93mtext1" # 'text1' is displayed in bright yellow color

# SYNTAX \e[34m
#T# blue text
echo -e "\e[34mtext1" # 'text1' is displayed in blue color

# SYNTAX \e[94m
#T# bright blue text
echo -e "\e[94mtext1" # 'text1' is displayed in bright blue color

# SYNTAX \e[35m
#T# magenta text
echo -e "\e[35mtext1" # 'text1' is displayed in magenta color

# SYNTAX \e[95m
#T# bright magenta text
echo -e "\e[95mtext1" # 'text1' is displayed in bright magenta color

# SYNTAX \e[36m
#T# cyan text
echo -e "\e[36mtext1" # 'text1' is displayed in cyan color

# SYNTAX \e[96m
#T# bright cyan text
echo -e "\e[96mtext1" # 'text1' is displayed in bright cyan color

# SYNTAX \e[37m
#T# white text
echo -e "\e[37mtext1" # 'text1' is displayed in white color

# SYNTAX \e[97m
#T# bright white text
echo -e "\e[97mtext1" # 'text1' is displayed in bright white color

# SYNTAX \e[39m
#T# default color
echo -e "\e[34mtext1\e[39mtext2" # 'text1' is in blue color, 'text2' is displayed with the default color

# SYNTAX \e[40m
#T# black background
echo -e "\e[40mtext1" # 'text1' is displayed in a black background

# SYNTAX \e[100m
#T# gray background
echo -e "\e[100mtext1" # 'text1' is displayed in a gray background

# SYNTAX \e[41m
#T# red background
echo -e "\e[41mtext1" # 'text1' is displayed in a red background

# SYNTAX \e[101m
#T# bright red background
echo -e "\e[101mtext1" # 'text1' is displayed in a bright red background

# SYNTAX \e[42m
#T# green background
echo -e "\e[42mtext1" # 'text1' is displayed in a green background

# SYNTAX \e[102m
#T# bright green background
echo -e "\e[102mtext1" # 'text1' is displayed in a bright green background

# SYNTAX \e[43m
#T# yellow (or orange) background
echo -e "\e[43mtext1" # 'text1' is displayed in a yellow background

# SYNTAX \e[103m
#T# bright yellow background
echo -e "\e[103mtext1" # 'text1' is displayed in a bright yellow background

# SYNTAX \e[44m
#T# blue background
echo -e "\e[44mtext1" # 'text1' is displayed in a blue background

# SYNTAX \e[104m
#T# bright blue background
echo -e "\e[104mtext1" # 'text1' is displayed in a bright blue background

# SYNTAX \e[45m
#T# magenta background
echo -e "\e[45mtext1" # 'text1' is displayed in a magenta background

# SYNTAX \e[105m
#T# bright magenta background
echo -e "\e[105mtext1" # 'text1' is displayed in a bright magenta background

# SYNTAX \e[46m
#T# cyan background
echo -e "\e[46mtext1" # 'text1' is displayed in a cyan background

# SYNTAX \e[106m
#T# bright cyan background
echo -e "\e[106mtext1" # 'text1' is displayed in a bright cyan background

# SYNTAX \e[47m
#T# white background
echo -e "\e[47mtext1" # 'text1' is displayed in a white background

# SYNTAX \e[107m
#T# bright white background
echo -e "\e[107mtext1" # 'text1' is displayed in a bright white background

# SYNTAX \e[49m
#T# default background color
echo -e "\e[44mtext1\e[49mtext2" # 'text1' is in a blue background, and 'text2' is displayed with the default background color

# SYNTAX \e[38;2;int1;int2;int3m
#T# this sets a 24 bit color for the text, int1 is an 8 bit number for the red color, int2 is an 8 bit number for the green color, and int3 is an 8 bit number for the blue color
echo -e "\e[38;2;32;75;223mtext1" # 'text1' is displayed in a heavily blue color

# SYNTAX \e[48;2;int1;int2;int3m
#T# this sets a 24 bit color for the background, int1 is an 8 bit number for the red color, int2 is an 8 bit number for the green color, and int3 is an 8 bit number for the blue color
echo -e "\e[48;2;114;106;24mtext1" # 'text1' is displayed in a yellow background between bright and dark

# SYNTAX \e[58;2;int1;int2;int3m
#T# this sets a 24 bit color for the underline, int1 is an 8 bit number for the red color, int2 is an 8 bit number for the green color, and int3 is an 8 bit number for the blue color
echo -e "\e[4m\e[58;2;74;239;81mtext1" # 'text1' is displayed with an underline of a soft green color

#T# a color palette can be created, which stores up to 256 colors, a syntax is needed to store a color in one of the 256 slots, and another syntax to use a color from the palette

# SYNTAX \e]4;int1;#six_hex1\a
#T# this stores a color into the color palette, int1 is the palette slot number (from 0 to 255), six_hex1 are six consecutive hexadecimal numbers that determine the color to be stored, first two are the red color byte, next tw are the green color byte, and last two are the blue color byte
echo -e "\e]4;27;#89A2CF\a" # this stores a desaturated blue in slot 27

# SYNTAX \e[38;5;int1m
#T# this sets the text color to be the one from the color palette indicated by int1
echo -e "\e[38;5;27mtext1" # 'text1' is displayed with the desaturated blue stored in slot 27 of the palette

# SYNTAX \e[48;5;int1m
#T# this sets the background color to be the one from the color palette indicated by int1
echo -e "\e[48;5;27mtext1" # 'text1' is displayed in a background colored with the desaturated blue stored in slot 27 of the palette

# SYNTAX \e[58;5;int1m
#T# this sets the underline color to be the one from the color palette indicated by int1
echo -e "\e[4m\e[58;5;27mtext1" # 'text1' is displayed with an underline colored with the desaturated blue stored in slot 27 of the palette

#T# several parts of the terminal can have their color modified using ANSI escape sequences

# SYNTAX \e]10;#six_hex1\a
#T# this sets the terminal foreground color (chars with default color, and the cursor), the new color is specified by six_hex1 as stated before
echo -e "\e]10;#C7B94A\a" # the text and cursor turn to a light yellow color

# SYNTAX \e]11;#six_hex1\a
#T# this sets the terminal background color, the new color is specified by six_hex1 as stated before
echo -e "\e]11;#DF79B8\a" # the terminal background becomes a pinkish color

# SYNTAX \e]12;#six_hex1\a
#T# this sets the cursor color, the new color is specified by six_hex1 as stated before
echo -e "\e]12;#1322DF\a" # the cursor turns soft blue
# |-----

# |-------------------------------------------------------------

#C# Shell session

# |-------------------------------------------------------------
#T# the env command outputs all the environment variables and their values
env # output too large

#T# to add an environment variable to the current shell session, the export command is used
export var1=75
#T# now var1 appears in the output of the env command
# |-------------------------------------------------------------