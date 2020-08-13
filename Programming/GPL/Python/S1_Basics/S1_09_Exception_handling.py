
#   Exception handling

#T# Table of contents

#T# Assertions
#T# Catching exceptions
#T# Throwing exceptions

#T# Beginning of content

#T# Assertions

int1 = 5
#T# make assertions with the assert keyword
# assert condition1, "assertion_error_string1"
#T# if condition1 returns False then an AssertionError is raised with the error string being "assertion_error_string1"
assert int1 == 5, "Either this file or the Python interpreter is corrupted"

#T# Catching exceptions

import traceback

int1 = int(input("Enter int1\n"))
#T# try except else statement
# try:
#     statements1
# except (Error1, Error2) as alias1:
#     statements2
# else:
#     statements3
#T# the statements1 are executed, if within the statements1 an exception is raised of the types Error1, or Error2, then statements2 are executed as a handling mechanism. In statements2 the error can be studied through alias1 which points to either Error1, or Error2. If no exceptions are raised during the execution of statements1 then statements3 are executed
try:
    assert (int1 >= 0), "int1 must be a positive integer"
except (AssertionError,IOError) as e1:
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
#T# if the input is less than zero then int1 == 7, otherwise int1 is twice the input

#T# try except finally statement
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
#T# int2 == 50

#T# Throwing exceptions

#T# to throw, or raise from now on, an exception the raise keyword is used
# raise ObjectError
#T# the ObjectError is the exception being raised
raise BrokenPipeError