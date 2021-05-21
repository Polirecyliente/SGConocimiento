--[[
#   Pandoc filters
--]]

-- #T# Table of contents

-- #C# Basic usage
-- #C# Terminology and synonyms
-- #C# Pandoc AST
-- #C# Elements
-- #C# - Parts of an element
-- #C# - Types of elements
-- #C# - Other functions and methods

-- #T# Beginning of content

-- #C# Basic usage

-- # |-------------------------------------------------------------
-- #T# the pandoc module for Lua comes embedded in Pandoc, so it's not necessary to import the pandoc module

-- #T# the pandoc module can be treated as an associative array table, it's functions, variables, constants, etcetera, can be accessed as keys of said table

-- #T# filters work by filtering the elements of the input document, and when a filter is able to modify an element, the element is modified in whichever way determined by the filter

-- #T# the following filter is used to filter elements of bold (strong) font, and then to apply a small capitalization font to the contents of these elements
function Strong(element1)
    return pandoc.SmallCaps(element1.content)
end
-- #T# the element1 is the element being filtered, which is a table that stores the contents of the element in element1.content, the Strong function filters elements of type Strong, and the SmallCaps function applies the small capitalization to its argument

-- #T# the following filter returns the element as a plain string, without the bold font
function Strong(element1)
    return pandoc.Str(element1.content[1].text)
end

-- #T# the return value of a filter function can be
-- #T#     nil, which doesn't change the filtered element
-- #T#     a single new element that replaces the filtered element, if the filtered element is inline or block, the new element must be inline or block respectively
-- #T#     an array table of elements that replaces the filtered element, if the filtered element is inline of block, each element in the array table must be inline or block respectively
function Strong(element1)
    return nil
end

function Strong(element1)
    return pandoc.SmallCaps(element1.content)
end

function Strong(element1)
    return {pandoc.SmallCaps(element1.content), pandoc.Str(element1.content[1].text)}
end
-- # |-------------------------------------------------------------

-- #C# Terminology and synonyms

-- # |-------------------------------------------------------------
-- #T# Lua's array tables are refered here as lists

-- #T# a function that is named the same as a Pandoc's AST element, is called a filter
-- # |-------------------------------------------------------------

-- #C# Pandoc AST

-- # |-------------------------------------------------------------
-- #T# AST stands for Abstract Syntax Tree

-- #T# filters modify the Pandoc AST, so the Pandoc AST must be studied to know how to create a filter that achieves a desired result

-- #T# to see the Pandoc AST of a document, execute `pandoc file1.md -t native`

-- #T# the native format is for Pandoc AST native representation

-- #T# the content of an element in the AST is enclosed in square brackets after the type of the element
-- #T# having as input a Markdown file named file1.md with `word1 word2 word3`, executing `pandoc file1.md -t native` the AST output is `[Para [Str "word1",Space,Str "word2",Space,Str "word3"]]`

-- #T# the whole document is enclosed in square brackets. The contents of the Para element are enclosed in square brackets: `[Str "word1",Space,Str "word2",Space,Str "word3"]`, each word becomes an element of type Str, and each space is an element of type Space

-- #T# there are elements that have more information apart from its content, elements that have metadata have it stored apart from the content. Elements with a link target have the link information stored apart from the content

-- #T# a Markdown file named file1.md with `[in span1]{#id1 .c1 .c2 k1='v1' k2='v2'}`, executing `pandoc file1.md -t native` the AST output is `[Para [Span ("id1",["c1","c2"],[("k1","v1"),("k2","v2")]) [Str "in",Space,Str "span1"]]]`, the metadata of the Span element is enclosed in parentheses before the content
-- # |-------------------------------------------------------------

-- #C# Elements

-- # |-------------------------------------------------------------
-- #T# when an element is filtered, the resulting new element is not filtered by subsequent filters
function Emph(element1)
    return pandoc.Strong(element1.content)
end
function Strong(element1)
    return pandoc.SmallCaps(element1.content)
