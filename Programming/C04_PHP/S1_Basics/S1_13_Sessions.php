<!--
    Sessions
-->

<html>
    <head><title>Sessions</title></head>
    <body>
    <?php

//T// start a session with session_start()
        session_start();

//T// check if a variable is set with isset(), see session variables with $_SESSION
        if (isset($_SESSION['seshVar1']))
        {
            $_SESSION['seshVar1'] *= 1.5;
        }
        else
        {
            $_SESSION['seshVar1'] = 2;
        }

        print("This time the session var is ".$_SESSION['seshVar1']);

        if ($_SESSION['seshVar1'] > 5)
        {
//T// finish a session with session_destroy()
            session_destroy();
        }
        
    ?>
    </body>
</html>