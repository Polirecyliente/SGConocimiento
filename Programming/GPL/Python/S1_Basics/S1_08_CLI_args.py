
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

#T# argparse

#T# command line arguments with argparse

#T# argparse is more complete and preferable to getopt
import argparse

#T# create a parser object to manage the parsing process with ArgumentParser()
parser = argparse.ArgumentParser()

#T# add recognized command line arguments with add_argument("argName"), in add_argument() you can include a help string, the type of the argument (e.g. float, int, str)
#T# use action="store_true" to make the arg a boolean flag, use choice=[] to make an argument have a list of valid choices, use action="count" to count occurrences of a flag, e.g. -vvv = 3, use default=val to set a default instead of None
parser.add_argument("posArg1",help="posArg1 is the string for the\
 positional argument 1",choices=['str1','st2','stringz'])
parser.add_argument("posArg2",help="posArg2 is the second argument,\
 it's a float number",type=float)
parser.add_argument("-f","--flag1",help="-f or --flag1 is a flag for\
 the program",action="store_true")
parser.add_argument("-o",help="count the o's",action="count",
    default=0)

#T# parse the arguments and store them in a Namespace object with parse_args()
args = parser.parse_args()