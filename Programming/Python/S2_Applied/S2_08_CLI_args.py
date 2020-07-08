#!/usr/bin/python3
#   CLI args

#T# import the sys module to be able to use command line args
import sys

#T# import the getopt module to parse flags or options
import getopt

#T# get the args with sys.argv
argvMain = sys.argv[1:]
#T# the getopt method only works if the script name is skipped in argv therefore argvMain skips the argument zero

try:
#T# the getopt syntax is getopt(argv,"shortOpts",["longOp1","longOp2"]), if a short option requires a value add :, if its a long one add =, getopt returns first a list of tuples with the options. Each tuple, stores the option and its value pair, and tuples are listed. The function getopt returns second a list with the rest of arguments, this list starts after the last option value pair (even if there are more options they will be considered arguments)
    optsRet, argsRet = \
getopt.getopt(argvMain,"ha:b",["help","optionA=","optionB"])

#T# catch getopt errors with the GetoptError exception, alias the exception with the as keyword
except getopt.GetoptError as err1:

#T# get the exception's message and wrong option with msg and opt
    print("the error message is:",err1.msg)
    print("the wrong option is:",err1.opt)
    sys.exit(2)

#T# access options and their values, take action according to each option
for opt,val in optsRet:
    if opt == '-h' or opt == '--help':
        print("This is the help feedback")
    elif opt == '-b' or opt == '--optionB':
        print("This is the option B")
    elif opt == '-a' or opt == '--optionA':
        valInScript = val
        print("Value of option a is:",valInScript)

i = 1
#T# access the rest of the arguments
for argScript in argsRet:
    print("Argument",i,"is",argScript)
    i = i+1