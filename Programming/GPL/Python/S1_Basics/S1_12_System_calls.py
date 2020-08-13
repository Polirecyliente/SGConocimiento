
#   System calls

#T# Table of contents

#T# Input output

#T# Process control

#T# Signal handling

#T# File management

#T# Beginning of content

#T# Input output

loc1 = "/home/jul/PolirecylBases/tutos/Python/Section1/Section1_14Debug"
#T# open a file with open()
fileh1 = open(loc1,"a+",1)
print("name:",fileh1.name,"closed?:",fileh1.closed,"mode:",fileh1.mode)

#T# write to a file with write()
fileh1.write("foto\nsintatos\n")

#T# get cursor position in file with tell()
print("cursor at",fileh1.tell())

#T# set cursor position in file with seek()
fileh1.seek(0,0)

#T# read a file with read()
strFromF1 = fileh1.read(100)
print("content read from file:",strFromF1)

#T# close a file with close()
fileh1.close()

#T# the os module allows other file manipulation
import os

newN = "/home/jul/PolirecylBases/tutos/Python/Section1/Section1_14New"
#T# rename a file with rename()
os.rename(loc1,newN)

#T# delete a file with remove()
os.remove(newN)

nDir = "/home/jul/PolirecylBases/tutos/Python/Section1/dirDebug"
#T# create a new directory with mkdir()
os.mkdir(nDir)

#T# change the current working directory with chdir()
os.chdir(nDir)

#T# get the current working directory with getcwd()
print("cwd is",os.getcwd())

#T# remove a directory with rmdir()
os.rmdir(nDir)

#T# Process control

#T# Signal handling

#T# terminate the script with the quit function
# quit()

#T# File management