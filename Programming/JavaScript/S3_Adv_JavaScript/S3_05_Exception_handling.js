/*
    Exception handling
*/

//T// try {} catch(){} construct (execution continues)
try
{
JSON.parse("a");
} catch(error)
{
    alert(error.message + " because of invalid object syntax");
}

console.log("continued code");

var int1 = 5;
if(int1 === 5)
{
//T// throw new Error()
    throw new Error("int1: unexpected value of 5");
}

console.log("unreachable code");