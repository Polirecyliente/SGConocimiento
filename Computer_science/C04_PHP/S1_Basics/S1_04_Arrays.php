<!--
    Arrays
-->

<html>
    <head><title>Arrays</title></head>
    <body>
    <?php

//T// numeric arrays
    $arr1 = array(2,"str1",7);
    $arr1[2] = "str2";
    foreach ($arr1 as $el) echo "array element: $el<br/>";

//T// The double arrow operator `=>` is used in associative arrays to associate a key to its value

//T// associative arrays or hashes
    $arr2 = array("key1" => "val1","key2" => 8,"key3" => "sV");
    $arr2["key3"] = "ThirdValue";
    echo "value in key three is: " . $arr2['key3'] . "<br/>";

//T// multidimensional arrays
    $arr3 = array(array(3,"numArr",5),"keyX" => array(90,"innK" => 7));

    echo "value in [0][1]: ".$arr3[0][1]."<br/>value in keyX[0]: "
    .$arr3["keyX"][0];

//T// Strings

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