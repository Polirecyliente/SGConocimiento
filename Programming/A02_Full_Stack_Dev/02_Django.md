---
title: DJANGO
toc-title: Table of Contents
---

# INTRODUCTION

Django is a framework to create the backend of web applications.

Django can be installed in a virtual environment using the `pipenv` program

``` bash
pipenv install django
```

# BASIC USAGE

A new Django project can be created with the `django-admin` program

``` {.bash .syntax}
django-admin startproject project1
```

This creates a directory named `project1`, inside it, there is a python file called `manage.py` that is executed to manage the web application backend being created with Django.


----

A new Django web application backend can be created with the following syntax.

``` {.bash .syntax}
python3 /path/to/project1/manage.py startapp application_backend1
```


----

A Django web application backend can be launched with the following syntax.

``` {.bash .syntax}
python3 /path/to/project1/manage.py runserver
```

By default the new web application can be accessed in the address `http://localhost:8000`. This address can be input in a browser like `firefox` or other.