---
title: DEFINITIONS
toc-title: Table of Contents
---

::: {#toc-id}
## Table of Contents {#toc-title}

-   [[1]{.toc-section-number} INTRODUCTION](#introduction)
-   [[2]{.toc-section-number} BASIC CONCEPTS](#basic-concepts)
-   [[3]{.toc-section-number} PARTS OF A COMPUTER](#parts-of-a-computer)
:::

# INTRODUCTION

This document contains the definitions needed to understand computer science.

# BASIC CONCEPTS {.break-before-class}

::: term
**Device**
  : Anything built using electronic circuits as part of it, that fulfills a purpose. For example, computers, mobiles (like cellphones), toasters, etcetera.
:::

::: term
**Computer**
  : A device that can do computations.
\\\
  For a user to make use of a computer, the user needs a way to let the computer know the computations that should be carried out, this is called **input**. On the other hand, the computer needs a way to let the user know the results of the computations, this is called **output**. Depending on the output, the user sends new input to the computer, and the computer sends to the user the results of the computations as new output. This establishes a cycle of interactions between the user and the computer.
\\\
  For this cycle of interactions to take place, the computer needs to have **peripherics**. The computer must have peripherics that receive the input from the user. The computer interprets this input to know which computations must be carried out. The computer must also have peripherics that send the output to the user. After the computations are carried out, the computer sends the output using these peripherics.
:::

::: term
**Input peripherics**
  : Devices connected to a computer, used by the user to send input to the computer. Input peripherics can be made into parts of the computer itself.
\\\
  The most common input peripherics are: the **mouse** and the **keyboard**. The mouse is used as a pointing device, the input consists of pointing to different points in space. The keyboard is used to send character input to the computer, to be able to write, and to send in band signaling (which means sending instructions via a sequence of characters, instead of sending the characters themselves).
:::

::: term
**Output peripherics**
  : Devices connected to a computer, used by the computer to send output to the user. Output peripherics can be made into parts of the computer itself.
\\\
  The most common output peripherics are: the **monitor** and the **printer**. The monitor is used to display output from computations. The printer is used to print documents.
:::

::: term
**Read**
  : In this context, to read is the act of doing an input operation.
:::

::: term
**Write**
  : In this context, to write is the act of doing an output operation
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
  : A way to write **computer programs**. Binary code uses only two symbols: "off" and "on", or 0 and 1.
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
\\\
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

::: term
**Software project**
  : A set of source code files that are meant to create a single program file.
:::

::: term
**Build a project**
  : The process of converting a software project into a single program file. The build is created by compiling all the different files of the software project, into the program itself.
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
\\\
  For a computer to execute a program, each instruction of the program is fetched, decoded, and executed in the order they appear in the program.
\\\
  The processor is commonly called CPU, it stands for Central Processing Unit.
:::

::: term
**Memory**
  : The part of a computer dedicated to hold programs retrieved from **storage**, and to feed the instructions of a program to the **processor**.
\\\
  The memory is also dedicated to hold computer data, be it data read from storage, or be it data that is the result of a computation.
\\\
  A common form of memory, when this was written, is RAM, which stands for Random Access Memory.
:::

::: term
**Storage**
  : The part of a computer dedicated to store programs and computer data.
\\\
  A common form of storage, when this was written, are hard drives.
:::

::: term
**Allocate**
  : In this context, to allocate is the act of preparing memory or storage for holding or storing a given amount of data.
:::

**About memory and storage**: It could be conceived that memory and storage are one and the same thing, because both hold (memory) or store (storage) programs and computer data. The reason why this distinction is necessary when this was written, is that hard drives are slower than RAM to feed the processor with instructions, and RAM loses its contents when disconnected from electric power. This two conditions make it necessary to have storage to store programs and data when the computer is powered off, and they make it necessary to have memory to feed instructions to the processor as fast as possible.

In a future it may be possible for memory and storage to be a single entity, that quickly feeds instructions to the processor, and can store as much data and programs as needed.

::: term
**Plain text format**
  : A file format that consists of only text. In a file with a plain text format, the data is stored as text.
\\\
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

## Operating system

::: term
**Operating system**
  : A program designed to coordinate the parts of a computer, including its attached peripherics. The operating system coordinates the feeding of instructions from memory to processor. It coordinates the retrieval of programs and data from storage into memory. It coordinates the reception of input from the keyboard. It coordinates the output to the monitor.
\\\
  Computer data is stored in storage, and it's organized in a **file system hierarchy**. The operating system coordinates the file system hierarchy, it grants or denies access to data, so that a program that instructs the computer to read a given data, may be denied from doing that reading operation by the operating system.
:::

::: term
**File system hierarchy**
  : The way data is organized in a computer. A common way to define a file system hierarchy is with directories and files, where there is a single root directory that contains all other directories and files.
\\\
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
\\\
  The file extension is written at the end of the file name after a dot, for example `file1.fmt` is a file with extension `fmt`. It can also be said that `fmt` is the format of the file.
:::

An operating system can be divided into a few main parts: the **kernel**, the **shell**, the **GUI**, and the **system programs**.

::: term
**Kernel**
  : A program that acts as the coordinator between the parts of the computer, so the kernel fulfills the main purpose of the operating system.
:::

::: term
**Shell**
  : An interpreter that can receive input from the keyboard, to receive instructions from the user. Instructions in a shell are called **commands**. The shell sends the commands to the **kernel**, to have them executed by the computer.
\\\
  The shell can also be called 'terminal', because shells are commonly designed to look like terminal screens. The shell is also called the Command Line Interface (acronymized as CLI), because the shell acts as an interface between the computer and the user, in which the user can input commands in the shell, and like any interpreter, one command is inputted per line.
:::

::: term
**Shell prompt**
  : The text in a the shell, before the cursor, that starts every new line. Common prompts contain the name of the computer, the user, and the current directory (some prompts may show the datetime, or other information). The prompt can be edited.
:::

::: term
**GUI**
  : GUI stands for Graphical User Interface. The GUI of an operating system is a set of programs that provide a graphical interface for the user, so that the user can see and interact with the contents of the monitor.
\\\
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
**Environment variable**
  : A variable created by the operating system. Environment variables are used to store values that can be used by programs. A program can be written to read the value of an environment variable, and change its execution according to said value.
\\\
  One of the most common environment variables, is called 'PATH'. The PATH environment variable stores a list of directories where the shell searches for programs. For example, when executing `program1` in a shell, the shell searches for a program called 'program1' in each of the directories listed in the PATH environment variable.
:::

::: term
**Virtual environment**
  : A shell with modified environment variables.
\\\
  A common use of virtual environments, is to modify the PATH environment variable. This allows installing programs in one environment, that are not visible in any other environment, by making the PATH to include the directory where those programs are installed. Other environments do not have this directory in their PATH environment variable, and so other environments can't access those programs, unless the whole path to them is specified.
:::

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

::: term
**Verbose output**
  : In a program that uses the CLI of the operating system, the program can output detailed information about its execution. This is called verbose output, because the program prints more information than normal.
:::

::: term
**Application**
  : A type of program that is intended to be used by an user (as opposed to programs used by the computer, like the operating system). Applications are commonly used as tools by the user. Most applications have a GUI, so CLI applications are more often called programs or commands.
:::

::: term
**Web application**
  : An application that is used via a web browser.
:::

::: term
**Frontend**
  : In web applications, the frontend is the user interface shown in the browser.
:::

::: term
**Backend**
  : In web applications, the backend is the server, database, APIs, programs, etcetera, that handle the requests made by the user in the frontend.
:::

::: term
**Code library**
  : A set of code that is organized for given purposes or uses. Code from a library can be used from code written by the user, by importing the library. This is used so that the code of the library does not need to be rewritten each time, but rather it's written once in the library, and reused as many times as needed in code written by the user.
:::

::: term
**API**
  : API stands for Application Programming Interface. An API is a set of code like a library, but this code calls other code outside of itself. For code written by the user, an API is used the same as a library (an API can be imported, for example), but the difference is that the API calls code that runs outside of itself, so the API acts as an interface between the code written by the user, and the code that the API calls. In a sense an API is a library that calls another library or libraries to work.
:::

::: term
**Framework**
  : A set of code that calls code written by the user, to achieve a given purpose. This concept is opposite, in a sense, to the concept of a library. In a library, the code written by the user, calls code from the library. In a framework, the framework calls code written by the user, so the roles are inverted. This loss of control from the user, is useful for creating applications that are very similar to each other, that only differ in a small amount of code, that can then be written by the user.
:::

::: term
**Computing platform**
  : The environment in which a program is designed to be executed. For an application, the computing platform is the hardware plus the operating system, for a web application, the computing platform is the browser.
:::

::: term
**SDK**
  : SDK stands for Software Development Kit. An SDK is a set of tools meant to help in software development, so an SDK is commonly composed of documentation, tutorials, APIs and libraries, compilers, etcetera.
\\\
  SDKs are commonly of two types: SDKs to develop code in a particular language, and SDKs to develop code for a particular computing platform.
:::

## Features of a programming language

Programming languages have several features, like:

  - **Syntax**, the way to write all of the following points.
  - **Data types** to hold data in memory and do calculations with it.
  - **Operators** to operate over data type values.
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
**Data type memory allocation**
  : In statically typed languages, each data type is allocated a given amount of memory, commonly measured in bytes. The amount of memory allocated is determined by the compiler or interpreter of the language, based on the hardware limitations of the computer.
:::

::: term
**Variable**
  : A form of naming data. In most programming languages data is hold in memory, and variables are made to point to that data in memory. Calculations can be done with variables, the results can be hold in variables. The data being hold by a variable is called the 'value' of the variable.
:::

::: term
**Constant**
  : A variable whose value does not change during the execution of the program. In most programming languages, trying to change the value of a constant throws an error.
:::

::: term
**Type casting**
  : Converting the data type of a variable, from its data type to another data type.
:::

::: term
**Integer data type**
  : A data type to hold integer numbers. In many programming languages, integers are created by writing the number directly, for example 5.
:::

::: term
**Signed and unsigned integers**
  : Some programming languages support a distinction between signed and unsigned integers. Signed integers are integers that can be positive or negative because they have a sign. Unsigned integers can only be positive because they have no sign. 
\\\
  This distinction is important to know how big can be an integer, because currently it's not possible to hold infinitely large integers in memory. A signed integer variable can hold about half the absolute values of a corresponding unsigned integer, because half of the values will be positive and the other half negative.
:::

::: term
**Float data type**
  : A data type to hold floating point numbers, which are numbers with decimals. In many programming languages, floats are created by writing the number directly, for example 14.8. Some programming languages also have a 'double' data type, which is a float data type that allocates double the memory for the float number.
:::

::: term
**Boolean data type**
  : A data type to hold truth values. The truth values are: true and false. In most programming languages, the truth values are written as 1 and 0 (for true and false), or True and False, On and Off, Yes and No, etcetera. The truth values are also called boolean values.
:::

::: term
**Character data type**
  : A data type to hold a single character. A character is any single letter, number, symbol, whitespace that can be written in a computer.
:::

::: term
**String data type**
  : A data type to hold characters. In many programming languages, strings are created by writing characters inside double quotes or inside single quotes, for example "first string" and 'second string'.
:::

::: term
**Escaping a character**
  : Make a character mean something different, in the programming language in which its written.
:::

::: term
**Escaped character**
  : In a given programming language, a character that acts as an operator must be escaped to become the literal character and not the operator.
\\\
  In most programming languages the backslash `\` is an operator, which is the operator to escape the next character, so to obtain a literal backslash, it must be escaped as `\\`.
:::

::: term
**Escape sequence**
  : A literal character (that does not act as an operator), that when escaped becomes an operator. The escape sequence is the literal character being escaped. It is an operator in the sense that it provides a given functionality.
\\\
  In many programming languages the character 'n' is a regular letter, the letter 'n'. The escape sequence `\n` means "introduce a newline here", which places a newline, or a linebreak at that position. For example, the string `"Line1\nLine2" when parsed creates two lines instead of one.
:::

::: term
**Lexicographical order**
  : The rules to decide the order of a set of characters. Given two characters, these rules allow saying which character comes first and which one comes after. For example, in most lexicographical orders that use the Latin alphabet, the character 'a' comes before 'b', so in this sense 'a' is less than 'b', or 'b' is greater than 'a', because 'b' comes after 'a'.
\\\
  The lexicographical difference between two characters, is the amount of characters to get from the second character to the first one. For example, the lexicographical difference between 'a' and 'c' is -2, and the lexicographical difference between 'c' and 'a' is 2 (in most lexicographical orders).
\\\
  The lexicographical order is a superset of the alphabetical order, because it also includes the order for numbers and symbols.
:::

::: term
**Pointer**
  : A data type to hold the address in memory of a given variable. Variables are hold in memory, each at a given address. This address itself can be hold in a variable, of pointer data type.
:::

::: term
**Composite data type**
  : A data type that can hold other data types, including other composite data types. The two main composite data types are: arrays and associative arrays.
\\\
  Arrays hold data in increasing numeric positions, starting at position 0 in most programming languages. For example, an array could be written as ['pos0', 'pos1', 'pos2'], which is an array of strings. Data is accessed knowing the position of the data, this position is also called index.
\\\
  Associative arrays hold data using strings to name positions (instead of using numbers as do arrays). The string that names a position is called 'key', and the data being hold in that position is called 'value', so an associative array is created as a set of key value pairs. For example, an associative array could be written as {'first key': 'first value', 'second key': 25}, in it, the first key holds a string, and the second holds an integer.
\\\
  Data in general, even outside the realm of programming, is commonly placed in composite data types.
:::

::: term
**Array indexing**
  : The act of accessing an element from an array, via its index in the array.
:::

::: term
**Operator**
  : Character used to operate over variables and over data type values. Operators have operands, which are the variables being operated with. Operators return a result of the operation.
\\\
  In most programming languages, the addition operator is `+`, and the assignment operator is `=`, so two variables could be added as `var1 = var2 + var3`.
\\\
  Operators are functions in practice, because they take arguments (which are the operands), and they return a value which is the result of the operation. For example, the operation `A + B` could be written as a function `add(A, B)`.
:::

::: term
**Evaluation order**
  : The order in which operators operate over their operands. This is necessary to define because when several different operators are used in an expression, the program needs a way to decide which operator to apply first, and which later.
:::

::: term
**Grouping operators**
  : Operators used to group operations and explicitly set their evaluation order, because expressions inside grouping operators are evaluated first. In most programming languages, the only grouping operator is the parentheses pair. For example, in `(operand1 op1 operand2) op2 operand3` where `op1` and `op2` are operators, `operand1` and `operand2` are operated first, then the result is operated with `operand3`.
:::

::: term
**Arithmetic operators**
  : Operators to make arithmetic operations with numbers. Most programming languages have operators for: addition, subtraction, multiplication, division, exponentiation, modulo, etcetera.
:::

::: term
**Relational operators**
  : Operators to compare variables. Most programming languages have operators to check if two variables are: equal, different, one greater than the other, one less than the other, one greater than or equal to the other, one less than or equal to the other, etcetera.
:::

::: term
**Logical operators**
  : Operators to make logical operations with boolean values. Most programming languages have operators for:

    - The AND operation: to check if two boolean values are both true.
    - The OR operation: to check if either one or both of two boolean values are true.
    - The NOT operation: to change the value of a single boolean value.
    - Etcetera.
:::

::: term
**Bitwise operators**
  : Operators to make bitwise operations with binary numbers. Most programming languages have operators for:

    - The AND operation: to check the positions in two sets of bits, where the bits in both positions are 1.
    - The OR operation: to check the positions in two sets of bits, where the bits in either one or both positions are 1.
    - The XOR operation: to check the positions in two sets of bits, where one bit is 1 and the other is 0. XOR stands for eXclusive OR.
    - The NOT operation: to flip the value of a the bits in a set of bits.
    - The left shift operation: to shift the bits in a set of bits, to the left a given amount of positions.
    - The right shift operation: to shift the bits in a set of bits, to the right a given amount of positions.
:::

::: term
**Assignment operators**
  : Operators to assign values to variables. Most programming language use the equal sign '=' as the basic assignment operator. Some programming languages support other assignment operators, commonly by mixing arithmetic operators with the equal sign (which do the arithmetic operation and then assign the result to the variable being assigned to).
:::

::: term
**Ternary operators**
  : Operator to make an if else statement. In the programming languages that support the ternary operators, the ternary operators are commonly two: one to specify the if statement, and one to specify the else statement.
:::

::: term
**Expression**
  : A combination of variables and operators that is syntactically correct. For example, in most programming languages `var1 + var2 - var3` is an expression, but `var1 var2 +` is not (in other languages `var1 var2 +` could be a way to write the sum of `var1` and `var2`). Evaluating an expression means doing the operations within the expression, to determine its value.
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
**Scope**
  : The possibility to access and change variables. In many programming languages, variables that are created inside a block of code are local to the block of code, so their scope is the block of code, which means that those variables can only be accessed and changed from within the block of code.
:::

::: term
**Control flow structures**
  : Code that allows controlling the flow of execution of code. The normal flow of execution is executing line by line in order, from the first line of code to the last line of code.
\\\
  Most programming languages have two control flow structures, one to skip over lines of code if a condition is not met, commonly created with the `if` keyword, and called a 'conditional statement'. The other control flow structure is used to repeat a set of lines of code, this kind of control flow structure is called a 'loop'.
\\\
  Some programming languages have a control flow structure called 'goto', which is used to make the execution go to a given labeled line of code.
:::

::: term
**Iteration**
  : In a loop, an iteration is each one of the times that the statements of the loop are repeated. Iterations commonly have an iterator, which is a variable that changes along with the iterations. The iterator can be an integer number that increases or decreases with each iteration, or it can be a value from a list of values so that the iterator takes each of these values in each iteration.
:::

::: term
**Function**
  : Code enveloped in a variable. In some programming languages, functions are treated as variables (functions that are variables are called 'first class citizen' functions).
\\\
  Functions are like variables that point to code, instead of pointing to data. To reuse the code being pointed by a function, the function is called (this is called a 'function call'). When a function is called, the code that the function points to gets executed.
\\\
  The syntax to write a function in a programming language could be like this: `func1(param1, param2){ statements1; return value1 }`.
\\\
  Functions are created with parameters, statements, and a return value. Parameters, `param1` and `param2` in the example, are variables or data type values that the function can use in `statements1`. The return value, `value1` in the example, is a variable or data type value that the function returns when called (see below).
\\\
  When doing a function call, the parameters are now called arguments, for example, `var1 = func1(arg1, arg2)`, this calls `func1` with arguments `arg1` and `arg2`, the return value is hold in `var1`. The saying 'passing the arguments to a function' means doing a function call with those arguments.
:::

::: term
**Package**
  : The organization of code in a hierarchy. In most programming languages, the hierarchy created by packages is equivalent to the **file system hierarchy**.
\\\
  Packages allow storing and accessing code in directories and subdirectories. In some programming languages, this is done using dot notation. For example a path to a given source code file in the file system hierarchy could be `path/to/source_code1.fmt`, the same path in a package would be written as `path.to.source_code1`, using dots instead of slashes, and commonly without the file extension at the end.
:::

::: term
**Error and exception handling**
  : Syntax used to handle errors in case they occur during execution.
:::

::: term
**Name**
  : In this context, a name is the string that identifies a variable, function, package, etcetera. In most programming languages, valid names are not keywords, do not start with a number, do not contain spaces, and only contain letters, numbers, the underscore _, and the hyphen -. For example, in a variable `var1`, the string 'var1' itself is the name of the variable.
:::

::: term
**NULL value**
  : A special value that means no value. Most programming languages have a keyword for the NULL value.
:::

::: term
**Directive**
  : Some programming languages support directives. Directives are used to change the way that code is parsed. They serve as a metadata of sorts inside the source code itself, but given that they can modify how the source code is parsed, they are not really metadata.
\\\
  Directives are also called 'pragmas'.
:::

::: term
**Declaration, definition, and initialization**
  : Some programming languages allow declaring and defining a variable or function, and initializing a variable. Declaring a variable or function means stating that it exists (without allocating memory for it, which is then done in a different moment). Defining a variable or function means stating that it exists and allocating memory for it. Initializing a variable means giving it an initial value.
:::

::: term
**Undefined behavior**
  : Behavior of code, that is not designed to occur in its programming language. A given code can have correct syntax in its programming language, and yet produce results that are not meant to happen.
\\\
  A traditional example, is accessing an element of an array, such that the element is out of the bounds of the array. There are programming languages that don't throw an error when accessing an array outside its bounds.
\\\
  Arrays are stored in memory, so accessing an array out of bounds means accessing other memory in the program that is outside the array. This is undefined behavior, because the programming language can't predict what would be the result of that array access out of bounds.
:::

::: term
**Builtin**
  : The set of names that come predefined in a programming language. A programming language can have builtins like functions, constants, classes, etcetera. They can be used without importing any external package or library, because they come built in.
:::

### Features of functions

Functions can come with several different features, depending on how they are written. Many features are not supported by all programming languages.

::: term
**Function signature**
  : In a given function `func1`, the signature of the function is `type1 func1(arg1, arg2)`, which is the data type of the return value, the name of the function, and its arguments. Most programming languages enclose the arguments in parentheses.
\\\
  `type1 func1(arg1, arg2)` is the function signature of the function `func1`, because it serves to identify `func1` and differentiate it from other functions, even from other functions that may have the same name but different arguments or different data type of the return value.
:::

::: term
**Subroutine**
  : A function that takes no arguments and returns no return value, so a subroutine is a function that only envelops code without taking input in its arguments nor giving output in its return value.
\\\
  This is useful, for example, to abbreviate lines of code that are repeated multiple times. Placing the repeating lines of code in a subroutine makes the code easier to read and maintain.
:::

::: term
**Function overloading**
  : The process of creating functions with the same name but different function signatures.
:::

::: term
**Function overriding**
  : In object oriented languages, function overriding is the process of inheriting methods with the same name and signature as the methods from the parent.
:::

::: term
**Passing an argument by value**
  : The act of passing an argument by value, which means that when using a variable as the argument, a copy of the variable is passed to the function, so that modifying the argument does not modify the variable outside of the function. This is the default in most programming languages.
:::

::: term
**Passing an argument by reference**
  : The act of passing an argument by reference, which means that when using a variable as the argument, the variable itself (or a reference to it) is passed to the function, so that modifying the argument does modify the variable outside of the function.
:::

::: term
**Function recursion**
  : The act of calling a function from within itself. By this definition, recursion can lead to a situation in which function calls itself indefinitely. To avoid this, the function must provide a way to return without recursing.
\\\
  A function that calls itself, has a set of statements before doing the recursion call, and a set of statements after the recursion call, and they relate to each other like nested parentheses. For example, a function that calls itself, and then calls itself, and then again, 5 times in total, could be shown as (1(2(3(4(5 5)4)3)2)1), where (1, (2, (3, (4, and (5 represent the statements before recursion, and 5), 4), 3), 2), and 1) represent the statements after recursion. Recursion stops in the parentheses 5, then the parentheses 4 is closed, then parentheses 3, parentheses 2, and parentheses 1. To guarantee that recursion stops at parentheses 5, the function must return before doing the recursion call to parentheses 6.
:::

::: term
**Variable arguments**
  : The possibility for a function to accept a variable amount of arguments, so that it can be called with a different amount of arguments each time.
:::

### Types of programming languages

::: term
**Programming paradigms**
  : Styles with which different programming languages have been designed. Many different paradigms can be mixed and used with each other to design a programming language.
:::

::: term
**GPL**
  : GPL stands for General Purpose Language, which is a programming language capable of creating programs of any kind, from operating systems, CLI programs, GUI programs, to simple programs that add two numbers for example.
:::

::: term
**DSL**
  : DSL stands for Domain Specific Language, which is a language designed for specific purposes, for example a programming language to prove mathematical theorems, or a language to manage databases, or a language to create slideshow presentations, etcetera.
:::

::: term
**Imperative language**
  : A programming language designed on writing statements to be executed one after the other. This includes the possibility of writing statements to jump to previous or future statements (this is called a 'GOTO' statement). The 'GOTO' statement is considered the main characteristic of imperative languages, because derived paradigms resign the use of the 'GOTO' statement.
:::

::: term
**Declarative language**
  : A programming language designed on writing the intended outcome of the program. This is fairly aligned with the concept of a DSL, and so many DSL are also declarative languages. For example, a language to prove theorems, it's a DSL in which the inteded outcome is written (the intended outcome can be to prove a theorem). Not every declarative language is a DSL and also not every DSL has to be declarative.
\\\
  A programming language can have declarative features and imperative features. A given feature can be written in an imperative manner and also in a declarative manner, in the same programming language. What matters is that declarative code shows the intended outcome, while imperative code shows the step by step statements that lead to that outcome.
\\\
  This difference between imperative and declarative implies an overlap between the two concepts. A set of step by step statements can be considered to show the intended outcome. A single line with the intended outcome can be considered as a single step statement. In this sense imperative and declarative are just different ways to perceive and interpret code, in which imperative means steps without caring to show intended outcome, and declarative means steps that directly show the intended outcome.
:::

::: term
**Structured language**
  : An imperative language in which the use of 'GOTO' statements is forbidden. Control flow structures are used instead of 'GOTO', to make the execution jump to a different line of code.
:::

::: term
**Object oriented language**
  : An structured language in which objects can be created. **Objects** are composite data types that can store both variables (here called **attributes**) and functions (here called **methods**). Object Oriented Programming is acronymized as OOP.
\\\
  Objects can also have **properties**, which are attributes accessed via methods. The methods that write the value of a property are called **setters**, and the methods that read the value of a property are called **getters**. Attributes, properties, and methods, are called **members** in general. Objects are **instances** of a class, a **class** is what defines the members, and then the particular object instances can have each member with different values.
\\\
  New object instances are created with a special method of the class, called the **constructor**. Object instances are deleted from memory with a special method of the class, called the **destructor**.
\\\
  OOP has four main features: inheritance, polymorphism, abstraction, and encapsulation. **Inheritance** is the possibility that a class inherits the members from another, parent class. **Polymorphism** is the possibility of overriding the methods of the parent class. **Abstraction** is the possibility of creating classes with empty methods, so that the methods are implemented by the child classes. **Encapsulation** is the possibility of applying access modifiers to the members, the **access modifiers** are: **public** (accessible outside the class), **private** (accessible only inside the class), or **protected** (accessible by the class and its children).
\\\
  A **static** member is a member of the class, and not of each object. This means that the value of a static member is the same for all intances.
:::

::: term
**Functional programming language**
  : A declarative language in which functions are forbidden from changing variables outside their scope, and they have to always produce the same return value given the same arguments.
:::

::: term
**Statically typed language**
  : A programming language in which variables must be defined with a given data type. The data type of the variable can't be changed after defined.
:::

::: term
**Dynamically typed language**
  : A programming language in which variables are not defined with a given data type, so they can have any data type. The data type of the variable can be changed after defined.
:::

# BINARY, OCTAL, AND HEXADECIMAL NUMBERS

Binary numbers are the numbers that arise from creating a place value system with only two symbols for the numbers. Those two symbols can be anything, but they are commonly 0 and 1.

By using the place value system logic to get a sequence of consecutive numbers, the first binary numbers are: 0, 1, 10, 11, 100, 101, 110, etcetera.

Binary numbers are used by computers for storing or holding data, and for giving instructions to the CPU. In a computer, data is composed of binary numbers, for example the number 110110000100 could represent and orange tone color, this orange color would be stored as data with the number 110110000100.

The instructions that a computer can execute are also binary numbers, for example the number 0100 could mean the instruction of adding two numbers. The number 0100 is sent as a signal to the CPU and the CPU then adds two given numbers.

Octal numbers and hexadecimal numbers are used as ways to make binary numbers more human readable. Decimal numbers are not used because converting binary numbers to decimal numbers (and vice versa) is not an straightforward process, whereas converting binary numbers to octal or hexadecimal numbers (and vice versa) is straightforward.

Octal numbers use eight symbols to create numbers, the symbols are: 0, 1, 2, 3, 4, 5, 6, and 7. One octal digit is always equivalent to three binary digits, so two octal digits are equivalent to six binary digits, and so on. The following table shows the equivalencies for one octal digit to three binary digits.

: Octal digit to binary equivalencies

+-------+---------+
| Octal | Binary  |
+:=====:+:=======:+
|   0   |   000   |
+-------+---------+
|   1   |   001   |
+-------+---------+
|   2   |   010   |
+-------+---------+
|   3   |   011   |
+-------+---------+
|   4   |   100   |
+-------+---------+
|   5   |   101   |
+-------+---------+
|   6   |   110   |
+-------+---------+
|   7   |   111   |
+-------+---------+

An octal number is converted to a binary number by directly replacing each octal digit for its equivalent three binary digits. For example the octal number 374 has the same value as the binary number 011 111 100 (spaces are added for clarity, the binary number itself is 011111100).

A binary number is converted to an octal number by directly replacing each group of three binary digits for its equivalent octal digit. The groups of three binary digits are created from right to left. If there are not enough digits to form a group of three, then the group is filled with zeros to the left. For example the binary number 10100, in groups of three is the same as 010 100, note that one 0 had to be added to the left of the number, to form a group of three digits. The number 010 100 is the octal number 24.

The conversion between hexadecimal and binary numbers follows the same process.

Hexadecimal numbers use sixteen symbols to create numbers, the symbols are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F. One hexadecimal digit is always equivalent to four binary digits, so two hexadecimal digits are equivalent to eight binary digits, and so on. The following table shows the equivalencies for one hexadecimal digit to four binary digits.

: Hexadecimal digit to binary equivalencies

+-------------+--------+
| Hexadecimal | Binary |
+:===========:+:======:+
|    0        |  0000  |
+-------------+--------+
|    1        |  0001  |
+-------------+--------+
|    2        |  0010  |
+-------------+--------+
|    3        |  0011  |
+-------------+--------+
|    4        |  0100  |
+-------------+--------+
|    5        |  0101  |
+-------------+--------+
|    6        |  0110  |
+-------------+--------+
|    7        |  0111  |
+-------------+--------+
|    8        |  1000  |
+-------------+--------+
|    9        |  1001  |
+-------------+--------+
|    A        |  1010  |
+-------------+--------+
|    B        |  1011  |
+-------------+--------+
|    C        |  1100  |
+-------------+--------+
|    D        |  1101  |
+-------------+--------+
|    E        |  1110  |
+-------------+--------+
|    F        |  1111  |
+-------------+--------+

An hexadecimal number is converted to a binary number by directly replacing each hexadecimal digit for its equivalent four binary digits. For example the hexadecimal number B9 has the same value as the binary number 1011 1001 (spaces are added for clarity, the binary number itself is 10111001).

A binary number is converted to a hexadecimal number by directly replacing each group of four binary digits for its equivalent hexadecimal digit. The groups of four binary digits are created from right to left. If there are not enough digits to form a group of four, then the group is filled with zeros to the left. For example the binary number 10100, in groups of four is the same as 0001 0100, note that three 0 had to be added to the left of the number, to form a group of four digits. The number 0001 0100 is the hexadecimal number 14.

## Measuring binary number sizes in bytes

In computers, data and instructions are represented in binary numbers, and given that memory and storage have limited capacity to hold and store data and instructions, and the CPU has a limited instruction size, it's necessary to measure the sizes of binary numbers.

::: term
**Bit**
  : The smallest possible binary number size, so it is the size of a single binary number, be it 0 or 1. For example, the number 01001 has 5 bits. The amount of bits of a binary number is the same as the amount of its digits.
:::

::: term
**Byte**
  : A binary number of 8 bits. If a binary number has less than 8 digits, it can be represented as a byte by placing zeros to the left of the number until reaching 8 bits. For example the number 10010 can be represented as a byte by placing three zeros to the left: 00010010.
\\\
  Every byte can be written as two hexadecimal digits, because one hexadecimal digit is equivalent to four binary digits. For example the binary number 00010010 is the hexadecimal number 12.
\\\
  Bytes can also be called 'octets', because they are made of eight bits (octo means eight in Latin).
:::

::: term
**Kilobyte**
  : 1000 bytes.
:::

::: term
**Kibibyte**
  : 2^10^ bytes, which is 1024 bytes.
:::

::: term
**Megabyte**
  : 1000 Kilobytes, the same as 1 000 000 bytes.
:::

::: term
**Mebibyte**
  : 2^10^ Kibibytes, which is 1024 Kibibytes, the same as 1 048 576 bytes.
:::

::: term
**Gigabyte**
  : 1000 Megabytes, the same as 1 000 000 000 bytes.
:::

::: term
**Gibibyte**
  : 2^10^ Mebibytes, which is 1024 Mebibytes, the same as 1 073 742 000 bytes.
:::

::: term
**Terabyte**
  : 1000 Gigabytes, the same as 1 000 000 000 000 bytes.
:::

::: term
**Tebibyte**
  : 2^10^ Gibibytes, which is 1024 Gibibytes, the same as 1 099 511 627 776 bytes.
:::

**About the size of a byte**: a byte does not have to be 8 bits, it could be any other amount of bits. One advantage of 8 bits per byte is that 8 is a power of 2, 8 is 2^3^. Also, 8 is the next power of 2 after 7, and 7 bits is the amount of bits necessary for the ASCII character encoding, which is a character encoding with a minimum amount of characters for basic purposes.

## Character encoding

The character encoding is the way that letters, numbers, and symbols (characters in general) are represented as bytes and vice versa. Character encodings are necessary to have characters in a computer, so it is only possible to write these words in the first place, because of a character encoding.

A character encoding can hold each character in a constant amount of bytes, or in a given amount of bytes that differs from the amount to hold other characters. This is specified as part of the character encoding.

::: term
**Character set**
  : A set of characters. A character set can have several different character encodings, so the character encodings are akin to implementations of the character set. For example, the Latin letters form a character set, the letters, numbers, and punctuation marks form another character set. The Latin character set can have different encodings to represent each character as a byte.
:::

::: term
**Code point**
  : The number that identifies a given character in a character set. This number is commonly expressed as a hexadecimal number that accommodates as many bytes as specified by the character encoding. When expressed as a binary number, the code point shows the data with which its character is represented in a computer.
\\\
  For example, in many character encodings, the letter 'A' is encoded with the decimal number 65, which is the same as the hexadecimal number 41, or the binary number 101001. In a computer in which text is being encoded with one of those character encodings, the letter 'A' is hold or stored as the binary number 101001. If the character encoding allocates 1 byte per character, then the data to hold or store the letter 'A' is 00101001.
:::

::: term
**ASCII character encoding**
  : A basic character encoding that encodes 128 characters, using the numbers from 0 to 127, which requires allocating 7 bits per character (from 000 0000 to 111 1111). This encoding includes the Latin alphabet without diacritics, in uppercase and lowercase forms, numbers, punctuation marks, symbols, whitespace characters, and a few control characters (which serve to control the display of other characters, for example the 'backspace' character, with code point 000 1000, deletes the previous character when displayed).
:::

::: term
**Unicode character set**
  : A character set that aims to contain all symbols in all written languages of humanity.
\\\
  There are three main character encodings that implement the Unicode character set, they are UTF-8, UTF-16, and UTF-32. UTF stands for Unicode Transformation Format. The number indicates the amount of bits used per character, so UTF-8 allocates 8 bits per character, and when more characters are needed, UTF-8 allocates a second set of 8 bits per character. UTF-16 allocates 16 bits per character. UTF-32 allocates 32 bits per character, which uses more memory or storage than the other two character encodings to hold the same characters.
\\\
  UTF-8 is the most used to write in English because it uses the least amount of memory or storage for writing in English and other languages that use the Latin alphabet.
:::

# DATABASES

A database is a place used to store data. The idea of making a database is to organize the stored data or information.

::: term
**Relational database**
  : The most common kind of database when this was written. A relational database is made with tables, each table is called a relation. The data is measured or collected, each measurement is called a **record**. Each record has a set of attributes, when creating a record, the value of each attribute is measured or collected. The tables are made such that each row is a record, and each column is an attribute of the records (called a **field**). The name of each field acts as a column header. There are no row headers.
:::

::: term
**Record**
  : In a relational database, a record is a particular data measurement. Each record is a set of measured fields.
:::

::: term
**Field**
  : In a relational database, a field is also called an attribute, because each field represents a measurable attribute of each record.
:::

The following shows the structure of a relational database.

: Relation1

|     Field1     |     Field2     |     FieldN     |
| :------------: | :------------: | :------------: |
| Record1_Field1 | Record1_Field2 | Record1_FieldN |
| Record2_Field1 | Record2_Field2 | Record2_FieldN |
| RecordM_Field1 | RecordM_Field2 | RecordM_FieldN |


: RelationZ

|     Field1     |     Field2     |     FieldQ     |
| :------------: | :------------: | :------------: |
| Record1_Field1 | Record1_Field2 | Record1_FieldQ |
| Record2_Field1 | Record2_Field2 | Record2_FieldQ |
| RecordP_Field1 | RecordP_Field2 | RecordP_FieldQ |

This database contains the relations from Relation1 to RelationZ. Relation1 has the fields from Field1 to FieldN, with M records. RelationZ has the fields from Field1 to FieldQ, with P records.

To populate Relation1, then Record1, Record2, RecordM, are measured or collected. Measuring RecordM, means measuring the specific values RecordM_Field1, RecordM_Field2, RecordM_FieldN.

Here is a small example of a possible database.

: Data about people

| Name    | Age |
| :-----: | :-: |
| Person1 | 752 |
| Person2 |  88 |

::: term
**RDMS**
  : RDMS stands for Relational Database Management System. It can be a software program that allows managing a relational database, like creating new databases, new tables, new fields, or deleting them, among other managing operations.
:::

::: term
**CRUD**
  : CRUD stands for Create Read Update Delete. There are the basic four managing operations in a system of databases.
\\\
  The create operations allow creating new databases, new users that can access the database, etcetera.
\\\
  The read operations allow reading and retrieving records from the databases.
\\\
  The update operations allow changing parts of the databases, like their names, or the names of the fields, or update the records, etcetera.
\\\
  The delete operations allow deleting parts of the databases, like users of the databases, records, fields, tables, etcetera.
:::

::: term
**SQL**
  : SQL stands for Structured Query Language. An SQL is any Domain Specific Language that allows doing the CRUD operations on a system of databases, by following an specification called the SQL specification (which states how to write the CRUD operations).
\\\
  An example of an SQL is MySQL, which is a language that allows the CRUD operations, from creating new databases, to maintaining and deleting them and all their parts.
:::

::: term
**Database driver**
  : An API between a system of databases and a programming language. A database driver is used to do the CRUD operations by writing them in a given programming language. If a database is managed with an SQL, then the database driver is an API between the SQL and a programming language, and so SQL instructions can be written in the programming language, instead of writing them in SQL.
:::

# NETWORKS

::: term
**Protocol**
  : The same as a standard, but for networks.
:::

::: term
**Computer network**
  : A set of computers that can communicate with each other. This communication is possible when the computers follow a given protocol or set of protocols, so that they understand the data sent by other computers, and can send data understandable by the other computers in the network.
:::

::: term
**Network**
  : In a more general sense, a network can connect devices, not only computers. For this to happen, the devices must be able to connect to a network.
:::

::: term
**Internet**
  : A network, to which all computers and devices in the planet can be connected. The Internet makes it possible to connect any two devices in the planet Earth.
:::

::: term
**Network topology**
  : A particular way to connect the devices in a network.
\\\
  Many different ways to connect devices can be conceived. For example, in a computer network, there can be a central device, that communicates with all computers, and computers don't communicate with each other, but rather they communicate only with the central device, and then the central device routes the communications to and from the computers. Other possibility is for computers to be connected directly to each other, and so on.
:::

::: term
**Client-server topology**
  : One of the most common network topologies when this was written. In this topology, a server serves files, and there can be one or many clients that request those files. The communication would go like this: the client sends a request for a file to the server, then the server serves the file (by sending it) to the client. The file can be plain text, an image, or any kind of file.
:::

::: term
**Internet address**
  : A number that uniquely identifies a server on the Internet. There are two versions of this number: IPv4 and IPv6 (IP stands for Internet Protocol).
:::

::: term
**Internet domain**
  : A string of characters that represent an Internet address. The idea of using Internet domains, is to use words instead of numbers, to interact with servers.
\\\
  An internet domain has at least two parts, separated by a dot, like this: 'domain1.ccTLD1'. ccTLD stands for country code Top-Level Domain, it's a two letter string that identifies the country where the Internet domain is registered. The reason that the ccTLD is called the top level domain, is because the level of the domain increases from left to right. This allows creating subdomains, for example: 'subdomainN.subdomain1.domain1.ccTLD1', in here 'domain1' has N subdomains. Subdomains have a lower level than the domain, in the sense that subdomains are contained in the domain.
:::

::: term
**DNS**
  : DNS stands for Domain Name System, it's a system in charge of converting Internet addresses into Internet domains and vice versa. When a new server is born, and the owners of the server want to give it an Internet domain, they rent or buy from the DNS, the name that will be the Internet domain for the server. For example, a server with Internet address 98.89.90.NN can have an Internet domain 'domain1.cc1'. The DNS stores this information, and with it is able to map the Internet address to the Internet domain, and vice versa.
:::

::: term
**CDN**
  : CDN stands for Content Distribution Network. A CDN is a server that can cache (store) some of the contents of a given server, so that when a client sends a request to the given server for that content, the client can be served by the nearest server. This reduces the necessary time to serve the client.
:::

::: term
**Webpage**
  : The basic type of file that is served by servers to clients. Webpages are commonly HTML files, with .html extension, and they are served by the server to the client, using the HTTP protocol. Webpages can contain multimedia files like images, audios, videos, etcetera, this way the server can serve multimedia files to clients.
:::

::: term
**Browser**
  : An application that can display webpages. When a server serves a webpage to a client, the application that receives the webpage is the browser. This is why browsers are also called user agents, because browsers act as agents to represent the user before the server.
:::

::: term
**Web component**
  : A set of code that generates a specific part of a webpage. The idea of creating web components, is to reuse them, with programmed changes, so that repeating a web component becomes easier.
:::

::: term
**Website**
  : The set of webpages that are served when browsing a given Internet domain and its subdomains.
:::