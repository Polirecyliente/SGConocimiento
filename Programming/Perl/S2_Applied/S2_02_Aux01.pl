#!/usr/bin/perl
#   Class instance and use

use Section2_2;
use Section2_2b;

#T# create a new object from the class
$obj1 = new Section2_2("a1Value","a2Value");

#T# get object's attribute
$val1 = $obj1->getAttr1();
print "$val1\n";

#T# set object's attribute
$obj1->setAttr1("newVlA1");

#T# check change in the value of the object's attribute
$val1 = $obj1->getAttr1();
print "$val1\n";

#T# create object of inherited class
$obj2 = new Section2_2b("inhVl1","inhVl2","a3Value");
print $obj2->getAttr3(),"\n";

#T# call AUTOLOAD() with unknown subroutine
$obj2->unknownSub();

#T# destroy objects with garbage collector DESTROY() in module file
print "$obj2\n";