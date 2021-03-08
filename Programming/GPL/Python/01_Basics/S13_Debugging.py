
#   Debugging

#T# Table of contents

#C# Python debugger (pdb)

#T# Beginning of content

#C# Python debugger (pdb)

# |-------------------------------------------------------------
#T# pdb is the builtin Python debugger, it has breakpoints, stepping through the code, printing the values of variables, post-mortem debugging, debugging of modules, functions, scripts, among other features

#T# pdb can be executed with an script argument to debug said script, the following syntax is done in the operating system shell
# SYNTAX python3 -m pdb script1.py
#T# python3 is the Python executable, -m pdb script1.py runs pdb to debug script1.py (see S14_Interpreter.py), this automatically enters post-mortem if script1 crashes

#T# the pdb module is imported to use the pdb debugger as part of a script
import pdb

#T# the run function of the pdb module allows debugging the execution of a Python string

# SYNTAX pdb.run('string1')
#T# the pdb debugger is started right before the execution of string1, and is used to debug whatever string1 executes

pdb.run('import S01_Basic_syntax') # this debugs the S01_Basic_syntax.py file, because the import statement executes the imported module

#T# the following code is used to show the syntax of the pdb debugger in its interactive mode
output_var1 = "help variable to show the different output of the pdb debugger"
var1 = [5, 2, 3]
var2 = 7
def func1(num1, num2):
    num3 = num1 + num2
    print("func1_string1")
    return num3
def func2():
    func1(var1[0], var1[2])
    loc1 = 72
    for i1 in [1, 2, 3]:
        print("i1 is", i1)
func2()

#T# create a breakpoint with the breakpoint function, this starts the (Pdb) interpreter to do interactive debugging
breakpoint()

# |--------------------------------------------------\
#T# the following syntaxes are written in the pdb debugger language, so they can't be written outside of a comment because they are not valid Python syntax and this .py file would show errors in an IDE (IDE stands for Integrated Development Environment)

#T# the 'output_var1' variable used in the following is used as a helper to signal and display the output of the pdb debugger commands

#T# the pdb debugger prompt is (Pdb), so anything shown after a (Pdb) means that it was typed in said prompt, e.g. '(Pdb) prompt_typings1' prompt_typings1 was typed directly in the pdb debugger prompt

#T# when source code is printed, the current line is shown with '->' after the line number

# SYNTAX next
#T# the next command executes code up to the next line of code (not entering functions)
output_var1 # (Pdb) next # this shows output of the script or program under debugging

# SYNTAX step
#T# the step command steps into functions or the next line
output_var1 # (Pdb) step # this shows output of the script or program under debugging, possibly inside a function

# SYNTAX continue
#T# the continue command continues execution until a breakpoint is found
output_var1 # (Pdb) continue # this shows output of the script or program under debugging, up to the next breakpoint or the end of the file

# SYNTAX until int1
#T# the until command continues execution until a line of number int1 or greater is reached, without int1 it continues until the next bigger line number
output_var1 # (Pdb) until # this shows output of the script or program under debugging, up to the next bigger line number

# SYNTAX return
#T# the return command continues execution until arriving at the return keyword of the current function, so this is used inside functions
output_var1 # (Pdb) return # inside a function, this shows output of the script or program under debugging, up to the return keyword of the current function

# SYNTAX run
# SYNTAX restart
#T# the run command and its alias the restart command restart the script or program under debugging, preserving the options and created breakpoints
output_var1 # (Pdb) restart # the script or program restarts

# SYNTAX p var1
#T# the p command (for print) prints the value of var1, if the name var1 is defined, this syntax is an alias for print(var1)
output_var1 # (Pdb) p var1      # [5, 2, 3]
output_var1 # (Pdb) print(var1) # [5, 2, 3]

# SYNTAX p func1
#T# same as before, but when used with a function, its address is printed
output_var1 # (Pdb) p func1 # <function func1 at 0x7f35210401f0> # or similar

