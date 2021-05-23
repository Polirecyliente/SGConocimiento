/*
    DOM
*/

//T// DOM stands for Document Object Model

//T// document object, getElementById()
var headerModif = document.getElementById("header1ID");

//T// getElementsByTagName()
var paragraphModif = document.getElementsByTagName('p');

//T// getElementsByClassName()
var header2Modif = document.getElementsByClassName('header2class');

//T// querySelector(), querySelectorAll()
var cssH3Modif1 = document.querySelector('#header3ID');
var csspModif2 = document.querySelectorAll('p');

//T// The `innerText` property of DOM elements, contains the inner text of the element.
var str1 = document.getElementById("id1").innerText

//T// the functions that returns a set of elements can be accessed as an array
var paragraphModif = document.getElementsByTagName('p');
console.log(paragraphModif[0].innerText)