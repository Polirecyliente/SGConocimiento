
#   System calls

#T# Table of contents

#T# Basic system calls
#T# File input output
#T# File manipulation
#T# Signal handling

#T# Beginning of content

#T# Basic system calls

# |-------------------------------------------------------------
import time

#T# the sleep function suspends the execution of the program for a given time in seconds
time.sleep(0.3) # None

#T# terminate the script with the quit function
# SYNTAX quit()
quit()
# |-------------------------------------------------------------

#T# File input output

# |-------------------------------------------------------------
str1 = "/tmp/SGC_Programming_GPL_Python_S1_file1"
#T# the contents of this example file should be
# üüüüü

# |--------------------------------------------------\
#T# the open function is used to open a file, or create it if it doesn't exist, it returns a TextIOWrapper object

# SYNTAX open("/path/to/file1", "mode1")
#T# the "/path/to/file1" is a string with the file path in the file system hierarchy

#T# the "mode1" is the mode in which the file is opened, and can be one of several values
#T#     "x"     create file mode
#T#     "r[b+]" read mode
#T#     "w[b+]" write mode
#T#     "a[b+]" append mode
#T# the [b+] are optional characters, b is for operating in bytes instead of chars, + is for extending the mode so r+ means read and write, w+ means write and read, a+ is append and read

#T# the file is opened with the context manager of the TextIOWrapper object returned by the open function, using the with keyword
list1 = []
with open(str1, "r") as textIOWrapper1:
    while (chars1 := textIOWrapper1.read(2)):
        list1.append(chars1)
# list1 == ['üü', 'üü', 'ü\n']

list1 = []
with open(str1, "rb") as textIOWrapper1:
    while (byte1 := textIOWrapper1.read(2)):
        list1.append(byte1)
# list1 == [b'\xc3\xbc', b'\xc3\xbc', b'\xc3\xbc', b'\xc3\xbc', b'\xc3\xbc', b'\n']
# |--------------------------------------------------/

#T# the name attribute of a TextIOWrapper object has the value of the file path in the file system hierarchy
str1 = textIOWrapper1.name # /tmp/SGC_Programming_GPL_Python_S1_file1

#T# the closed attribute of a TextIOWrapper object is a boolean that is True if the file is closed
bool1 = textIOWrapper1.closed # True

#T# the mode attribute of a TextIOWrapper object is a string with the mode with which the file is accessed
str1 = textIOWrapper1.mode # rb

#T# the write function serves to write characters, or bytes to a file
str1 = "/tmp/SGC_Programming_GPL_Python_S1_file1"
with open(str1, "a") as textIOWrapper1:
    textIOWrapper1.write("\u02A0")

#T# the tell function returns the cursor position in bytes
    int1 = textIOWrapper1.tell() # 13, from 10 of ü, 1 of \n, 2 of \u02A0

# |--------------------------------------------------\
#T# the seek function sets the cursor position in the file

# SYNTAX textIOWrapper1.seek(offset_int1, start_pos_int1)
#T# the offset_int1 is for the offset in bytes, it must be positive or zero

#T# the start_pos_int1 must have one of these values
#T#     0, start of the file
#T#     1, current cursor position, offset_int1 must be zero
#T#     2, end of the file

with open(str1, "r+") as textIOWrapper1:
    textIOWrapper1.seek(2, 0)
    textIOWrapper1.write("AB") # two bytes written to replace one 'ü'
# üABüüü\nʠ are the file contents
# |--------------------------------------------------/

#T# the close function is used to explicitly close a file
textIOWrapper1.close()
# |-------------------------------------------------------------

#T# File manipulation

# |-------------------------------------------------------------
#T# the os module allows file manipulation in the file system hierarchy
import os

#T# the rename function serves to rename a file
# SYNTAX os.rename("original_filename1", "new_filename1")
str2 = "/tmp/renamed_file1"
os.rename(str1, str2)

#T# the remove function serves to remove a file
os.remove(str2)

#T# the mkdir function serves to create a new directory
str1 = "/tmp/temporary_dir1"
os.mkdir(str1)

#T# the chdir function serves to change the current working directory for the directory of its argument
os.chdir(str1)

#T# the getcwd function returns the current working directory
str1 = os.getcwd() # /tmp/temporary_dir1

#T# the rmdir function serves to remove a directory
os.rmdir(str1)
# |-------------------------------------------------------------

#T# Signal handling

# |-------------------------------------------------------------
#T# the getpid function returns the pid of the caller
int1 = os.getpid() # 175344, or similar

#T# the signal module is used for signal handling, the two types of signals or interrupts are, maskable (can be ignored), and non maskable (cannot be ignored)
print("Waiting to receive a signal")
import signal

# |--------------------------------------------------\
#T# a signal handler is a callback function that is executed when a signal it handles is received

# SYNTAX signal handler
# def signal_handler_func1(signal_number1, signal_frame1):
#     statements1
#T# signal_number1 is an integer with the number of the signal, signal_frame1 is the stack frame where the signal was received

import traceback
def sig_handler1(sig_number, sig_frame):
    print("signal number is:", sig_number)
    traceback.print_stack(sig_frame)
    quit()
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# the signal function serves to register a signal handler so it executes when a given signal is received by the program

# SYNTAX signal.signal(signal.SIG1, signal_handler_func1)
#T# whenever the signal SIG1 is received, the function signal_handler_func1 will execute

signal.signal(signal.SIGHUP, sig_handler1)    # SIGHUP for hangup
signal.signal(signal.SIGINT, sig_handler1)    # SIGINT for interrupt
signal.signal(signal.SIGQUIT, sig_handler1)   # SIGQUIT for quit
signal.signal(signal.SIGILL, sig_handler1)    # SIGILL for illegal instruction
signal.signal(signal.SIGTRAP, sig_handler1)   # SIGTRAP for trap
signal.signal(signal.SIGABRT, sig_handler1)   # SIGABRT for abort
signal.signal(signal.SIGBUS, sig_handler1)    # SIGBUS for bus error
signal.signal(signal.SIGFPE, sig_handler1)    # SIGFPE for floating point error
signal.signal(signal.SIGUSR1, sig_handler1)   # SIGUSR1 for user defined 1
signal.signal(signal.SIGSEGV, sig_handler1)   # SIGSEGV for segment violation
signal.signal(signal.SIGUSR2, sig_handler1)   # SIGUSR2 for user defined 2
signal.signal(signal.SIGPIPE, sig_handler1)   # SIGPIPE for pipe error
signal.signal(signal.SIGALRM, sig_handler1)   # SIGALRM for alarm
signal.signal(signal.SIGTERM, signal.SIG_IGN) # SIGTERM for terminate, the SIG_IGN enum element serves to ignore the signal when received
#T# only the signal 9, signal.SIGKILL, can't be registered this way as it is a non maskable signal
# |--------------------------------------------------/

#T# the pause function pauses the execution until a signal is received
signal.pause()
# |-------------------------------------------------------------