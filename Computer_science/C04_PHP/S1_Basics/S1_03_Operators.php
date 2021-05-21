<!--
    Operators
-->

<html>
    <head><title>Operators</title></head>
    <body>
    <?php

        $a = 10;
        $b = 15;
        echo "a is $a, b is $b<br/>";
//T// arithmetic operators
        $c = $a + $b;
        echo "a plus b: $c<br/>";
        $c = $a - $b;
        echo "a minus b: $c<br/>";
        $c = $a * $b;
        echo "a times b: $c<br/>";
        $c = $a/$b;
        echo "a over b: $c<br/>";
        $c = $b%$a;
        echo "b modulo a: $c<br/>";
        $a++;
        $c = $a;
        echo "a plus plus: $c<br/>";
        $b--;
        $c = $b;
        echo "b minus minus; $c<br/><br/>";

//T// relational operators
//T// cast boolean to int to avoid empty string when false
        $c = (int)($a == $b);
        echo "a equals b? $c<br/>";
        $c = (int)($a > $b);
        echo "is a greater than b? $c<br/>";
        $c = (int)($a < $b);
        echo "is a less than b? $c<br/>";
        $c = (int)($a != $b);
        echo "a not equals b? $c<br/>";
        $c = (int)($a >= $b);
        echo "is a greater than or equal to b? $c<br/>";
        $c = (int)($a <= $b);
        echo "is a less than or equal to b? $c<br/><br/>";

//T// logical operators
        $c = (int)!$a;
        echo "not a is: $c<br/>";
        $c = (int)($a && $b);
        echo "a and b is: $c<br/>";
        $c = (int)($a and $b);
        echo "another a and b is: $c<br/>";
        $c = (int)($a || $b);
        echo "a or b is: $c<br/>";
        $c = (int)($a or $b);
        echo "another a or b is: $c<br/><br/>";

//T// assignment operators
        echo "initial c value: $c<br/>";
        $c += $a;
        echo "plus a: $c<br/>";
        $c -= $b;
        echo "minus b: $c<br/>";
        $c *= $a;
        echo "times a: $c<br/>";
        $c /= $b;
        echo "over b: $c<br/>";
        $c %= $a;
        echo "modulo a: $c<br/><br/>";

//T// conditional ternary operator
        $c = ($a > $b) ? $a : $b;
        echo "c is the greater of a and b: $c<br/>";

    ?>
    </body>
</html>