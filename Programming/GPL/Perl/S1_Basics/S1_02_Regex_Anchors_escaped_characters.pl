#!/usr/bin/perl
#   Anchors, escaped characters

#T# end match with newline $, global modifier /g, continue modifier /c
if("ae\n" =~ m/e$/){print "Matched1: $&\n";}
print "Matched2: ";while("M1B1C3" =~ m/[A-Z]\d/g){print "$&";}print "\n";
$str1 = "<F>";
print "Matched3: ";
while($str1 =~ m/\G</gc)
{
    print "$&";
    if($str1 =~ m/\GB>/){print "$&\n";}
    elsif($str1 =~ m/\GF>/){print "$& ";}
}
while($str1 =~ /\G./g)
{
    print "$&";
}
print "\n";

#T# continue at end of the previous match \G
my $txt = "abc3de";
print "Matched4: ";
while( $txt =~ /\G[a-z]/g)
{
    print "$&";
}
print "\n";

#T# discard match before \K, match back-reference \g{}
if ("hello world" =~ m/hello \K(world)/){print "Matched5: $&\n";}
if ("mat matc" =~ m/(\w+)\s\g{1}/){print "Matched6: $&\n";}

#T# unicode properties match \p{} doesn't match \P{} # TODO \X matches an unicode char
if ("A_B5[" =~ m/\w+\p{N}\P{N}/){print "Matched7: $& $1\n";}