end
-- #| with these filters, an Emph element is turned into a Strong element, but that resulting Strong element is not converted into a SmallCaps element, it remains as a Strong element

-- #C# - Parts of an element

-- # |-----
-- #T# an element is a table, so its contents can be inspected as a regular table
function Strong(element1)
    print(element1) -- # table: 0x7fd82c0fdd30
    for k1, v1 in pairs(element1) do 
        print(k1, "|-|", v1) -- # content	|-|	table: 0x7fac16ba5cb0
    end 
    for k1, v1 in pairs(element1.content) do
        print(k1, "|-|", v1) -- # 1	|-|	table: 0x7f8752cd4500
    end
    for k1, v1 in pairs(element1.content[1]) do
        print(k1, "|-|", v1) -- # text	|-|	line1
    end
    print(element1.content[1].text) -- # line1
end
-- #T# an element is an associative array table, it's keys depend on the type of the element, for example a Strong element has the content key

-- #T# in a Strong element, the value of the content key is an array table, the value in content[1] is a table with the text key whose value is the text of the element

-- #T# the parts of an Strong element can be summarized as element1.content[1].text
-- # |-----

-- #C# - Types of elements

-- # |-----
-- #T# the type of an element is one of the pandoc types, the pandoc types make the set of possible elements with which filters can work

-- #T# the Inlines filter takes an Inlines type as argument, this argument is the list of inlines inside a given filtered block of the input document
function Inlines(inlines1)
    print(inlines1[1].text)
    return inlines1
end
-- #| this filter prints the text in the first inline element of each block

-- #T# the Blocks filter takes a Blocks type as argument, this argument is the list of blocks of the input document
function Blocks(blocks1)
    print(blocks1[6].content[1].text)
    return blocks1
end
-- #| this filter prints the text of the first content of the block number 6

-- #T# Lists are a type of element, Inlines are a type of List, so the List methods can be used with Inlines

-- #T# the insert method of Lists is used to insert an element at a given index in a list

-- # SYNTAX List1:insert(int1, value1)
-- #T# value1 is inserted at position int1 from List1

-- #T# the remove method of Lists is used to remove the element at a given index in a list

-- # SYNTAX List1:remove(int1)
-- #T# the element at position int1 from List1 is removed

function Inlines(inlines1)
    if (inlines1[1].text == "A" and inlines1[2].tag == "Space") then
        inlines1:remove(1)
        inlines1:insert(1, pandoc.Str("B"))
    end
    return inlines1
end

-- #T# This filter replaces any string "A " that starts a block, for "B "

-- #T# the Str type is the basic inline type, it represents a string, for example 'word1' in Markdown

-- #T# the Space type represents a whitespace, for example ' ' in Markdown

-- #T# the Str filter takes a Str type as argument, this argument is the Str element being filtered
function Str(content1)
    return pandoc.Str(content1.text.."Suffix text")
end

-- #T# the LineBreak type represents a newline
function LineBreak()
    return {pandoc.LineBreak(), pandoc.LineBreak()}
end
-- #| this filter replaces every LineBreak element with two LineBreak elements

-- #T# the Para type is the basic block type, it represents a paragraph

-- #T# the Para filter takes a Para type as argument, this argument is the Para element being filtered
function Para(element1)
    print(element1.tag)
    print(element1.content[1].content[1].text)
    return pandoc.Para(element1.content)
end
-- #T# this filter prints the tag attribute of the Para element, which is the string 'Para', and using a Markdown file with `*word1*` this filter prints 'word1'

-- #T# the tag attribute is common to many types, is contains a string with the name of the type itself

-- #T# the Pandoc type is the basic document type, it represents a document

-- #T# a Markdown file containing `word1 *word2 word3*` produces the native AST `[Para [Str "word1",Space,Emph [Str "word2",Space,Str "word3"]]]`, the following filter is applied to it

