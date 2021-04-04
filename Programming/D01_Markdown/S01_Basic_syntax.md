<!-- 
#   Basic syntax
-->

<!-- #T# Table of contents -->

<!-- #C# Relationship between Markdown and HTML -->
<!-- #C# Metadata -->
<!-- #C# Normal text -->
<!-- #C# Headings -->
<!-- #C# Text formatting -->
<!-- #C# Links, images and videos, footnotes, citations -->
<!-- #C# Blocks of content -->
<!-- #C# - Tables -->
<!-- #C# - Lists of items -->
<!-- #C# - Blockquotes -->
<!-- #C# - Source code -->
<!-- #C# - Equations -->
<!-- #C# Decor and characters -->
<!-- #C# Inserting raw code from other languages -->

<!-- #T# Beginning of content -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# the Markdown syntax in this file includes regular Markdown syntax and Pandoc Markdown syntax, because the Markdown files of this project at large are meant to be converted to other formats with Pandoc -->

<!-- #T# render a Markdown file as an HTML file with the pandoc command -->

<!-- # SYNTAX pandoc input_file1.md -s --katex -o output_file1.html -->

<!-- #T# Mathjax and/or Katex must be installed locally to render math equations from Markdown to HTML using Pandoc -->

<!-- #T# render a Markdown file as a PDF file with the pandoc command -->

<!-- # SYNTAX pandoc input_file1.md -o output_file1.pdf -->

<!-- #T# render a Markdown file as an HTML file stylized with a CSS file, but store the output as a PDF file with the pandoc command -->

<!-- # SYNTAX pandoc input_file1.md -s --katex -t html -c file1.css -o output_file1.pdf -->

<!-- #T# the HTML output of examples shown in this file, is the output of the pandoc command taking the example as input -->
<!-- # |------------------------------------------------------------- -->

<!-- #C# Relationship between Markdown and HTML -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# Markdown is a markup language that tries to be minimalistic, it tries to take the amount of markup down, which is a possible reason for its name -->

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
<!-- #T# the default metadata can be set at the start of the file, as three lines that start with a percent sign, the first for the title, the second for the authors, and the third for the date, the title can span several lines, the authors can be placed one per line or separated by semicolon -->
% Title of
  this file
% Author1; Author2;
  Author3
% 15 Dec

<!-- #T# metadata and configuration are enclosed inside a triple hyphens pair, using YAML syntax, at the start of the file -->
---
key1: value1
key2: value2
---

<!-- #T# the following metadata shows key value pairs understood by Pandoc -->
---
title: Title for this document
author: Unknown
date: 10 Feb 2020
lang: en
toc-title: Title for the table of contents
nocite: |
  @source_id1, @source_id2
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

<!-- #T# line blocks are another way to write text without collapsing whitespace, and to use the same font of regular text, line blocks are created with a vertical bar and a space starting the text of a line -->
| line1
|  line2
|   line3
|             lineE
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

<!-- #T# headings can have metadata, specifically an identifier, HTML classes, and key value pairs (treated as HTML attribute value pairs) -->
<!-- # SYNTAX Heading1 {#id1 .class1 .class2 key1='value1' key2='value2'} -->
# First heading {#id1 .class1 .class2 key1='value1' key2='value2'}
<!-- # <h1 class="class1 class2" data-key1="value1" data-key2="value2" id="id1">First heading</h1> #| the keys in the key value pairs have 'data-' prepended to them -->

<!-- #T# there are a few predefined classes for headings -->
<!-- #T#     the .unnumbered class makes its heading unnumbered, even if the other headings are numbered (it's not counted in the numbering) -->
<!-- #T#     the .unlisted class takes its heading out of the table of contents, it must be used along with the .unnumbered class -->
<!-- # |------------------------------------------------------------- -->

<!-- #C# Text formatting -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# bold text is written within double asterisks ** or double underscores __ -->
Normal text **bold text** continue normal __bold text two.__

<!-- #T# the double asterisks that create bold text act as an inline tag, inline tags are parse from beginning to end of the line -->
Normal text **bold** normal asterisks** text <!-- #| the third set of double asterisks is treated as plain text -->

<!-- #T# italic text is written within single asterisks * or single underscores _ -->
Normal text *italic text* continue normal _italic text two._

