/*
    Scope
*/

//T// Using the `var` keyword, there is only function scope (rest is global)
var a = 5;
if (a < 6)
{
    var b1 = 3;
}
var c1 = a + b1;

//T// Printing `c1` outputs:

``` output
8
```

var func1 = function()
{

//T// function scope
    var b2 = 4;
}
//T// var c2 = a + b2; Gives error: b2 is not defined

//T// Using the `let` keyword, the scope is block scope.
var a = 5;
if (a < 6)
{
    let x1 = 3;
}
var c1 = a + x1;

//T// This outputs:

``` output
ReferenceError: x1 is not defined
```