---
title: LANGUAGE BASICS
toc-title: Table of Contents
---

# INTRODUCTION

This document is about the C programming language and its features.

The C language is a compiled language, which means that a compiler is needed to convert C source code into binary code.

This project uses the `gcc` compiler to compile C source code files into binary code files. GCC stands for GNU Compiler Collection. GNU stands for GNU is Not Unix, GNU is a free and open source software project.

To install the `gcc` compiler, the following command can be used, in an Ubuntu machine.

``` bash
sudo apt install build-essential
```

The concepts used here are defined in [Programming definitions](../01_Programming_definitions.md).

# BASIC USAGE

Source code files of the C language have the file extension `.c` and they are written in a plain text format.

Compile a C source code file `/path/to/file1.c` into a binary code file `/path/to/bin1`, by using the following command in a shell.

``` {.bash .syntax}
gcc /path/to/file1.c -o /path/to/bin1
```

To execute the binary code file, use the following command in a shell.

``` {.bash .syntax}
/path/to/bin1
```

# BASIC SYNTAX

Every program created with the C language must have one and only one function called `main`, the `main` function is the entry point where the execution of the program starts.

The `main` function returns an integer value, the value $0$ means that the program was executed successfully. Any value different from $0$ indicates that the program exits because of an error.

The syntax of the `main` function is as follows:

``` {.C .syntax}
int main()
{
	statements1;
	return 0;
}
```

`int` and `return` are keywords, they are explained in this document.

`statements1` represents the statements of the code. The smallest possible C program that does nothing is produced by deleting the `statements1;` line.

## Statements and blocks of code

Statements in C must be terminated with a semicolon, `statement1;`.

Blocks of code in C are enclosed in braces, `{ block_of_code1 }`.


----

C ignores whitespace and so it does not require indentation, so the following is valid C syntax.

``` {.C .syntax}
int main() { statement1; return 0; }
```


----

Multiple statements can be written per line.

``` {.C .syntax}
statement1; statement2; statementN;
```


----

