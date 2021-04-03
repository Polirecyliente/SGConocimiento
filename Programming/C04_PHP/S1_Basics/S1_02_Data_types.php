<!--
    Data types
-->

<?php
//T// integer, double, boolean, NULL, string
    $int1 = 0x17 - 011;
    $dou1 = 4.521 + 3.1;
    $bool1 = TRUE;
    $null1 = NULL;
    $str1 = "test string";

//T// global variable
    $globalVar = "glbVl";

//T// function parameter
    function fun1($param1)
    {
        $param1 = "Parameter vl";
        GLOBAL $globalVar;
        $globalVar = "Global vl";
        
//T// local variable
        $localVar = "Local vl";
        
//T// static variable
        STATIC $staticVar = 0;
        $staticVar++;
    }
?>