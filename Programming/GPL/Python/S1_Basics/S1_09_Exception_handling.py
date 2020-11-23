
#   Exception handling

#T# Table of contents

#C# Assertions
#C# Catching exceptions
#C# Throwing exceptions
#C# Context managers

#T# Beginning of content

#C# Assertions

# |-------------------------------------------------------------
#T# make assertions with the assert keyword

# SYNTAX assert condition1, "assertion_error_string1"
#T# if condition1 returns False then an AssertionError is raised with the error string being "assertion_error_string1"

int1 = 5
assert int1 == 5, "Either this file or the Python interpreter is corrupted"
# |-------------------------------------------------------------

#C# Catching exceptions

# |-------------------------------------------------------------
import traceback

# |--------------------------------------------------\
#T# exception handling with the try, except, else keywords

# SYNTAX try, except, else
# try:
#     statements1
# except (Error1, Error2) as alias1:
#     statements2
# else:
#     statements3
#T# the statements1 are executed, if within the statements1 an exception is raised of the types Error1, or Error2, then statements2 are executed as a handling mechanism

#T# in statements2, the error can be studied through alias1 which points to either Error1, or Error2

#T# if no exceptions are raised during the execution of statements1 then statements3 are executed

int1 = int(input("Enter int1\n"))
try:
    assert (int1 >= 0), "int1 must be a positive integer"
except (AssertionError, IOError) as e1:
    int1 = 7
    str1 = repr(e1) # "AssertionError('int1 must be a positive integer')"

#T# the print_exc function prints the traceback of the exception in a summarized manner
    traceback.print_exc()
#T# this prints the following
# Traceback (most recent call last):
#   File "S1_09_Exception_handling.py", line 34, in <module>
#     assert (int1 >= 0), "int1 must be a positive integer"
# AssertionError: int1 must be a positive integer

else:
    int1 *= 2
# int1 == 7 if the input is less than zero then, otherwise int1 is twice the input
# |--------------------------------------------------/

#T# exception handling with the try, except, finally keywords

# SYNTAX try, except, finally
# try:
#     statements1
# except Error1, Error2:
#     statements2
# finally:
#     statements3
#T# the statements1 are executed, if within the statements1 an exception is raised of the types Error1, or Error2, then statements2 are executed as a handling mechanism. The statements3 are executed in any and all cases

try:
    assert int1 == 7, "int1 has to be 7"
except AssertionError:
    int1 = 97
finally:
    int2 = 50
# int2 == 50
# |-------------------------------------------------------------

#C# Throwing exceptions

# |-------------------------------------------------------------
#T# to throw (or raise from now on) an exception, the raise keyword is used

# SYNTAX raise ObjectError
#T# the ObjectError is the exception being raised

raise BrokenPipeError
# |-------------------------------------------------------------

#C# Context managers

# |-------------------------------------------------------------
#T# a context manager gives a context for operations, so that by executing one of them, others execute in turn, no need to execute them directly

#T# the with keyword allows the use of an object in a context manager

# SYNTAX with
# with context_obj1 as alias1
#     statements1
#T# the context_obj1 is the object that has the context manager, it can have an alias alias1, if a statement in statements1 operates on context_obj1 then any other related statements will execute in turn, without writing them

#T# the with syntax can be used on file handles, because the text IO wrapper objects have a context manager, so that the open operation causes the close operation to execute later
with open("/tmp/file1", "r") as textIOWrapper1:
    textIOWrapper1.read(2)
#T# after this statement the file is closed, even if an exception is raised
# |-------------------------------------------------------------