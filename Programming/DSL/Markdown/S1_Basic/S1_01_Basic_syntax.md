
#   Basic syntax

//T// write normal text without any special syxtax
Normal text example

//T// write headers with the hash symbol, up to 6
# Header1
## Header2
###### Header6

//T// bold words are written within double asterisks or double underscore
normal text **bold text** continue normal

//T// italic words are written within single asterisks or single underscore
normal text *italic text* continue normal

//T// create anchors to links with square brackets and normal brackets
[anchor](https://google.com)

//T// strikethrough within double tildes
~~strikethrough words~~

//T// make ordered lists with any number and a dot
1. item1
    1. subItem1
    1. subItem2
1. item2
1. lastItem

//T// make unordered lists with asterisks, plus or minus
* Item
    * Subitem
        - Subsub
            * sub4
+ Another item

//T// embed images as an anchor but starting with exclamation mark
![image1](../../Octave/S1_Basic/S1_03_Aux01.svg)

//T// make quotes with the greater than symbol
> quoted words. Author

//T// one liner code goes within backticks
`lineOfCode = 1`

//T// fence multi line code within 3 backticks
```genericLanguage
    if(lineOfCode == 1)
    {
        print("str1");
    }
```