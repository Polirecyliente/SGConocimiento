/*
    Local storage
*/

//T// save local data with localStorage.setItem()
localStorage.setItem('identifier1',JSON.stringify({
    prop1: 5,
    prop2: 'valuep2'
}));

//T// get data saved with localStorage.getItem()
var dataValue1 = JSON.parse(localStorage.getItem('identifier1'));

console.log(dataValue1);