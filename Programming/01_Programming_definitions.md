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
        Processor --- Memory & Storage
        Memory --- Storage
      end
    end
    Computer --> Output
  end
  Output --> Input

  linkStyle default interpolate linear
  style Computer stroke: black
```