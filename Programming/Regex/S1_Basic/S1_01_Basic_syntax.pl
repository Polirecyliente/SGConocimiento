#!/usr/bin/perl
#   Basic syntax

#T# pattern search: binding operator =~, pattern delimiters //,
$text = "text to make regex tests";
if($text =~ m/make/)
{
    print "Matched\n"
}
else
{
    print "No Match\n"
}

#T# detect UTF-8 character set
use utf8;
use open ':std', ':encoding(UTF-8)';

#T# before pattern $`, pattern $&, after pattern $'
if ("befPATaft" =~ m/PAT/){print "before:$`\npattern:$&\nafter:$'\n"}

#T# characters

#T# digit \d, word char \w (letter, digit, underscore)
if ("file_25" =~ m/file_\d\d/){print "Matched1:$&\n"}
if ("b_1" =~ m/\w\w\w/){print "Matched2:$&\n"}

#T# whitespace \s (space, tab, newline, carriage return, vertical tab)
if ("a b\nc" =~ m/a\sb\sc/){print "Matched3:$&\n"}

#T# not a digit \D, not a word char \W, not whitespace \S
if ("A C" =~ m/\D\D\D/){print "Matched4:$&\n"}
if ("*-+=(" =~ m/\W\W\W\W\W/){print "Matched5:$&\n"}
if ("A_C" =~ m/\S\S\S/){print "Matched6:$&\n"}

#T# quantifiers

#T# one or more +, zero or more *, zero or one ?
if ("Version A-b1_1" =~ m/\w-\w+/){print "Matched7:$&\n"}
if ("AAACC" =~ m/A*B*C*/){print "Matched8:$&\n"}
if ("plural" =~ m/plurals?/){print "Matched9:$&\n"}

#T# exactly n times {n}, m to n times {m,n}, more than n times {n,}
if ("A C" =~ m/\D{3}/){print "Matched10:$&\n"}
if ("978" =~ m/\d{2,4}/){print "Matched11:$&\n"}
if ("word1_word2" =~ m/\w{9,}/){print "Matched12:$&\n"}

#T# more characters

#T# any char . (except line break), escape metacharacter \
if ("\nabc123\nABC456" =~ m/.+/){print "Matched13:$&\n"}
if (".*+?^\$/\\[{()}]" =~ m/\.\*\+\?\^\$\/\\\[\{\(\)\}\]/)
    {print "Matched14:$&\n"}

#T# logic

#T# or |, capturing group (), groups \1, \2, non capturing group (?:) $1
if ("33" =~ m/22|33/){print "Matched15:$&\n"}
if ("Apple" =~ m/A(nt|pple)/){print "Matched16:$&\n"}
if ("regex" =~ m/r(\w)g\1x/){print "Matched17:$&\n"}
if ("12+65=65+12" =~ m/(\d\d)\+(\d\d)=\2\+\1/){print "Matched18:$&\n"}
if ("Apple" =~ m/A(?:nt|pp)(le)/){print "Matched19:$& Group1:$1\n"}

#T# more whitespace

#T# tab \t, carriage return \r, newline \n
if ("T\tab" =~ m/T\t\w{2}/){print "Matched20:$&\n"}
if ("a\rb" =~ m/a\rb/){print "Matched21:$&\n"}
if ("AB\nCD" =~ m/AB\nCD/){print "Matched22:$&\n"}

#T# not a newline \N, horizontal space \h, not a horizontal space \H
if ("AB\nCD" =~ m/\N+/){print "Matched23:$&\n"}
if ("AB CD" =~ m/\h+/){print "Matched24:$&\n"}
if ("AB CD" =~ m/\H+/){print "Matched25:$&\n"}

#T# more quantifiers

#T# lazy +?, lazy *?, lazy {m,n}?
if ("12345" =~ m/\d+?/){print "Matched26:$&\n"}
if ("AAA" =~ m/A*?/){print "Matched27:$&\n"}
if ("abcd" =~ m/\w{2,4}?/){print "Matched28:$&\n"}

#T# character classes

#T# one of the chars [], char range [-], not one of the chars [^]
if ("IEOUA" =~ m/[AEIOU]/){print "Matched29:$&\n"}
if ("m" =~ m/[h-n]/){print "Matched30:$&\n"}
if ("A1!" =~ m/[^a-z]{3}/){print "Matched31:$&\n"}

#T# anchors and boundaries

#T# start of string ^, end of string $, start of string \A
if ("abcdefghijk" =~ m/^abc.*?/){print "Matched32:$&\n"}
if ("is the end\n" =~ m/ the end$/){print "Matched33:$&\n"}
if ("abcdefghijk" =~ m/\Aabc[\d\D]*/){print "Matched34:$&\n"}

#T# end without newline \z, end with newline \Z
if ("is the end" =~ m/ the end\z/){print "Matched35:$&\n"}
if ("is the end\n" =~ m/ the end\Z/){print "Matched36:$&\n"}

#T# word boundary \b, not a word boundary \B
if ("start middle\nend" =~ m/\bmiddle\b/){print "Matched37:$&\n"}
if ("startmiddléend" =~ m/\Bmiddlé\B/){print "Matched38:$&\n"}

#T# inline modifiers

#T# case insensitive (?i), dotall or single line mode (?s)
if ("monDAY" =~ m/(?i)Monday/){print "Matched39:$&\n"}
if ("From A\nto Z" =~ m/(?s)Fr.* Z/){print "Matched40:$&\n"}

#T# multiline mode (?m), free spacing mode (?x), turn off (?-)
if ("l1\nl2\nl3" =~ m/(?m)^l2$/){print "Matched41:$&\n"}
if ("ab cde" =~ m/(?x)ab\ cd e/){print "Matched42:$&\n"}
if ("ab\ncd" =~ m/(?i-m)^Ab\nCd$/){print "Matched42a:$&\n"}

#T# lookarounds

#T# positive lookahead (?=), positive lookbehind (?<=)
if ("foo1barfoo2qux" =~ m/foo\d(?=qux)/){print "Matched43:$&\n"}
if ("foo1barfoo2qux" =~ m/(?<=bar)foo\d/){print "Matched44:$&\n"}

#T# negative lookahead (?!), negative lookbehind (?<!)
if ("foo1barfoo2qux" =~ m/foo\d(?!qux)/){print "Matched45:$&\n"}
if ("foo1barfoo2qux" =~ m/(?<!bar)foo\d/){print "Matched46:$&\n"}

#T# others

#T# escape all \Q...\E
if ("a.+?z" =~ m/\Qa.+?\E/){print "Matched47:$&\n"}