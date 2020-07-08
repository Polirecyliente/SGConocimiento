#!/usr/bin/perl
#   Subroutines, scope

use feature 'state';

#T# subroutine syntax, @_, $_[arg], return, local variable with my
sub subRoutine1
{
    my $totalArgs = scalar(@_);
    my $firstArg = $_[0];
    my $secondArg = $_[1];

    print "total: $totalArgs, firstA: $firstArg, secondA: $secondArg\n";

    return $secondArg;
}
my %hash1 = (-k1,'v1',-k2,5);
my @arr1 = ('pos0','pos1','pos2');

$val1 = subRoutine1(%hash1,@arr1);
print "$val1\n";

#T# local(), state() for static vars
$str1 = "string word";
sub localTest
{
    local($str1);
    $str1 = "in: new str word";

    state $cou1 = 1;
    print "$str1,$cou1\n";
    $cou1 = $cou1 + 5;
}
localTest();
localTest();
print "out: $str1\n";