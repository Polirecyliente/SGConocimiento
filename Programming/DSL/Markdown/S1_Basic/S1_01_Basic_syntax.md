<!-- 
    Basic syntax
-->

<!-- #T# normal text is written without any special syxtax -->
Normal text, normal text.

<!-- #T# headers start with the hash symbol, up to 6 -->
# Header1
## Header2
###### Header6

<!-- #T# bold text is written within double asterisks or double underscore -->
Normal text **bold text** continue normal __bold text two.__

<!-- #T# italic text is written within single asterisks or single underscore -->
Normal text *italic text* continue normal _italic text two._

<!-- #T# create anchors to links -->
<!-- # [anchor_text1](hyperlink1) -->
[anchor to Duckduckgo](https://duckduckgo.com/)

<!-- #T# strikethrough text is written within double tildes -->
~~strikethrough text~~

<!-- #T# make ordered lists with any number and a dot -->
1. item1
    1. subitem1
        1. subsubitem1
        1. subsubitem2
    1. subitem2
1. item2
1. item3

<!-- #T# make unordered lists with asterisks, plus or minus -->
* item
    + subitem
        - subsubitem
            * subsubsubitem
+ item

<!-- #T# embed images with an anchor but starting with an exclamation mark -->
<!-- # ![image_anchor_text1](image_location1) -->
![image1](../../Octave/S1_Basic/S1_08_B__Aux01.svg)

<!-- #T# create a blockquote by starting each line in the block with the greater than symbol -->
> Text in the blockquote is
> commonly for related content

<!-- #T# one liner code goes within backticks -->
`line_of_code = 1`

<!-- #T# fence multi line code within 3 backticks -->
```C
    if(line_of_code == 1)
    {
        print("str1");
    }
```