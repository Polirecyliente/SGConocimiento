
#   Packages

#T# Table of contents

#T# Importing modules
#T# Using modules
#T# Importing packages
#T# Info about modules

#T# Beginning of content

#T# Importing modules

# |-------------------------------------------------------------
#T# the import keyword imports a package or module to use its code in this file
import S1_10_P_Module_example

# |--------------------------------------------------\
#T# an import statement is executed from the level of the file in execution, so a file down in the hierarchy can import a file in another branch

# SYNTAX file system hierarchy
# package1
# -- main.py
# -- subpackage1
# -- -- subp1_module1.py
# -- subpackage2
# -- -- subp2_module1.py

#T# the file subp2_module1.py imports subp1_module1.py with the following

# SYNTAX import subpackage1.subp1_module1
#T# this path is the same as seen from main.py
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# specific functions, and classes from a module can be imported, without importing the rest of the module

# SYNTAX from module1 import func1 as alias1
#T# this imports only func1 from module1 into the namespace of this file with the alias alias1

from S1_06_Functions import func1 as f1
# |--------------------------------------------------/

import importlib
#T# execute a module again with the reload function
importlib.reload(S1_10_P_Module_example)
# |-------------------------------------------------------------

#T# Using modules

# |-------------------------------------------------------------
#T# call module's function
int1 = S1_10_P_Module_example.func1() # 56 # func1() returns 56

int1 = f1(7) # 53 # f1(arg1) returns 53
# |-------------------------------------------------------------

#T# Importing packages

# |-------------------------------------------------------------
#T# import a package, which is a directory with an __init__.py file, when the package is imported the __init__.py file is executed
import package
int1 = package.anon_func1(8, -5) # 50
# |-------------------------------------------------------------

#T# Info about modules

# |-------------------------------------------------------------
import math
#T# the help function prints to stdout the generated help for its module argument
help(math)

#T# an special argument to the help function is "modules" which lists the installed modules
help("modules")

#T# the __file__ attribute of a module contains its location in the system, and if it has no file then the module is possibly builtin
str1 = importlib.__file__ # /usr/lib/python3.8/importlib/__init__.py
# |-------------------------------------------------------------