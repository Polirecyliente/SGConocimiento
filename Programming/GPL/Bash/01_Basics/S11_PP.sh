
#   PP

#T# Table of contents

#C# Procedures
#C# --- Interaction between procedures

#T# Beginning of content

# |-------------------------------------------------------------
#T# PP stands for Procedural Programming
# |-------------------------------------------------------------

#C# Procedures

# |-------------------------------------------------------------
#T# procedures are code that can be called, executes a set of instructions, receives input via arguments, and sends output via a return value and direct output to stdout

#T# in Bash, procedures are created with functions
func1() { var1=57; echo "var1 is $var1"; }
func1

#C# --- Interaction between procedures

# |-----
#T# procedures can interact to change the general state of the program, they can be called from within each other, or interact through variables
func2() { echo "here var1 is $var1"; var1=68; echo "now var1 is $var1"; }
func2
# |-----

# |-------------------------------------------------------------