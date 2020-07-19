/*
    OOP
*/

//T// OOP stands for Object Oriented Programming

//T// constructor function
var Constructor1 = function(prop1)
{
//T// this keyword points to the object created with new keyword
    this.prop1 = prop1;
};
//T// prototype property of constructors
Constructor1.prototype.meth1 = function ()
{
    console.log(this.prop1 + " in meth1");
};
//T// object instantiation with new
var obj1 = new Constructor1(5);

//T// object accessing
obj1.meth1();