#!/usr/bin/perl
#   Backtracking control verbs

#T# (*THEN), (*PRUNE), (*SKIP), (*COMMIT), (*ACCEPT), (*FAIL), (*MARK)
if("CnnD" =~ m/(?:A.?.?(*THEN)B|C.?.?(*THEN)D)/){print "Matched1: $&\n";}
if("abcd_mat" =~ m/\w{3,}(*PRUNE)mat/){print "UnMatched $&\n";}
if("123ABC" =~ m/123(*SKIP)B|.{3}/){print "Matched2: $&\n";}
if("123ABC" =~ m/123(*COMMIT)B|.{3}/){print "UnMatched: $&\n";}
if("BOZ" =~ m/B(?:I|A|O(*ACCEPT))Z/){print "Matched3: $&\n";}
'abc' =~ /\w+(?{print "Match4: $& ";})(*FAIL)/; print "\n";
if("123ABC456" =~ m/123(*MARK:tag1)[A-Z]+(*SKIP:tag1)NO.|.{6}/)
{print "Matched5: $&\n";}