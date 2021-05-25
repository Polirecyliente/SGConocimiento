---
title: COMMON LIBRARIES
toc-title: Table of Contents
---

# INTRODUCTION

This document is about commonly used JavaScript libraries and their functions.

# MATHEMATICS

The `Math` builtin object has properties and methods used to do mathematics. It's used with the following syntax.

``` {.syntax .javascript}
Math.name1
```

`name1` is an attribute or method of the `Math` object.


----

The `round` function is used to round a floating point number to the nearest integer.

``` {.javascript in="in a browser console"}
Math.round(3.5)
```

``` output
4
```

``` {.javascript in="in a browser console"}
Math.round(3.4)
```

``` output
3
```


----

The `max` function returns the maximum of its arguments.

``` {.syntax .javascript}
Math.max(num1, numN)
```

``` {.javascript in="in a browser console"}
Math.max(3, 9, 5)
```

``` output
9
```

# BROWSER

The `navigator` object has properties and methods used to get information about the browser, in which the JavaScript code is executed. It's used with the following syntax.

``` {.syntax .javascript}
navigator.name1
```


----

The `appCodeName` property contains the name of the browser.

``` {.javascript in="in a browser console"}
navigator.appCodeName
```

``` output
"Mozilla"
```

This output changes, according to the browser used.


----

The `window` object has properties and methods to manage browser tabs, each of which is a window. It's used with the following syntax.

``` {.syntax .javascript}
window.name1
```


----

The `open` function is used to open a new tab, with a given URL and a given name.

``` {.syntax .javascript}
window.open("url1", "window_name1")
```


----

The name of a window can be read with the `name` property.

``` {.syntax .javascript}
var1 = window.name
```