/*
    jQuery AJAX
*/

//T// The basic usage of AJAX is done with the `XMLHttpRequest` constructor.

function func1()
{
    var XHRequest1 = new XMLHttpRequest()
    XHRequest1.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            document.getElementsByTagName("p")[0].innerHTML = this.responseText;
        }
    }
    XHRequest1.open("GET", "file1.html")
    XHRequest1.send()
}

//T// In this case, `func1` should be used as a callback function, for example as the callback for the event of clicking a button. `func1` exchanges the `innerHTML` of the first `<p>` element, for the contents of `file1.html`.

//T// `XMLHttpRequest` objects have:
//T// - A `readyState` property (explained below).
//T// - An `status` property, which is a number with the HTTP response status code.
//T// - A `responseText` property, with the text of the HTTP response (which is the text acquired through the `open` function).

//T// The `readyState` property is a number that represents the ready state of the request, it's value can be:
//T// - 0, which means the UNSENT state, where the `open` function has not been called.
//T// - 1, which means the OPENED state, where the `open` function has just been called.
//T// - 2, which means the HEADERS_RECEIVED state, where the `send` function has just been called.
//T// - 3, which means the LOADING state, where the `responseText` property is being loaded with the data from the server, that results from the URL in the `open` function.
//T// - 4, which means the DONE state, where the request and response are completed.

//T// The `open` function attempts to asynchronously open an URL, using a given HTTP method, its syntax is:

XMLHttpRequest_object1.open("HTTP_method1", "URL")

//T// The `send` function sends the request to the server.

//T// Asynchronous calls can also be made with 'promises'. In JavaScript, a promise is an asynchronous call, that if it succeeds then a success callback is called, and if it fails then a fail callback is called. This is necessary because it's impossible to predict whether or not an asynchronous call will be successful or not (for that, it would need to be synchronous).

//T// In a JavaScript promise, the success callback is placed inside the `then` function, and the fail callback is placed inside the `catch` function.

function promise1()
{
    return new Promise((resolve, reject) => {
    statements1
    resolve()
    })
}

promise1().then(() => {
    statements2
})
.then(() => {
    statementsN
})
.catch(() => {
    fail_statements1
})
.then(() => {
    after_fail_statements1
});

//T// Note that the `promise1` function returns a `Promise` object, whose constructor takes a `resolve` and a `reject` functions as arguments. The `resolve` function must be called (even if it's empty), for the promise chain to take place.

// <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>

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