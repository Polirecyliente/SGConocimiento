#!/usr/bin/perl
#   Groups, subroutines

#T# atomic group (?>), also ++, conditional (?(1)}|]), subroutine (?1)
if("foots" =~ m/(?>foot|foo)s/){print "Matched1: $&\n"}
if("AAAABC" =~ m/A++[A-Z]C/){print "Matched2: $&\n"}
if("start[5462]end" =~ m/({)?\[?\d+(?(1)}|\])/){print "Matched3: $&\n"}
if("one two" =~ m/(\w+) (?1)/){print "Matched4: $&\n"}

#T# named groups (?<name>) \k, turn off all inline modifiers (?^)
if("235.67 67" =~ m/(?<intPart>\d+)\.(?<decPart>\d+)\s\k<decPart>/)
{print "Matched5: $& $+{intPart}$+{decPart}\n"}
if("str sTr StR" =~ m/(str) (?i)\1 (?^)\1?/){print "Matched6: $&\n"}

#T# relative subroutine (?-1) (?+1), named subroutine (?&name)
if("one three 5 7" =~ m/(\w+) (?-1) (?+1) (\d+)/){print "Matched7: $&\n"}
if("one four" =~ m/(?<wd>\w+) (?&wd)/){print "Matched8: $&\n"}

#T# Predefined subroutine (?(DEFINE)), recursive expression (?R)
if("Str1 sTr2 stR3" =~ m/(?(DEFINE)(?<subA>Str|sTr|stR)
(?<subB>1|2|3))(?&subA)(?&subB)\ (?&subA)/){print "Matched9: $&\n"}
if("aAAZZZz" =~ m/A(?R)?Z/){print "Matched10: $&\n"}

#T# branch reset (?|), comment (?#), code capsule (?{})
if("B12" =~ m/(?|A(\d+)|B(\d+)|C(\d+))/){print "Matched11: $&\n"}
if("str1" =~ m/(?# comment1)str1/){print "Matched12: $&\n"}
if("abcd" =~ m/(?:[a-z](?{print "CodeCap:$& "}))+/){print "\n"}