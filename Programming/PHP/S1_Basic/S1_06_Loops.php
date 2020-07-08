<!--
    Loops
-->

<html>
    <head><title>Loops</title></head>
    <body>
    <?php

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