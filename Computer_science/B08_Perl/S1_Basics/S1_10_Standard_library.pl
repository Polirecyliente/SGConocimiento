
#   Date and time

use POSIX qw/strftime/;

#T# localtime(), gmtime(), time(), strftime()
print "Local time: ".localtime()."\n";
print "GMT: ".gmtime()."\n";
print "Seconds from beginning: ".time()."\n";
print "Local time with time(): ".localtime(time())."\n";
print "Formatted time: ".strftime("%B-%A->%d, %G%%",localtime())."\n";