<!-- #T# italic bold text is written within triple asterisks *** -->
Normal text ***italic bold text*** continue normal

<!-- #T# strikethrough text is written within double tildes ~~ -->
~~strikethrough text~~

<!-- #T# superscript text is written inside carets, with space escaped -->
Text ^superscript\ text^

<!-- #T# subscript text is written inside tildes, with space escaped -->
Text ~subscript\ text~

<!-- #T# small capitalization style is applied to the text of a <span> element with the .smallcaps class -->
Text [Text in small caps]{.smallcaps} text
<!-- # |------------------------------------------------------------- -->

<!-- #C# Links, images and videos, footnotes, citations -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# create links with the following syntax -->
<!-- # SYNTAX [link_name1](target/of/link1 "link_tooltip1") -->
[link to Duckduckgo](https://duckduckgo.com/ "link tooltip")

<!-- #T# a link reference defines a link, with a link name, a path to the target location of the link, and a tooltip that displays when hovering the mouse over the link, the link reference only defines a link, i.e. it's not a link in itself and it doesn't appear when converting into HTML -->
<!-- # SYNTAX [link_name1]: target/of/link1 "link_tooltip1" -->
[link to something]: target/of/link1 "link tooltip"

<!-- #T# in a link reference, the link target location can also be written inside angle brackets, the angle brackets can be empty, the tooltip is optional -->
[link to something]: <target/of/link1>

<!-- #T# given that the link reference only defines a link, to create instances of the link, only the link name is required, it can be repeated in different places, each repetition is another instance of the link, a link instance can be placed before its link reference -->
<!-- # SYNTAX [link_name1] -->
text [link to something] text [link to something] text

<!-- #T# links can have metadata, specifically an identifier, HTML classes, and key value pairs (treated as HTML attribute value pairs) -->
<!-- # SYNTAX [link_name1]: target/of/link1 "link_tooltip1" {#id1 .class1 .class2 key1='value1' key2='value2'} -->
[link to something]: target/of/link1 "link tooltip" {#id1 .class1 .class2 key1='value1' key2='value2'}
<!-- # <p><a href="target/of/link1" id="id1" class="class1 class2" data-key1="value1" data-key2="value2" title="link tooltip">link to something</a></p> -->

<!-- #T# embed images with a link, but starting with an exclamation mark -->
<!-- # SYNTAX ![image_link_name1](path/to/image1 "link_tooltip1") -->
![image1](../path/to/image1.svg "image tooltip")

<!-- #T# create a link reference to an image like a regular link reference -->
[link to an image]: path/to/image1 "image tooltip"

<!-- #T# create an instance of a link to an image, by starting with an exclamation mark -->
![link to an image]

<!-- #T# a link can point to another link, which points to a given location, this effectively is a way to create a link with a new name -->
<!-- # SYNTAX [new_link_name1][link_name1] -->
[new link name][link to something] <!-- #| this points to target/of/link1 -->

<!-- #T# a link to a video is made with the same syntax as a link to an image -->
![link to a video](/path/to/video1.mp4)

<!-- #T# headings can be linked to, by placing their content as the link name -->
# Heading one
[Heading one]
[text to link to the heading][Heading one] 
<!-- # <p><a href="#heading-one">text to link to the heading</a></p> -->

<!-- #T# a link to a heading can be created this way as well -->
# Heading two
[link to heading](#heading-two)

<!-- #T# footnote references are created with the following syntaxes -->

<!-- # SYNTAX [^int1] -->
<!-- #T# int1 is a number for the footnote -->

Text [^3] text. <!-- #| this is rendered as Text ^1^ text. -->

<!-- # SYNTAX [^string1] -->
<!-- #T# string1 is a single word for the footnote -->

Text [^footnote_string] text. <!-- #| this is rendered as Text ^2^ text. -->

<!-- #T# the footnote content itself must be placed in the file, it starts as [^footnote_label1]: -->
[^3]: content of the footnote
[^footnote_string]: content of the footnote

<!-- #T# the footnotes are numbered sequentially, regardless of the label used to create them -->

<!-- #T# an inline footnote is created with the following syntax -->
<!-- # SYNTAX ^[footnote_text1] -->
text text^[text in the footnote]

<!-- #T# a citation is created with this syntax -->

<!-- # SYNTAX [@citation_label1] -->
<!-- #T# citation_label1 must be a citation label written in a bibliography file such as a .bib file or a .yaml file. To render the bibliography, see Pandoc.md -->

text [@book1] text <!-- Markdown output #| text (Author1 Year1) text -->

<!-- #T# an inline citation is created with this syntax -->
<!-- # SYNTAX @citation_label1 -->
text @book1 text <!-- Markdown output #| text Author1 (Year1) text -->
<!-- # |------------------------------------------------------------- -->

<!-- #C# Blocks of content -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# blocks of content contain their content (like text, images, etc.) in blocks, some blocks have an inline version -->

<!-- #T# the generic block of content in HTML is the <div> tag, this is created by enclosing content in a pair of three or more colons, the first pair must be followed by an info string of a single word, the info string is treated as the class of the <div> tag -->
::: info_string1
  text in a block
:::
<!-- # <div class="info_string1"><p>text in a block</p></div> -->

<!-- #T# div blocks can be nested -->
::: div1
text1

:::: div2
text2
::::

:::

<!-- #T# the inline version is the <span> tag, which is made here by placing metadata on a link, doing so converts the link into a <span> tag, the metadata that can be used is an identifier, HTML classes, and key value pairs (treated as HTML attribute value pairs) -->
<!-- # SYNTAX [span_content1]{#id1 .class1 .class2 key1='value1' key2='value2'} -->
[text in a span]{#id1 .class1 .class2 key1='value1' key2='value2'}
<!-- # <p><span id="id1" class="class1 class2" data-key1="value1" data-key2="value2">text in a span</span></p> -->

<!-- #C# - Tables -->

<!-- # |----- -->
<!-- #T# there are a few ways to create a table -->

<!-- #T# a way to create a table, is with a vertical bar | separating the columns, and below the headers at least one hyphen - per column -->

<!-- #T# colon signs : are used to set the text alignment per column, '-:' is for right justification, ':-' is for left justification, ':-:' is for center justification -->

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

<!-- #T# a table caption can be created, it works the same for all four ways of making a table, a table caption is created with a colon and a space followed by the table caption, the table caption can be placed above or below the table, separated by zero or more blank lines -->
: Table caption1

|  Center  |   Right | Left    |
| :------: | ------: | :------ |
|  text1   |   text2 | text3   |
|  textA   |   textB | textC   |

<!-- #T# another way to create a table, is with the headers placed above hyphens, the alignment of the header over the hyphens determines the text alignment in its column -->

<!-- #T# given that a line of hyphens under text can be interpreted as a heading, a table of this type requires either at least two columns, or one column with a table caption on top -->
 Center     Right Left
-------- -------- -------
 text1      text2 text3
 textA      textB textC

<!-- #T# a version of this table without headers can be done by enclosing the table within two lines of hyphens separated by column, the column alignment is based on the first line of each column -->
-------- -------- -------
 text1      text2 text3
 textA      textB textC
-------- -------- -------

<!-- #T# another way to create a table is by enclosing the table in two rows filled with hyphens, with the table rows separated by blank lines, this allows the table to have table rows with multiple lines -->

<!-- #T# for the column alignment, each header has hyphens below, and the alignment of the header over the hyphens determines the text alignment in its column -->
-------------------------
 Center     Right Left
-------- -------- -------
 text1      text2 text3
 text1

 textA      textB textC
                  textC
-------------------------

<!-- #T# a version of this table without headers can be done by enclosing the table within two lines of hyphens separated by column, the column alignment is based on the first line of each column -->
-------- -------- -------
 text1      text2 text3
 text1

 textA      textB textC
                  textC
-------- -------- -------

<!-- #T# another way to create a table is by creating a grid, with a plus in each table cell corner, row separators are hyphens, column separators are vertical bars, and the headers are placed on top of equal signs -->

<!-- #T# column alignment is set the colons, '=:' is for right justification, ':=' is for left justification, ':=:' is for center justification -->
+--------+--------+--------+
| Center |  Right | Left   |
+:======:+=======:+:=======+
| text1  |  text2 | text3  |
| text1  |        |        |
+--------+--------+--------+
| textA  |  textB | textC  |
|        |        | textC  |
+--------+--------+--------+

<!-- #T# a version of this table without headers can be done by replacing the equals with hyphens -->
+:------:+-------:+:-------+
| text1  |  text2 | text3  |
| text1  |        |        |
+--------+--------+--------+
| textA  |  textB | textC  |
|        |        | textC  |
+--------+--------+--------+
<!-- # |----- -->

<!-- #C# - Lists of items -->

<!-- # |----- -->
<!-- #T# make ordered lists with any number and a dot, num1., preformatted text is indented four spaces relative to the previous paragraph, sublists are introduced with the same indentation of the paragraph of the previous list item -->

<!-- #T# the first number in the ordered list is taken as an starting value to number the list items -->
4. item1 <!-- #| this list starts with 4 -->

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

<!-- #T# the text in a list item must be separated by at least one space from the list marker (num1. for ordered lists, and *, +, - for unordered lists) -->

<!-- #T# ordered lists can also be created in several different ways -->
<!-- #T#     a number followed by a closing parenthesis, num1) -->
<!-- #T#     a number inside parentheses, (num1) -->
<!-- #T#     a lowercase letter followed by a dot, lower_letter1. -->
<!-- #T#     a lowercase letter followed by a closing parenthesis, lower_letter1) -->
<!-- #T#     a lowercase letter inside parentheses, (lower_letter1) -->
<!-- #T#     an uppercase letter followed by a dot and two spaces, upper_letter1.  -->
<!-- #T#     an uppercase letter followed by a closing parenthesis, upper_letter1) -->
<!-- #T#     an uppercase letter inside parentheses, (upper_letter1) -->
<!-- #T#     a lowercase roman numeral followed by a dot, lower_roman_num1. -->
<!-- #T#     a lowercase roman numeral followed by a closing parenthesis, lower_roman_num1) -->
<!-- #T#     a lowercase roman numeral inside parentheses, (lower_roman_num1) -->
<!-- #T#     an uppercase roman numeral followed by a dot and two spaces, upper_roman_num1.  -->
<!-- #T#     an uppercase roman numeral followed by a closing parenthesis, upper_roman_num1) -->
<!-- #T#     an uppercase roman numeral inside parentheses, (upper_roman_num1) -->
<!-- #T#     a hash followed by a point, #. -->
1) item1
2) item2

(7) item7
(1) item8

z. item z
c. item aa

z) item z
c) item aa

