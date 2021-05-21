
#   Regex

$str1 = "string to do matches on";
#T# regex relational operators: matches =~, does not match !~
$str1 =~ m/^string/;
$str1 !~ m/^anythingElse/;

#T# regex operator match m// returns captured groups in list context
@arr1 = ($str1 =~ m/(^stri)ng (\w+)(\s)(do)/);
print "@arr1\n";

#T# regex operator substitution s///
$str1 =~ s/^string/cord/;
print "$str1\n";

#T# regex operator transliterate tr///
$str1 =~ tr/o/y/dc;
print "$str1\n";