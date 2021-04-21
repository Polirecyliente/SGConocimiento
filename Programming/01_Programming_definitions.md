---
title: PROGRAMMING DEFINITIONS
toc-title: Table of Contents
---

::: {#toc-id}
## Table of Contents {#toc-title}

-   [[1]{.toc-section-number} INTRODUCTION](#introduction)
-   [[2]{.toc-section-number} BASIC CONCEPTS](#basic-concepts)
-   [[3]{.toc-section-number} PARTS OF A COMPUTER](#parts-of-a-computer)
:::

# INTRODUCTION

This document contains the definitions needed to understand computer programming.

The directory that contains this file is called 'Programming', in this context the word 'programming' means 'computer programming'.

# BASIC CONCEPTS {.break-before-class}

::: term
**Computer**
  : A device that can do computations.
  \
  For a user to make use of a computer, the user needs a way to let the computer know the computations that should be carried out, this is called **input**. On the other hand, the computer needs a way to let the user know the results of the computations, this is called **output**. Depending on the output, the user sends new input to the computer, and the computer sends to the user the results of the computations as new output. This establishes a cycle of interactions between the user and the computer.
  \
  For this cycle of interactions to take place, the computer needs to have **peripherics**. The computer must have peripherics that receive the input from the user. The computer interprets this input to know which computations must be carried out. The computer must also have peripherics that send the output to the user. After the computations are carried out, the computer sends the output using these peripherics.
:::

::: term
**Input peripherics**
  : Devices connected to a computer, used by the user to send input to the computer. Input peripherics can be made into parts of the computer itself.
  \
  The most common input peripherics are: the **mouse** and the **keyboard**. The mouse is used as a pointing device, the input consists of pointing to different points in space. The keyboard is used to send character input to the computer, to be able to write, and to send in band signaling (which means sending instructions via a sequence of characters, instead of sending the characters themselves).
:::

::: term
**Output peripherics**
  : Devices connected to a computer, used by the computer to send output to the user. Output peripherics can be made into parts of the computer itself.
  \
  The most common output peripherics are: the **monitor** and the **printer**. The monitor is used to display output from computations. The printer is used to print documents.
:::

::: term
**Computer instruction**
  : The antecedent of a **computation**. An instruction instructs the computer to carry out a given computation.
:::

::: term
**Computer data**
  : The result of a computation. Data can be used as part of other computations, and it can be stored for future use.
:::

::: term
**Metadata**
  : Data about a given data. For example, the date of creation of the data, or the date of last modification of the data, or the size of the data, or the format of the data, are examples of metadata.
:::

::: term
**Computer program**
  : A set of instructions to be carried out by a computer. These instructions are written in **binary code** (as seen in most computers in the moment this was documented).
:::

::: term
**Binary code**
  : A way to write **computer programs**. Binary code uses only two symbols: "off" and "on", or $0$ and $1$.
:::

::: term
**Source code**
  : A way to write **computer programs**. Source code uses human readable symbols, such as words and statements, written in a given **programming language**. Source code must be **compiled** or **interpreted** into binary code, so that the computer can execute the program.
:::

::: term
**Compiler**
  : A computer program that compiles source code written in a given **programming language**, into binary code, effectively converting source code into binary code. When a source code file is compiled, the result is a binary code file, so the whole source code file is compiled as a unit.
:::

::: term
**Interpreter**
  : A computer program that interprets source code written in a given **programming language**, into binary code, effectively converting source code into binary code. When a source code file is interpreted, each line of the file is interpreted as a unit. This allows for more interactivity than a compiler, because even a single line can be interpreted and the resulting binary code executed.
:::

::: term
**Script**
  : A source code file written in an interpreted language. Scripts are executed by an interpreter, line by line.
:::

::: term
**Intermediate code**
  : Code that is produced as an intermediate step between source code and binary code.
  \
  A common intermediate code is **maching code** also called **assembly**.
:::

::: term
**Programming language**
  : A language in which to write source code. The compiler or interpreter effectively determines the possible statements that can be created with a programming language. For example, if a compiled language is defined with certain feature, but the current compiler does not support that feature, then any source code file that uses that feature will throw error when compiled with said compiler.
:::

::: term
**Machine code**
  : Code written in assembly language. Assembly is a type of programming language in which the instructions are written directly, using words and numbers instead of only binary numbers.
:::

# PARTS OF A COMPUTER

For a computer to be able to carry out computations, it needs a number of parts. 
The verb 'carry out' here means 'process', so the computer needs a **processor** to process computations. Each computation comes from an instruction, these instructions need to be placed somewhere, so the computer needs a **memory** in which to place instructions. Instructions are part of programs, so the computer needs **storage** in which to place programs and any file needed by those programs. To coordinate the interactions between these parts, and between the computer and the **peripherics**, the computer needs an **operating system**.

``` {.mermaid caption="Computer-User interaction loop" format="svg"}
flowchart TB
  Input
  subgraph s1 ["Computer"]

      Input --> Computer

    subgraph s2 [" "]
      subgraph Computer [" "]
        Processor --- Memory --- Storage --- Processor
      end
    end

      Computer --> Output

  end

      Output --> Input

  linkStyle default interpolate linear
  style Computer stroke: black
```

As shown in the diagram, the interaction between computer and user forms a loop. The user interacts via input, but a computer could receive input from other computers, when they are connected in a network. The connection from output to input means that a given output influences future input, be it from the user or from other computers in a network (it does not mean that the computer sends output as input to itself).

::: term
**Processor**
  : The part of a computer dedicated to process instructions, by fetching each instruction from a given program, decoding the instruction into a computation, and executing the computation. This is called **Fetch-Decode-Execute cycle**.
  \
  For a computer to execute a program, each instruction of the program is fetched, decoded, and executed in the order they appear in the program.
  \
  The processor is commonly called CPU, it stands for Central Processing Unit.
:::

::: term
**Memory**
  : The part of a computer dedicated to hold programs retrieved from **storage**, and to feed the instructions of a program to the **processor**.
  \
  The memory is also dedicated to hold computer data, be it data read from storage, or be it data that is the result of a computation.
  \
  A common form of memory, when this was written, is RAM, which stands for Random Access Memory.
:::

::: term
**Storage**
  : The part of a computer dedicated to store programs and computer data.
  \
  A common form of storage, when this was written, are hard drives.
:::

**About memory and storage**: It could be conceived that memory and storage are one and the same thing, because both hold (memory) or store (storage) programs and computer data. The reason why this distinction is necessary when this was written, is that hard drives are slower than RAM to feed the processor with instructions, and RAM loses its contents when disconnected from electric power. This two conditions make it necessary to have storage to store programs and data when the computer is powered off, and they make it necessary to have memory to feed instructions to the processor as fast as possible.

In a future it may be possible for memory and storage to be a single entity, that quickly feeds instructions to the processor, and can store as much data and programs as needed.

::: term
**Operating system**
  : A program designed to coordinate the parts of a computer, including its attached peripherics. The operating system coordinates the feeding of instructions from memory to processor. It coordinates the retrieval of programs and data from storage into memory. It coordinates the reception of input from the keyboard. It coordinates the output to the monitor.
  \
  Computer data is stored in storage, and it's organized in a **file system hierarchy**. The operating system coordinates the file system hierarchy, it grants or denies access to data, so that a program that instructs the computer to read a given data, may be denied from doing that reading operation by the operating system.
:::

::: term
**File system hierarchy**
  : The way data is organized in a computer. A common way to define a file system hierarchy is with directories and files, where there is a single root directory that contains all other directories and files.
  \
  Both files and directories are forms of computer data. In this paradigm, a directory contains files and other directories, but a directory can't contain itself as a subdirectory, which leads to a tree structure with a single root node.
:::

``` {.mermaid caption="File system hierarchy" format="svg"}
graph TB
  root_dir --> dir1 & dir2 & dir3
    dir1 --> f1[file1] & d1[subdir1]
      d1 --> f2[file1]
    dir2 --> f3[file1] & file2 & file3
    dir3 --> d2[subdir1] & subdir2
      subdir2 --> f4[file1]
```

In a computer, programs access files and directories in the file system hierarchy to modify them according to how the user wants to modify those files and directories. When a program is given access to a file, the file is copied from storage into memory, so that the processor can access the contents of the file and modify it following the instructions of the program. The program can also instruct the computer to save the changes made to the file, by copying the file back from memory into the storage.

**Uses of the word 'file'**: Directories are treated as files, it's just that they are files that can contain other files. The word 'file' can mean files that are not directories, or it can mean files in general (including directories). The meaning should be obtained directly from the context.

::: term
**File path**
  : In a file system hierarchy, every file has a path, which is the sequence of directories traversed from the root directory to the file itself.

  This project is mainly about Unix operating systems, and particularly about Linux. In Linux a file path is written as `/dir1/subdir1/file1`, separating each directory in the path with a '/', the first '/' is the root directory.
:::

::: term
**File extension**
  : A file that is not a directory can have a file extension. The extension is written at the end of the file name, it serves to give information about the format of the file, which in turn gives information about the programs that may be able to read, use, and modify the file.
  \
  The file extension is written at the end of the file name after a dot, for example `file1.fmt` is a file with extension `fmt`. It can also be said that `fmt` is the format of the file.
:::

::: term
**Plain text format**
  : A file format that consists of only text. In a file with a plain text format, the data is stored as text.
  \
  Programs that read plain text files can render them in different ways. For example the SVG format stands for Scalable Vector Graphics. SVG is a plain text format for images, so a program could render SVG as text, and another program could render SVG as an image.
:::

::: term
**Software**
  : Programs, including their source code, their binary code, and any intermediate code.
:::

::: term
**Hardware**
  : The physical parts of a computer, like the monitor, the CPU, etcetera.
:::

## Parts of an operating system

An operating system can be divided into a few main parts: the **kernel**, the **shell**, the **GUI**, and the **system programs**.

::: term
**Kernel**
  : A program that acts as the coordinator between the parts of the computer, so the kernel fulfills the main purpose of the operating system.
:::

::: term
**Shell**
  : An interpreter that can receive input from the keyboard, to receive instructions from the user. Instructions in a shell are called **commands**. The shell sends the commands to the **kernel**, to have them executed by the computer.
  \
  The shell can also be called 'terminal', because shells are commonly designed to look like terminal screens.
:::

::: term
**GUI**
  : GUI stands for Graphical User Interface. The GUI of an operating system is a set of programs that provide a graphical interface for the user, so that the user can see and interact with the contents of the monitor.
  \
  Through the GUI, the user can see the programs installed on the computer and start them. GUIs commonly come with a file explorer that displays the file system hierarchy to the user, with the posibility to create, move, copy, and delete files and directories.
:::

::: term
**System programs**
  : A set of auxiliary programs that are used by the **shell**, the **kernel** and the **GUI**. For example, when the user writes a command in the shell to copy a file, there must be a system program to copy files. The shell sends the command to the kernel, so that the system program copies the file, if allowed by the kernel.
:::

``` {.mermaid caption="Operating system and hardware" format="svg"}
flowchart TB
  subgraph OS[Operating system]
    subgraph s1[" "]
      Shell & GUI & Sp[System programs]
    end
    Shell & GUI & Sp[System programs] --- Kernel
  end

  subgraph Hardware
  subgraph s2[" "]
    CPU & Memory & Storage & Peripherics
  end
  end

  Kernel --- CPU & Memory & Storage & Peripherics

  style OS stroke: blue
  style Hardware stroke: blue
```

This diagram shows the interactions between the operating system parts and the hardware. The diagram does not imply location, only relationship, because for example the kernel is stored in storage, and is loaded in memory when the computer is turned on.

::: term
**Standard input**
  : A file that reads the keystrokes from the keyboard that are typed in a shell. This file is used by programs that use the shell, to obtain input from the keyboard. This file is also called 'stdin'.
:::

::: term
**Standard output**
  : A file that writes character output to the shell, to print that output in the screen. This file is used by programs that use the shell, to print output in the screen. This file is also called 'stdout'.
:::

::: term
**Standard error**
  : A file that writes errors as output to the shell, to print those errors in the screen. This file is used by programs that use the shell, to print errors in the screen. This file is also called 'stderr'.
:::

# SOFTWARE CONCEPTS

::: term
**Open source software**
  : Software whose source code is open to be obtained by any person at no monetary charge.
:::

## Features of a programming language

Programming languages have several features, like:
  
  - **Syntax**, the way to write all of the following points.
  - **Data types** to hold data in memory and do calculations with it.
  - **Operators** to operate over data types.
  - **Control flow structures** to skip or repeat code.
  - **Functions** and **subroutines** to reuse pieces of code.
  - **Packages** to give hierarchy to the code and organize it.
  - **Error and exception handling** to handle errors that may occur during execution.
  - And other features that are particular to each language.

::: term
**Syntax**
  : In a programming language, syntax is what the compiler or interpreter understands. The plain text that the compiler or interpreter can convert into binary code must have valid syntax. In each programming language, data types have their syntax, functions have their syntax, etcetera.
:::

::: term
**Keyword**
  : Words in a programming language that have a reserved meaning. Keywords provide a given feature or features of the programming language. For example a keyword `keyword1` could convert the next word into a variable that can only hold integer values.
:::

::: term
**Data types**
  : In computers, data in memory is hold as binary numbers. Programming languages can represent those binary numbers in different forms, they can represent words, numbers, logical values (true or false), or composite data (data that contains other data).
:::

::: term
**Variable**
  : A form of naming data. In most programming languages data is hold in memory, and variables are made to point to that data in memory. Calculations can be done with variables, the results can be hold in variables.
:::

::: term
**Constant**
  : A variable whose value does not change during the execution of the program. In most programming languages, trying to change the value of a constant throws an error.
:::

::: term
**String data type**
  : A data type to hold characters. In many programming languages, strings are created by writing characters inside double quotes or inside single quotes, for example "first string" and 'second string'.
:::

::: term
**Integer data type**
  : A data type to hold integer numbers. In many programming languages, integers are created by writing the number directly, for example 5.
:::

::: term
**Signed and unsigned integers**
  : Some programming languages support a distinction between signed and unsigned integers. Signed integers are integers that can be positive or negative because they have a sign. Unsigned integers can only be positive because they have no sign. 
  \
  This distinction is important to know how big can be an integer, because currently it's not possible to hold infinitely large integers in memory. A signed integer variable can hold about half the absolute values of a corresponding unsigned integer, because half of the values will be positive and the other half negative.
:::

::: term
**Float data type**
  : A data type to hold floating point numbers, which are decimal numbers. In many programming languages, floats are created by writing the number directly, for example 14.8. Some programming languages also have a 'double' data type, which is a float data type that allocates double the memory for the float number.
:::

::: term
**Composite data type**
  : A data type that can hold other data types, including other composite data types. The two main composite data types are: arrays and associative arrays.
  \
  Arrays hold data in increasing numeric positions, starting at position 0 in most programming languages. For example, an array could be written as ['pos0', 'pos1', 'pos2'], which is an array of strings. Data is accessed knowing the position of the data, this position is also called index.
  \
  Associative arrays hold data using strings to name positions (instead of using numbers as do arrays). The string that names a position is called 'key', and the data being hold in that position is called 'value', so an associative array is created as a set of key value pairs. For example, an associative array could be written as {'first key': 'first value', 'second key': 25}, in it, the first key holds a string, and the second holds an integer.
  \
  Data in general, even outside the realm of programming, is commonly placed in composite data types.
:::

::: term
**Operator**
  : Character used to operate over variables and over data types.
  \
  In most programming languages, the addition operator is `+`, and the assignment operator is `=`, so two variables could be added as `var1 = var2 + var3`.
:::

::: term
**Statement**
  : The minimum amount of code that is a complete instruction. Statements in the source code are converted into instructions in the binary code.
:::

::: term
**Block of code**
  : A set of statements that are grouped together. Each programming language has its own way to show where a block starts and where it ends.
:::

::: term
**Control flow structures**
  : Code that allows controlling the flow of execution of code. The normal flow of execution is execute line by line in order, from the first line of code to the last line of code.
  \
  Most programming languages have two control flow structures, one to skip over lines of code if a condition is not met, commonly created with the `if` keyword. The other control flow structure is used to repeat a set of lines of code, they are called 'loops'.
:::

::: term
**Function**
  : Code enveloped in a variable. In some programming languages, functions are treated as variables (functions that are variables are called 'first class citizen' functions).
  \
  Functions are like variables that point to code, instead of pointing to data. To reuse the code being pointed by a function, the function is called. When a function is called, the code that the function points to gets executed.
  \
  Functions can receive arguments and return a return value. Arguments are varibles or data types that the function can use inside the code it envelops. The return value is a variable or data type that the function can return to the place where it was called, meaning that the return value can be hold in a variable, and used as a variable without calling the function again.
  \
  A function `func1` has a **function signature**. The signature of the function is `type1 func1(arg1, arg2)`, which is the data type of the return value, the name of the function, and its arguments. Most programming languages enclose the arguments in parentheses.
:::

::: term
**Subroutine**
  : A function that takes no arguments and returns no return value, so a subroutine is a function that only envelops code without taking input in its arguments nor giving output in its return value.
  \
  This is useful to abbreviate lines of code that are repeated multiple times. Placing the repeating lines of code in a subroutine makes the code easier to read and maintain.
:::

::: term
**Package**
  : The organization of code in a hierarchy. In most programming languages, the hierarchy created by packages is equivalent to the **file system hierarchy**.
  \
  Packages allow storing and accessing code in directories and subdirectories. In some programming languages, this is done using dot notation. For example a path to a given source code file in the file system hierarchy could be `path/to/source_code1.fmt`, the same path in a package would be written as `path.to.source_code1`, using dots instead of slashes, and commonly without the file extension at the end.
:::

::: term
**Error and exception handling**
  : Syntax used to handle errors in case they occur during execution.
:::

::: term
**Directive**
  : Some programming languages support directives. Directives are used to change the way that code is parsed. They serve as a metadata of sorts inside the source code itself, but given that they can modify how the source code is parsed, they are not really metadata.
  \
  Directives are also called 'pragmas'.
:::

::: term
**Declaration and definition**
  : Some programming languages allow to differentiate between declaring a variable or function, and defining a variable or function. Declaring a variable or function means stating that it exists (without giving it a value). Defining a variable or function means stating that it exists and giving it a value.
:::

::: term
**Undefined behavior**
  : Behavior of code, that is not designed to occur in its programming language. A given code can have correct syntax in its programming language, and yet produce results that are not meant to happen.
  \
  A traditional example, is accessing an element of an array, such that the element is out of the bounds of the array. There are programming languages that don't throw an error when accessing an array outside its bounds.
  \
  Arrays are stored in memory, so accessing an array out of bounds means accessing other memory in the program that is outside the array. This is undefined behavior, because the programming language can't predict what would be the result of that array access out of bounds.
:::

### Types of programming languages

::: term
**Statically typed language**
  : A programming language in which variables must be defined with a given data type. The data type of the variable can't be changed after defined.
:::

::: term
**Dynamically typed language**
  : A programming language in which variables don't have a data type, so they can have any data type. The data type of the variable can be changed after defined.
:::

# BINARY NUMBERS