(z) item z
(c) item aa

Z.  item Z
H.  item AA

Z) item Z
H) item AA

(Z) item Z
(H) item AA

iii. item iii
 iv. item iv
  v. item v

iii) item iii
 iv) item iv
  v) item v

(iii) item iii
 (iv) item iv
  (v) item v

III.  item III
 IV.  item IV
  V.  item V

III) item III
 IV) item IV
  V) item V

(III) item III
 (IV) item IV
  (V) item V

#. item1
#. item2

<!-- #T# a checklist can be created with an unordered list, starting each list item with a pair of square brackets with a space inside -->

<!-- an 'x' inside a pair of brackets indicates a checklist item being checked -->
- [x] checklist item 1 checked
- [ ] checklist item 2
- [ ] checklist item 3

<!-- #T# definition lists can be created, a term is created as a regular paragraph, and then the definitions of the term are placed below, starting each definition with a colon or a tilde -->

<!-- #T# terms are separated with a blank line -->
Term1
~ Definition1
~ Definition2

Term1
  : Definition1
  : Definition2

<!-- #T# the parts of a definition list can be separated with blank lines, this extra spacing is preserved in the output -->
Term1

: Definition1

: Definition2

<!-- #T# example lists can be created, they are numbered lists whose list items do not need to be contiguous, so their items are numbered up to the end of the file -->

