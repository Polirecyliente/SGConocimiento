#!/usr/bin/perl
#   Input output

use Fcntl;

#T# open(FILEHANDLE, "<file") the "<" for read-only mode, die() to signal error, show error calling open() with $!
open(FILEH,"<Programming/Perl/S1_Basic/S1_01_Basic_syntax.pl") 
or die("Can't open the file, $!");

#T# read file handle in list context
@arr1 = <FILEH>;

#T# current position in bytes inside file with tell()
print tell(FILEH),"\n";

#T# go to byte 0 of the file with seek(), SEEK_SET to position relative to the beginning of the file
seek(FILEH,0,SEEK_SET);

#T# read line by line with <FILEHANDLE>, print line with $_
while (<FILEH>)
{
    print "$_";
}
print "\n";

#T# close file with close(FILEHANDLE)
close(FILEH) or die("Can't close the file, $!");

#T# ">" writes to the file truncating it
open(FILEH,">tutos/Perl/Section1/Section1_11Debug") or die("$!");
close(FILEH) or die("Can't close the file, $!");

#T# "+<" or "+>" adds write or read access
open(FILEH,"+<tutos/Perl/Section1/Section1_11Debug") or die("$!");
close(FILEH) or die("Can't close the file, $!");

#T# append mode with ">>"
open(FILEH,">>tutos/Perl/Section1/Section1_11Debug") or die("$!");

#T# write to file with print()
print(FILEH "appended to File\n");
close(FILEH) or die("Can't close the file, $!");

#T# sysopen(), O_RDWR open with read write access
sysopen(FILEH,"tutos/Perl/Section1/Section1_11Debug",O_RDWR);
close(FILEH) or die("Can't close the file, $!");

#T# truncate with O_TRUNC
sysopen(FILEH,"tutos/Perl/Section1/Section1_11Debug", O_RDWR|O_TRUNC);
close(FILEH) or die("Can't close the file, $!");

#T# create the file with O_CREAT, read only with O_RDONLY, stop creating if the file already exists with O_EXCL, don't stop execution with warn()
sysopen(FILEH,"tutos/Perl/Section1/Section1_11Debug",O_CREAT|O_RDONLY|
O_EXCL);
close(FILEH) or warn("Can't close the file, $!");

#T# write only access with O_WRONLY, append with O_APPEND
sysopen(FILEH,"tutos/Perl/Section1/Section1_11Debug",O_WRONLY|O_APPEND);
print(FILEH"characters");

sysopen(FILEH,"tutos/Perl/Section1/Section1_11Debug",O_RDWR);
#T# get one char from file with getc
$val1 = getc(FILEH);

#T# read FH into $val1 by a byte block with read(FH,$val1,block_size)
read(FILEH,$val1,3);
close(FILEH) or die("Can't close the file, $!");

#T# rename a file with rename()
rename("tutos/Perl/Section1/Section1_11Debug",
"tutos/Perl/Section1/Section1_11DebugRe");

$testF = "tutos/Perl/Section1/Section1_11DebugRe";
#T# file test operators
if (-e $testF){print "the file exists\n";}
if (-R $testF){print "the file is readable by uid or gid\n";}
if (-W $testF){print "the file is writable by uid or gid\n";}
if (-X $testF){print "the file is executable by uid or gid\n";}
if (-S $testF){print "the file is a socket file\n";}
if (-T $testF){print "the file is a text file\n";}
if (-B $testF){print "the file is a binary file\n";}
if (-b $testF){print "the file is a block device file\n";}
if (-c $testF){print "the file is a character device file\n";}
if (-d $testF){print "the file is a directory\n";}
if (-f $testF){print "the file is a plain file\n";}
if (-l $testF){print "the file is a symbolic link\n";}
if (-p $testF){print "the file is a named pipe\n";}
if (-z $testF){print "the file has a zero size\n"}
if (-s $testF > 0){print "the size of the file is ",-s $testF,"B\n";}

#T# delete a file with unlink()
unlink("tutos/Perl/Section1/Section1_11DebugRe");