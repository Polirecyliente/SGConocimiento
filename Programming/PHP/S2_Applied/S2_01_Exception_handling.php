<!--
    Exception handling
-->

<html>
    <head><title>Exception handling</title></head>
    <body>
    <?php

        ini_set('display_errors',1);
        ini_set('display_startup_errors',1);

//T// log errors in server log with log_errors
        ini_set('log_errors',1);

        $var1 = 3;
//T// make error terminate program with die()
        if ($var1 == 5) die("The script can't continue");
        
//T// set the error report level, like errors, warnings with error_reporting()
        error_reporting(E_ALL);

        function customErr1($errno,$errstr,$error_file,$error_line)
        {
            print("The error $errno in line $error_line of the file\
$error_file has the message: $errstr<br/>");
            print("The script must quit");
            die();
        }

//T// set a function to be the error handler with set_error_handler()
        set_error_handler("customErr1");

//T// trigger an error with trigger_error()
        if ($var1 == 4)
        {
            trigger_error("Bad line, can't be an even number ",E_USER_ERROR);
        }
        
//T// exception handling with throw, try, and catch
        try
        {
            print("In try catch construct<br/>");
            if ($var1 == 3) throw new Exception("An exception appeared");
        }
        catch (Exception $ex1)
        {
            print("Script ends here<br/>");
            print("Exception message: ".$ex1->getMessage()."<br/>");
            print("Exception code: ".$ex1->getCode()."<br/>");
            print("Exception source file: ".$ex1->getFile()."<br/>");
            print("Exception source line: ".$ex1->getLine()."<br/>");
            print("Exception backtrace: ".$ex1->getTraceAsString()."<br/>");
        }

        function customExc1($excepAsArg)
        {
            print("An exception was processed by a custom function, The
message of the exception is: ".$excepAsArg->getMessage()."<br/>");
        }

//T// set a function to be the exception handler with set_exception_handler()
        set_exception_handler("customExc1");

        throw new Exception("Exception targeted for custom function");

        print("Unreachable code");

    ?>
    </body>
</html>