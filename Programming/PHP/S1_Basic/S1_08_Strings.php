<!--
    Strings
-->

<html>
    <head><title>Strings</title></head>
    <body>
    <?php

//T// define strings in single, and double quotes
        $str1 = "firstString $str2";
        $str2 = 'secondString $str1';
        echo "String one is: $str1<br/>String two is: $str2<br/>";

//T// concatenation operator dot .
        echo "Full string ".$str1." ".$str2."<br/>";

//T// get the string length with strlen()
        echo "str1 size: ".strlen($str1)."<br/>";

//T// get the position of a match in a string with strpos()
        echo "position of ing in str1: ".strpos($str1,"ing")."<br/>";
    ?>
    </body>
</html>