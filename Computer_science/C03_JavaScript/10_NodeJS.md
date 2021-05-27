---
title: NODEJS
toc-title: Table of Contents
---

# INTRODUCTION

Node.js is a set of software that allows running JavaScript code directly in a computer, on top of its operating system (normally, JavaScript code can only be run from a browser). This allows JavaScript to be used as a General Purpose Language, to write servers, desktop applications, web applications, etcetera.

The `node` program, that makes part of Node.js, is an interpreter of JavaScript code. `node` can be executed in a shell.

The following, starts a Node.js interpreter session, this allows using JavaScript as a scripting language.

``` {.bash in="in a CLI"}
node
```

The following, executes `file1.js` in the computer.

``` {.bash in="in a CLI"}
node /path/to/file1.js
```

# INSTALLATION

Node.js can be installed as follows.

``` {.bash in="in a CLI"}
sudo apt install nodejs
```

Check that Node.js is installed.

``` {.bash in="in a CLI"}
node -v
```

This should output the installed version of Node.js

# BASIC USAGE

Quit or exit from a Node.js program with the `process.exit()` function.

``` {.javascript .syntax}
process.exit(int1)
```

`int1` is the exit code of the program, a value of 0 commonly means a successful execution, and any other number means an error exit code.

# MODULES

Node.js comes with several builtin modules, and more modules can be added.

The `require` function can be used to import a module.

``` {.javascript .syntax}
var obj1 = require('/path/to/module1')
```

In this case, `obj1` is an object that has the names exposed by `module1`. For builtin modules, the directory path to the module is not necessary (this is also the case for modules installed via `npm`).

``` {.javascript in="in file1.js"}
var obj1 = require('http')
```

This imports the `http` builtin module, with it, servers can be created.


----

The `exports` object is used to expose the names from a module.

``` {.javascript in="in module1.js"}
exports.exposed_name1 = name1
```

`name1` is defined in `module1`. Commonly, `exposed_name1` is left the same as `name1`, but they don't have to be the same.

Only the names that are exported, are members of the object returned by the `require` function.


----

New modules can be installed. https://www.npmjs.com is a popular website that publishes Node.js modules and packages. The `npm` command can be used to install Node.js modules and packages from https://www.npmjs.com.

``` {.bash .syntax}
npm install module1
```

This installs `module1` in the current directory, inside a directory named `node_modules`. It also creates the `package.json` and `package-lock.json` files (or updates them, if they already exist).


----

Installed Node.js modules and packages can be removed.

``` {.bash .syntax}
npm remove module1
```

# CREATING A PROJECT

Node.js and https://www.npmjs.com, can be used to create projects. A project will be converted into a package or a module, depending on the project itself. To create a new project from JavaScript code, execute the following command.

``` {.bash in="in a CLI"}
npm init
```

This starts an interactive session to configure the new project. The resulting configuration is stored in the `package.json` file.


----

The dependencies of a project, are listed in the `package.json` file (there is an object called `dependencies`). To install all the dependencies of a project, execute the following command.

``` {.bash in="in a CLI}
npm install
```

This can be used if the `node_modules` directory is deleted, or if there are missing dependencies.


----

Inside the `package.json` file, there is an object called `scripts` (if not, it can be created). This object can be used by the `npm` command.

``` {.bash .syntax}
npm run script1
```

`script1` must be one of the properties of the `scripts` object. The value of the `script1` property is executed in the shell.


----

There is a special script named `start`, which can be run by doing:

``` {.bash}
npm start
```

This executes the value of the `start` property of the `scripts` object, inside the `package.json` file.

# HTTP server

Import the `http` builtin module to create and manage HTTP servers.

``` {.javascript in="in file1.js"}
const http = require('http')
```


----

Create an HTTP server with the `createServer` function.

``` {.javascript .syntax}
const http = require('http')

http.createServer(request_listener1).listen(port1)
```

`request_listener1` is a function that is called whenever the server gets an HTTP request. `port1` is the port number where the server will listen to. By default, the server can be accessed at the address 'http://localhost:port1'. For example:

``` {.javascript in="in file1.js"}
const http = require('http')

function request_listener1(req, res)
{
    res.writeHead(200, {'Content-type': 'text/html'})
    res.write('<p>text <b>in bold</b><p>')
    res.end()
}

http.createServer(request_listener1).listen(5000)
```

`request_listener1` takes two arguments, `req` to represents the HTTP request, and `res` to represent the HTTP response.

The `writeHead` and `write` functions, are used as part of the HTTP request. `writeHead` is used to write metadata, and `write` is used to write data (in this case HTML text).

In `res.writeHead(200, {'Content-type': 'text/html'})`, the `200` is an HTTP response status code, `200` is for the OK status, meaning that the request was successful and the response can take place.

The `end` function ends the response. To turn on this server, execute:

``` {.bash in="in a CLI"}
node /path/to/file1.js
```

Then in a browser, go to the address 'http://localhost:5000' to see the server response.