<!-- #T# example list items are created with an at symbol enclosed in parentheses (@) starting the line -->

<!-- #T# an example list item can be named, so that it can be referenced in other places, using the syntax (@name1) -->
(@) item1
(@example_item2) item2

paragraph

paragraph that references (@example_item2)

(@) item3
<!-- # |----- -->

<!-- #C# - Blockquotes -->

<!-- # |----- -->
<!-- #T# create a blockquote by starting each line in the block with the greater than symbol -->
> Text in the blockquote is
> commonly for related content

<!-- #T# preformatted text is inserted in a blockquote, after four or more spaces, which means five or more spaces totals after the '>', because the blockquote takes one space after the '>' -->
> Line1
>
>     Preformatted text in the blockquote
<!-- # |----- -->

<!-- #C# - Source code -->

<!-- # |----- -->
<!-- #T# inline code goes within backticks -->
`line_of_code = 1`

<!-- #T# if the inline code requires using backticks as a character, then the number of enclosing backticks must be different -->
``a ` b`` <!-- # <p><code>a ` b</code></p> -->
` a `` b ` <!-- # <p><code>a `` b</code></p> -->

<!-- #T# fence multiple lines of code within a pair of three or more backticks, an info string can be placed after the first backticks line, the info string indicates the language inside the fenced code block, the info string must not have spaces -->
```C
    if(line_of_code == 1)
    {
        print("str1");
    }
```
<!-- #T# available syntax highlighting options are, 'C' (as shown), 'json', 'python', and others, to see the list, execute in a Bash shell `pandoc --list-highlight-languages` -->

