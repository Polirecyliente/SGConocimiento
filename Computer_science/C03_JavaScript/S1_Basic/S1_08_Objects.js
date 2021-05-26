/*
    Objects
*/

//T// object definition, this is an object literal (as opposed to an object instantiated from a class)
var obj1 = 
{
//T// object's properties
    prop1: "Property 1",
    prop2: 5,

//T// object's methods
    meth1: function()
    {
        alert("Method 1");
    }
};

//T// object modification
obj1.prop2 = 12;

//T// new object's properties and methods
obj1.newProp = "New Property";
obj1.newMeth = function()
{
    alert("New Method");
};

//T// nested object
obj1.nestedObj = 
{
    nestedProp: 2.6,
    nestedMeth: function()
    {
        alert("In nested object");
    }
};

//T// members of an object can also be accessed using bracket notation.

obj1 =
{
    sub_obj1 :
    {
        sub_prop1: 5
    },
    prop1: 9
}

var1 = obj1['sub_obj1']['sub_prop1']

``` output
5
```