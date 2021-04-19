---
title: Language basics
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

`statements1` represents the statements of the code. The smallest possible C program that does nothing is produced by deleting the `statements1` line.

# DIRECTIVES

The C language support directives, they are placed at the start of the file.

``` {.syntax}
#directive1

rest_of_file1
```

The `#define` directive is used to define macros. Macros are code that replaces other code, so macros can be used as variables, or as functions. By convention, macros are named using uppercase letters.

> Macro as a variable
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

> Macro as a function
>
> ``` {.C .syntax}
> #define MACRO1(arg1, arg2)
> ```


The `#include` directive is used to include headers. Headers are files that declare or define variables, functions, and macros, so that they can be used in C source code. This is useful for example, to include functions defined in other files, so that it is not necessary to create those functions from scratch.

<!--
//T// include directive
#include <stdio.h>

//T// define directive
#define LENGTH1 10

//T// main function, (), {}
int main ()
{
//T// int, identifiers, ",", ";"
	int a,b,c;

//T// =, 0x, 0octal, u, +
	a = 0x5p-2,b = 03u,c = a + b;

//T// printf, escapes \n and modifiers %d
	printf("Hello World!\nNum:%d\n",c);

//T// Variables, constants, literals

//T// const keyword
    const int LENGTH2 = 5;

//T// return keyword
	return 0;
}
-->

# Data types

## Composite types

# Operators

# Control flow

# Functions

# Packages

# Standard library

# Object oriented programming

# Error and exception handling

# Command line interface

# Debugging

# System calls

# Building a project

# Bibliography

---
nocite: |
  @C_main_tutorial
---