Multiline statements are written directly (names of variables and functions can't be broken into lines).

``` {.C .syntax}
state
ment1
;
```

For example:

``` C
int
main
()
{
	  statement1
	  ;
    return
    0
    ;
}
```

## Basic input and output

To use basic functionality, like read keyboard input from standard input, and printing character output to standard output, the `stdio.h` header is used. The `stdio.h` header is included with the `#include` directive. Headers and directives are explained in this document.

The following syntax shows a common way to write a file to test C source code.

``` {.C .syntax}
#include <stdio.h>

int main()
{
	statements1;
	return 0;
}
```


----

To print characters to standard output, use the `printf` function. This function is included with the `stdio.h` header.

``` {.C .syntax}
printf("This text will be printed to standard output");
```

To print a given variable do:

``` {.C .syntax}
int var1 = value1;
printf("%d", var1);
```

`int var1 = value1` creates a variable `var1` of data type `int` (for integer) with a value of `value1`. `%d` is called a format specifier. Variables, data types, and format specifiers are explained in this document. This is placed here because it's the minimum required to use the `printf` function to print the value of an integer variable.

The following is a minimal complete program that prints to standard output.

``` C
#include <stdio.h>
int main()
{
  printf("string1");
  return 0;
}
```

Compiling and executing this program in a shell outputs:

``` output
string1
```

The following program prints an integer variable to standard output.

``` C
#include <stdio.h>
int main()
{
    int var1 = 5;
  printf("%d", var1);
  return 0;
}
```

Compiling and executing this program in a shell outputs:

``` output
5
```


----

To read data from standard input, use the `scanf` function.

``` {.C .syntax}
int a;
scanf("%d", &a);
```

The `&` in `&a` is the address operator, `&a` is the address of the variable `a`. The address operator, and the address of a variable are explained in this document. This is placed here because the `scanf` function requires the address of a variable and not the variable itself.

The following is a minimal complete program that reads from standard input.

``` C
#include <stdio.h>

int main()
{
    int a;
    scanf("%d", &a);
    printf("%d", a);
    return 0;
}
```

Compiling and executing this program in a shell, prompts the user to enter characters with the keyboard. Use the `enter` key to finish inputting characters. In this program, the input expected is an integer number, for example '34', but inputting text does not throw an error, it is undefined behavior.

After inputting an integer number, this program prints that integer and exits. Inputting text makes the program print numbers that change. Even when inputting the same text, the printed output number varies because doing so is undefined behavior.

# DATA TYPES

C is a statically typed language, so to create a variable, the data type of the variable must be specified. In order to achieve this, the C language has keywords for the data types.

A variable is defined by writing the keyword of its data type and then the name of the variable.

``` {.C .syntax}
data_type1 var1;
```

`var1` is the name of the variable, and `data_type1` is a keyword of the data type of `var1`. This syntax is for the definition of `var1`.


----

Several variables of the same data type can be defined in a single statement, separating the variables by comma.

``` {.C .syntax}
data_type1 var1, var2, varN;
```


----

The equal sign '=' is used as an assignment operator to assign a value to a variable.

``` {.C .syntax}
data_type1 var1 = value1;
```

`value1` must be of the same data type as `data_type1`, otherwise it's undefined behavior. This syntax is for the definition of `var1`.


----

Several variables of the same data type can be defined in a single statement, separating the variables by comma.

``` {.C .syntax}
data_type1 var1 = value1, var2 = value2, varN = valueN;
```


----

Definitions and initialization of variables, can be mixed in a single statement.

``` {.C .syntax}
data_type1 var1, var2 = value2;
```


----

`var1` can be defined on one statement, and initialized on another statement.

``` {.C .syntax}
data_type1 var1;
var1 = value1;
```


----

In C, each data type is allocated a given amount of bytes in memory, during the program execution. To know this amount of bytes for a given data type, the `sizeof` function is used.

``` {.C .syntax}
int var1;
var1 = sizeof(data_type1);
```

`var1` holds the amount of bytes allocated to a variable of data type data_type1.


----

The `void` keyword represents the lack of data type, it's used in functions and in type casting.

The `NULL` keyword represents a NULL value.


----

Constants can be created with the `const` keyword placed before the data type in a variable declaration or definition.

``` {.C .syntax}
const data_type1 CONSTANT1 = value1;
```

The name of constants is written in uppercase by convention. For example:

``` C
const int NUMBER = 8;
```

## Numeric data types

C has numeric data types for integer numbers, and for numbers with decimals (also known as floating point numbers).

### Integer data types

The `int` keyword is used to create variables of integer data type. An `int` is a data type that has at least 2 bytes of memory allocated to it. An `int` can have 4 bytes of memory allocated to it by the compiler.

``` {.C .syntax}
int var1 = num1;
```

For example:

``` {.C}
int var1 = 5;
```


----

Hexadecimal integers can be written by prefixing the number with `0x`, for example the hexadecimal number '5A' would be written as `0x5A`.

``` C
int var1 = 0x5A;
```


----

Octal integers can be written by prefixing the number with `0`, for example the octal number '11' would be written as `011`.

``` C
int var1 = 011;
```


----

Binary integers can be written by prefixing the number with `0b`, for example the binary number '10100' woud be written as `0b10100`.

``` C
int var1 = 0b10100;
```


----

Integers can be signed or unsigned. By default, integers are signed.

``` C
int var1 = -20000;
```


----

The `unsigned` keyword makes the number unsigned.

``` C
unsigned int var1 = 50000
```


----

The `signed` keyword makes the number signed.

``` C
signed int var1 = -20000
```


----

The `short` keyword modifies an `int` data type, making a `short int` data type have less (or equal) memory allocated than an `int` data type. See below for details.

``` {.C .syntax}
short int var1 = value1;
```

Using the `short` keyword alone, means the same as `short int`.

``` {.C .syntax}
short var1 = value1;
```

The `long` keyword modifies an `int` data type, making a `long int` data type have more (or equal) memory allocated than an `int` data type. See below for details.

``` {.C .syntax}
long int var1 = value1;
```

Using the `long` keyword alone, means the same as `long int`.

``` {.C .syntax}
long var1 = value1;
```

The `long long` keyword modifies an `int` data type, making a `long long int` data type have more (or equal) memory allocated than a `long int` data type. See below for details.

``` {.C .syntax}
long long var1 = value1;
```

Using the `long long` keyword alone, means the same as `long long int`.

``` {.C .syntax}
long long var1 = value1;
```

: Integer data types and their minimum memory allocations

     Data type     Minimum memory
  --------------- ----------------
     short int        2 bytes
        int           2 bytes
     long int         4 bytes
   long long int      8 bytes

As the table shows, each data type has a minimum memory allocation, but there is no maximum, so a compiler could allocate 8 bytes for all data types and that would be valid C.

The memory allocation of each of these data types is less than or equal the memory allocation of the next bigger data type. This means that `sizeof(short int)`{.C} $\le$ `sizeof(int)`{.C} $\le$ `sizeof(long int)`{.C} $\le$ `sizeof(long long int)`{.C}.

### Floating point data types

The `float` keyword is used to create variables that hold floating point numbers.

``` {.C .syntax}
float var1 = value1;
```

For example:

``` C
float var1 = 5.18;
```


----

The `double` keyword is used like the `float` keyword, but a variable of data type `double` is allocated in double the amount of memory of a `float` data type.

``` {.C .syntax}
double var1 = value1;
```

For example:

``` C
double var1 = 50000.9815;
```


----

The `long` keyword can be used to modify the `double` keyword. A `long double` data type is allocated more (or equal) memory than a `double` data type.

``` {.C .syntax}
long double var1 = value1;
```

### Suffixes for numeric data types

Numbers can have suffixes.

There are suffixes that act as keywords, for example the `u` or `U` suffix are used to make an unsigned number.

``` {.C .syntax}
int var1 = num1u;
int var2 = num1U;
```

For example:

``` C
int var1 = 50000u;
```

This makes `var1` an unsigned integer variable.


----

The `p` or `P` suffix is used to multiply a hexadecimal number by a power of 2. This suffix is necessary to create floating hexadecimals.

``` {.C .syntax}
float var1 = num1pint1;
float var2 = num2Pint2;
```

`int1` and `int2` can be positive or negative integers.

For example:

``` C
float var1 = 0x5.1p0;
```

Printing `var1` outputs:

``` output
5.062500
```

An example with an exponent different from 0:

``` C
float var1 = 0x5.1p4;
```

Printing `var1` outputs:

``` output
81.000000
```

The decimal number 81 is equivalent to the hexadecimal 0x51.

## Boolean data type

The `bool` keyword is used to create variables of boolean data type. To use the `bool` keyword, the `stdbool.h` header must be included.

``` {.C .syntax}
#include <stdbool.h>
bool var1 = value1;
```

`value1` can only have one of the two truth values: `true` or `false`.

For example:

``` C
#include <stdbool.h>
bool var1 = true, var2 = false;
```

Printing `var1` and `var2` outputs:

``` output
var1: 1
var2: 0
```

This shows that the boolean value `true` is treated as the integer 1, and the boolean value `false` is treated as the integer 0.


----

A boolean variable can be assigned to any value, not only to a boolean value. The only two ways to make a boolean variable `false` are: using the `false` keyword like regular, or making the boolean variable equal to 0. For example:

``` C
#include <stdbool.h>
bool var1, var2, var3;
var1 = 587.2;
var2 = "string1";
var3 = 0;
```

Printing `var1`, `var2` and `var3` outputs:

``` output
var1: 1
var2: 1
var3: 0
```

## String data types

C has string data types for individual characters, and for strings in general.

### Character data type

In C the basic string data type is the character data type.

The `char` keyword is used to create variables of character data type.

``` {.C .syntax}
char var1 = 'char1';
```

Note that `'char1'` must be enclosed in single quotes. Single quotes are used to enclose single characters.

For example:

``` C
char var1 = 'n';
```


----

The `char` data type is an integer, so integers can be used to create characters, for example:

``` C
char var1 = 65;
```

Printing `var1` as a character outputs:

``` output
A
```


----

Not any arbitrary character can be created with the `char` data type, only the first 127 ASCII characters.

``` C
char var1 = 128;
```

Printing `var1` as a character outputs:

``` output
�
```


----

A `char` data type can be made unsigned, so that it holds values as big as 255, but this does not mean that up to 255 characters are supported, only the same first 127 ASCII characters are supported with the `unsigned char` data type.

### Strings as arrays

A string can be created as an array of characters. Arrays are explained in this document.

``` {.C .syntax}
char var1[int1] = "string1";
```

`int1` must be big enough to accommodate for `"string1"`, otherwise `"string1"` will be truncated to the size given by `int1`.

It's possible to create the string without `int1` so that the size of the array is automatically calculated.

``` {.C .syntax}
char var1[] = "string1";
```

For example:

``` C
char var1[] = "string1";
```

Printing `var1` outputs:

``` output
string1
```


----

A string can be created with a pointer to a character. Pointers are explained in this document.

``` {.C .syntax}
char *var1 = "string1";
```

The asterisk '*' means that `*var1` is a pointer to a character. Note that `"string1"` must be enclosed in double quotes. Double quotes are used to enclose strings.


----

A valid C string must be terminated with a null character. The null character is '\0'.

### Escaped characters and escape sequences

Characters and strings may be composed of escaped characters and escape sequences.
In the following tables, the output is the output of printing the variable in the example of the same table row.


----

: Escaped characters

   Escaped character            Example                 Output
  ------------------- ---------------------------- ----------------
        `'\\'`         `char *var1 = "A\\B";`{.C}   `A\B`{.output}


----

: Escape sequences

  ------------------------------------------------------------------------
   Escape sequence            Example                    Output
  ----------------- --------------------------------- --------------------
        `\n`            `char *var1 = "A\nB";`{.C}       `A`{.output}\
                                                         `B`{.output}

      `\uXXXX`         `char *var1 = "\uA888";`{.C}      `ꢈ`{.output}

    `\UXXXXXXXX`     `char *var1 = "\U0001F39B";`{.C}    `🎛`{.output}

        `\0`         `char *var1 = "str\0TRUNC";`{.C}    `str`{.output}
  ------------------------------------------------------------------------

In the escape sequence `\n`, the 'n' stands for newline. This escape sequence introduces a newline in its location.

In the escape sequence `\uXXXX`, the 'u' stands for Unicode, the 'XXXX' represents a hexadecimal number of four digits, with the code point of an UTF-8 character.

In the escape sequence `\UXXXXXXXX`, the 'U' stands for Unicode, the 'XXXXXXXX' represents a hexadecimal number of eight digits, with the code point of an UTF-8 character.

The escape sequence `\0` is the null character, in C it's used to terminate strings, so when printing the string `"str\0TRUNC"`, the `TRUNC` part is truncated because it's after the character `\0`.

## Pointers

Array names behave like pointers, except `sizeof` of the array name returns the size of the array, whereas the `sizeof` of the pointer returns the size of the pointer. For example:

``` C
int array1[10];
int *ptr1;
ptr1 = array1;
```

Printing `sizeof(array1)` and `sizeof(ptr1)` outputs:

``` output
sizeof(array1): 40
sizeof(ptr1):    8
```

## Composite types

Arrays are the basic composite type in C.

There are a few ways to define an array.

``` {.C .syntax}
data_type1 array1[int1] = {value1, value2, valueN};

data_type2 array2[] = {value1, value2, valueN};
```

In C, the array elements are indexed starting with index 0, which means that value1 is at index 0, value2 is at index 1, valueN is at index N - 1, etcetera.

For example:

``` C
int array1[3] = {4, 7, 6};

int array2[] = {4, 7, 6};
```


----

Array indexing is done with the following syntax.

``` {.C .syntax}
var1 = array1[int1];
```

This assings to `var1` the value of the element at index `int1` from `array1`.

For example:

``` C
int var1;
int array1[3] = {4, 7, 6};

var1 = array1[2];
```

Printing `var1` outputs:

``` output
6
```


----

Array indexing is also used to set or change the value of an element from an array.

``` {.C .syntax}
array1[int1] = value1;
```

This assigns `value1` to the element at index `int1` from `array1`.

For example:

``` C
int array1[3] = {4, 7, 6};
array1[2] = 55;
```

Printing `array1[2]` outputs:

``` output
55
```


----

An array can be defined with the following syntax.

``` {.C .syntax}
data_type1 array1[int1];
```

Its elements can be filled via array indexing. For example:

``` C
int array1[2];
array1[0] = 13;
array1[1] = 24;
```

`array1[0]` holds the value 13, and `array1[1]` holds the value 24.


----

Arrays can have their elements initialized by default. Numeric arrays have their elements initialized to 0 by default. String arrays have their elements initialized to `NULL` by default. For example:

``` C
int array1[3] = {7};
char *array2[3] = {"string1"};
```

Printing all the elements from the arrays `array1` and `array2` outputs:

``` output
array1[0]: 7
array1[1]: 0
array1[2]: 0

array2[0]: string1
array2[1]: (null)
array2[2]: (null)
```

`(null)` is the way the `NULL` value is printed on the machine this code was tested.

### Multidimensional arrays

Multidimensional arrays can be created by appending square bracket pairs to an array, one per dimension.

``` {.C .syntax}
data_type1 array1[][int1][intN] = {{{value1, value2}, {value1, value2}}, {{value1, value2}, {value1, value2}}};
```

The multidimensional array `{{{value1, value2}, {value1, value2}}, {{value1, value2}, {value1, value2}}}` is only placed there to show the syntax.

`intN` is the size of the innermost dimension, `int1` is the size of the second inner dimension, and so on when there are more square brackets. The outermost dimension can be left blank, to calculate its required size automatically, but this outermost dimension can also be specified like the others. For example:

``` C
int array1[3][2] = {{1, 1}, {2, 2}, {3, 3}};
```

This shows that a multidimensional array is indexed like a regular array, but with more square brackets.

Printing `array1[2][0]` outputs:

``` output
array1[2][0]: 3
```

The previous array could be placed into an array. For example:

``` C
int array1[2][3][2] = {{{1, 1}, {2, 2}, {3, 3}}, {{1, 1}, {2, 2}, {3, 3}}};
```

## Type casting

Type casting is done with the following syntax

``` {.C .syntax}
(data_type1) expression1;
```

`expression1` can be an expression or variable.

For example

``` C
int var1 = 5, var2 = 3;
double var3;
var3 = (double) var1/var2;
```

Printing `var3` outputs:

``` output
1.666667
```

Without the `(double)` type casting, printing `var3` outputs:

``` output
1.000000
```

Casting to `(double)` is necessary in this case to let the operation `var1/var2` result in a floating point number.

# OPERATORS

C supports several kinds of operators:

  - Grouping operator.
  - Arithmetic operators.
  - Relational operators.
  - Logical operators.
  - Bitwise operators.
  - Assignment operators.
  - Ternary operators.

## Grouping operator

The parentheses pair is the grouping operator.

``` {.C .syntax}
var1 = (var2 operator1 var3);
```

`operator1` is an operator, like the `+` operator that adds numbers (the `+` operator is explained in this document), for example:

``` C
int var1, var2 = 4, var3 = 5;
var1 = (var2 + var3);
```

Printing `var1` outputs:

``` output
9
```

## Arithmetic operators

There are several arithmetic operators for different arithmetic operations.

### Addition operator

The addition operator is the plus sign `+`.

``` {.C .syntax}
var1 = var2 + var3;
```

For example:

``` C
int var1, var2 = 5, var3 = 3;
var1 = var2 + var3;
```

Printing `var1` outputs:

``` output
8
```

### Subtraction operator

The subtraction operator is the minus sign `-`.

``` {.C .syntax}
var1 = var2 - var3;
```

For example:

``` C
int var1, var2 = 5, var3 = 3;
var1 = var2 - var3;
```

Printing `var1` outputs:

``` output
2
```

### Multiplication operator

The multiplication operator is the asterisk `*`.

``` {.C .syntax}
var1 = var2*var3;
```

For example:

``` C
int var1, var2 = 5, var3 = 3;
var1 = var2*var3;
```

Printing `var1` outputs:

``` output
15
```

### Division operator

The division operator is the slash `/`.

``` {.C .syntax}
var1 = var2/var3;
```

For example:

``` C
float var1, var2 = 5, var3 = 3;
var1 = var2/var3;
```

Printing `var1` outputs:

``` output
1.666667
```

### Modulo operator

The modulo operator is the percent sign `%`.

``` {.C .syntax}
var1 = var2%var3;
```

For example:

``` C
int var1, var2 = 5, var3 = 3;
var1 = var2%var3;
```

Printing `var1` outputs:

``` output
2
```

### Increment operator

The increment operator is `++`.

The increment operator can be used after a variable.

``` {.C .syntax}
var1 = var2++;
```

Placing `++` after `var2`, assigns to `var1` the value of `var2`, and then increments `var2` by 1.

For example:

``` C
int var1, var2 = 5;
var1 = var2++;
```

Printing `var1` and `var2` outputs:

``` output
var1: 5
var2: 6
```


----

The increment operator can also be used before a variable.

``` {.C .syntax}
var1 = ++var2;
```

Placing `++` before `var2`, increments `var2` by 1, and then assigns to `var1` the value of `var2`.

For example:

``` C
int var1, var2 = 5;
var1 = ++var2;
```

Printing `var1` and `var2` outputs:

``` output
var1: 6
var2: 6
```

### Decrement operator

The decrement operator is `--`.

The decrement operator can be used after a variable.

``` {.C .syntax}
var1 = var2--;
```

Placing `--` after `var2`, assigns to `var1` the value of `var2`, and then decrements `var2` by 1.

For example:

``` C
int var1, var2 = 5;
var1 = var2--;
```

Printing `var1` and `var2` outputs:

``` output
var1: 5
var2: 4
```


----

The decrement operator can also be used before a variable.

``` {.C .syntax}
var1 = --var2;
```

Placing `--` before `var2`, decrements `var2` by 1, and then assigns to `var1` the value of `var2`.

For example:

``` C
int var1, var2 = 5;
var1 = --var2;
```

Printing `var1` and `var2` outputs:

``` output
var1: 4
var2: 4
```

## Relational operators

There are several relational operators for different comparisons between values.

### Equals operator

The equals operator is `==`. It's used to check if two values are equal.

``` {.C .syntax}
bool var1;
var1 = var2 == var3;
```

The equals operator returns a boolean value, so this value is hold in a boolean variable. For example:

``` C
bool var1;
int var2 = 5, var3 = 5;
var1 = var2 == var3;
```

Printing `var1` outputs:

``` output
1
```

### Not equals operator

The not equals operator is `!=`. It's used to check if two values are different.

``` {.C .syntax}
bool var1;
var1 = var2 != var3;
```

The not equals operator returns a boolean value, so this value is hold in a boolean variable. For example:

``` C
bool var1;
int var2 = 5, var3 = 5;
var1 = var2 != var3;
```

Printing `var1` outputs:

``` output
0
```

### Greater than operator

The greater than operator is the greater than sign `>`. It's used to check if a value is greater than another.

``` {.C .syntax}
bool var1;
var1 = var2 > var3;
```

The greater than operator returns a boolean value, so this value is hold in a boolean variable. For example:

``` C
bool var1;
int var2 = 7, var3 = 4;
var1 = var2 > var3;
```

Printing `var1` outputs:

``` output
1
```

### Greater than or equal to operator

The greater than or equal to operator is `>=`. It's used to check if a value is greater than or equal to another.

``` {.C .syntax}
bool var1;
var1 = var2 >= var3;
```

The greater than or equal to operator returns a boolean value, so this value is hold in a boolean variable. For example:

``` C
bool var1;
int var2 = 5, var3 = 5;
var1 = var2 >= var3;
```

Printing `var1` outputs:

``` output
1
```

### Less than operator

The less than operator is the less than sign `<`. It's used to check if a value is less than another.

``` {.C .syntax}
bool var1;
var1 = var2 < var3;
```

The less than operator returns a boolean value, so this value is hold in a boolean variable. For example:

``` C
bool var1;
int var2 = 4, var3 = 7;
var1 = var2 < var3;
```

Printing `var1` outputs:

``` output
1
```

### Less than or equal to operator

The less than or equal to operator is `<=`. It's used to check if a value is less than or equal to another.

``` {.C .syntax}
bool var1;
var1 = var2 <= var3;
```

The less than or equal to operator returns a boolean value, so this value is hold in a boolean variable. For example:

``` C
bool var1;
int var2 = 5, var3 = 5;
var1 = var2 <= var3;
```

Printing `var1` outputs:

``` output
1
```

## Logical operators

There are several logical operators for different logical operations.

### Logical AND operator

The logical AND operator is `&&`. It's used to check if two boolean values are both true, so that the value one AND the value two are true.

``` {.C .syntax}
bool var1, var2 = value2, var3 = value3;
var1 = var2 && var3;
```

For example:

``` C
bool var1, var2 = true, var3 = false;
var1 = var2 && var3;
```

Printing `var1` outputs:

``` output
0
```

### Logical OR operator

The logical OR operator is `||`. It's used to check if two boolean values are either one or both true, so that the value one OR the value two are true.

``` {.C .syntax}
bool var1, var2 = value2, var3 = value3;
var1 = var2 || var3;
```

For example:

``` C
bool var1, var2 = true, var3 = false;
var1 = var2 || var3;
```

Printing `var1` outputs:

``` output
1
```

### Logical NOT operator

The logical NOT operator is the exclamation mark `!`. It's used to flip a boolean value, from `true` to `false`, or from `false` to `true`.

``` {.C .syntax}
bool var1, var2 = value2;
var1 = !var2;
```

For example:

``` C
bool var1, var2 = true;
var1 = !var2;
```

Printing `var1` and `var2` outputs:

``` output
var1: 0
var2: 1
```

## Bitwise operators

There are several bitwise operators for different bitwise operations.

### Bitwise AND operator

The bitwise AND operator is the ampersand `&`. It's used to AND the digits of two binary numbers, as shown below.

``` {.C .syntax}
int var1, var2 = value2, var3 = value3;
var1 = var2 & var3;
```

For example:

``` C
int var1, var2 = 0xA, var3 = 0x3;
var1 = var2 & var3;
```

Printing `var1` outputs:

``` output
0x2
```

As can be seen (after converting these hexadecimal numbers into binary numbers), only in the places where both binary numbers have a 1, there is a 1 in the result.

### Bitwise OR operator

The bitwise OR operator is the vertical bar `|`. It's used to OR the digits of two binary numbers, as shown below.

``` {.C .syntax}
int var1, var2 = value2, var3 = value3;
var1 = var2 | var3;
```

For example:

``` C
int var1, var2 = 0xA, var3 = 0x3;
var1 = var2 | var3;
```

Printing `var1` outputs:

``` output
0xB
```

As can be seen (after converting these hexadecimal numbers into binary numbers), in the places where either one or both binary numbers have a 1, there is a 1 in the result.

### Bitwise XOR operator

The bitwise XOR operator is the caret `^`. It's used to XOR the digits of two binary numbers, as shown below.

``` {.C .syntax}
int var1, var2 = value2, var3 = value3;
var1 = var2 ^ var3;
```

For example:

``` C
int var1, var2 = 0xA, var3 = 0x3;
var1 = var2 ^ var3;
```

Printing `var1` outputs:

``` output
0x9
```

As can be seen (after converting these hexadecimal numbers into binary numbers), in the places where one but not both binary numbers have a 1, there is a 1 in the result.

### Bitwise NOT operator

The bitwise NOT operator is the tilde `~`. It's used to NOT the digits of a binary number, as shown below.

``` {.C .syntax}
int var1, var2 = value2;
var1 = ~var2;
```

For example:

``` C
int var1, var2 = 0xA;
var1 = ~var2;
```

Printing `var1` outputs:

``` output
0xFFFFFFF5
```

As can be seen (after converting these hexadecimal numbers into binary numbers), the NOT operation is the result of flipping each digit from 1 to 0, or from 0 to 1. Flipping only the number 0xA results in the number 0x5, but the output shows the number 0xFFFFFFF5, because an `int` in this case has 4 bytes, with two hexadecimal digits per byte, so the number 0xA expressed as an `int` is the number 0x0000000A, which after the NOT operation results in the number 0xFFFFFFF5.

### Bitwise left shift operator

The bitwise left shift operator is `<<`. It's used to shift the digits of a binary number to the left.

``` {.C .syntax}
int var1, var2 = value2, var3 = value3;
var1 = var2 << var3;
```

For example:

``` C
int var1, var2 = 0x3, var3 = 1;
var1 = var2 << var3;
```

Printing `var1` outputs:

``` output
0x6
```

As can be seen (after converting these hexadecimal numbers into binary numbers), each binary digit is moved to the left 1 time, which creates a new digit. A 0 is placed in each new digit needed.

### Bitwise right shift operator

The bitwise right shift operator is `>>`. It's used to shift the digits of a binary number to the right.

``` {.C .syntax}
int var1, var2 = value2, var3 = value3;
var1 = var2 >> var3;
```

For example:

``` C
int var1, var2 = 0xE, var3 = 1;
var1 = var2 >> var3;
```

Printing `var1` outputs:

``` output
0x7
```

As can be seen (after converting these hexadecimal numbers into binary numbers), each binary digit is moved to the right 1 time, which deletes the first digit. Shifting a binary number to the right a given amount of times, deletes that amount of digits at the right side of the number.

## Assignment operators

The basic assignment operator is the equal sign `=`. It assigns the value in its right side, to the variable in its left side.

``` {.C .syntax}
var1 = var2;
```

This assigns the value of var2 to var1. For example:

``` C
int var1, var2 = 13;
var1 = var2;
```

Printing `var1` outputs:

``` output
13
```


----

Given that the assignment operator `=` works by assigning the value in its right side to the variable in its left side, it is possible to change the value of a variable and then assign that changed value to the variable itself. For example:

``` C
int var1 = 10;
var1 = var1 + 1;
```

In the right side of the `=` the value of `var1` is 10, which is then added to 1, and that results in 11. The value 11 is assigned to `var1`. This shows that in an assignment operation, the right side is evaluated first, and then the result is assigned to the left side.

Printing `var1` outputs:

``` output
11
```

### Addition assignment operator

The addition assignment operator is `+=`. It adds a value to a variable, and then assigns the result to that same variable.

``` {.C .syntax}
var1 += var2;
```

This is equivalent to the statement `var1 = var1 + var2;`. For example:

``` C
int var1 = 5, var2 = 4;
var1 += var2;
```

Printing `var1` outputs:

``` output
9
```

### Subtraction assignment operator

The subtraction assignment operator is `-=`. It subtracts a value from a variable, and then assigns the result to that same variable.

``` {.C .syntax}
var1 -= var2;
```

This is equivalent to the statement `var1 = var1 - var2;`. For example:

``` C
int var1 = 5, var2 = 4;
var1 -= var2;
```

Printing `var1` outputs:

``` output
1
```

### Multiplication assignment operator

The multiplication assignment operator is `*=`. It multiplies a value by a variable, and then assigns the result to that same variable.

``` {.C .syntax}
var1 *= var2;
```

This is equivalent to the statement `var1 = var1*var2;`. For example:

``` C
int var1 = 5, var2 = 4;
var1 *= var2;
```

Printing `var1` outputs:

``` output
20
```

### Division assignment operator

The division assignment operator is `/=`. It divides a variable by a value, and then assigns the result to that same variable.

``` {.C .syntax}
var1 /= var2;
```

This is equivalent to the statement `var1 = var1/var2;`. For example:

``` C
int var1 = 20, var2 = 2;
var1 /= var2;
```

Printing `var1` outputs:

``` output
10
```

### Modulo assignment operator

The modulo assignment operator is `%=`. It takes the modulo of a variable over a value, and then assigns the result to that same variable.

``` {.C .syntax}
var1 %= var2;
```

This is equivalent to the statement `var1 = var1%var2;`. For example:

``` C
int var1 = 5, var2 = 3;
var1 %= var2;
```

Printing `var1` outputs:

``` output
2
```

### Bitwise AND assignment operator

The bitwise AND assignment operator is `&=`. It does the bitwise AND operation with a variable and a value, and then assigns the result to that same variable.

``` {.C .syntax}
var1 &= var2;
```

This is equivalent to the statement `var1 = var1 & var2;`. For example:

``` C
int var1 = 0xA, var2 = 0x3;
var1 &= var2;
```

Printing `var1` outputs:

``` output
0x2
```

### Bitwise OR assignment operator

The bitwise OR assignment operator is `|=`. It does the bitwise OR operation with a variable and a value, and then assigns the result to that same variable.

``` {.C .syntax}
var1 |= var2;
```

This is equivalent to the statement `var1 = var1 | var2;`. For example:

``` C
int var1 = 0xA, var2 = 0x3;
var1 |= var2;
```

Printing `var1` outputs:

``` output
0xB
```

### Bitwise XOR assignment operator

The bitwise XOR assignment operator is `^`. It does the bitwise XOR operation with a variable and a value, and then assigns the result to that same variable.

``` {.C .syntax}
var1 ^= var2;
```

This is equivalent to the statement `var1 = var1 ^ var2;`. For example:

``` C
int var1 = 0xA, var2 = 0x3;
var1 ^= var2;
```

Printing `var1` outputs:

``` output
0x9
```

### Bitwise left shift assignment operator

The bitwise left shift assignment operator is `<<=`. It does the bitwise left shift operation, shifting a variable by a given value, and then assigns the result to that same variable.

``` {.C .syntax}
var1 <<= var2;
```

This is equivalent to the statement `var1 = var1 << var2;`. For example:

``` C
int var1 = 0x3, var2 = 1;
var1 <<= var2;
```

Printing `var1` outputs:

``` output
0x6
```

### Bitwise right shift assignment operator

The bitwise right shift assignment operator is `>>=`. It does the bitwise right shift operation, shifting a variable by a given value, and then assigns the result to that same variable.

``` {.C .syntax}
var1 >>= var2;
```

This is equivalent to the statement `var1 = var1 >> var2;`. For example:

``` C
int var1 = 0xE, var2 = 1;
var1 >>= var2;
```

Printing `var1` outputs:

``` output
0x7
```

## Ternary operators

The ternary operators serve to make an if else statement, but using operators.

In the ternary operators, the if operator is the question mark `?`, and the else operator is the colon `:`. They must be used together, so the if operator `?` can't be used without the else operator `:`.

``` {.C .syntax}
bool var2;
var1 = var2 ? value_if1 : value_else1;
```

If `var2` is `true`, then this assigns `value_if1` to `var1`. Else, if `var2` is `false`, then this assigns `value_else1` to `var1`. For example:

``` C
int var1;
bool var2 = false;
var1 = var2 ? 12 : -9;
```

Printing `var1` outputs:

``` output
-9
```

# CONTROL FLOW

In C, there are three kinds of control flow structures: goto statements, conditional statements, and loops.

## Goto statements

Goto statements make the execution go to a labeled line of code. The `goto` keyword is used for this.

``` {.C .syntax}
label1:;

statements1;

goto label1;
```

The `label1:;` statement is ignored, then `statements1` are executed, and then the `goto label1;` statement makes the execution go to the `label1:` label. `statements1` are executed again, so this particular syntax creates an infinite loop in which `statements1` are executed for as long as the program is running.

``` {.C .syntax}
goto label2;

statements2;

label2:;
```

`statements2` are never executed, because the `goto label2;` statement makes the execution go to the `label2:` label, skipping `statements2`.

As can be seen, labels are created like any valid C name, ended with a colon (and then the statement ended with a semicolon as regular). The goto statement can be placed before or after its label.

## Conditional statements

### If-else conditional statement

The `if` keyword is used to make a basic conditional statement.

``` {.C .syntax}
if (condition1)
{
    statements1;
}
```

`condition1` is any expression that evaluates to a boolean value. Any valid C expression can be seen as a boolean value, so in reality any expression can be used as `condition1`. The values 0 and `false` make `condition1` false, other values make `condition1` true.

Note that `condition1` must be enclosed in parentheses. `statements1` are executed when `condition1` evaluates to true. For example:

``` C
if (25)
{
    printf("This always executes");
}
```

Given that `(25)` evaluates to true, the statement with the `printf` function always executes when running this code.


----

A conditional statement can have more conditions, one after the other, so that if one condition is false, a next condition may be true and execute that code. These other conditions are created with the `else if` keyword.

``` {.C .syntax}
if (condition1)
{
    statements1;
}
else if (condition2)
{
    statements2;
}
else if (conditionN)
{
    statementsN;
}
```

Each condition is checked once, and if true then its statements are executed, and none of the other conditions are checked, so only the first condition to be true (if any) has its statements executed. For example:

``` C
int var1 = 20;
if (var1 < 20)
{
    printf("var1 is less than 20\n");
}
else if (var1 == 20)
{
    printf("var1 is 20\n");
}
```

The condition `(var1 < 20)` is evaluated, and it's false because of the statement `int var1 = 20;`. Next the condition `(var1 == 20)` is evaluated and it's true, so the statement `printf("var1 is 20\n");` is executed.


----

In a conditional, if all the conditions are false, then a set of statements can be executed. This is done with the `else` keyword.

``` {.C .syntax}
if (condition1)
{
    statements1;
}
else if (conditionN)
{
    statementsN;
}
else
{
    statementsN+1;
}
```

If all the conditions are false, from `condition1` to `conditionN`, then `statementsN+1` are executed. For example:

``` C
int var1 = 21;
if (var1 < 20)
{
    printf("var1 is less than 20\n");
}
else if (var1 == 20)
{
    printf("var1 is 20\n");
}
else
{
    printf("Other\n");
}
```

In this example, the statement `int var1 = 21;` makes all conditions false, so the statement `printf("Other\n");` is executed.


----

`if`, `else if`, and `else` statements can be nested inside each other. For example:

``` C
if (condition1)
{
    statements1;
    if (condition2)
    {
        statements2;
    }
    else if (condition3)
    {
        statements3;
        if (condition4)
        {
            statements4;
        }
    }
}
```


----

Conditional statements can be written in a single line.

``` C
if (condition1) statement1; else if (condition2) statement2; else statement3;
```

### Switch-case conditional statement

Instead of using a conditional statement with several `else if`, `else if`, `else if`, that check for several possible values of an integer variable, a `switch` statement can be used.

``` {.C .syntax}
switch (var1)
{
    case value1 :
        statements1;
        break;
    case value2 :
        statements2;
        break;
    case valueN :
        statementsN;
        break;
    default :
        statementsN+1;
}
```

A `switch` statement only works if `var1` is an integer type, so it can be a `char`, `int`, or any of their modified types (such as `short` for example).

`value1` through `valueN` are the possible values of `var1` that are tested, so that if the value of `var1` is equal to one values in the list of values from `value1` to `valueN`, then its corresponding statements are executed. For example, if tha value of `var1` is equal to `valueN` then statementsN are executed. The rest of statements are not executed.

Each value from `value1` to `valueN` is preceded by the `case` keyword, and is followed by a colon. The `break` keyword is necessary because when omitted, all the following statements will be executed, until a `break` keyword is found, or until the end of the `switch` statement.

The `default` keyword is used for the case in which none of the values matches the value of `var1`. In this case, `statementsN+1` are executed.

When `var1` is a `char`, it can only accept one of the 128 values possible in a `char` type. When `var1` is an `int` it can accept any integer number that can be hold by an `int` variable.

For example:

``` C
int var1 = 100;
switch (var1)
{
    case 10 :
        printf("var1 is 10\n");
        break;
    case 100 :
        printf("var1 is 100\n");
        break;
    case 1000 :
        printf("var1 is 1000\n");
        break;
    default :
        printf("var1 is another value\n");
}
```

This executes the `printf("var1 is 100\n");` statement. Deleting the `break;` statement under, would also result in the execution of the `printf("var1 is 1000\n");` statement.

`switch` statements can also be nested if needed.

## Loops

C has `for`, `while`, and `do while` loops.

### For loop

The basic loop is made with the `for` keyword. A `for` loop executes its statements a counted amount of times (or iterations).

``` {.C .syntax}
for (start_statement1; condition1; statementN)
{
    statements1;
}
```

`start_statement1` is a statement that is executed only once at the start of the loop, before executing `statements1` for the first iteration. 

`condition1` can be any condition, the `statements1` keep being executed for as long as `condition1` evaluates to true. `condition1` is commonly used to check the value of the iterator.

`statementN` is a statement that is executed at the very end of each iteration, commonly used to change the value of the iterator, which is usually the last step of an iteration.

Given these definitions, a possible `for` loop example is the following:

``` C
int it1 = 5;
for (printf("Start of loop\n"); it1 < 20; printf("End of iteration\n"))
{
    it1 *= 2;
}
```

Executing this example code outputs:

``` output
Start of loop
End of iteration
End of iteration
```

'End of iteration' appears twice because this loop is repeated two times. Initially `it1` is 5, then the statement `it1 *= 2;` duplicates `it1`, so at the end of the first iteration `it1` is 10. In the second iteration `it1` is 20, so when the third iteration would start, the condition `it1 < 20` is false, and the `for` loop ends.

A more common way to write a `for` loop in C, is to use the iterator `it1` in the three parts of the parentheses of the `for` loop. For example:

``` C
for (int it1 = 0; it1 < 3; it1++)
{
    printf("it1: %d\n", it1);
}
```

This is more common because it shows the count of iterations that the `for` loop will do, in this case, three iterations (because `it1` starts at 0 and ends at 2).

Executing this example code outputs:

```
it1: 0
it1: 1
it1: 2
```

### While loop

There is the `while` loop in C, which is a loop that iterates while a given condition evaluates to true.

``` {.C .syntax}
while (condition1)
{
    statements1
}
```

`condition1` is checked at the start of each iteration (including the first iteration), and if it's true then `statements1` are executed, otherwise the loop ends, so `statements1` must include a way to modify `condition1` so that eventually it evaluates to false (unless an infinite loop is desired). For example

``` C
int it1 = 0;
while (it1 < 3)
{
    printf("it1: %d\n", it1);
    it1 += 1;
}
```

The statement `it1 += 1;` modifies `it1` inside the `while` loop, because otherwise `it1` does not change and the `while` loop becomes an infinite loop.

Executing this example code outputs:

``` output
it1: 0
it1: 1
it1: 2
```

### Do while loop

C also has the `do while` loop, which used the `do` and the `while` keywords.

``` {.C .syntax}
do
{
    statements1
} while (condition1);
```

This works the same as the regular `while` loop, except that `condition1` is checked at the end of each iteration, which means that `statements1` will be executed at least once, even when `condition1` evaluates to false. For example:

``` C
int it1 = 0;
do
{
    printf("Do while loop\n");
} while (it1 != 0);
```

The condition `(it1 != 0)` is false because `it1` is 0, so this loop executes the statement `printf("Do while loop\n");` only once.

### Break out of a loop

A loop can be stopped with the `break` keyword.

``` {.C .syntax}
loop1
{
    if (condition1) break;
    statements1;
}
```

`loop1` is ended if `condition1` evaluates to true in any iteration. For example:

``` C
int it1 = 0;
while (it1 < 3)
{
    if (it1 == 1) break;
    printf("it1: %d\n", it1);
    it1++;
}
```

Executing this example code outputs:

``` output
it1: 0
```

### Continue at the next iteration of a loop

The current iteration of a loop can be stopped with the `continue` keyword. Execution continues at the start of the next iteration.

``` {.C .syntax}
loop1
{
    if (condition1) continue;
    statements1;
}
```

If `condition1` evaluates to true in any iteration, `statements1` are skipped in that iteration, and the loop continues at the next iteration. For example:

``` C
int it1 = 0;
while (it1 < 3)
{
    if (it1 == 1) { it1++; continue; }
    printf("it1: %d\n", it1);
    it1++;
}
```

In `if (it1 == 1) { it1++; continue; }` it's necessary to add the `it1++;` statement, otherwise `it1` remains being 1, and the loop becomes infinite.

Executing this example code outputs:

``` output
it1: 0
it1: 2
```

# FUNCTIONS

Functions are defined with the following syntax.

``` {.C .syntax}
return_data_type1 func1(data_type1 param1, data_typeN paramN)
{
    statements1;
    return value1;
}
```

`func1` is the name of the function. `param1` through `paramN` are the parameters of the function, commonly used in `statements1` to calculate `value1`. `value1` must have the data type `return_data_type1`, and it must be placed after the `return` keyword.

## Function signature

In C, the signature of a function is written with the following syntax.

``` {.C .syntax}
return_data_type1 func1(param_data_type1, param_data_typeN);
```

For example:

``` C
int func1(char, char*);
```

`func1` returns an `int` data type, and it takes two arguments, a `char` data type, and then a `char*` data type.

Writing the function signature alone is the function declaration (so, it must be defined elsewhere in the code, or in an included header).

## Function call

A function is called with the following syntax.

``` {.C .syntax}
var1 = func1(arg1, argN);
```

`var1` is a variable of the same data type as the return value of `func1`, because `var1` holds the return value of `func1`. `arg1` through `argN` are the arguments passed to the function. The arguments replace the parameters inside the function, so there is one argument per parameter (unless the parameters are optional, of course).


----

By default, an argument is passed to a function by value.

``` C
// Before the `main` function:
void func1(int arg1)
{
    arg1 = 55;
}

// Inside the `main` function:
int var1 = 11;
func1(var1);
```

Printing `var1` after calling `func1(var1)` outputs:

``` output
11
```

This shows that `var1` was not modified by `func1`, because `var1` was passed by value.


----

An argument can be passed by reference to a function. Pointers are used to pass by reference.

``` {.C .syntax}
// Before the `main` function:
void func1(int *arg1)
{
    arg1[0] = 55;
}

// Inside the `main` function:
int var1 = 11;
int *ptr1 = &var1;
func1(ptr1);
```

`ptr1` is a pointer to `var1`.

Printing `var1` after calling `func1(ptr1)` outputs

``` output
55
```

## The `void` keyword

The `void` keyword can be used in functions. Using the `void` keyword as the data type of the return value of a function, means that the function returns nothing.

``` {.C .syntax}
void func1()
{
    statements1;
}
```

Note that `func1` has no return statement.


----

The `void` keyword is used to make a function take no arguments.

``` {.C .syntax}
data_type1 func1(void)
{
    statements1;
    return ret_val1;
}
```

For example:

``` C
int func1(void)
{
    return 5;
}
```

## Arrays in functions

Arrays can be passed as arguments to functions, and returned as return values of functions.

The function signature of a function that takes arrays as arguments, and returns an array, has the following syntax.

``` {.C .syntax}
return_data_type1 * func1(param_data_type1 *, param_data_typeN *)
```

As can be seen, arrays are passed and returned via pointers. For example:

``` C
int * func1(int *);
```

`func1` takes an `int` pointer, which can be the name of an `int` array, and returns an `int` pointer, which can be the name of another `int` array.

An example definition for `func1` is the following:

``` C
int * func1(int *param_array1)
{
    static int return_array1[3];
    return_array1[1] = param_array1[1]*2;
    return return_array1;
}
```

`return_array1` is made `static` because otherwise it's allocated memory may be overwritten. The `static` keyword in this case ensures that the memory allocated for `return_array1` is still allocated after the function call finishes.

`func1` in this case doesn't really do anything useful, it assigns to its second element, twice the second element of `param_array1`. It's just for demonstration.

## Recursion

Function recursion can be done with the following syntax.

``` {.C .syntax}
return_data_type1 func1(params1)
{
    statements1;

    if (condition1) return value1;

    var1 = expression1_with_func1(args1);

    statements2;

    return var1;
}
```

`statements1` are executed before the recursion, and `statements2` are executed after the recursion. The conditional statement `if (condition1) return value1;` ensures that the function has a way to stop recursion, so this conditional statement should be placed before calling `func1` inside itself.

`value1` is the value returned when recursion stops, so it is the initial value that will be used by all the previous recursions made.

`expression1_with_func1(args1)` is an expression that uses `func1(args1)`. It's necessary to modify `func1(args1)`, because in the case that `var1 = func1(args1)` it happens that `var1 = value1` in all the recursions, so the idea is to modify `value1` to change `var1`. This expression can give the logic or intention of the recursion.

A common basic example of recursion, is a function that calculates the factorial of a positive integer. The following is a full code example:

``` C
#include <stdio.h>

int func1(int param1)
{
    printf("Statements before recursion\n");

    if (param1 <= 1) { printf("First statement after recursion\n"); return 1; }

    int var1;
    var1 = param1 * func1(param1 - 1);

    printf("Value of var1 in this recursion call: %d\n", var1);
    
    return var1;
}

int main()
{

    int num1;
    num1 = func1(5);
    printf("\nThe factorial of 5 is: %d\n", num1);

    return 0;
}
```

Executing this example code outputs:

``` output
Statements before recursion
Statements before recursion
Statements before recursion
Statements before recursion
Statements before recursion
First statement after recursion
Value of var1 in this recursion call: 2
Value of var1 in this recursion call: 6
Value of var1 in this recursion call: 24
Value of var1 in this recursion call: 120

The factorial of 5 is: 120
```

As can be seen from this output, the statements before the recursion are executed first, until recursion stops. In this case the argument is 5 because the factorial of 5 is being calculated, so the first 5 lines of output say 'Statements before recursion'. The next 5 lines of output come from the statements after recursion.

## Variable arguments

To use variable arguments, the `<stdarg.h>` header must be included.

``` {.C .syntax}
#include <stdarg.h>
```

The following syntax shows how to write functions that make use of variable arguments.

``` {.C .syntax}
return_data_type1 func1(param1, paramN, ...)
{
    statements1;

    va_list args1;

    va_start(args1, paramN);

    statement1_with_va_arg(args1, data_type1);
    statementM_with_va_arg(args1, data_typeM);

    va_end(args1);

    return value1;
}
```

This syntax shows the various parts of the `<stdarg.h>` header, that are used to manage variable arguments.

`param1` through `paramN` are the obligatory, non-variable, regular parameters. The last parameter of `func1` is the ellipsis `...`, this indicates that the function receives a variable amount of arguments, placed after `paramN`.

Inside `func1`, a few names starting with `va_` can be observed. These names are defined in the `<stdarg.h>` header. `va_list` is a data type for the list of variable arguments, so `args1` is a variable that holds the list of variable arguments.

The `va_start(args1, paramN)` function, starts the use of `args1` (so that the `va_arg` function works, see below). `paramN` is the second argument in `va_start(args1, paramN)`, because `paramN` is supposed to contain information about the data types of the variable arguments, so `func1` should have information about these data types, and this is commonly passed to `func1` via `paramN`.

The `va_arg(args1, data_typeM)` function, takes the `M` argument in `args1` and treats it as if it was a `data_typeM`. The next time that `va_arg` is called, it has the form `va_arg(args1, data_typeM+1)`, which takes the `M+1` argument in `args1` and treats it as if it was a `data_typeM+1`. So the `va_arg` function takes each individual variable argument, sequentially. The next time `va_arg` is called, it takes the next variable argument, and so on. It's common to use a loop, to loop through all the variable arguments.

The `va_end` function, ends the use of `args1`. `va_start` can be called again, after having called `va_end`, to process the variable arguments again if needed.

An example function definition using variable arguments is the following.

``` C
// At the start of the file:
#include <stdarg.h>

// Definition of the function with variable arguments, placed before the `main` function:
void func1(int index1, ...)
{
    va_list args1;
    
    va_start(args1, index1);

    if (index1 == 1)
    {
        int arg1 = va_arg(args1, int);
        printf("arg is: %d\n", arg1);
    }
    else if (index1 == 2)
    {
        double arg1 = va_arg(args1, double);
        int arg2 = va_arg(args1, int);
        printf("arg1 is: %f\narg2 is: %d\n", arg1, arg2);
    }

    va_end(args1);
}

// Inside the `main` function:
func1(1, 60);
printf("\n");
func1(2, 9.877, 130);
```

Executing this example code outputs:

``` output
arg is: 60

arg1 is: 9.877000
arg2 is: 130
```

The `index1` parameter of the `func1` function determines the amount of variable arguments that will be parsed, and the data type of each variable argument. This means that the user of `func1` should know how `func1` parses the variable arguments, otherwise it could produce undefined behavior. This happens with the `printf` function, the user of the `printf` function must know how to pass information about the data types of the arguments to the function, because the `printf` function uses variable arguments.

# PACKAGES

# HEADERS

# DIRECTIVES

The C language support directives, they are placed at the start of the file.

``` {.C .syntax}
#directive1

rest_of_file1
```


----

The `#define` directive is used to define macros. Macros are code that replaces other code, so macros can be used as variables, or as functions. By convention, macros are named using uppercase letters.


----

Macros can be created as variables

``` {.C .syntax}
#define MACRO1 value1
```

For example:

``` C
#define FIRST_NUMBER 6
```

This macro defines `FIRST_NUMBER` as a variable, but given that macros can't be changed in the code, `FIRST_NUMBER` is effectively a constant.


----

To create a macro as a variable, that holds a multiline string, use the following syntax.

``` {.C .syntax}
#define STRING1 "string starts"\
                " and continues"
```

Printing `STRING1` outputs:

``` output
string starts and continues
```


----

**Macro as a function**

``` {.C .syntax}
#define MACRO1(arg1, arg2) function_body1
```

For example:

``` C
#define F1(A, B) 2*A + B
```


----

The `#include` directive is used to include headers. Headers are files that declare or define variables, functions, and macros, so that they can be used in C source code. This is useful for example, to include functions defined in other files, so that it is not necessary to create those functions from scratch.

Headers are files that have the `.h` file extension, written in a plain text format. They are external files to the C source code files with the `.c` file extension.


----

Headers are searched for in a search path, because they are external files. The search path is a set of directories where the compiler searches for headers when they are included in a `.c` file being compiled.

A header that is in one of the directories in the search path, is included with the following syntax.

``` {.C .syntax}
#include <relative/path/to/header1.h>
```

`header1.h` is called a system header, because the search path is made of directories where the compiler expects the operating system to place headers to be used by any program that includes them.

The directory `relative/path/to/` is a subdirectory from one of the directories in the search path.

In case that `relative/path/to/header1.h` leads to two different `header1.h` files, the compiler will choose only one of them. To avoid this ambiguity, use the following syntax.

``` {.C .syntax}
#include </path/to/header1.h>
```

`/path/to/header1.h` is the full path of `header1.h`. This avoids ambiguity as to which header file is included.


----

Custom headers, that exist in the same directory or in a subdirectory of a `.c` file being compile, can be included with a different syntax.

``` {.C .syntax}
#include "relative/path/to/header1.h"
```

`relative/path/to/header1.h` is a relative path, relative to the `.c` file that includes `header1.h`.

This syntax of `"header1.h"` has precedence over the syntax for system headers `<header1.h>`, so writing `#include "header1.h"` includes the file `header1.h` in the same directory as the `.c` file that includes it, even if there is a system header called `header1.h`.

# ERROR AND EXCEPTION HANDLING

# OBJECT ORIENTED PROGRAMMING

# COMMAND LINE INTERFACE

# DEBBUGING

# SYSTEM CALLS

# BUILDING A PROJECT

# STANDARD LIBRARY

## The `printf` function

The `printf` function deserves its own section in the standard library. This function is used as a basic interaction between the programmer and the programs being created by them in C. It is used as a basic debugging function, to print the value of a variable in the program, and check if the variable has an expected value or not.

After creating and debugging a program, the amount of calls to the `printf` function may be reduced, compared to the amount of calls during development. This depends on the type of program being made. A program that uses the GUI of the operating system, could need the `printf` function less than a program that uses the CLI of the operating system. In theory, a purely GUI program would never need to call the `printf` function, but in practice, most GUI programs can be started from the CLI, and GUI programs print to standard output about their execution.

It may happen that a program does not call `printf` directly, but rather calls a modified `printf` function.


----

The signature of the `printf` function is:

``` {.C .syntax}
printf("text %format1 text %formatN text", var1, varN);
```

Only the first argument is obligatory, the rest are optional arguments. There is one `%formatN` for each `varN`.


----

In the `printf` function signature, `%formatN` is the format specifier, it minimally consists of the percent sign and a single character that determines the expected data type format of its corresponding `varN`. The format specifier specifies the data type that `varN` must have. The format specifier is used to format `varN` according to its data type. A single data type can have a few different format specifiers to format said data type.

The format specifier can be modified, this is done with format modifiers. The following is the syntax for a format specifier that has format modifiers.

``` {.C .syntax}
%flag1width1.precision1length1specifier1
```

As can be seen, the format modifiers and the specifier at the end are written together with no spaces between them. All the modifiers are optional, the period goes with the `.precision1` modifier.


----

: Format specifiers

  -------------------------------------------------------------
   Format specifier            Example               Output
  ------------------ --------------------------- --------------
         `%d`           `int var1 = 5;`{.C}      `5`{.output}
                      `printf("%d", var1);`{.C}

         `%f`          `float var1 = 7.3`{.C}    `7.3`{.output}
                      `printf("%f", var1);`{.C}
  -------------------------------------------------------------

In `%d`, the 'd' stands for digit. It's used to format variables of data type `int` as regular digits.

In `%f`, the 'f' stands for float. It's used to format variables of data type `float` or `double`.

## String functions

C has several string manipulation functions to operate over strings. Many of these functions are defined by including the `string.h` header.

``` {.C .syntax}
#include <string.h>
```


----

The `strcpy` function copies a string into another. This function is necessary because an array can't be assigned to another array, unlike non-array variables. For example, an `int` variable can be assigned to another `int` variable, which is a way of copying the first `int` variable into the second.

``` {.C .syntax}
#include <string.h>
char *source_string1 = "string1";
char destination_string1[int];
strcpy(destination_string1, source_string1);
```

This copies `source_string1` into `destination_string1`, replacing the contents of `destination_string1`. This means that `int1` must be big enough to accommodate for `"string1"`.

`int1` is the array size of `destination_string1`, it must be explicitly known, to ensure that copying a string into it, does not attempt to overwrite other memory from the program. For example:

``` C
#include <string.h>
char *source_string1 = "string1";
char destination_string1[7];
strcpy(destination_string1, source_string1);
```

Printing `destination_string1` outputs:

``` output
string1
```


----

The `strcat` function concatenates two strings.

``` {.C .syntax}
#include <string.h>
char string1[int1] = "start";
char *appended_string1 = "_end";
strcat(string1, appended_string1);
```

This appends `appended_string1` to `string1`, thus modifying `string1`, so `int1` must be big enough to accommodate both `string1` and `appended_string1`. For example:

``` C
#include <string.h>
char string1[9] = "start";
char *appended_string1 = "_end";
strcat(string1, appended_string1);
```

Printing both `string1` and `appended_string1` outputs:

``` output
string1:          start_end
appended_string1: _end
```


----

The `strlen` function returns the amount of bytes of a string, before the string termination character `\0` (see the null character).

``` C
#include <string.h>
int var1;
char *var2 = "stríng1";
var1 = strlen(var2);
```

`"stríng1"` has a `\0` automatically placed at its end.

Printing `var1` outputs:

``` output
8
```

`"string1"` has 7 characters, with 1 byte per character it's the same as 7 bytes. But the `"í"` in `"stríng1"` counts as two bytes because of the diacritic, so the total count is 8 bytes.


----

The `strcmp` function is used to compare two strings lexicographically. It returns the lexicographical difference between the first differing characters of the two strings, or 0 if both strings have all the same characters. For example:

``` C
#include <string.h>
int var1;
char *var2 = "sar";
char *var3 = "scr";
var1 = strcmp(var2, var3);
```

Printing `var1` outputs:

``` output
-2
```

This is because the lexicographical difference between 'a' and 'c' is -2.

Another example:

``` C
#include <string.h>
int var1;
char *var2 = "Ă";
char *var3 = "Ċ";
var1 = strcmp(var2, var3);
```

Printing `var1` outputs:

``` output
-8
```

This shows that the lexicographical order of the `strcmp` function, uses (or complies with) the Unicode UTF-8 character encoding. This is because the characters 'Ă' and 'Ċ' are both outside the ASCII character encoding, and their lexicographical difference in UTF-8 is exactly -8, meaning that 'Ċ' is 8 characters after 'Ă' in the lexicographical order given by UTF-8.


----

The `strchr` function finds the first occurrence of a given character in a given string, and returns a substring that starts at that occurrence, and goes until the end of the given string. For example:

``` C
char char1 = 'c';
char *var1 = "stricng1";
char *var2;

var2 = strchr(var1, char1);
```

This finds the first occurrence of `char1` (which is `'c'`) in the string `var1`. `var2` is the substring starting from `'c'` to the end of `var1`. If `char1` is not found in `var1`, then the `strchr` function returns a `NULL` value.

Printing `var2` outputs:

``` output
cng1
```


----

The `strstr` function finds the first occurrence of a given substring in a given string, and returns a substring that starts at that occurrence, and goes until the end of the given string. For example:

``` C
char *str1 = "sub";
char *var1 = "strisubng1";
char *var2;

var2 = strstr(var1, str1);
```

This finds the first occurrence of `str1` (which is `"sub"`) in the string `var1`. `var2` is the substring starting from `"sub"` to the end of `var1`. If `str1` is not found in `var1`, then the `strstr` function returns a `NULL` value.

Printing `var2` outputs

``` output
subng1
```

# BIBLIOGRAPHY

---
nocite: |
  @C_main_tutorial
  @C_reference_manual
---