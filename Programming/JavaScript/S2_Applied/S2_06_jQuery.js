/*
    jQuery
*/

//T// add the jQuery script at the end of the HTML file, before other scripts

//T// $(document), $("selector"), ready(), click() event handling
$(document).ready(function(){
    $("p").click(function(){
        alert ("jQuery event handling")
    });

//T// jQuery DOM API

//T// select and change: $("selector").prop1(vl1).prop2(vl2), height(), width(), css()
$(".header2class").height(50).width(86).css("background","green");
});

//T// get properties (if many, gets the first element)
var currentHeight = $(".header2class").height(), 
currentColor = $(".header2class").css("color");

//T// select from DOM within context
var $subh3 = $("#subh3");
$("p",$subh3).css("background","blue");

//T// other functionality

var JSstyle = 0, jQstyle = 0;
var afterLoadJS = function(event)
{
    alert("JS style " + ++JSstyle);
}
var afterLoadjQ = function(event)
{
    alert("jQuery style " + ++jQstyle);
}

//T// JS event DOMContentLoaded -> jQuery $().ready()
window.addEventListener("DOMContentLoaded",afterLoadJS); // JS
$(window).ready(afterLoadjQ); // jQuery

//T// after images load: JS event load -> jQuery $().on("load")
window.addEventListener("load",afterLoadJS); // JS
$(window).on("load",afterLoadjQ); // jQuery

//T// jQuery type checking: $.isArray(), $.isFunction(), $.isNumeric(), $.isPlainObject()
var typeChk = $.isArray([0, 1, 2]);
typeChk = $.isFunction(function(){});
typeChk = $.isNumeric(10);
typeChk = $.isPlainObject({prop1: "str1"});