--[[
#   Control flow
--]]

-- #T# Table of contents

-- #C# Decision making
-- #C# - Conditional statements
-- #C# Loops
-- #C# - for loop
-- #C# - while loop
-- #C# - repeat-until loop

-- #T# Beginning of content

-- #C# Decision making

-- # |-------------------------------------------------------------
-- #T# decision making is made with the if, then, elseif, else, and end keywords

-- #T# in an if conditional statement a condition is checked and if it returns true, then the if block is executed, this also happens in an elseif conditional statement

-- #T# in an else conditional statement no condition is checked, but the else requires an if above it, the elseif also requires an if above it, the else block executes when the if and elseif blocks do not, and at the end of all this there must be the end keyword

-- #C# - Conditional statements

-- # |-----
-- #T# conditional statements are carried out with the following syntax

-- # SYNTAX if, elseif, else, conditional statements
-- # if condition1 then
-- #     statements1
-- # elseif condition2 then
-- #     statements2
-- # else
-- #     statements3
-- # end
-- #T# if condition1 returns true then the statements1 are executed, else if condition2 returns true then statements2 are executed, else statements3 are executed. Decision making statements can be nested

int1 = false
if int1 then
    int2 = 1
elseif not int1 then
    if int1 == false then
        int2 = 2
    end
else
    int2 = 3
end
-- # int2 == 2

-- #T# conditional statements can be made into a one liner
str1 = 'a'
if str1 == 'a' then print("in a one liner") elseif str1 == 'b' then print("in str1 = b") else print("in else") end -- # in a one liner
-- # |-----

-- # |-------------------------------------------------------------

-- #C# Loops

-- # |-------------------------------------------------------------
-- #T# loops are made with the for, while, and repeat-until constructs

-- #T# in a for loop, the loop is repeated for each element of an iterable, or for each number in an interval of numbers

-- #T# in a while loop, the loop is repeated as long as the while condition returns true

-- #T# in a repeat-until loop, the loop is repeated as long as the until condition returns false

-- #C# - for loop

-- # |-----
-- #T# the for loop is made with the following syntaxes

-- # SYNTAX for loop using an iterable
-- # for elem_i1 in iterable1 do
-- #     statements1
-- #     [break]
-- # end
-- #T# the loop executes the statements1 for each value in iterable1, said value is assigned to the iterator elem_i1 in each iteration

-- #T# the break keyword is used to skip all remaining iterations of the loop that contains the break, it must be placed at the end of its containing block

table1 = {'value1', 'value2', 'value3', 'unreachable1', 'unreachable2'}
for index1, val1 in ipairs(table1) do
    print(val1)
    if index1 == 3 then break end
end
-- #T# the former prints
-- # value1
-- # value2
-- # value3

-- # SYNTAX for loop using an interval of numbers
-- # for it1 = iniN, endN, stepN do
-- #     statements1
-- #     [break]
-- # end
-- #T# the loop executes statements1 for each value of it1, starting at iniN, ending at endN, and with a step of stepN, so iniN, endN, and stepN must be integers

for it1 = 1, 12, 3 do
    print(it1)
end
-- #T# the former prints
-- # 1
-- # 4
-- # 7
-- # 10
-- # |-----

-- #C# - while loop

-- # |-----
-- #T# the while loop is made with the following syntax

-- # SYNTAX while loop
-- # while condition1 do
-- #     statements1
-- #     [break]
-- # end
-- #T# the statements1 are executed while condition1 returns true, (for the break keyword, see the for loop subsection)

int1 = 0
while (int1 < 80) do
    int1 = int1 + 30
end
-- # int1 == 90
-- # |-----

-- #C# - repeat-until loop

-- # |-----
-- #T# the repeat-until loop is made with the following syntax

-- # SYNTAX repeat-until loop
-- # repeat
-- #     statements1
-- #     [break]
-- # until condition1
-- #T# the statements1 are executed as long as condition1 returns false, statements1 are executed at least one time (for the break keyword, see the for loop subsection)

int1 = 0
repeat
    int1 = int1 + 30
until int1 > 80
-- # int1 == 90
-- # |-----

-- # |-------------------------------------------------------------