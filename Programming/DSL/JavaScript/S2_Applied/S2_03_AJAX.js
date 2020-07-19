/*
    AJAX
*/

//T// AJAX stands for Asynchronous JavaScript And XML

//T// XMLHttpRequest(): onload, open, send
var req1 = new XMLHttpRequest();
req1.onload = function(event)
{
    alert("data loaded");
};
req1.open('get','https://localhost/test.txt',true);
req1.send();