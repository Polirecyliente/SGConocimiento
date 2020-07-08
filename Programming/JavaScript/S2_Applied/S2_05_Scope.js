/*
    Scope
*/

//T// there is only function scope (rest is global)
var a = 5;
if (a > 6)
{
    var b1 = 3;
}
var c1 = a + b1;

var func1 = function()
{

//T// function scope
    var b2 = 4;
}
//T// var c2 = a + b2; Gives error: b2 is not defined