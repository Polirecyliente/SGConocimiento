/*
    Elements
*/

//T// creating elements

//T// document.createElement(), element.textContent, element.setAttribute(), document.body.appendChild
var divCreated = document.createElement('div');
divCreated.textContent = "text created in JavaScript";
divCreated.setAttribute('class','header3class');
document.body.appendChild(divCreated);

//T// append to created element
var header4 = document.createElement('h4');
header4.textContent = "Fourth Header";
divCreated.appendChild(header4);

//T// remove with element removeChild()
document.body.removeChild(divCreated);