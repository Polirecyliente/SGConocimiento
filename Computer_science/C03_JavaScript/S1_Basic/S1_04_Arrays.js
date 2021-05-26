/*
    Arrays
*/

//T// array definition
var arr1 = ['elem0', 'elem1', 'elem2'];

//T// array accessing and assignment
arr1[1] = 'firstElem';

//T// array length
var arr1len = arr1.length;

//T// push(), pop() (LIFO or stack)
arr1.push(4);
arr1.pop();

//T// An array can be made with the spread operator
var array1 = ['elem1', 'elem2', 'elemN']
var array2 = [...array1, 'elemN+1']

//T// Printing `array2` outputs:

``` output
Array(4) [ "elem1", "elem2", "elemN", "elemN+1" ]
```