
#   System calls

#T# Table of contents

#C# Basic system calls
#C# File input output
#C# --- Piping and redirection
#C# File manipulation
#C# Signal handling

#T# Beginning of content

#C# Basic system calls

# |-------------------------------------------------------------
#T# the sleep command suspends the execution of the script or program for a given time in secods
sleep 3 # suspends the execution for 3 seconds

#T# the exit command serves to quit the current script or interpreter session, the number after it is the exit status
exit 0
# |-------------------------------------------------------------

#C# File input output

# |-------------------------------------------------------------
#T# several commands can read files that are readable to the current user, but most of the file input output is done through piping and redirection

#T# the nl command reads the content of a file a numbers its lines
nl file1 # outputs the contents of file1 with numbered lines

#C# --- Piping and redirection

# |-----

# |--------------------------------------------------\
#T# piping uses the vertical bar |, it serves to send the output of the command to the left of | to the input of the command to the right of |

#T# several commands connected with pipes form a pipeline, and each command in the pipeline is executed in a subshell

# SYNTAX command1 | command2 | command3
#T# the output of command1 becomes the input of command2, the output of command2 becomes the input of command3, and so on up to commandN

echo "value1" | cat # value1
echo "value2" | read var1
echo $var1 # value2 # this only works with the lastpipe shell option (see S1_14_Interpreter.sh), otherwise var1 is read in a subshell

# SYNTAX command1 |& command2
#T# this sends both the output and the errors from command1 as input for command2, up to commandN

ls no_file1 |& read var1
echo $var1 # ls: cannot access 'no_file1': No such file or directory # this only works with the lastpipe shell option (see S1_14_Interpreter.sh)
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# redirection is made to change the input source to a command and/or the output destination from a command

#T# file descriptors are necessary for redirection, 0 is standard input, 1 is standard output, 2 is standard error, 3 or more can be used for common files, in the following fd stands for file descriptor

#T# file descriptors 0 and 1, can be left out of the commands since they are the default values for input and output file descriptors

# SYNTAX command1 fd1>file1
#T# this redirects the output of fd1 of command1 to file1, overwriting its content

echo "string1" 1>file1
cat file1 # string1
ls no_file1 2>file1
cat file1 # ls: cannot access 'no_file1': No such file or directory

# SYNTAX command1 fd1>>file1
#T# this redirects the output of fd1 of command1 to file1, appending the output at the end of the file

echo "appended_string1" 1>>file1
cat file1
#T# the former prints (if this is the content of file1)
# string1
# appended_string1

# SYNTAX command1 &>file1
# SYNTAX command1 &>>file1
#T# same as before, but the ampersand & serves to redirect both the output and the errors (file descriptors 1 and 2) from command1 to file1

ls file1 &>file1
ls no_file1 &>>file1
cat file1
#T# the former prints
# file1
# ls: cannot access 'no_file1': No such file or directory

# SYNTAX command1 fd1>&fd2
#T# this redirects the output of fd1 of command1 to fd2

ls no_file1 1>file1 2>&1
cat file1 # ls: cannot access 'no_file1': No such file or directory

# SYNTAX command1 fd1>|file1
#T# this redirects the output of fd1 of command1 to file1, even if overwriting is prohibited (see S1_14_Interpreter.sh)

set -C
echo "can't overwrite" 1>|file1
cat file1 # can't overwrite
set +C

# SYNTAX command1 fd1<file1
#T# this redirects the content of file1 to the input of fd1

cat file1 # first string
grep 'str' 0<file1 # first string # 'str' is highlighted

# SYNTAX exec fd1<>file1
#T# this opens file1 with the file descriptor fd1 (greater than 2), in read '<' and write '>' mode, other modes can be achieved by deleting '<' or '>'

exec 149<>file1
echo "string to file1" 1>&149
cat file1 # string to file1

# SYNTAX exec {var1}<>file1
#T# same as before, but this creates a file descriptor, and assigns its integer value to var1
# SYNTAX command1 fd1>&$var1
#T# this redirects the output of fd1 of command1 to the file descriptor stored in var1

exec {var1}<>file1
echo "fd in var1 is $var1" 1>&$var1
cat file1 # fd in var1 is 19

# SYNTAX exec fd1<&-
# SYNTAX exec {var1}<&-
#T# this closes fd1 or the file descriptor stored in var1, for read '<' mode
# SYNTAX exec fd1>&-
# SYNTAX exec {var1}>&-
#T# this closes fd1 or the file descriptor stored in var1, for write '>' mode

exec {var1}<&-
exec {var1}>&-
echo "string1" 1>&$var1 # bash: $var1: Bad file descriptor
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# a special construct with redirections allows using the while loop to read a file line by line, for this, the file is passed to the input of the read command inside the while loop

# SYNTAX while read -r line1; do statements1; done < file1
# SYNTAX 
# |--------------------------------------------------/

# |-----

# |-------------------------------------------------------------



# the syntax to read a file line by line 'while read -r line1; do echo $line1; done < file1', or 'file1 output | while read line1...'



# trapping operating system signals, trap -l (lists the operating system signals)

#T# job control for foreground and background processes, ampersand & (and the coproc keyword) to start an asynchronous script or command as a background process vs semicolon ; to start processes synchronously, the vertical line | pipes the output of a command as input of another
# && and || in piping commands