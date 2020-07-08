#!/usr/bin/python3
#   pdb

#T# pdb is the Python debugger

a1 = [5,2,3]
#T# create a breakpoint with breakpoint()
breakpoint()
a2 = 7
def eofF1(nu1,nu2):
    nu3 = nu1+nu2
    print("EOFString")
def fun2():
    eofF1(a1[0],a1[2])
    loc2 = 72
    for i in [1,2,3]:
        print("i is",i)
fun2()

#T# print a variable's value with p (for print)
# p a1
#T# execute to the next line (not entering functions) with next
# next
# next
#T# a function address can be printed by printing its handle
# p eofF1
# next
#T# step into functions or next line with step
# step
#T# long list the local source code with ll
# ll
#T# list 11 source code lines around line n with l n
# l 3
#T# create a breakpoint with break file(:lineNum|.func),conditionToBreak
# break Section2_9:12
# break Section2_9.eofF1,a2 < 10
#T# display all breakpoints with break (alone)
# break
#T# disable a breakpoint with disable bpNum
# disable 1
#T# enable a breakpoint with enable bpNum
# enable 1
#T# completely delete a breakpoint with clear bpNum
# clear 1
#T# continue execution until a breakpoint is found with continue
# continue
#T# display the arguments passed to a function with args
# args
#T# get into loops only once by going to a greater lineNum with until
# until
#T# print a variable each time it changes with diplay var1
# display i
# display x
#T# stop displaying a variable with undisplay
# undisplay x
#T# print the stack_frame trace with where
# where
#T# go up to an older frame in the stack trace with up framesAmount
# up 1
#T# go down to a newer frame in the stack trace with down framesAmount
# down 1
#T# print the debugger pdb help with help
#T# quit the debugger with quit
# quit