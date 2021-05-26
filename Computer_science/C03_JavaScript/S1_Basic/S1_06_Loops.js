/*
    Loops
*/

var iter = 1;
//T// while
while (iter <= 3)
{
    alert(iter);
    iter = iter + 1;
}

//T// for
for (var i = 7; i <= 9; i++)
{
    alert(i);
}

//T// A generator is created with the following syntax.

function* generator1(params1)
{
    yield value1
    yield value2
    yield valueN
    return valueN+1
}

//T// The `yield` keyword acts the same as the `return` keyword, because it returns the value in front of it and ends the function. The idea is that the next time the generator is used, the next value from the next `yield` keyword, is returned.

//T// A generator can be used with the `next` function

var gen1 = generator1(args1)
var obj1 = gen1.next()
var obj1 = gen1.next()
var var1 = obj1.value

//T// In this case, `obj1` is an object that contains two properties, `value` with the value yielded or returned from `generator1`, and `done` which is a boolean value that is `true` if `generator1` is done returning all the values it can return (otherwise `false`).

//T// For example:

function* generator1(param1)
{
    yield 2*param1
    yield 4*param1
    yield 8*param1
    return param1
}

var gen1 = generator1(5)
var obj1 = gen1.next()
var obj1 = gen1.next()
var var1 = obj1.value

//T// Printing `var1` outputs:

``` output
20
```

//T// Generators are iterable, they can be iterated through, with the following syntax.

var gen1 = generator1(args1)

for (let it1 of gen1)
{
    statements1
}

//T// The syntax `let it1 of gen1` means that the iterator variable `it1` is created, and will take each of the values yielded by `gen1` in the for loop.