# SYNTAX p func1(arg1, arg2)
#T# same as before, but this prints any output from func1 and its return value using arg1, arg2 as arguments, and any other arguments present
output_var1 # (Pdb) p func1(2, 3)
#T# the former prints
# func1_string1
# 5

# SYNTAX args
#T# the args command displays the arguments passed to a function
output_var1 # (Pdb) args # inside func1(5, 3)
#T# the former prints 
# num1 = 5
# num2 = 3

# SYNTAX display var1
#T# the display command prints a variable each time it changes

# SYNTAX undisplay var1
#T# stop displaying a variable var1 with the undisplay command

# SYNTAX l int1
#T# the l command lists 11 source code lines, this is done around line int1, 5 lines above and 5 lines below it, this syntax is an alias for list int1
output_var1 # (Pdb) l 7 # (Pdb) list 7
#T# the former prints
#  2  	#   Debugging
#  3  	
#  4  	#T# Table of contents
#  5  	
#  6  	#C# Python debugger (pdb)
#  7  	
#  8  	#T# Beginning of content
#  9  	
# 10  	#C# Python debugger (pdb)
# 11  	
# 12  	# |-------------------------------------------------------------

# SYNTAX l .
#T# same as before, but list source code lines around the current line
output_var1 # (Pdb) l . # this prints similar as before

# SYNTAX ll
#T# the ll commands does a long list of the source code local to the current line
output_var1 # (Pdb) ll # the output is too large to put here, more than 150 lines

# SYNTAX break
#T# the break command alone displays all breakpoints
output_var1 # (Pdb) break # with two breakpoints already created
#T# the former prints
# Num Type         Disp Enb   Where
# 1   breakpoint   keep yes   at /path/to/S13_Debugging.py:20
# 2   breakpoint   keep yes   at /path/to/S13_Debugging.py:35
# 	      stop only if var2 < 10

# SYNTAX break file1:int1
#T# the break command is used to create breakpoints in file1 (the current python script name without the .py extension), in line int1
output_var1 # (Pdb) break S13_Debugging:20 # Breakpoint 1 at /path/to/S13_Debugging.py:20

# SYNTAX break file1.func1, condition1
#T# same as before, but the breakpoint is created in the first line of func1 (its def line), and the breakpoint only activates if condition1 evaluates to True using Python boolean syntax
output_var1 # (Pdb) break S13_Debugging.func1, var2 < 10 # Breakpoint 2 at /path/to/S13_Debugging.py:35

# SYNTAX disable int1
#T# the disable command disables the breakpoint numbered with the number int1
output_var1 # (Pdb) disable 1 # Disabled breakpoint 1 at /path/to/S13_Debugging.py:20

# SYNTAX enable int1
#T# the enable command enables the breakpoint numbered with the number int1
output_var1 # (Pdb) enable 1 # Enabled breakpoint 1 at /path/to/S13_Debugging.py:20

# SYNTAX clear int1
#T# the clear command completely deletes a breakpoint
output_var1 # (Pdb) clear 1 # Deleted breakpoint 1 at /path/to/S13_Debugging.py:20

# SYNTAX where
#T# the where command prints the stack_frame trace
output_var1 # (Pdb) where
#T# the former prints
#  /path/to/S13_Debugging.py(46)<module>()
#-> func2()
#  /path/to/S13_Debugging.py(42)func2()
#-> func1(var1[0], var1[2])
#> /path/to/S13_Debugging.py(40)func1()->8
#-> return num3

# SYNTAX up int1
#T# the up command goes up to an older frame in the stack trace, the amount of frames that go up is int1
output_var1 # (Pdb) up 1
#T# the former prints
#> /path/to/S13_Debugging.py(42)func2()
#-> func1(var1[0], var1[2])

# SYNTAX down int1
#T# the down command goes down to a newer frame in the stack trace, the amount of frames that go down is int1
output_var1 # (Pdb) down 1 # *** Newest frame # this is the output at the lowest frame

# SYNTAX help
#T# print the debugger pdb help with the help command

# SYNTAX quit
#T# quit the debugger with the quit command
# |--------------------------------------------------/

# |-------------------------------------------------------------