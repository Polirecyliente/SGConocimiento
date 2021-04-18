---
title: Language basics
toc-title: Table of contents
---

# Introduction

This document is about the C programming language and its features.

The C language is a compiled language, which means that a compiler is needed to convert C source code into binary code.

# Basic usage

Source code files of the C language have the file extension `.c` and they are written in a plain text format.

This project uses the `gcc` compiler to compile C source code files into binary code files. GCC stands for GNU Compiler Collection. GNU stands for GNU is Not Unix, GNU is a free and open source software project.



# Basic syntax



<!--
//T// Variables, constants, literals

//T// compile any C file /path/to/file1.c in a terminal with
// gcc /path/to/file1.c -o /path/to/exec1
//T// run the compiled executable in a shell with
// /path/to/exec1

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