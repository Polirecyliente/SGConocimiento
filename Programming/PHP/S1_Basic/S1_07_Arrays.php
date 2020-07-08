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

//T// associative arrays or hashes
        $arr2 = array("key1" => "val1","key2" => 8,"key3" => "sV");
        $arr2["key3"] = "ThirdValue";
        echo "value in key three is: " . $arr2['key3'] . "<br/>";

//T// multidimensional arrays
        $arr3 = array(array(3,"numArr",5),"keyX" => array(90,"innK" => 7));
        
        echo "value in [0][1]: ".$arr3[0][1]."<br/>value in keyX[0]: "
        .$arr3["keyX"][0];

    ?>
    </body>
</html>