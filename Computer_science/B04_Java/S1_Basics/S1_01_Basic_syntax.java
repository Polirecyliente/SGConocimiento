/*
    Basic syntax
*/

//T// Contents
//T// Basic syntax
//T// Variables, constants, literals

# INSTALLATION

Install the JDK (Java Development Kit), which contains programs like `java` and `javac`.

``` {.bash in="in CLI"}
sudo apt install default-jdk
```

//T// compile any Java file /path/to/file1.java in a terminal with
// javac /path/to/file1.java
//T// the executable is called /path/to/file1.class
//T// run the compiled executable in a terminal with
// java /path/to/file1.class

//T// public class block
public class S1_01_Basic_syntax
{
//T// main() method where execution starts
    public static void main(String []args)
    {
//T// keywords and identifiers
        int a1 = 5;
//T// function call to print in terminal
        System.out.println("Hello World: " + a1);
    }
}