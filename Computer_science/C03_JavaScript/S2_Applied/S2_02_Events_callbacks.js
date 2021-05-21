/*
    Events, callbacks
*/

//T// callback function definition
var handleH3Click =  function(event)
{
    alert("handled event");
};
//T// object that will be listened for events
var h3Modif = document.getElementsByTagName('h3');

//T// relate the object's listened event with the callback
h3Modif[0].addEventListener('click',handleH3Click);