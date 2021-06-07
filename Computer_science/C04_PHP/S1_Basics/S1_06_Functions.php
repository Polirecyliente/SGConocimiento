<!--
    Functions
-->

<html>
    <head><title>Functions</title></head>
    <body>
    <?php
    ini_set('display_errors',1);
    ini_set('display_startup_errors',1);

//T// create a function fun1(), arguments in parentheses, byref with &
    function fun1($arg1,&$arg2)
    {
        print("print wrapper function $arg1<br/>");
        $arg2 = "newStr";

//T// return a value with the return keyword
        return 2 * $arg1;
    }

    $var1 = 3;
    $var2 = 0;
//T// call the function fun1()
    $retV = fun1($var1,$var2);
    echo "var two is: $var2<br/>ret val is: $retV<br/>";

    $str1 = "fun1";
//T// call the function from a string, also called dynamic function call
    print("doing dynamic function call:<br/>");
    $str1(5,$var2);


    ?>
    </body>
</html>

Anonymous functions are supported in PHP, they can be created with the following syntax.

$var_func1 = function (args1)
{
    statements1;
};

For example:

in file1.php
<?php
$var_func1 = function ($arg1)
{
    print("$arg1\n");
};
$var_func1("string1");
$var_func1("string2");
?>

Executing `php file1.php` in a shell, outputs:

``` output
string1
string2
```


----

Arrow function notation, is another way to create anonymous functions. The `fn` keyword is needed to create anonymous functions in this way.

$var_func1 = fn(args1) => return_value1;

For example:

$var_func1 = fn($arg1, $arg2) => 2*$arg1 + $arg2;
$var1 = $var_func1(3, 4); // 10


----

The `use` keyword can be used to create closures, that take a variable from the outer scope and store its value, so this value remains the same, even if the variable changes in the outer scope.

in file1.php
<?php
{
    $var1 = 'value1';
    $func1 = function () use ($var1)
    {
        echo $var1;
    };
    $var1 = 'new_value1';
    $func1();
}
?>

Executing `php file1.php` outputs:

``` output
value1
```

`$var1` has the value `'new_value1'`, but `func1` stores the value of `$var1` at the moment `func1` was defined, which is `'value1'` in this case.