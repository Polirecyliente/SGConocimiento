/*
    DOM
*/

//T// DOM stands for Document Object Model

//T// A `document` object is created for each webpage that the browser visits. This allows manipulating the webpages, via this `document` object.

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

//T// Create an HTML element.

const elem1 = document.createElement('tag1')

//T// For example:

const elem1 = document.createElement('div')

//T// This creates a `div` element in the console.

//T// A system notification can be fired, using the `Notification` constructor.

const notif1 = new Notification('Notification message')