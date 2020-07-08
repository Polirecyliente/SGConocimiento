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