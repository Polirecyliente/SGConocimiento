--[[
#   Composite types
--]]

-- #T# Table of contents

-- #C# Composite types in general
-- #C# Tables

-- #T# Beginning of content

-- #C# Composite types in general

-- # |-------------------------------------------------------------
-- #T# the only composite type is the table, strings are always arrays of characters
str1 = "example string"
table1 = {1, 99, 2, 99, 99, 3}
-- # |-------------------------------------------------------------

-- #C# Tables

-- # |-------------------------------------------------------------
-- #T# tables can be made like arrays (with numbers as indexes), or like associative arrays (with key value pairs)

-- #T# create an array table
table1 = {'value1', 2, 3}

-- #T# create an associative array table
table1 = {key1 = 'value1', key2 = 2}

-- #T# create a new reference to a table
table2 = table1

-- #T# modify a value of a table
table2.key1 = 'modified1'
str1 = table1.key1 -- # modified1

-- #T# add key value pairs
table1["new_key1"] = 'new_value1'
table1.new_key2 = 'new_value2'

-- #T# delete a table by making its references null values
table1 = nil
table2 = nil

-- #T# in array tables, the first element has index 1, the second element has index 2, and so on
table1 = {'value1', 2, 3}
str1 = table1[1] -- # value1
int1 = table1[2] -- # 2

-- #T# concatenate the elements of an array table into a single string with the table.concat function
table1 = {'value1', 2, 3}
str1 = table.concat(table1) -- # value123

-- #T# insert a new element in an array table

-- # SYNTAX table.insert(table1, index1, 'new_element1')
-- #T# 'new_element1' is inserted into table1 at index1

table1 = {'value1', 2, 3}
table.insert(table1, 2, 'new_element1')
str1 = table1[2] -- # new_element1
int1 = table1[3] -- # 2 #| the elements have been shifted to the right

-- #T# remove an element from an array table (the removed element is returned)

-- # SYNTAX table.remove(table1, index1)
-- #T# the element at index1 from table1 is removed

table1 = {'value1', 2, 3}
str1 = table.remove(table1, 1) -- # value1

-- #T# iterate through the key value pairs of an associative array table with the pairs function
table1 = {key1 = 'value1', key2 = 2}
for key1, val1 in pairs(table1) do print(key1, val1) end
-- #T# the former prints
-- # key1    value1
-- # key2    2

-- #T# iterate through the values of an array table with the ipairs function
table1 = {'value1', 2, 3}
for index1, val1 in ipairs(table1) do print(index1, val1) end
-- #T# the former prints
-- # 1    value1
-- # 2    2
-- # 3    3

-- #T# unpack an array table with the table.unpack function
table1 = {'value1', 2, 3}
var1, var2, var3 = table.unpack(table1)
var1 -- # value1
var2 -- # 2
var3 -- # 3

-- #T# create and access a nested associative array table
table1 = {key1 = 'val1', key2 = {sub_key1 = 'sub_val1'}}
str1 = table1.key2.sub_key1 -- # sub_val1
-- # |-------------------------------------------------------------