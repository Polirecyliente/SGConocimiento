
#   Functions

#T# Table of contents

#T# Function definition
#T# Function call
#T# Anonymous functions
#T# Functions as first class citizens
#T# Function decorators
#T# Function annotations

#T# Beginning of content

#T# Function definition

#T# functions are defined with parameters to return a value, they are called with arguments to process the return value

# def func1 (param1,param2 = default_value2,*varargs_tuple1): 
#     "docstring1"
#     statements1
#     return val1
#T# func1 is the function name, param1 is an obligatory parameter, param2 has a default default_value2, *varargs_tuple1 is a tuple with a variable amount of parameters, so param1 has to come before the other kinds of parameters, "docstring1" is the help string, statements1 are executed when func1 is called, and then val1 is returned from the function, it can be an array
def func1 (param1,param2 = 5,*varargs_tuple1):
    "func1 docstring or documentation string with its purpose"
    val1 = param1 * (5 + param2) # param1 * 10 with default param2
    for elem_i1 in varargs_tuple1:
        val1 /= elem_i1
    return val1

#T# Function call

arg1 = 6
#T# make a function call
# return_value1 = func1(param1 = arg1,arg2,arg3,arg4)
#T# as in the definition, arg1 is obligatory and is a keyword argument (kwarg), arg2 is optional and overrides the default value, arg3, and arg4 are varargs
ret1 = func1(arg1,5,3) # 20.0

#T# Anonymous functions

#T# create anonymous functions with the lambda keyword
# anon_func1 = lambda arg1, arg2, arg3: (arg1 + arg2)/arg3
#T# the expresion after the colon can be any other, the function name is anon_func1, arg1, arg2, and arg3 are the arguments
anon_func1 = lambda arg1, arg2: 7 * arg1 + (arg2 - 1)
ret1 = anon_func1(3,6) # 26

#T# Functions as first class citizens

#T# as first class citizens, functions can be assigned to vars, passed as args, and returned from functions

#T# assign a function to a variable
var1 = func1
ret1 = var1(5) # 50

#T# create a function that takes a function as a parameter and returns a function
def func2(f1,arg1):
    def ret_func1():
        val1 = f1(arg1,-3) # same as arg1 * 2
        return val1
    return ret_func1

var1 = func2(func1,17) # this returns func1(17,-3) as a function
ret1 = var1() # 34, no need to use arguments

#T# Function decorators

#T# a function decorator takes a function and decorates it, by adding extra functionality to the original function

#T# create a function decorator, f1 is the function to decorate
def decorator1(f1):
    """make f1 only work on odd numbers"""
    def inner_func1(arg1, arg2):
        if (arg1%2 != 0) and (arg2%2 != 0):
            return f1(arg1, arg2)
        return None
    return inner_func1

#T# apply a decorator to a function with the decorator operator @
# @decorator_func1
# def func1(*args,**kwargs):
#     statements1
#T# the decorator must be applied right before the function definition, doing this is the same as doing
# func1 = decorator_func1(func1)
@decorator1
def func1(param1, param2):
    return param1 + param2

ret1 = func1(3,4) # None
ret1 = func1(3,5) # 8

#T# Function annotations

#T# create function annotations for the parameters and for the return value
def func1(param1: "param1_annotation") -> "return_value_annotation":
    return None

#T# get a dictionary with the annotations from a function with the __annotations__ attribute
dict1 = func1.__annotations__