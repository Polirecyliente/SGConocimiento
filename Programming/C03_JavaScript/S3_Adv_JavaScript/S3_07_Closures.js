/*
    Closures
*/

var closureRetFnc = function(arg1)
{
//T// closure function is returned
    return function(arg2)
    {
        return (2 * arg1) + arg2;
    };
};

console.log(closureRetFnc(7)(3));