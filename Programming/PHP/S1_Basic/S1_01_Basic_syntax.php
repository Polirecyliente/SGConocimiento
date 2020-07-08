<!--
    Basic syntax
-->


<?php 
//T// Escaping to php with php tags "<?php ? >"
    echo "Hello, World!";

//T// Here document
    print <<<EOF
    FistLine secondWord.
    SecondLine.
EOF;

//T// Variable assignment
    $var1 = 5 + 3;

//T// a block of code goes between curly brackets {}
    {
        print " Val: $var1";
    }
?>