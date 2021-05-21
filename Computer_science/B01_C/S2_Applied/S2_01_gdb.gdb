
#   gdb

#T# GNU Debugger

#T# commands in bash

#T# compile a file with debugging information with the -g flag
# gcc -g sourceFile.c -o execFile

#T# execute the interactive debugger with gdb filename
# gdb section2Debug

#T# commands in gdb

#T# execute a batch gdb file with
# gdb -batch -x=file1.gdb exec1 > log1
#T# where the kwarg -x specifies the script file, exec1 is the executable to debug, and log1 is the file where the results will be written to

#T# create a breakpoint with break fun1, or with break filename:linenumber
break main
# break sourceFile.c:48

#T# bpNumber stands for breakpoint number
#T# delete a breakpoint with del bpNumber
# del 1
#T# disable a breakpoint with dis bpNumber
# dis 1
#T# enable a breakpoint with en bpNumber
# en 1
#T# ignore a breakpoint until it's crossed N1 times with ignore bpNumber N1
# ignore 1 5

#T# run the executable under debugging with run
run

#T# go to the next line with next
next

#T# get info on many aspects with info topic, e.g. get the addresses and values in all registers with info all-registers
# info all-registers
#T# get the list of topics with available info with
info

#T# step into the next line or function with step
step

#T# print the value of a variable with print varName
print i1

#T# see the byte contents in a memory address with x/(size)x(for hex)b(byte)
x/4xb &i1

#T# change a variable's value with set var
set var i1 = 12

#T# set the starting command line arguments with set args -param1 arg2
# set args -o "3*2"

next
#T# get the type of anything with ptype
ptype arr1

#T# print 20 lines of source code around with 
list

#T# execute the remaining lines with
continue

#T# disassemble the program to see the assembly code with 
disassemble

#T# go to the next assembly instruction with
# nexti

#T# step into an assembly function call or next instruction with
# stepi

#T# print the value in an address from register with x/d $regName+0xOffset
# x/d $rsp+0x0

#T# quit gdb with quit
quit