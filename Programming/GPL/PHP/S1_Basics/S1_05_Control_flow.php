<!--
    Control flow
-->

<html>
    <head><title>Control flow</title></head>
    <body>
    <?php

//T// Contents
//T// Decision making
//T// Loops

//T// Decision making

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

//T// Loops

//T// for loop, continue
    for ($i = 2;$i < 6;$i++)
    {
        if ($i == 3) continue;
        echo "i is $i<br/>";
    }

    echo "<br/>";
//T// while loop, nested loop
    while ($i > 4)
    {
        for ($j = 0;$j < 2;$j++)
        {
            echo "i is $i, j is $j<br/>";
        }
        $i--;
    }

    echo "<br/>";
//T// do while loop, break
    do
    {
        echo "i is $i<br/>";
        $i++;
        if ($i == 8) break;
    } while ($i < 50);

    echo "<br/>";
    $arr1 = array(12,"str1",7);
//T// foreach as loop
    foreach ($arr1 as $valEl)
    {
        echo "Current value un array is $valEl<br/>";
    }

    ?>
    </body>
</html>