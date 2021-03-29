<!-- 
#   Basic syntax
-->

<!-- #T# Table of contents -->

<!-- #C# Relationship between Markdown and HTML -->
<!-- #C# Metadata -->
<!-- #C# Normal text -->
<!-- #C# Headings -->
<!-- #C# Text formatting -->
<!-- #C# Bulleted lists -->
<!-- #C# Anchors, links -->
<!-- #C# Tables -->
<!-- #C# Blockquotes -->
<!-- #C# Source code -->
<!-- #C# Equations -->
<!-- #C# Decor -->

<!-- #T# Beginning of content -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# render a Markdown file as an HTML file with the pandoc command -->

<!-- # SYNTAX pandoc input_file1.md -s --katex -o output_file1.html -->

<!-- #T# Mathjax and/or Katex must be installed locally to render math equations from Markdown to HTML using Pandoc -->

<!-- #T# render a Markdown file as a PDF file with the pandoc command -->

<!-- # SYNTAX pandoc input_file1.md -o output_file1.pdf -->

<!-- #T# render a Markdown file as an HTML file stylized with a CSS file, but store the output as a PDF file with the pandoc command -->

<!-- # SYNTAX pandoc input_file1.md -s --katex -t html -c file1.css -o output_file1.pdf -->

<!-- #T# the Markdown syntax in this file includes regular Markdown syntax and also Pandoc Markdown syntax, because the Markdown files of this project at large are meant to be compiled with Pandoc -->

<!-- #T# the output of examples shown in this file, is the output of the pandoc command taking the example as input -->
<!-- # |------------------------------------------------------------- -->

<!-- #C# Relationship between Markdown and HTML -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# Markdown is a markup language that tries to be minimalistic, it tries to take the amount of markup down, hence its name -->

<!-- #T# as a markup language, Markdown can be converted into other markup languages, and Markdown was designed to be converted into HTML -->

<!-- #T# the same as in HTML, the tags in Markdown are classified as either blocks, or inlines, when parsing tags, block tags are parsed in a first step, and then inline tags in a second step -->

<!-- #T# regular HTML markup can be written directly in a Markdown file -->
<address>
    <q>quote1</q>
</address>

<!-- #T# invented tags are placed inside a <p> tag -->
<tag1>content1</tag1> <!-- # <p><tag1>content1</tag1></p> -->
<!-- # |------------------------------------------------------------- -->

<!-- #C# Metadata -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# metadata and configuration are enclosed inside a triple hyphens pair, using YAML syntax, at the start of a file -->

---
key1: value1
metadata: value of the metadata
title: Basic syntax
author: Unknown
date: 10 Feb 2020
lang: en
---

<!-- # |------------------------------------------------------------- -->

<!-- #C# Normal text -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# normal text is written without any special syxtax -->
Normal text, normal text.

<!-- #T# paragraphs are separated with a blank line between them -->
Paragraph1

Paragraph2

<!-- #T# text in consecutive lines form a single paragraph, because of whitespace collapse -->
Text in paragraph1
  More text in paragraph1 <!-- # Text in paragraph1 More text in paragraph1 -->

<!-- #T# to write text without collapsing whitespace, it can be indented with four or more spaces, text indented with four or more spaces is treated as preformatted code text -->
    Preformatted code text
      Whitespace  will   be  preserved as long as it's indented with four or more spaces, a newline is NOT created at the end of the margin of the page, so this line may overflow outside of the page.
<!-- # |------------------------------------------------------------- -->

<!-- #C# Headings -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# headings start with the hash #, up to 6 consecutive hashes ###### -->
# Heading1
## Heading2
### Heading3
#### Heading4
##### Heading5
###### Heading6

<!-- #T# a heading can end with hashes, after a space all ending hashes will be ignored -->
## Heading text ####### end ####################
<!-- # Heading text ####### end -->

<!-- #T# the first two heading levels can also be made by underlining the heading text with at least one '=' for the first level, and with at least one '-' for the second level -->
Heading level 1 
=

Heading level 1 
===============

Heading level 2
-

Heading level 2
---------------
<!-- # |------------------------------------------------------------- -->

<!-- #C# Text formatting -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# bold text is written within double asterisks ** or double underscores __ -->
Normal text **bold text** continue normal __bold text two.__

<!-- #T# italic text is written within single asterisks * or single underscores _ -->
Normal text *italic text* continue normal _italic text two._

<!-- #T# italic bold text is written within triple asterisks *** -->
Normal text ***italic bold text*** continue normal

