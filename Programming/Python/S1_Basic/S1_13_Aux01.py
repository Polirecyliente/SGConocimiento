#!/usr/bin/python3
#   More on modules, and scope

#T# import statement
import S1_13_Modules

#T# an import statement is executed from the level of the file in execution, so a file buried in the hierarchy can import a file in another branch, this branch file is imported using the path relative to the executing file

print("In common file")

#T# call module's function
S1_13_Modules.modFun1()

#T# from module import statement
from S1_12_Functions import fun1
retV = fun1(7)
print("return val of imported function",retV)

#T# see location of module with __file__
import calendar
print(calendar.__file__)

var1 = 5
#T# global scope to emulate by ref in functions with global, get dict of local names with locals() and global ones with globals()
def pFun1():
    loc1 = 5; oL2 = 7; mVar3 = 9
    global var1
    var1 = 7
    print("local names:",locals(),"\nglobal names:",globals())
    return 3 * (loc1 + oL2 + mVar3)

pFun1()
print("var1 after function:",var1)

#T# list the names in a namespace with dir()
print("names from Section1_13\n",dir(Section1_13))
print("names from calendar\n",dir(calendar))

import importlib
#T# execute a module again with reload()
importlib.reload(S1_13_Modules)

#T# import a package from a folder with a __init__.py file
import package1Aux
var2 = package1Aux.fun1(12)
print("value from package:",var2)