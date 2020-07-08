<!--
    Upload files
-->

<html>
    <head><title>Upload files</title></head>
    <body>
    <?php

//T// access uploaded files attributes with global PHP variable $_FILES
        print("uploaded file is ".$_FILES['upl1']['name']."<br/>");
        print("file type is: ".$_FILES['upl1']['type']."<br/>");

//T// move uploaded file from temporal location to server location
        move_uploaded_file($_FILES['upl1']['tmp_name'],
                            $_FILES['upl1']['name']);

//T// use the enctype attribute with "multipart/form-data" to upload files
    ?>
    <form action="<?php $_PHP_SELF ?>" method="POST" 
    enctype="multipart/form-data">
        <input type="file" name="upl1"/>
        <input type="submit"/>
    </form>
    </body>
</html>