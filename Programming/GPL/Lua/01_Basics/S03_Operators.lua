--[[
    Operators
--]]

-- #T# Table of contents

-- #C# Arithmetic operators
-- #C# Relational operators
-- #C# Bitwise operators
-- #C# Logical operators
-- #C# Grouping operators
-- #C# Length of array operator

-- #T# Beginning of content

-- #C# Arithmetic operators

-- # |-------------------------------------------------------------
-- #T# addition operation
a = 5; b = 3
num1 = a + b -- # 8

-- #T# subtraction operation
a = 5; b = 3
num1 = a - b -- # 2

-- #T# change sign operator (the same as the subtraction operator)
a = 5
num1 = -a    -- # -5

-- #T# multiplication operation
a = 5; b = 3
num1 = a * b -- # 15

-- #T# division operation
a = 5; b = 3
num1 = b/a   -- # 0.6

-- #T# modulo operation
a = 5; b = 3
num1 = b % a -- # 3

-- #T# exponentiation operation
a = 5; b = 3
num1 = a ^ b -- # 125
-- # |-------------------------------------------------------------

-- #C# Relational operators

-- # |-------------------------------------------------------------
-- #T# equality operator
a = 5; b = 3
bool1 = (a == b) -- # false

-- #T# not equal operator
a = 5; b = 3
bool1 = (a ~= b) -- # true

-- #T# greater than operator
a = 5; b = 3
bool1 = (a > b)  -- # true

-- #T# less than operator
a = 5; b = 3
bool1 = (a < b)  -- # false

-- #T# greater than or equal to operator
a = 5; b = 3
bool1 = (a >= b) -- # true

-- #T# less than or equal to operator
a = 5; b = 3
bool1 = (a <= b) -- # false
-- # |-------------------------------------------------------------

-- #C# Bitwise operators

-- # |-------------------------------------------------------------
-- #T# and operator
num1 = 0xA & 0x3 -- # 0x2

-- #T# or operator
num1 = 0xA | 0x3 -- # 0xB

-- #T# xor operator
num1 = 0xA ~ 0x3 -- # 0x9

-- #T# not operator
num1 = ~0xA -- # 0x5 #| the output is -0xB which is 0x5 in bits

-- #T# left shift operator
num1 = 0x3 << 1 -- # 0x6

-- #T# right shift operator
num1 = 0xE >> 1 -- # 0x7
-- # |-------------------------------------------------------------

-- #C# Logical operators

-- # |-------------------------------------------------------------
-- #T# logical and operator
a = true; b = false
bool1 = (a and b) -- # false

-- #T# logical or operator
a = true; b = false
bool1 = (a or b) -- # true

-- #T# logical not operator
a = false
bool1 = (not a) -- # true
-- # |-------------------------------------------------------------

-- #C# Grouping operators

-- # |-------------------------------------------------------------
-- #T# the basic grouping operator is the parenthesis pair ()
num1 = ((3 + 4) * 5) + 1 -- # 36 #| ((7) * 5) + 1 == 35 + 1
-- # |-------------------------------------------------------------

-- #C# Length of array operator

-- # |-------------------------------------------------------------
-- #T# the length of array operator is the hash # operator
str1 = 'chars6'
int1 = #str1 -- # 6

table1 = {'val1', 'val2', 'val3'}
int1 = #table1 -- # 3
-- # |-------------------------------------------------------------