<!-- #T# strikethrough text is written within double tildes ~~ -->
~~strikethrough text~~

<!-- #T# superscript text is written inside HTML style tags called 'sup' -->
Text<sup>superscript text</sup>

<!-- #T# subscript text is written inside HTML style tags called 'sub' -->
Text<sub>subscript text</sub>
<!-- # |------------------------------------------------------------- -->

<!-- #C# Bulleted lists -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# sublists are introduced with 4 spaces before the list symbol -->

<!-- #T# make ordered lists with any number and a dot, num1., preformatted text is indented four spaces relative to the previous paragraph -->
1. item1

   text in item1

       preformatted  text

    1. subitem1
        1. subsubitem1

           preformatted text in subsubitem1

        1. subsubitem2
    1. subitem2
1. item2
1. item3

<!-- #T# make unordered lists with asterisks *, plus + or minus -, the indentation is neccessary to distinguish sublevels -->
* item
    + subitem
        - subsubitem
            * subsubsubitem
+ item
<!-- # |------------------------------------------------------------- -->

<!-- #C# Anchors, links -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# create anchors to links -->
<!-- # SYNTAX [anchor_text1](hyperlink1) -->
[anchor to Duckduckgo](https://duckduckgo.com/)

<!-- #T# embed images with an anchor but starting with an exclamation mark -->
<!-- # SYNTAX ![image_anchor_text1](image_location1) -->
![image1](../../Octave/S1_Basic/S1_08_B__Aux01.svg)
<!-- # |------------------------------------------------------------- -->

<!-- #C# Tables -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# tables are defined with a vertical bar | per row, and below the headers at least one hyphen - per column. Colon signs : can be used to set the text alignment per column, '-:' is for right justification, ':-' is for left justification, ':-:' is for center justification -->

<!-- #T# table with minimal elements -->
Column1 |
 -:
first_cell_string1 |
second_cell_string1 |
<!-- #| '-:' makes the text alignment right justified -->

<!-- #T# prettier table -->
| Column1 | Column2 | Column3 |
| :-----: | ------: | :------ |
| text1   | text2   | text3   |
<!-- # |------------------------------------------------------------- -->

<!-- #C# Blockquotes -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# create a blockquote by starting each line in the block with the greater than symbol -->
> Text in the blockquote is
> commonly for related content

<!-- #T# preformatted text is inserted in a blockquote, after four or more spaces, which means five or more spaces totals after the '>', because the blockquote takes one space after the '>' -->
> Line1
>
>     Preformatted text in the blockquote
<!-- # |------------------------------------------------------------- -->

<!-- #C# Source code -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# one liner code goes within backticks -->
`line_of_code = 1`

<!-- #T# fence multiple lines of code within a pair of three or more backticks, an info string can be placed after the first backticks line, the info string indicates the language inside the fenced code block, the info string must not have spaces -->
```C
    if(line_of_code == 1)
    {
        print("str1");
    }
```
<!-- #T# available syntax highlighting options are, 'C' (as shown), 'json', 'python' -->

<!-- #T# extra options are, 'mermaid' (creates diagrams from plain text), 'smiles' (creates a 2D molecular diagram of a given molecule) -->

<!-- fenced code blocks can also be created inside a pair of three or more tildes -->
~~~~~~~~~~~~~~~~~~~~~~~~~~ python
    def func1():
        return 5
~~~~~~~~~~~~~~~~~~~~~~~~~~
<!-- # |------------------------------------------------------------- -->

<!-- #C# Equations -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# equations can be written, using Latex syntax -->

<!-- #T# inline equations are enclosed in single dollar signs -->
Inline $x = 3$ equation

<!-- #T# an equation block is enclosed in double dollar signs, the equation numbering can be set in parentheses after the double dollar signs -->
$$\alpha A\pm\sqrt{x} \over y^{2}$$ (1)
<!-- # |------------------------------------------------------------- -->

<!-- #C# Decor -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# draw an horizontal line (known as a thematic break) with four hyphens preceded by a newline and followed by a newline -->
text before horizontal line

----

text after horizontal line

<!-- #T# this can also be done with three hyphens, but here four hyphens are used to differentiate it from the YAML delimiters which are three hyphens -->

<!-- #T# an horizontal line can also be drawn with three asterisks or with three underscores, in these two cases, the preceding and following newlines are not required -->
***
___
<!-- # |------------------------------------------------------------- -->