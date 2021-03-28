--[[
#   Functions
--]]

-- #T# Table of contents

-- #C# Function definition
-- #C# Function call
-- #C# Scope
-- #C# Recursion
-- #C# Anonymous functions
-- #C# Functions as first class citizens
-- #C# - Closures
-- #C# Methods

-- #T# Beginning of content

-- #C# Function definition

-- # |-------------------------------------------------------------
-- #T# functions are defined with parameters, and a return value (or values), they are called with arguments to calculate the return value if any

-- # SYNTAX function definition, parameters, return
-- # function func1(param1, param2)
-- #     statements1
-- #     return val1, val2
-- # end
-- #T# the function keyword starts the function definition, func1 is the function name, param1 is the first parameter, param2 is the second parameter, there can be more parameters, statements1 are executed when func1 is called, and then val1 and val2 are returned from the function, there can be more return values

function func1(param1, param2)
    val1 = param1 * (5 + param2)
    val2 = 8
    return val1, val2
end

-- #T# there is also a syntax to create functions that receives a variable amount of arguments

-- # SYNTAX function that receives a variable amount of arguments
-- # function func1(...)
-- #     statements1
-- #     select(int1, ...)
-- # end
-- #T# same as before, the ellipsis ... in func1(...) denotes the use of a variable amount of arguments, the arguments are accessed with the select function, which returns all arguments starting at index int1 and after, if int1 is replaced with '#', then the select function returns the amount of arguments

function func1(...)
    arg1, arg2 = select(1, ...)
    argc = select('#', ...)
    val1 = arg1 + arg2 + argc
    return val1
end
-- # |-------------------------------------------------------------

-- #C# Function call

-- # |-------------------------------------------------------------
-- #T# make a function call

-- # SYNTAX return_value1, return_value2 = func1(arg1, arg2)
-- #T# as in the definition, arg1 is the argument for the first parameter, arg2 is the argument for the second parameter, and so on, return_value1 and return_value2 are variables that stores the return values from func1

function func1(param1, param2)
    val1 = param1 * (5 + param2)
    val2 = 8
    return val1, val2
end

arg1 = 6
ret1, ret2 = func1(arg1, 5) -- # 60, 8
-- # |-------------------------------------------------------------

-- #C# Scope

-- # |-------------------------------------------------------------
-- #T# variables have a global scope by default, even variables inside functions, they are global once the function is called, to make variables local, the local keyword is used, it makes the variable local to the block in which it's created
function func1()
    var1 = 5
end

func1()
int1 = var1 -- # 5

function func2()
    local var2 = 25
end

func2()
int1 = var2 -- # nil
-- # |-------------------------------------------------------------

-- #C# Recursion

-- # |-------------------------------------------------------------
-- #T# recursion allows calling a function from inside itself

-- # SYNTAX function recursion
-- # function func1(params1):
-- #     statements1
-- #     func1(args1)
-- #     return vals1
-- #T# same as before, but func1 is called inside func1 with arguments args1, statements1 must ensure that there is a way to stop calling func1, so that recursion stops

var1 = 0
function recursion_func1(int1)
    if (int1 >= 0) then
        var1 = var1 + 1
        recursion_func1(int1 - 1)
    end
end
recursion_func1(3)
int1 = var1 -- # 4
-- # |-------------------------------------------------------------

-- #C# Anonymous functions

-- # |-------------------------------------------------------------
-- #T# anonymous functions can be created directly

-- # SYNTAX anon_func1 = function (params1) statements1 return return_value1 end
-- #T# same as before

anon_func1 = function (arg1, arg2) var1 = 7 * arg1 + (arg2 - 1); return var1 end
ret1 = anon_func1(3, 6) -- # 26
-- # |-------------------------------------------------------------

-- #C# Functions as first class citizens

-- # |-------------------------------------------------------------
-- #T# as first class citizens, functions can be assigned to vars, passed as args, and returned from functions

function func1 (param1, param2)
    val1 = param1 * (5 + param2)
    return val1
end

-- #T# assign a function to a variable
var1 = func1
ret1 = var1(5, 5) -- # 50

-- #T# create a function that takes a function as a parameter and returns a function
function func2(f1, arg1)
    function ret_func1()
        val1 = f1(arg1, -3) -- # same as arg1 * 2
        return val1
    end
    return ret_func1
end

var1 = func2(func1, 17) -- # this returns func1(17, -3) as a function
ret1 = var1() -- # 34, no need to use arguments

-- #C# - Closures

-- # |-----
-- #T# closures are functions returned by a function that contains it, that use variables from the function that contains it

-- # SYNTAX closure
-- # function func1()
-- #     local var1 = 'val1'
-- #     function closure1()
-- #         statements1
-- #     end
-- #     return closure1
-- # end
-- #T# var1 must be created local because it's global by default (and then all closures would share var1), statements1 can modify var1, and each new call to closure1 will use its modified value of var1

function func1()
    local var1 = 0
    function closure1(arg1)
        var1 = var1 + arg1
        return var1
    end
    return closure1
end

clo1 = func1()
clo2 = func1()

clo1(1)   -- #    1
clo1(4)   -- #    5
clo1(9)   -- #   14

clo2(-2)  -- #   -2
clo2(-8)  -- #  -10
clo2(-90) -- # -100
-- # |-----

-- # |-------------------------------------------------------------

-- #C# Methods

-- # |-------------------------------------------------------------
-- #T# Lua is not a full object oriented programming language, as of the moment this was written, but there is a syntax that allows treating tables as objects, and tables can store attributes and methods, which is the most basic object oriented functionality

-- # SYNTAX call a method from an object
-- # function method1(self, param1, param2) statements1 end
-- # object1 = {key1 = value1, key2 = method1}
-- # return_value1 = object1:key2(arg1, arg2)
-- #T# in the syntax 'object1:key2(arg1, arg2)', the colon ':' makes it equivalent to the syntax 'object1.key2(self, arg1, arg2)', so the colon is used to access methods from objects

function method1(self, a1, a2) return a1 + 2*a2 end
object1 = {attribute1 = 'value1', m1 = method1}
int1 = object1:m1(1, 2) -- # 5
-- # |-------------------------------------------------------------