#!/usr/bin/perl
#   Packages, modules

package pack1;

#T# END block executed at the very end
END
{
    print "Instruction 1, in END\n";
}

print "Instruction 2\n";

#T# BEGIN block executed at the beginning
BEGIN
{
    print "Instruction 3, in BEGIN\n";
}

#T# require loads modules but doesn't import to namespace
require Section1_13Aux;
Section1_13Aux::scriptCarp();

#T# use imports into namespace
use Section2_4a;
useMe();