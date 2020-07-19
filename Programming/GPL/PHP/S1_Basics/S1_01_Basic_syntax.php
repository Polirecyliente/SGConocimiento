<!--
    Basic syntax
-->


<?php

//T// Contents
//T// Basic syntax
//T// Variables, constants, literals

//T// Escaping to php with php tags "<?php ? >"
    echo "Hello, World!";

//T// Here document
    print <<<EOF
    FistLine secondWord.
    SecondLine.
EOF;

//T// Variable assignment
    $var1 = 5 + 3;

//T// a block of code goes between curly brackets {}
    {
        print " Val: $var1";
    }

//T// Variables, constants, literals

//T// make a constant with define()
define("CONST1",12);

//T// read a constant's value with constant()
    echo constant("CONST1");

//T// predefined constants
    echo "\t";
    echo __LINE__;
    echo __FILE__;
    echo __FUNCTION__;
    echo __CLASS__;
    echo __METHOD__;
    echo __DIR__;
    echo __NAMESPACE__;
?>