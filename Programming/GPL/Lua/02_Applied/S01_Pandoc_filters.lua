--[[
#   Pandoc filters
--]]

-- #T# Table of contents

-- #C# Basic usage

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
-- # |-------------------------------------------------------------