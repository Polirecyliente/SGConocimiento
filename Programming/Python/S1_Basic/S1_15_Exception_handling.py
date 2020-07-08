#!/usr/bin/python3
#   Exception handling

var1 = 5
#T# make assertions with assert
assert (var1 >= 0),"var1 must not be less than zero"

#T# try except else statement
try:
    fh1 = open("/root/officeonlin-install.sh/loolwsd.cfg","a")
    fh1.write("writing this to file")
    print("This won't be printed")
except (IOError,RuntimeError):
    print("Can't access the file")
else:
    print("File accessed and information appended")

#T# try except finally statement
try:
    fh1 = open("/root/officeonlin-install.sh/loolwsd.cfg","a")
    fh1.write("another attempt to write")
except (IOError,RuntimeError):
    print("Can't access the file")
finally:
    print("This will be printed, exception or not")

class NewMeaninglessError(Exception):
    pass
var2 = 0
#T# throw or raise an exception with raise applied to exception object
def attemptFun(vF):
    if (vF < 1):
        raise NewMeaninglessError

attemptFun(var2)