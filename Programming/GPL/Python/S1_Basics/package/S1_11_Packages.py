
#   Packages

#T# Contents
#T# Modules

#T# Modules

#T# module's definitions
def modFun1():
    print("In module's function")
    return None

#T# code that will execute when the module is imported
print("In module")
modFun1()

#T# get help and documentation about a module with pydoc moduleName, execute pydoc from a terminal, NOT from this script
# pydoc itertools

#T# list all installed modules by entering the Python REPL (python3), and then with help("modules") in the Python interpreter

#T# show information about a module with the command pip3 show moduleName if it returns nothing the package is not installed
# pip3 show alabaster

#T# if the installation of a module gets timeout errors in the download, it may be fixed with the --default-timeout=1000 option
# pip3 install --default-timeout=1000 matplotlib