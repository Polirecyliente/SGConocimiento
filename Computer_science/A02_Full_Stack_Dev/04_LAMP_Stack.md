---
title: LAMP STACK
toc-title: Table of Contents
---

# INTRODUCTION

LAMP stands for Linux Apache MySQL PHP, it's a stack of software intended to create web servers that have databases.

Apache is a framework to create web servers using the HTTP protocol, i.e. HTTP servers.

MySQL is both an SQL language, as well as a RDMS (Relational Database Management System).

PHP is a programming language, designed for creating web pages.

Both MySQL and PHP as languages have their syntaxes detailed in their respective language files in this project. Here they will be treated as tools to create web servers.

phpMyAdmin is a tool that allows managing MySQL databases in a web server via PHP (instead of doing it in the regular MySQL command line interface).

# INSTALLATION

Apache can be installed with:

``` bash
sudo apt install apache2
```


----

MySQL server allows having databases in the web server, it can be installed as follows.

``` bash
sudo apt install mysql-server
```

The MySQL installation can be secured, for example by creating a root user that can manage the databases.

``` bash
sudo mysql_secure_installation
```

Executing this program, prompts the user for different security options. It should be done at least once after intalling MySQL, to secure the installation.


----

phpMyAdmin can be installed as follows.

``` bash
sudo apt install phpmyadmin
```

This installation asks the user to follow a few instructions to configure the phpMyAdmin installation.

Include the phpMyAdmin configuration file into the Apache configuration, by adding the following in the `/etc/apache2/apache2.conf` file.

``` apache
# Include the phpMyAdmin configuration file
Include /etc/phpmyadmin/apache.conf
```

After these steps, the Apache server should be restarted.

``` bash
sudo systemctl restart apache2
```

# BASIC USAGE

Check if the Apache server is on.

``` bash
sudo systemctl status apache2
```

If the Apacher server is not on, then start it.

``` bash
sudo systemctl start apache2
```

Use a browser like Firefox, to go to the server address, by default it's located in the localhost, at port 80.

```
http://localhost:80
```

Enter this address in the browser, if the default server is correct, an Apache2 default web page will be served.


----

Check if the MySQL server is running.

``` bash
sudo systemctl status mysql
```

If the MySQL server is not running, then start it.

``` bash
sudo systemctl start mysql
```

Start the MySQL command line interface.

``` bash
sudo mysql -u root -p
```

This starts a prompt `mysql>` by default. The `-u` option is for user, the `-p` option is for password. Logging in as `root`, requires `sudo`.

By default, the MySQL server is located at the port 3306.


----

Go to the phpMyAdmin interface in a browser, by default it's located at the address `http://localhost/phpmyadmin`.

Here, an UI is presented to enter the username and password credentials. The user must NOT have the authentication type `auth_socket`, but another one, like for example `caching_sha2_password` (to check the authentication type of the users, use the SQL query `SELECT user, plugin FROM mysql.user;`, the `plugin` column shows the authentication type).

# APACHE

Check the Apache syntax of configuration files.

``` bash
apache2ctl -t
```

This shows any syntax errors in the Apache server configuration files (like `/etc/apache2/apache2.conf`).


----

Display the loaded Apache modules.

``` bash
apache2ctl -M
```


----

Enable an Apache module, to use it in the server.

``` {.syntax .bash}
sudo a2enmod module1
```

For example:

``` bash
sudo a2enmod headers
```


----

Disable an Apache module.

``` {.syntax .bash}
sudo a2dismod module1
```