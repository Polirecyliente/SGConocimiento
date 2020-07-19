
#   Control flow

#T# Contents
#T# Decision making
#T# Loops

#T# Decision making

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

#T# Loops

$val1 = 5;
#T# while loop
while ($val1 < 7)
{
    print "In while, $val1\n";
    $val1 = $val1 + 1;
}

#T# until loop
until ($val1 > 10)
{
    print "In until, $val1\n";
    $val1 = $val1 + 2;
}

#T# for loop
for ($val1 = 11;$val1 < 16;$val1 = $val1 + 3)
{
    print "In for, $val1\n";
}

print "Before: $val1\n";
@arr1 = (2.92,'el2');
#T# foreach loop, continue {} with while or foreach
foreach $foreachVar1 (@arr1)
{
    print "In foreach, $foreachVar1\n";
} continue
{
    $val1 = $val1 + 1;
}
print "After: $val1\n";

$val1 = $val1 - 2;
#T# do while loop, nested loops
do
{
    print "In do while, $val1\n";
    $val1 = $val1 + 1;
    foreach $val2 (@arr1)
    {
        print "In nested loop\n";
    }
} while ($val1 < 19);

$val1 = 0;
#T# next [label]
LABEL1: while ($val1 < 2)
{
    $val1 = $val1 + 1;
    while ($val1 < 999)
    {
        print "Before next label\n";
        next LABEL1;
    }
}

$val1 = 0;
#T# last [label]
LABEL2: while ($val1 < 2)
{
    $val1 = $val1 + 1;
    while ($val1 < 999)
    {
        print "Before last label\n";
        last LABEL2;
    }
}

$gotoVar1 = 0;
LABEL4:
$val1 = 0;
#T# redo [label]
LABEL3: while ($val1 < 2)
{
    $val1 = $val1 + 1;
    while ($val1 <= 3)
    {
        print "Before redo label\n";
        redo LABEL3;
    }
}

#T# goto label with expression
if ($gotoVar1 == 0)
{
    $val2 = 4;
    $gotoVar1 = 1;
    goto "LABEL".$val2;
}