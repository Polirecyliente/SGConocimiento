
#   System calls

#T# Table of contents

#C# Basic system calls
#C# File input output
#C# --- Piping and redirection
#C# File manipulation
#C# Signal handling
#C# Multiprocessing
#C# --- Job control

#T# Beginning of content

#C# Basic system calls

# |-------------------------------------------------------------
#T# the sleep command suspends the execution of the script or program for a given time in seconds, or on another time unit given as suffix to the number

# SYNTAX sleep num1str1
#T# str1 is the time unit, it can be 's' for seconds, 'm' for minutes, 'h' for hours, 'd' for days, num1 is a number

sleep 3  #| suspends the execution for 3 seconds
sleep 5m #| suspends the execution for 5 minutes
sleep 2d #| suspends the execution for 2 days

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
echo $var1 # value2 # this only works with the lastpipe shell option (see S14_Interpreter.sh), otherwise var1 is read in a subshell

# SYNTAX command1 |& command2
#T# this sends both the output and the errors from command1 as input for command2, up to commandN

ls no_file1 |& read var1
echo $var1 # ls: cannot access 'no_file1': No such file or directory # this only works with the lastpipe shell option (see S14_Interpreter.sh)
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
#T# this redirects the output of fd1 of command1 to file1, even if overwriting is prohibited (see S14_Interpreter.sh)

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

#T# a special construct with redirections allows using the while loop to read a file line by line, for this, the file is passed to the input of the read command inside the while loop

# SYNTAX while read line1; do statements1; done 0<file1
# SYNTAX file1_output1 | while read line1; do statements1; done
#T# both syntaxes are equivalent, and in both of them the idea is about sending the contents of file1 to the input of the read command

while read line1; do echo $line1; sleep .5; done 0<file1
cat file1 | while read line1; do echo $line1; sleep .5; done
#T# the former both print (if these are the contents of file1)
# first line
# second line
# current final line

#T# a named pipe can be created with the mkfifo command, it's a file that works like the vertical bar | pipe, but with input and output redirections
mkfifo pipe1
ls -l 1>pipe1 &
cat 0<pipe1
#T# the former prints
# -rw-rw---- 2 jul jul     42 nov  3 18:12 file1
# -rw-rw---- 1 jul jul      4 oct 22 21:39 file2
# -rw-rw---- 2 jul jul     42 nov  3 18:12 file3
# drwxrwx--- 3 jul jul   4096 oct 11 17:17 dir1
# prw-rw---- 1 jul jul      0 nov  4 11:14 pipe1
# [1]+  Done                    ls --color=auto -l > pipe1
# |-----

# |-------------------------------------------------------------

#C# File manipulation

# |-------------------------------------------------------------
#T# create an empty file with the touch command
touch file1

#T# rename and move a file with the mv command
# SYNTAX mv /path/to/original/file1 /path/to/renamed_or_moved/file1
mv file1 new/path/renamed_file1

#T# remove a file with the rm command
rm file1

#T# create an empty directory with the mkdir command
mkdir dir1

#T# change the working directory with the cd command
cd dir1

#T# print the working directory with the pwd command
pwd
# |-------------------------------------------------------------

#C# Signal handling

# |-------------------------------------------------------------
#T# there are several operating system signals that can be handled with traps (see S09_Exception_handling)

#T# the -l flag of the trap command lists the operating system signals
trap -l # the system signals are the output

#T# handling operating system signals follows the same rules as exception handling

# SYNTAX trap "command1" signal1 signal2
# SYNTAX trap "command1" int1 int2
#T# both syntaxes are equivalent, command1 is the signal handler, signal1, signal2, up to signalN, are the signals being handled, when executing trap -l each signal has a integer associated, this integer can be used to identify the signal to be handled, such as int1, int2, up to intN

signal_handler1() { echo -e "\noperating system signal handled"; }
trap signal_handler1 SIGINT
trap signal_handler1 2
#T# both commands make signal_handler1 handle the interrumpt signal
# |-------------------------------------------------------------

#C# Multiprocessing

# |-------------------------------------------------------------

#C# --- Job control

# |-----
#T# the jobs command prints the current jobs
jobs
#T# the former prints this jobs table (with gedit, firefox, and sleep opened in the backgroung)
# [2]   Running                 gedit &
# [3]-  Done                    firefox
# [4]+  Running                 sleep 10000 &
#T# particular jobs can be identified inside commands by using the percent sign % followed by the job number (the one inside the brackets)

#T# a command can be started in the background by ending it with an ampersand &
gedit &
firefox &
sleep &
#T# this order of commands was used to create the former jobs table

#T# the fg command serves to bring a job to the foreground

# SYNTAX fg %int1
# SYNTAX fg %?substring1
#T# int1 is the number of the job as seen in the table of the jobs command inside brackets, substring1 is any substring inside the command of the job

fg %4    # sleep 10000
fg %?lee # sleep 10000

#T# the bg command serves to send a job to the background

# SYNTAX bg %int
# SYNTAX bg %?substring1
#T# same as before (see the fg command)

bg %4    # [4]+ sleep 10000 & # assuming that job 4 was stopped before
bg %?lee # [4]+ sleep 10000 &

# SYNTAX job_control_command1 %%
# SYNTAX job_control_command1 %+
#T# this applies job_control_command1 (such as fg, bg, etcetera) to the current job, the current job is noted in the jobs table with a plus sign + after the job number in brackets

fg %% # sleep 10000
bg %+ # [4]+ sleep 10000 &

# SYNTAX job_control_command1 %-
#T# same as before, but here job_control_command1 is applied to the previous job, the previous job is noted in the jobs table with a minus sign - after the job number in brackets

fg %- # gedit

# SYNTAX disown %job1
#T# the disown command makes the background job1 independent from the shell, job1 can be identified in any of the shown was (an integer, a substring, through the current job %%, etc.)

disown %4

#T# jobs can be stopped with the suspend character CTRL-Z (or ^Z)
# |-----

#T# using job control, multiprocessing is made straightforward

# SYNTAX multiprocessing
# command1 &
# command2 &
# wait
#T# this runs command1, up to commandN, in the background in parallel, the wait command is used to wait until all background processes end

sleep 50 &
gedit &
wait #| the prompt returns after 50 seconds and after closing gedit
# |-------------------------------------------------------------