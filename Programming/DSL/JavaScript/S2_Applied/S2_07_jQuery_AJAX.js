/*
    jQuery AJAX
*/

$(document).ready(function(){});

//T// $.ajax({url:, method, success: })
$.ajax({
    url: "https://localhost/textTest.txt",
    method: "GET",
    success: function()
    {
        alert("got file in jQuery AJAX");
    }
});

//T// $.get().fail()
$.get("Section2/sectionName", function(data){
    console.log("success get");
    console.log(data);
}).fail(function(){
    console.log("fail get");
});

//T// $.post().fail()
$.post("Section2/sectionName","postedString",function(data){
    console.log("success post");
    console.log(data);
}).fail(function(){
    console.log("fail post");
});