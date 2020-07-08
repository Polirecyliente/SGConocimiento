#!/usr/bin/perl
#   Directories

#T# open directory with a DIRHANDLE with opendir()
opendir(DIRH,"tutos/Perl/Section1");

#T# read directory's DIRHANDLE with readdir()
while(readdir(DIRH)){}

#T# rewind directory with rewinddir()
rewinddir(DIRH);

#T# return the position in reading the directory with telldir()
$val1 = telldir(DIRH);

#T# change position in dir with seekdir()
seekdir(DIRH,0);

#T# close the dir with closedir()
closedir(DIRH);

#T# return list of contents of a dir with glob()
@contents = glob("tutos/Perl/Section1/*");

#T# create a dir with mkdir()
mkdir("tutos/Perl/Section1/dirDebug");

#T# remove a dir with rmdir()
rmdir("tutos/Perl/Section1/dirDebug");

#T# change dir of working directory with chdir()
chdir("tutos");