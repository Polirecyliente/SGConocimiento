--[[
    Packages
--]]

-- #T# Table of contents

-- #C# Importing packages

-- #T# Beginning of content

-- #C# Importing packages

-- # |-------------------------------------------------------------
-- #T# a package is imported with the require function applied to each lua file in the package

-- # SYNTAX require("/path/to/file1")
-- #T# file1 is a lua file

require("S06_Functions") -- #| this file should be executed from a directory that contains both this file and S06_Functions.lua

clo1 = func1() -- # func1 comes from the imported file
print(clo1(3)) -- # 3
print(clo1(4)) -- # 7
-- # |-------------------------------------------------------------