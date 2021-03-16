<!-- 
    Basic syntax
-->

<!-- #T# Table of contents -->

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
<!-- #T# using the CLI, render a Markdown file as an HTML file with the pandoc command -->

<!-- # pandoc --katex input_file1.md -o output_file1.html -->

<!-- #T# using the CLI, render a Markdown file as a PDF file with the pandoc command -->

<!-- # pandoc --katex input_file1.md -o output_file1.pdf -->

<!-- #T# render a Markdown file as an HTML file (no CLI) using the Markdown Preview Enhanced extension, right click the .md preview file and click "Open in Browser", this can be printed as PDF in Chromium -->
<!-- # |------------------------------------------------------------- -->

<!-- #C# Metadata -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# metadata key value pairs are enclosed inside a three hyphens pair, a key is separated from its value with a colon -->

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
<!-- # |------------------------------------------------------------- -->

<!-- #C# Text formatting -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# bold text is written within double asterisks ** or double underscores __ -->
Normal text **bold text** continue normal __bold text two.__

<!-- #T# italic text is written within single asterisks * or single underscores _ -->
Normal text *italic text* continue normal _italic text two._

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

<!-- #T# make ordered lists with any number and a dot, num1. -->
1. item1
    1. subitem1
        1. subsubitem1
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
<!-- # |------------------------------------------------------------- -->

<!-- #C# Source code -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# one liner code goes within backticks -->
`line_of_code = 1`

<!-- #T# fence multi line code within a 3 backticks pair -->
```C
    if(line_of_code == 1)
    {
        print("str1");
    }
```
<!-- #T# available syntax highlighting options are, 'C' (as shown), 'json'  -->

<!-- #T# extra options are, 'mermaid' (creates diagrams from plain text), 'smiles' (creates a 2D molecular diagram of a given molecule) -->
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
<!-- #T# draw an horizontal line with four hyphens preceded by a newline and followed by a newline -->
text before horizontal line

----

text after horizontal line
<!-- # |------------------------------------------------------------- -->