<!--
    Constants
-->

<?php

//T// make a constant with define()
    define("CONST1",12);

//T// read a constant's value with constant()
    echo constant("CONST1");

//T// predefined constants
    echo "\t";
    echo __LINE__;
    echo __FILE__;
    echo __FUNCTION__;
    echo __CLASS__;
    echo __METHOD__;
    echo __DIR__;
    echo __NAMESPACE__;
?>