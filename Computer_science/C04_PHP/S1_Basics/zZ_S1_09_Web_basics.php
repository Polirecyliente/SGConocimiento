<!--
    Web basics
-->


<html>
    <head><title>Web basics</title></head>
    <body>
    <?php
//T// environment variables like the user agent with superglobal $_SERVER
        echo "The user agent is: <br/>";
        print_r($_SERVER['HTTP_USER_AGENT']);
        print("<br/></br>");

//T// seed random number with srand(), make a random number with rand()
        srand(4);
        $rn1 = rand();
        print_r("Random number is -> $rn1<br/><br/>");

//T// print data submitted to HTML form
        print("Data submitted is: ".$_POST['varF1']."<br/><br/>");

//T// make HTTP headers with header(), POST variables with $_POST
        if ($_POST['varF1'] == 5) 
        {
            header("Location:https://google.com");

//T// exit the script with exit()
            exit();
        }

//T// GET variables with $_GET
        if ($_GET['varF2']) print("Please look at the URL<br/>");

//T// both POST and GET variables with $_REQUEST
        if ($_REQUEST['varF1'] && $_REQUEST['varF2']) print("Both vars!!");


//T// call the same script with $_PHP_SELF
    ?>
    <form action="<?php $_PHP_SELF ?>" method="POST">
        Entry1: <input type="text" name="varF1"/>
        <input type="submit"/>
    </form>
    <form action="<?php $_PHP_SELF ?>" method="GET">
        Entry2: <input type="text" name="varF2"/>
        <input type="submit"/>
    </form>
    </body>
</html>