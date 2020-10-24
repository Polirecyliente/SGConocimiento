
#   Interpreter

#T# Table of contents

#C# Interpreter customization
#C# --- Interpreter options

#T# Beginning of content

#C# Interpreter customization

# |-------------------------------------------------------------

#C# --- Interpreter options

# |-----
#T# the interpreter can have several options set at the start

# SYNTAX python3 -o1
#T# this must be executed outside Python, in the operating system shell, o1 is the flag being turned on, the flags that modify the options of the interpreter are set before starting it, python3 is the Python interpreter

#T# there are several flags used for different options
#T#     -v, print the initialized modules and their file location
#T#     -vv, like -v, but also print a message for each file checked when searching a module

#T# others are options (or kwargs)
#T#     -m script1, searches for script1.py in the environment path and executes it, taking the remaining tokens as arguments
# |-----

# |-------------------------------------------------------------