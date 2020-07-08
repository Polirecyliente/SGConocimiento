#!/usr/bin/python3
#   argparse

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