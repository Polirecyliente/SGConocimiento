<!--
    Decision making
-->

<html>
    <head><title>Decision making</title></head>
    <body>
    <?php

    $a = 1;
    echo "a value is: $a<br/>";
//T// if, elseif, else statement
    if ($a > 0)
    {
        echo "a is greater than 0<br/><br/>";
    }
    elseif ($a == 0)
    {
        echo "a equals 0<br/><br/>";
    }
    else
    {
        echo "a is less than 0<br/><br/>";
    }

//T// switch statement
    switch ($a)
    {   
        case 0:
            echo "a is the number zero<br/>";
        case "str1":
            echo "a is a string.. or is it?<br/>";
            break;
        case 1:
            echo "a is the number one<br/>";
            break;
        default:
            echo "a wasn't matched to any value<br/>";
    }

    ?>
    </body>
</html>