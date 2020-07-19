
#   Special variables

use English;

#T# scalar special variables

#T# default input $_ or $ARG
foreach ("val1","val2")
{
    print "$_ ";
}
print "\n";

sysopen(FILEH,"tutos/Perl/Sources",O_RDONLY);
$val1 = <FILEH>;
$val1 = <FILEH>;
#T# last read file line number $. or $NR
print "Line number: $.\n";
close(FILEH);

#T# input record separator $/ or $RS
print "Input Record Separator: newline$/";

#T# output field separator for print() $, or $OFS
local $, = "-|-";
#T# print with newline at end with say()
CORE::say("w1","w2","w3");

@arr1 = ("w1A","w2A","w3A");
#T# list separator $" or $LIST_SEPARATOR
$" = $";
CORE::say("List Separator: el1-$LIST_SEPARATOR-el2");
CORE::say("@arr1");

#T# output record separator $\ or $ORS
local $\ = "_-_\n";
CORE::say("Output Record Separator: $ORS ");
print("print line1 ");

#T# error in child process $? or $CHILD_ERROR
close(FILEH) or warn("Child process error: $CHILD_ERROR");

#T# OS error $! or $OS_ERROR
close(FILEH) or warn("OS error: $OS_ERROR");

#T# eval error $@ or $EVAL_ERROR
eval
{
    close(FILEH) or warn("Eval error: $EVAL_ERROR");
};

#T# pid $$ or $PID
CORE::say("pid $PID");

#T# real uid $< or $UID
CORE::say("real uid $UID");

#T# effective uid $> or $EUID
CORE::say("effective suid $EUID");

#T# real gid $( or $GID
CORE::say("real gid $(");

#T# effective gid $) or $EGID
CORE::say("effective sgid $)");

#T# file name of executing script $0 or $PROGRAM_NAME
CORE::say("prog name is $PROGRAM_NAME");

#T# perl version $] or $PERL_VERSION
CORE::say("Perl version is $PERL_VERSION");

#T# host OS $^O or $OSNAME
CORE::say("operating system is $OSNAME");

#T# perl's binary path $^X or $EXECUTABLE_NAME
CORE::say("Perl's path is $EXECUTABLE_NAME");

#T# array special variables

#T# array of arguments passed to the script @ARGV
CORE::say("args: @ARGV");

#T# path where perl looks for modules, or perl scripts @INC
CORE::say("Perl's include path is @INC");

#T# hash special variables

#T# included files %INC
CORE::say("Perl's included files are ",%INC);

#T# evironment variables %ENV
CORE::say("environment variables are ",%ENV);

#T# signal handlers %SIG
CORE::say("signal handlers are ",%SIG);
$SIG{'INT'} = sub {die("SIGINT signal sent by the OS, $!");};

#T# file handles

#T# file handle of arguments passed to script ARGV
while (<ARGV>)
{
    print "$_";
}

#T# file handle of standard input STDIN
my $val1 = <STDIN>;

#T# file handle of standard output STDOUT
print(STDOUT "directed to std output");

#T# file handle of standard error STDERR
print(STDERR "directed to std error");

#T# file handle for text or data at the end of the file DATA
while (<DATA>)
{
    print("$_");
}

#T# special constants

#T# file name __FILE__
print __FILE__;

#T# line in script __LINE__
print __LINE__;

#T# package name of this script __PACKAGE__
print __PACKAGE__;

#T# text in the end of the file special constant __END__
__END__
Ulterior message
and a table of data
h1  h2  h3  h4
7   a   lo  y
9   8   0   qu
r3  r3  r3  r3