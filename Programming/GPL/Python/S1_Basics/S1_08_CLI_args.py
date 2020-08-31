
#   CLI args

#T# Table of contents

#T# Argparse

#T# Beginning of content

# |-------------------------------------------------------------
#T# execute this file with command line arguments: str2 5.4 -oCount -oCount
# |-------------------------------------------------------------

#T# Argparse

# |-------------------------------------------------------------
#T# manage command line arguments with the argparse module
import argparse

#T# create a parser object with the ArgumentParser constructor
parser1 = argparse.ArgumentParser()

# |--------------------------------------------------\
#T# the add_argument function adds command line arguments that the program will recognize

# SYNTAX parser1.add_argument("arg_name1", help = "help_string1", choices = list1, type = type1, action = "action1", default = val1)

#T# an argument named "arg_name1" is added to parser1, if "arg_name1" starts with a hyphen then it's an optional argument, otherwise it's positional, the value of "arg_name1" is the value entered in the CLI

#T# the help kwarg is for the help string "help_string1"
#T# the choices kwarg forces the value of "arg_name1" to be an element of list1
#T# the type kwarg ensures type1 to be the type of "arg_name1"

#T# the following kwargs are used with optional arguments

#T# the action kwarg has a few posible values for "action1"
#T#     if "action1" is "store_true" then "arg_name1" is a boolean flag, which becomes True with the presence of "arg_name1", and False with its absence
#T#     if "action1" is "count" then count the occurrences of "arg_name1", e.g. in -vvv the count is 3, or in -flag1 -flag1 the count is 2
#T# the default kwarg sets val1 as the default instead of None

#T# an optional argument can have a short and a large version, e.g. "-o", "--optional"

list1 = ['str1', 'str2']
parser1.add_argument("positional_arg1", help = "this is the first arg", choices = list1)
parser1.add_argument("positional_arg2", type = float)
parser1.add_argument("-f", "--flag1", action = "store_true")
parser1.add_argument("-oCount", action = "count", default = 0)
# |--------------------------------------------------/

#T# the parse_args function returns a Namespace object with the args and its values obtained from the CLI
args1 = parser1.parse_args() # Namespace(flag1 = False, oCount = 2, positional_arg1 = 'str2', positional_arg2 = 5.4)

#T# access the elements in a Namespace object using dot notation, as each argument name becomes an attribute of the Namespace object
arg1_value = args1.positional_arg1 # str2
oCount_value = args1.oCount # 2
# |-------------------------------------------------------------