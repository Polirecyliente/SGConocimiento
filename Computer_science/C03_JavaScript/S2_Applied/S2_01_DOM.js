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

//T// The `document` object has a property named `readyState`. The `readyState` property is a string with the value of the state of readiness of the HTML document.

//T// The value of the `readyState` attribute can be:
//T// - "loading",     the document is currently loading in the browser.
//T// - "interactive", the base document is loaded, but resources (like images, videos, etcetera), are still loading.
//T// - "complete",    the document and all its resources are loaded and can be displayed by the browser.

//T// Every time there is a change in the `readyState` property, a `readystatechange` event is fired.

let var1 = document.readyState