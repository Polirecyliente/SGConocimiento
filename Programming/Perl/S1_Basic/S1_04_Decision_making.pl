#!/usr/bin/perl
#   Decision making

use Switch;

#T# if elsif else statement
if ((2 == 3))
{
    print "Executed in if\n";
}
elsif (2 == 2)
{
    print "Executed in if elsif\n";
}
else
{
    print "Executed in if else\n";
}

#T# unless else statement
unless ((2 == 2))
{
    print "Executed in unless\n";
}
elsif (2 == 2)
{
    print "Executed in unless elsif\n";
}
else
{
    print "Executed in unless else\n";
}

@arr1 = (3,'arrStr1',2.99);
%hash1 = ('k1'=>9,'k2'=>12,'k3','valStr1');
#T# switch case next else statement
switch('valStr1')
{
    case 1
    {
        print "Executed in case 1\n";
        next;
    }
    case "str1"
    {
        print "Executed in case str1\n";
    }
    case [1,4..21,34,79]
    {
        print "Executed in case [1,4..21,34,79]\n";
    }
    case (\@arr1)
    {
        print "Executed in case (@arr1)\n";
    }
    case (\%hash1)
    {
        print "Executed in case (%hash1)\n";
    }
    else
    {
        print "Executed in switch else\n";
    }
}

#T# ternary operator ? :
$val1 = (5 < 3)? 2.9 : 999;