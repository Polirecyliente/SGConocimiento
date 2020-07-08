#!/usr/bin/perl
#   Loops

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