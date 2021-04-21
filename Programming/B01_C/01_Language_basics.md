---
title: LANGUAGE BASICS
toc-title: Table of contents
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

`statements1` represents the statements of the code. The smallest possible C program that does nothing is produced by deleting the `statements1` line.

Statements in C must be terminated with a semicolon, `statement1;`.

Blocks of code in C are enclosed in curly braces, `{ block_of_code1 }`.

C ignores whitespace and so it does not require indentation, so the following is a valid C program.

``` {.C .syntax}
int main() { statement1; return 0; }
```

Multiple statements can be written per line.

``` {.C .syntax}
statement1; statement2; statementN;
```

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
    return 0;
}
```

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

To print characters to standard output, use the `printf` function. This function is included with the `stdio.h` header.

``` {.C .syntax}
printf("This text will be printed to standard output");
```

::: block
> **Example code to print to standard output**
>
> The following is a minimal complete program that prints to standard output.
>
> ``` C
> #include <stdio.h>
>
> int main()
> {
>	  printf("string1");
>	  return 0;
> }
> ```
>
> Compiling and executing this program in a shell outputs:
>
> `string1`{.output}
:::

To print a given variable do:

``` {.C .syntax}
int a = 5;
printf("%d", a);
```

This outputs:

`5`{.output}

`int a = 5` creates a variable `a` of data type `int` (for integer) with a value of `5`. `%d` is called a format specifier. Variables, data types, and format specifiers are explained in this document. This is placed here because it's the minimum required to use the `printf` function to print the value of an integer variable.

To read data from standard input, use the `scanf` function.

``` {.C .syntax}
int a;
scanf("%d", &a);
```

The `&` in `&a` is the address operator, `&a` is the address of the variable `a`. The address operator, and the address of a variable are explained in this document. This is placed here because the `scanf` function requires the address of a variable and not the variable itself.

::: block
> **Example code to read from standard input**
>
> The following is a minimal complete program that reads from standard input.
>
> ``` C
> #include <stdio.h>
>
> int main()
> {
>	  int a;
>	  scanf("%d", &a);
>     printf("%d", a);
>	  return 0;
> }
> ```
>
> Compiling and executing this program in a shell, prompts the user to enter characters with the keyboard. Use the `enter` key to finish inputting characters. In this program, the input expected is an integer number, for example '34', but inputting text does not throw an error, it is undefined behavior.
>
> After inputting an integer number, this program prints that integer and exits. Inputting text makes the program print numbers that change. Even when inputting the same text, the printed output number varies because doing so is undefined behavior.
:::

# Data types

C is a statically typed language, so to create a variable, the data type of the variable must be specified. In order to achieve this, the C language has keywords for the data types.

A variable is created by writing the keyword of its data type and then the name of the variable.

`data_type1 var1;`{.syntax}

`var1` is the name of the variable, and `data_type1` is a keyword of the data type of `var1`.

Several variables of the same data type can be declared in a single statement, separating the variables by comma.

`data_type1 var1, var2, varN;`{.syntax}

The equal sign '=' is used as an assignment operator to assign a value to a variable.

`data_type1 var1 = value1;`{.syntax}

`value1` must be of the same data type as `data_type1`, otherwise it's undefined behavior.

## Numeric data types

The `int` keyword is used to create variables of integer data type.

`int var1 = 5;`{.syntax}

Hexadecimal integers can be written by prefixing the number with `0x`, for example the hexadecimal number '5A' would be written as `0x5A`.

`int var1 = 0x5A;`{.syntax}

Octal integers can be written by prefixing the number with `0`, for example the octal number '11' would be written as `011`.

`int var1 = 011;`{.syntax}

Integers can be signed or unsigned.




<!--
//T// u
	a = 0x5p-2,b = 03u;

//T// escapes \n
-->

## Constant variables

<!--
//T// const keyword
    const int LENGTH2 = 5;
-->

## Composite types

# Operators

<!--
c = a + b;
-->

# Control flow

# Functions

<!--
//T// return keyword
	return 0;
-->

# Packages

# HEADERS

# DIRECTIVES

The C language support directives, they are placed at the start of the file.

``` {.C .syntax}
#directive1

rest_of_file1
```

The `#define` directive is used to define macros. Macros are code that replaces other code, so macros can be used as variables, or as functions. By convention, macros are named using uppercase letters.

::: block
> **Macro as a variable**
>
> ``` {.C .syntax}
> #define MACRO1 value1
> ```
>
> For example:
>
> ``` C
> #define FIRST_NUMBER 6
> ```
>
> This macro defines `FIRST_NUMBER` as a variable, but given that macros can't be changed in the code, `FIRST_NUMBER` is effectively a constant.
:::

<!-- line continuation for defined string variables -->

::: block
> **Macro as a function**
>
> ``` {.C .syntax}
> #define MACRO1(arg1, arg2) function_body1
> ```
>
> For example:
>
> ``` C
> #define F1(A, B) 2*A + B
> ```
:::

The `#include` directive is used to include headers. Headers are files that declare or define variables, functions, and macros, so that they can be used in C source code. This is useful for example, to include functions defined in other files, so that it is not necessary to create those functions from scratch.

# Error and exception handling

# Object oriented programming

# Command line interface

# Debugging

# System calls

# Building a project

# Standard library

<!--
//T// printf, format specifiers and modifiers %d
    printf("Hello World!\nNum:%d\n",c);
-->

# Bibliography

---
nocite: |
  @C_main_tutorial
---