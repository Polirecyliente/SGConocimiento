/*
    Operators
*/

var v1 = 5, v2 = 10;
//T// operations: addition +, subtraction -, multiplication *, division /
var res1 = v1 + v2;
res1 = v2 - v1;
res1 = v1 * v2;
res1 = v2/v1;

//T// operator precedence override ()
res1 = (v1 + v2)/3;

var a = 5;
var b = 6;
var c = '5';
//T// comparison operators: ===, ==, !==, !=, >, <, >=, <=
var res1 = (a === c);
res1 = (a == c);
res1 = (a !== b);
res1 = (a != c);
res1 = (b > a);
res1 = (b < a);
res1 = (b >= a);
res1 = (b <= a);