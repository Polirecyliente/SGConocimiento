<!--
    Date, time
-->

<html>
    <head><title>Date and Time</title></head>
    <body>
    <?php

//T// get current date and time in seconds from UNIX epoch with time()
        print("Seconds since UNIX epoch are: ".time()."<br/>");

        $var1 = time();
//T// convert from UNIX epoch seconds to associative array with getdate()
        $arr1 = getdate($var1);
        print("The number of seconds is: ".$arr1['seconds']."<br/>");
        print("The number of minutes is: ".$arr1['minutes']."<br/>");
        print("The number of hours is: ".$arr1['hours']."<br/>");
        print("The day of the year is: ".$arr1['yday']."<br/>");
        print("The day of the month is: ".$arr1['mday']."<br/>");
        print("The day of the week is: ".$arr1['wday']."<br/>");
        print("The weekday is: ".$arr1['weekday']."<br/>");
        print("The month number is: ".$arr1['mon']."<br/>");
        print("The month is: ".$arr1['month']."<br/>");
        print("The year is: ".$arr1['year']."<br/><br/>");

//T// format a date in a non UNIX way with date()
        print("Formatted date is: ".date("m/M",time()));
    ?>
    </body>
</html>