<!--
    Cookies
-->

<?php

//T// set a cookie with setcookie()
    setcookie("cookie1","CookieFlavor",time()+3600,"/",".localhost",1);
?>

<html>
    <head><title>Cookies</title></head>
    <body>
    <?php

//T// read cookies values with $_COOKIE
        echo "The cookie's value is: ".$_COOKIE['cookie1']."<br/>";
        
    ?>
    </body>
</html>