---
title: LANGUAGE BASICS
toc-title: Table of Contents
---

# INTRODUCTION

This document is about the C programming language and its features.

The C language is a compiled language, which means that a compiler is needed to convert C source code into binary code.

The concepts used here are defined in [Programming definitions](../01_Programming_definitions.md).

# BASIC USAGE

Source code files of the C language have the file extension `.c` and they are written in a plain text format.

This project uses the `gcc` compiler to compile C source code files into binary code files. GCC stands for GNU Compiler Collection. GNU stands for GNU is Not Unix, GNU is a free and open source software project.

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


----

`statements1` represents the statements of the code. The smallest possible C program that does nothing is produced by deleting the `statements1` line.

Statements in C must be terminated with a semicolon, `statement1;`.

Blocks of code in C are enclosed in braces, `{ block_of_code1 }`.


----

C ignores whitespace and so it does not require indentation, so the following is a valid C program.

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


----

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


----

A variable is created by writing the keyword of its data type and then the name of the variable.

``` {.C .syntax}
data_type1 var1;
```

`var1` is the name of the variable, and `data_type1` is a keyword of the data type of `var1`. This syntax is for the declaration of `var1`.


----

Several variables of the same data type can be declared in a single statement, separating the variables by comma.

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

Declarations and definitions in a single statement can be mixed.

``` {.C .syntax}
data_type1 var1, var2 = value2;
```


----

`var1` can be declared on one statement, and defined on another statement.

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

## Numeric data types

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


----

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


----

A string can be created as an array of characters. Arrays are explained in this document.

``` {.C .syntax}
char var1[int1] = "string1";
```

`int1` must be big enough to accommodate for "string1", otherwise "string1" will be truncated to the size given by `int1`.

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
  ------------------------------------------------------------------------

In the escape sequence `\n`, the 'n' stands for newline. This escape sequence introduces a newline in its location.

In the escape sequence `\uXXXX`, the 'u' stands for Unicode, the 'XXXX' represents a hexadecimal number of four digits, with the code point of an UTF-8 character.

In the escape sequence `\UXXXXXXXX`, the 'U' stands for Unicode, the 'XXXXXXXX' represents a hexadecimal number of eight digits, with the code point of an UTF-8 character.

## Constants

Constants can be created with the `const` keyword placed before the data type in a variable declaration or definition.

``` {.C .syntax}
const data_type1 CONSTANT1 = value1;
```

The name of constants is written in uppercase by convention. For example:

``` C
const int NUMBER = 8;
```

## Pointers

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

An array can be declared with the following syntax.

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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


----

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

# FUNCTIONS

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


----

The `return` keyword must be followed by the return value of the function.

``` {.C .syntax}
return return_value1;
```

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

  ------------------------------------------------------------
   Format specifier           Example               Output
  ------------------ -------------------------- --------------
         `%d`           `int var1 = 5;`{.C}      `5`{.output}
                      `print("%d", var1);`{.C}

  ------------------------------------------------------------

In the format specifier `%d`, the 'd' stands for digit. It's used to format variables of data type `int` as regular digits.

## String functions

C has several string manipulation functions to operate over strings. Many of these functions are defined by including the `string.h` header.

``` {.C .syntax}
#include <string.h>
```


----

The `strcpy` function copies a string into another. This function is necessary because an array can't be assigned to another array, unlike non-array variables. For example, an `int` variable can be assigned to another `int` variable, which is a way of copying the first `int` variable into the second.



# BIBLIOGRAPHY

---
nocite: |
  @C_main_tutorial
---