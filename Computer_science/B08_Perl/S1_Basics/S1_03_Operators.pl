
#   Operators

$a = 10, $b = 20;
#T# arithmetic operators
$c = $a + $b;
$c = $a - $b;
$c = $a * $b;
$c = $b/$a;
$c = $b % $a;
$c = $a ** $b;

#T# relational operators
$c = ($a == $b);
$c = ($a eq $b);
$c = ($a != $b);
$c = ($a ne $b);
$c = ($a <=> $b);
$c = ($a cmp $b);
$c = ($a > $b);
$c = ($a gt $b);
$c = ($a < $b);
$c = ($a lt $b);
$c = ($a >= $b);
$c = ($a ge $b);
$c = ($a <= $b);
$c = ($a le $b);

#T# assignment operators
$c = $a;
$c += $a;
$c -= $a;
$c *= $a;
$c /= $a;
$c %= $a;
$c **= $a;

$b1 = 0x00C98011, $b2= 0x00362057;
#T# bitwise operators
$c = $b1 & $b2; #0X00000011 _> 17
$c = $b1 | $b2; #0X00FFA057 _> 16752727
$c = $b1 ^ $b2; #0X00FFA046 _> 16752710
$c = ~$b1;      #0XFF367FEE or 0xFFFFFFFFFF367FEE
                # _> 4281761774 or 18446744073696346094
$c = $b1 << 3;  #0X064C0088 _> 105644168
$c = $b1 >> 1;  #0X0064C008 _> 6602760

$d = !(2 == 2);
#T# logical operators
$c = ($d && $a);
$c = ($d and $a);
$c = ($d || $a);
$c = ($d or $a);
$c = not($d);

#T# quote-like operators
$c = q/singleQuotes $a/;
$c = qq/doubleQuotes $a/;
$c = qx/date/;

#T# other operators
$c = ("a" x 4);
$c = $a++;
$c = $a--;