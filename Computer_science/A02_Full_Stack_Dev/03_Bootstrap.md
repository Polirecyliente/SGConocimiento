---
title: BOOTSTRAP
toc-title: Table of Contents
---

# INTRODUCTION

A framework that combines HTML, CSS and JavaScript, designed to create web pages to be viewed in mobile devices.

# INSTALLATION

Bootstrap can be installed with the Node Package Manager.

``` bash
npm install bootstrap
```

Bootstrap is installed in the current directory.

Bootstrap can also be fetched as a CDN file.

``` {.html in="in file1.html"}
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
```

# BASIC USAGE

To use Bootstrap, the following metadata is commonly used, it's placed inside the `<head>` tag.

``` {.html in="in file1.html"}
<meta name="viewport" content="width=device-width, initial-scale=1">
```

The `width=device-width` metadata makes the width to follow the width of the device. `initial-scale=1` sets the initial zoom.

# CSS classes

The basic functionality of Bootstrap comes through CSS classes.


----

Bootstrap uses containers as a first level of organization of content. The two main container classes are `.container` and `.container-fluid`.

``` {.html .syntax}
<div class="container">
    content1
</div>

<div class="container-fluid">
    content2
</div>
```

The difference is that `.container` keeps a margin to the left and right sides of the viewport, and `.container-fluid` fills the content up to the left and right edges of the viewport.