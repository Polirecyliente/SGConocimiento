
#   Basic syntax

#T# Contents
#T# Basic syntax
#T# Variables, constants, literals

#T# variable declaration and initialization, identifiers
$var1 = 5;

#T# function call, print to the terminal
print "Hello, world. Var: $var1\n";

#T# Double quotes interpolate its content, single quotes do not
print 'Var: $var1\n';

#T# plain old documentation (pod)
=begin comment
    This multi line comment begins with =begin and ends with =end.
    The pod section ends with =cut
=end comment
=head1 First header
    Text here is under the header 1. Headers can be made up to =head4
=over 4
=item item in list, ends with =back
=item second item
=item third item
=back
=cut

#T# here documents
$text1 = <<"EOF";
    FirstLine
    SecondLine Word3
    Line with var, $var1
EOF
print("\nWholeText:\n$text1");

#T# Variables, constants, literals

#T# Types of variables: scalars, arrays, and hashes

#T# scalar
$str1 = "first of strings";
$val1 = 5E+2;
$flt1 = -10.237;
$val2 = 2.5 * $val1;
$octal1 = 010;
$hex1 = 0x10;

#T# array
@arr1 = (3, "Pos1", 9.24);
$flt2 = $arr1[0] + $arr1[2];

#T# hash
%hash1 = ('key1',5,'key2','val2','key3',1.1);
$flt3 = 3 * $hash1{'key3'};

#T# concatenate strings with .
$str2 = $str1 . " " . $val1 . $flt3;
print "$str2\n";

#T# print unicode characters with \x{} hexadecimal, with vDECIMAL strings
print "\x{02A0}\x{02A1}\n";
print v672.673 . "\n";

#T# special literals: __FILE__, __LINE__, and __PACKAGE__
print __FILE__ . ", is the file. Line is: " . __LINE__ . ", package: "
. __PACKAGE__ . "\n";

#T# array creation with qw quote word
@arr1 = qw/wor1 wor2 wor4/;
print "@arr1"." "."a$arr1[-1]"."\n";

#T# array's range operator (..), scalar function, max index $#arrName
@arr1 = (5..27);
@arr1 = (c..n);
$val1 = scalar @arr1;
$val1 = $#arr1;

#T# array functions: push, pop, unshift, shift
@arr1 = ("center");
push(@arr1,1,2,3,4);
pop(@arr1);
unshift(@arr1,-4,-3,-2,-1);
shift(@arr1);
print "@arr1\n";

#T# array slice @arrName[el1,el2,,,]
@arr1 = @arr1[2..4];

#T# array function: splice()
push(@arr1,"elEx1","elEx2","elEx3");
splice(@arr1,3,2,"Repl1","Repl2","Repl3");
print "@arr1\n";

#T# string function split() to create arrays
@arr1 = split("-","el1-el2-el3",2);
print "@arr1\n";

#T# arrays to strings with function join()
$str1 = join(",",@arr1);
print "$str1\n";

#T# sort array's elements with function sort()
@arr1 = ("il","el","ol","ul","al");
@arr1 = sort(@arr1);
print "@arr1\n";

#T# show first index with varible $[
print "First index of all arrays is $[\n";

#T# array element with ()[]
$val1 = (3,2,"value",1,0)[2];

#T# hashes key value separator fat comma =>, key denoter -
%hash1 = (-key1 => 'v1',-key2=>'v2');
print "$hash1{-key2}\n";

#T# hash slice @hashName{-key1,-key2}
@arr1 = @hash1{-key1,-key2};
print "@arr1\n";

#T# hash functions: keys(), values(), exists(), delete()
@arr1 = keys(%hash1);
@arr1 = values(%hash1);
$val1 = exists($hash1{-key2});
delete($hash1{-key1});
@arr1 = @hash1{-key1,-key2};
print "@arr1\n";

#T# multidimensional arrays with anonymous array []
@mArr1 = ([3,1,"el1,3"],[9,"el2,2"]);
print "@mArr1[0]->[2]\n";

#T# anonymous hash {}
$refToAnonHash1 = {'k1'=>3,'k2'=>'vle2'};
print "$refToAnonHash1->{'k2'}\n";