-- #T# the Pandoc filter takes a Pandoc type as argument, this argument is the Pandoc element being filtered
function Pandoc(document1)
    print(document1.blocks[1].content[3].content[3].text) -- # word3
    print(document1.meta) -- #| no output
    return nil
end

-- #T# the reason for which there is no output for `print(document1.meta)`, is that `document.meta` is a table with no elements, because there is no metadata for this example

-- #T# the Span type represents a <span> tag, so it can have metadata

-- #| the Mardown file for the following filter contains `[in span1]{#id1 .c1 .c2 k1='v1' k2='v2'}`

-- #T# the Span filter takes a Span type as argument, this argument is the Span element being filtered
function Span(element1)
    print(element1.identifier)    -- # id1
    print(element1.classes[1])    -- # c1
    print(element1.classes[2])    -- # c2
    print(element1.attributes.k1) -- # v1
    print(element1.attributes.k2) -- # v2
    return element1
end

-- #T# the identifier attribute is a string with the identifier in the metadata of the Span element
-- #T# the classes attribute is a list with the classes in the metadata of the Span element
-- #T# the attributes attribute is a table with the attribute value pairs in the metadata of the Span element
-- # |-----

-- #C# - Other functions and methods

-- # |-----
-- #T# the walk_block function is used to apply a given filter to a particular block

-- # SYNTAX pandoc.walk_block(block_element1, filter1)

-- #| for the following example, the Markdown file contains `word1 word2 word3`

function Para(element1)
    return pandoc.walk_block(element1, { Str = function(element1) return pandoc.Str("replacement") end })
end

-- #| this filter takes Para elements and replaces their Str elements for the string "replacement". In this example, from walk_block(block_element1, filter1), filter1 is defined as an anonymous function, because otherwise the Str filter would apply to all Str elements in the document.

-- #T# the pandoc.walk_inline function is used to apply a given filter to a particular inline

-- # SYNTAX pandoc.walk_inline(inline_element1, filter1)

-- #| for the following example, the Markdown file contains `word1 *word2 word3*`

function Emph(element1)
    return pandoc.walk_inline(element1, { Str = function(element1) return pandoc.Strong(element1) end })
end

-- #| this filter takes Emph elements and places their Str elements into Strong elements. In this example, from walk_inline(inline_element, filter1), filter1 is defined as an anonymous function, because otherwise the Str filter would apply to all Str elements in the document.

-- #T# the pandoc.read function is used to read a string as a document from a given language

-- # SYNTAX pandoc.read(document_string1, language_string1)
-- #T# the pandoc.read function returns a Pandoc document created from reading document_string1 written in language_string1

-- #| the following filter can be used on any Markdown file
function Pandoc(document1)
    return pandoc.read("**only this**", "markdown")
end
-- #| this filter converts any Markdown file into `**only this**`

-- #T# the pandoc.pipe function is used to pipe into an external command and pipe back into the filter

-- # SYNTAX pandoc.pipe(command_string1, {arg_string1, arg_string2, arg_stringN}, input_string1)
-- #T# command_string1 is executed in the operating system, using the list of arguments as arguments for the command, and receiving input_string1 as if it was input from stdin

-- #| the Markdown file for this example contains `text1 text2`
function Str(content1)
    return pandoc.Str(pandoc.pipe("sed", {"-e", "s/text/Text/"}, content1.text))
end
-- #| the Markdown output is `Text1 Text2`

-- #T# the clone method can be used on Pandoc objects to create copies of them

-- # syntax pandoc_element1:clone()
-- #T# pandoc_element1 is any Pandoc object that is non read-only

-- #| the Markdown file for this example contains `text **TEXT** text`
function Strong(element1)
    emph1 = pandoc.Emph(element1.content)
    emph2 = emph1:clone()
    return {emph1, emph2}
end
-- #| the Markdown output is `text *TEXTTEXT* text`, the emph1 object is cloned in emph2, and then both objects are returned in a list
-- # |-----

-- # |-------------------------------------------------------------