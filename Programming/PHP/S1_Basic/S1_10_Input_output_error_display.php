<!--
    Input output, error display
-->

<html>
    <head><title>Files I/O</title></head>
    <body>
    <?php

//T// change ini settings with ini_set(), display PHP errors in browser setting display_errors to 1, the same for display_startup_errors
    ini_set('display_errors',1);
    ini_set('display_startup_errors',1);

//T// include files' content with include()
        include("HTMLDebug.html");

//T// use require() to throw fatal exception on error
        require("HTMLDebug.html");

//T// open a file with fopen()
        $fH1 = fopen("txtDebug.txt","a+");

//T// get the file size in bytes with filesize()
        $f1size = filesize("txtDebug.txt");

//T// read from the file with fread()
        $f1content = fread($fH1,$f1size);

        print("The file's total size is ${f1size}Bytes<br/>");
        print("Its contents are:<br/>$f1content<br/>");

//T// write to the file with fwrite()
        fwrite($fH1,"\nwriting to file.. it used to weight ${f1size}B.\n");

//T// close a file with fclose()
        fclose($fH1);
    ?>
    </body>
</html>