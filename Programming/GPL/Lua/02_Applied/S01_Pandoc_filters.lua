--[[
#   Pandoc filters
--]]

-- #T# Table of contents

-- #C# Basic usage
-- #C# Parts of an element
-- #C# Pandoc types

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
-- # |-------------------------------------------------------------

-- #C# Parts of an element

-- # |-------------------------------------------------------------
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
-- # |-------------------------------------------------------------

-- #C# Pandoc types

-- # |-------------------------------------------------------------
-- #T# the pandoc types make the set of possible elements with which filters can work


-- # |-------------------------------------------------------------