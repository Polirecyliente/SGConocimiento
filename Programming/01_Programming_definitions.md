---
title: PROGRAMMING DEFINITIONS
toc-title: Table of Contents
---

::: {#toc-id}
## Table of Contents {#toc-title}

-   [[1]{.toc-section-number} INTRODUCTION](#introduction)
-   [[2]{.toc-section-number} BASIC CONCEPTS](#basic-concepts)
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
**Programming language**
  : A language in which to write source code. The compiler or interpreter effectively determines the possible statements that can be created with a programming language. For example, if a compiled language is defined with certain feature, but the current compiler does not support that feature, then any source code file that uses that feature will throw error when compiled with said compiler.
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