<!-- #T# extra options are, 'mermaid' (creates diagrams from plain text), 'smiles' (creates a 2D molecular diagram of a given molecule) -->

<!-- #T# fenced code blocks can also be created inside a pair of three or more tildes -->
~~~~~~~~~~~~~~~~~~~~~~~~~~ python
def func1():
    return 5
~~~~~~~~~~~~~~~~~~~~~~~~~~

<!-- #T# fenced code blocks can have metadata, specifically an identifier, HTML classes, and key value pairs (treated as HTML attribute value pairs) -->
<!-- # SYNTAX ~~~ {#id1 .class1 .class2 key1='value1' key2='value2'} -->
~~~~~~~~~~~~ {#id1 .class1 .class2 key1='value1' key2='value2'}
text
~~~~~~~~~~~~
<!-- # <pre id="id1" class="class1 class2" data-key1="value1" data-key2="value2"><code>text</code></pre> -->

<!-- #T# as can be seen, if a fenced code block has metadata then it cannot have an info string, the programming language of the code block can be passed as a predefined class, there are a few predefined classes and attributes for code blocks -->
<!-- #T#     the .python class sets the language of the code block to be Python -->
<!-- #T#     the .numberLines class is used to number the lines in the code block -->
<!-- #T#       the startFrom attribute is a number that sets the starting line number of the code block -->
~~~ {.numberLines startFrom=5}
line5
line6

line8
~~~
<!-- # |----- -->

<!-- #C# - Equations -->

<!-- # |----- -->
<!-- #T# equations can be written, using Latex syntax -->

<!-- #T# inline equations are enclosed in single dollar signs -->
Inline $x = 3$ equation

<!-- #T# an equation block is enclosed in double dollar signs, the equation numbering can be set in parentheses after the double dollar signs -->
$$\alpha A\pm\sqrt{x} \over y^{2}$$ (1)
<!-- # |----- -->

<!-- # |------------------------------------------------------------- -->

<!-- #C# Decor and characters -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# draw an horizontal line (known as a thematic break) with four hyphens preceded by a newline and followed by a newline -->
text before horizontal line

----

text after horizontal line

<!-- #T# this can also be done with three hyphens, but here four hyphens are used to differentiate it from the YAML delimiters which are three hyphens -->

<!-- #T# an horizontal line can also be drawn with three asterisks or with three underscores, in these two cases, the preceding and following newlines are not required -->
***
___

<!-- #T# operators can be escaped with a backslash -->
text \*\*not bold\*\* text <!-- #| the asterisks are taken literally -->

<!-- #T# to get a literal backslash, it must be escaped -->
text \\a text <!-- # <p>text \a text</p> -->

<!-- #T# the newline at the end of a line can be escaped to be taken literally -->
line1\
line2

<!-- #T# the backslash is always literal in verbatim environments -->
    text \* text
<!-- # <pre><code>text \* text</code></pre> -->

<!-- #T# insert unicode characters with their hexadecimal code point -->
<!-- # SYNTAX &#xHex_num1; -->
&#x02A0;

<!-- #T# HTML entities can also be inserted -->
&amp;
<!-- # |------------------------------------------------------------- -->

<!-- #C# Inserting raw code from other languages -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# raw code from other languages can be written and used in this file, for this, the inline code and the fenced code blocks are used, with the language of the raw code being the only metadata, specified after an equal sign inside the metadata curly braces -->
Raw Latex: `\begin{align}\sqrt{x_1}\end{align}`{=latex}
<!-- # |------------------------------------------------------------- -->