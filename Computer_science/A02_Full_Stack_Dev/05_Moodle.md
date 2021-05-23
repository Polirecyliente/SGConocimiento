---
title: MOODLE
toc-title: Table of Contents
---

# INTRODUCTION

Moodle is a learning management system, the idea is to host it in a server, so it needs PHP and MySQL to work (the LAMP stack can be used to host Moodle).

Moodle stands for Modular Object-Oriented Dynamic Learning Environment, but its letters are not capitalized.

# INSTALLATION

Download Moodle from its official website https://moodle.org/.

The downloaded file has a name of the form `moodle-latest-NNN.tgz` where `NNN` represents a number of the Moodle's version.

Extract the downloaded file, the result is a directory named `moodle`. This directory should be moved to the directory where the server is stored (commonly in `/var/www/html/` for an Apache server, in this case the final path of the `moodle` directory is `/var/www/html/moodle`).

After doing this, in a browser go to `localhost/moodle`, this starts an installation for Moodle (with the `install.php` file). Follow the instructions there.

If the installation complains about missing dependencies, install them, restart the Apache server, and then reload the Moodle installation.