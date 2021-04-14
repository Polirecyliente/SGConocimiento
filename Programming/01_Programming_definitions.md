---
title: PROGRAMMING DEFINITIONS
toc-title: Table of Contents
---

::: {#toc-id}
## Table of Contents {#toc-title}

-   [[1]{.toc-section-number} INTRODUCTION](#introduction)
-   [[2]{.toc-section-number} BASIC CONCEPTS](#basic-concepts)
-   [[3]{.toc-section-number} PROGRAMMING LANGUAGES](#programming-languages)
-   [[4]{.toc-section-number} ALGORITHMS](#algorithms)
    -   [[4.1]{.toc-section-number} Cryptography](#cryptography)
-   [[5]{.toc-section-number} APPLICATIONS](#applications)
-   [[6]{.toc-section-number} NETWORKING](#networking)
:::

# INTRODUCTION

This document contains the definitions needed to understand computer programming.

# BASIC CONCEPTS

**Computer**
  : A device that can do computations.
  \
  For a user to make use of a computer, the user needs a way to let the computer know the computations that should be carried out, this is called **input**. On the other hand, the computer needs a way to let the user know the results of the computations, this is called **output**. Depending on the output, the user sends new input to the computer, and the computer sends to the user the results of the computations as new output. This establishes a cycle of interactions between the user and the computer.
  \
  For this cycle of interactions to take place, the computer must have peripherics that receive the input from the user. The computer interprets this input to know which computations must be carried out. The computer must also have peripherics that send the output to the user. After the computations are carried out, the computer sends the output using these peripherics.

**Input peripherics**
  : Devices connected to a computer, used by the user to send input to the computer. Input peripherics can be made into parts of the computer itself.
  \
  The most common input peripherics are: the mouse and the keyboard. The mouse is used as a pointing device, the input consists of pointing to different points in space. The keyboard is used to send character input to the computer, to be able to write, and to send in band signaling (which means sending instructions via a sequence of characters, instead of sending the characters themselves).

**Output peripherics**
  : Devices connected to a computer, used by the computer to send output to the user. Output peripherics can be made into parts of the computer itself.
  \
  The most common output peripherics are: the monitor and the printer. The monitor is used to display output from computations in real time. The printer is used to print documents.

# PROGRAMMING LANGUAGES

AST: Abstract Syntax Tree, a tree diagram to show the syntactic elements in a given source code.

DOM: Document Object Model, in a markup language, the DOM is the set of tags and their hierarchical structure.

GPL: General Purpose Language, a programming language capable of creating programs of any kind.

DSL: Domain Specific Language, a language used with a particular purpose, that doesn't work for creating programs of any kind.

SQL: Structured Query Language, a DSL used to query and manage databases.

SGML: Standard Generalized Markup Language, a standard to define markup languages. For example, HTML and XML comply with this standard.

HTML: HyperText Markup Language, a markup language commonly used to create webpages, because browsers understand HTML, browsers draw a webpage from a given HTML file.

XML: eXtended Markup Language, a multipurpose markup language, commonly used as a format for applications to write their output.

# ALGORITHMS

## Cryptography

DSA: Digital Signature Algorithm, an asymmetric cryptography (public key) algorithm.

ECDSA: Elliptic Curve Digital Signature Algorithm, a variant of the DSA.

EdDSA: Edwards-curve Digital Signature Algorithm, an asymmetric cryptography (public key) algorithm.

RSA: Rivest, Shamir, Adleman, an asymmetric cryptography (public key) algorithm.

# APPLICATIONS

LSP: Language Server Protocol, a protocol to provide autocompletion for a given language, for example to autocomplete libraries so that available libraries can be listed.

IDE: Integrated Development Environment, an application used to write code, so it commonly has syntax highlight, an LSP for autocompletion,

# NETWORKING

MIME: Multipurpose Internet Mail Extensions, a way to express file extensions.

HTTP: Hypertext Transfer Protocol, a networking protocol to exchange hypertext files.