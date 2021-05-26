/*
    Functions
*/

//T// function definition
var adder = function(a,b)
{
    return a + b;
}

//T// function call
var res1 = adder(5,3);

//T// A function can be defined in a one liner with the arrow function syntax.

func1 = (params1) => return_value1

//T// For example:

func1 = (param1) => 3*param1
var var1 = func1(5)

//T// Printing `var1` outputs:

``` output
15
```

//T// When a function only has one parameter, the parenthesis can be removed in the arrow function syntax

func1 = param1 => return_value1

//T// The arrow function syntax can span more than one line of code.

func1 = (params1) => {
    statements1
}

//T// For example:

func1 = (param1, param2) => {
    var return_value1 = param1 + 2*param2
    return return_value1
}
var var1 = func1(4, 5)

//T// Printing `var1` outputs:

``` output
14
```

//T// Functions and classes can be decorated. Decorators start with the at symbol @, and they are placed in the previous line to the function or class they decorate. Decorators are functions that take a function or class as argument, and return the function modified or modify the class.

@decorator1
func1_definition

@decorator2
class1_definition

//T// For example:

decorator1 = function(func1)
{
    inner_func1 = function(arg1, arg2)
    {
        if (arg1%2 != 0 && arg2%2 != 0)
        {
            return func1(arg1, arg2)
        }
        return null
    }
    return inner_func1
}

@decorator1
func1 = function(param1, param2)
{
    param1 + param2
}

decorator2 = function(class1)
{
    class1.new_member1 = 78
}

@decorator2
class class1
{
    constructor(param1)
    {
        this.member1 = param1
    }
}

//T// The `arguments` object contains the arguments passed to a function.

func1 = function(param1, param2, param3)
{
    console.log(arguments)
}

func1(5, 4, 1)

``` output
Arguments { 0: 5, 1: 4, 2: 1, … }
```

//T// The arguments are counted starting from 0.

//T// Variable arguments are created with the rest parameter syntax (which uses the spread operator).

func1 = function(param1, paramN, ...params1)
{
    statements1
}

//T// This passes `params1` as an array, to `func1`.