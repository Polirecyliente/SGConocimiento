/*
    OOP
*/

//T// OOP stands for Object Oriented Programming

//T// Class definition:

class class1
{
    constructor(params1)
    {
        constructor_statements1
    }
    member1
    memberN
}

//T// For example:

class class1
{
    constructor(param1, param2)
    {
        this.member1 = param1
        this.member2 = param2
    }
    method1 = function() { return 27 }
}

//T// constructor function
var Constructor1 = function(prop1)
{
//T// this keyword points to the object created with new keyword
    this.prop1 = prop1;
};
//T// prototype property of constructors
Constructor1.prototype.method1 = function ()
{
    console.log(this.prop1 + " in method1")
}
//T// object instantiation with new
var obj1 = new Constructor1(5)

//T// To add an static member, it's added directly to the constructor
Constructor1.static_member1 = value1

//T// object accessing
obj1.method1()

//T// A method can also be created with the following syntax.

obj1.new_method1 = function(params1)
{
    statements1
}

//T// The `Object` constructor can be used to create references to objects.
var obj1 = new Object(object_o1)

//T// `object_o1` is an object, this syntax makes `obj1` to be a reference to `object_o1`.

var obj1 = new Object()
obj1.prop1 = 85
obj1.method1 = function() { return 27 }

var obj2 = new Object(obj1)

obj2.new_prop1 = 77
var var1 = obj1.new_prop1

//T// Printing `var1` outputs

``` output
77
```

//T// This is because `new_prop1` was created in `obj2` which is a reference to `obj1`, so now `obj1` also has the property `new_prop1`.

//T// The `create` function can be used to create object clones.

var obj1 = {prop1: 8}
var obj2 = Object.create(obj1)

//T// The `getPrototypeOf` function, returns the prototype of an object

var1 = 500
var2 = Object.getPrototypeOf(var1)

//T// Printing var2 outputs

``` output
Number { 0 }
```

//T// Class inheritance is done with the `extends` keyword.

class class1 extends parent_class1
{
    constructor(params1)
    {
        super(params1)
        constructor_statements1
    }
    member1
    member2 = super.memberM
    memberN
}

//T// The `super` keyword is the parent constructor. When using `super` inside the constructor, it must be used before using the `this` keyword. For example:

class parent_class1
{
    constructor(param1)
    {
        this.member1 = param1
    }
    method1() { return 2 }
}

class class1 extends parent_class1
{
    constructor(param1, param2)
    {
        super(param1)
        this.member2 = this.member1 + param2 + super.method1()
    }
}

var var1 = new class1(3, 4)
var var2 = var1.member2

//T// Printing `var2` outputs:

``` output
9
```

//T// This comes from `this.member2 = this.member1 + param2 + super.method1()` being the same as `this.member2 = 3 + 4 + 2`, which gives `9`.

//T// A static member is created with the `static` keyword.

class class1
{
    static static_member1 = value1
}