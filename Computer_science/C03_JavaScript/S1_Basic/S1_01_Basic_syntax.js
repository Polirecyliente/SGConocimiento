/*
    Basic syntax
*/

//T// inside script tag, alert()
alert("Hello, world.");

//T// Packages and modules

//T// JavaScript modules are created like regular JavaScript files, except that they contain import and export statements

//T// An import statement allows importing names that are defined in another file.
import {name1, name2, nameN} from "/path/to/file1.js"

//T// `name1` through `nameN` are variables, functions, classes, etcetera.

//T// To import `file1.js` using a relative path, use the following syntax.
import {name1, name2, nameN} from "./relative/path/to/file1.js"

//T// For a file in the same directory, the syntax is as follows.
import {name1, name2, nameN} from "./file1.js"

//T// An import statement can use aliases for the imported names, with the `as` keyword
import {name1 as var1, name2 as var2, nameN as varN} from "/path/to/file1.js"

//T// Import everything from a file, with the wildcard *
import * as names1 from "/path/to/file1.js"
var1 = names1.name1
var2 = names1.name2
varN = names1.nameN

//T// names1 is an object containing all the names in the file `/path/to/file1.js`.

//T// A name can only be imported if it is exported from another JavaScript file.

//T// An export statement exposes names so they can be imported from other files.
export {name1, name2, nameN}

//T// An export statement can use aliases for the exported names, with the `as` keyword
export {name1 as var1, name2 as var2, nameN as varN}

//T// All the names exported from another file, can be re-exported
export * from "/path/to/file1.js"

//T// This exports everything exported from `/path/to/file1.js`

//T// There can be a default export, so that it can be imported without curly braces.

//T// In the file that exports `file1.js`
export default name1

//T// In the file that imports
import new_name1 from "relative/path/to/file1.js"

//T// Commonly, `new_name1` is the same as `name1`. The `default` keyword can only be used once per module.

//T// Several modules can be loaded asynchronously, using the RequireJS module loader.

//T// The RequireJS module loader can be installed in different ways, or it can be included as a script using a CDN or a link to the RequireJS file.

//T// Inside the <head> tag, the RequireJS file can be included as follows.

// <script src=https://requirejs.org/docs/release/2.3.6/minified/require.js></syntax>

//T// This example link is from the official RequireJS webpage, so a newer version could be available.

//T// To import a JavaScript module using RequireJS, the `requirejs` function is used

// <script>requirejs(["relative/path/to/module1", "moduleN"], function (arg1){ arg1.func1() });</script>

//T// Here "module1" does not need to have the ".js" extension written. `arg1` holds an object with the names exported from `module1.js`. The first argument of the `requirejs` function is an array with the modules being imported. The second argument is a callback function, executed after importing the modules.

//T// `func1` is defined in the `module1.js` file in this way:

// define([dependencies1], function () { return { func1 : function (){ statements1; } }; });

//T// So the `define` function is used to define the names that will be exported from `module1.js`. The first argument is an array of dependencies1, which is an array of modules imported (the same as the first argument from the `requirejs` function), and the second is a function that returns the names exported from `module1.js`.

//T// When including the RequireJS file in an HTML file, it's possible to execute a JavaScript file to do the imports via that JavaScript file. This is done using the `data-main` attribute.

// <script data-main="main_script1" src="https://requirejs.org/docs/release/2.3.6/minified/require.js"></script>

//T// This executes `main_script1.js`, the idea is to place the imports in the `main_script1.js` file, for example:

// requirejs(["module1"], function (arg1){ arg1.func1() });

//T// Command Line Interface (CLI)

//T// JavaScript code can be executed in a CLI, many browsers like Firefox have a CLI, also called a console, in which to execute JavaScript lines of code.

//T// The `clear` function is used to clear the console
clear()

//T// Strict mode of execution

//T// JavaScript code can be executed in a strict mode, this shows more warnings and errors, and helps in optimization of JavaScript code, so using strict mode is considered a good practice.

//T// To enable strict mode, use the following syntax.

'use strict';

//T// This should be placed at the start of a script, or at the start of a function (this applies strict mode only to the function)

function func1()
{
    'use strict';
    statements1;
}


//T// In JavaScript, semicolons ; at the end of a line are optional.

//T// The `typeof` keyword is used to get the type of a given name

// typeof(name1)

//T// The `instanceof` keyword is used to check if a given name is an instance of a given class

// name1 instanceof constructor1

//T// This returns a boolean value, `true` if `name1` is an object created with `constructor1`, otherwise `false`.

//T// Strings are created within single quotes or double quotes.

var str1 = 'string one'
var str1 = "string one"

//T// String interpolation is done with backticks. A string created within backticks is called a 'template literal' in JavaScript.

var var1 = 103
var str1 = `string ${var1}`

//T// Printing `var1` outputs:

``` output
string 103
```

//T// The spread operator is the ellipsis ..., it's used to unpack an array into a set of arguments.

var array1 = ['elem1', 'elem2', 'elemN']
func1(...array1)

//T// This syntax passes `'elem1'` through `'elemN'` as arguments to `func1`. For example:

func1 = (a1, a2, a3) => a1 + 2*a2 + 3*a3
var array1 = [4, 5, 1]
var var1 = func1(...array1)

``` output
17
```

//T// A constant is created with the `const` keyword.

const constant1 = value1