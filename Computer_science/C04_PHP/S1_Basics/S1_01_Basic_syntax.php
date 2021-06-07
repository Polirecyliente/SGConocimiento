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

//T// `print` and `echo` can be used the same, to print output. One difference is that `echo` has no return value, and `print` returns the value 1.

    $var1 = print("string")
    echo $var1 // 1

//T// `echo` can receive several arguments, separated by comma.
    echo "arg1", "arg2", "argN" //arg1arg2argN

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

Create a namespace with the `namespace` keyword. It must be used at the start of a PHP file. Only classes can be made part of a namespace, variables and functions must be made into members of a class to make them part of a namespace.

in file1.php
<?php
namespace namespace1;
class class1
{
    public $var1 = 'value1';
}
?>

This makes `class1` part of `namespace1`.

The `use` keyword and the `as` keyword can be used together, to set an alias for a namespace.

in file2.php
<?php
include("file1.php");
use \namespace1 as n1;
$obj1 = new n1\class1();
echo $obj1->var1
?>

Executing `php file2.php` in a shell, outputs:

``` output
value1
```

