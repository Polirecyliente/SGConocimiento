
#   Builds

#T# Table of contents

#C# Compiling to bytecode
#C# Building a project to binary

#T# Beginning of content

#C# Compiling to bytecode

# |-------------------------------------------------------------
#T# Python code is compiled from .py source code files, to .pyc bytecode files

#T# in the operating system shell, the py_compile script can be run to compile a .py file into .pyc
# SYNTAX python3 -m py_compile script1.py
#T# the script1.py is compiled, python3 is the Python executable, -m is a Python option to run py_compile (see the file titled Interpreter)

#T# the output file is stored in a directory named __pycache__/ under the directory of script1.py, named something like __pycache__/script1.cpython-38.pyc, the cpython-38 part of the name stands for the Python version, in this case version 3.8

#T# in the operating system shell, a compiled .pyc file can be executed like a source code script
# SYNTAX python3 __pycache__/script1.cpython-38.pyc
#T# python3 is the Python executable, this syntax executes script1.cpython-38.pyc which gives the same output as executing script1.py
# |-------------------------------------------------------------

#C# Building a project to binary

# |-------------------------------------------------------------
#T# a Python project is formed by several related Python files whose execution starts at a main file, a project can be built into a binary executable so that the whole project resides in a single file, which doesn't depend on the Python interpreter to be executed

#T# in the operating system shell, the PyInstaller module can be executed to build a Python project (it can be installed with pip)
# SYNTAX pyinstaller --onefile main1.py dir1/module1.py dir1/dir1_1/script1.py
#T# this creates an executable file named main1 in a directory under the working directory named dist/, so the executable file is dist/main1, the --onefile option makes it so that dist/ only contains one file

print("Built")
# |-------------------------------------------------------------