#!/usr/bin/perl
#   Referencing

$val1 = 2;
@arr1 = ('el1',5);
%hash1 = ('k1'=>9.1,'k2'=>7);
sub sub1 {print "letters\n";}
#T# create pointers to variables
$pointerToVal = \$val1;
$pointerToArr = \@arr1;
$pointerToHash = \%hash1;
$pointerToSub = \&sub1;

#T# dereference pointers
print "$$pointerToVal .. @$pointerToArr .. ",%$pointerToHash,"\n";
&$pointerToSub();

#T# ref() to know pointer's type
print ref($pointerToArr),"\n";