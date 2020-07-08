#!/usr/bin/perl
#   Format

#T# format keyword, @<<<, @>>>, @|||, @##.#
format formatName =
===--------------------------===
@<<<<<<<<<<<<<<<<<<< @>>>>>>>>>>
$val1,$val2
Middle Part
@||||||||||||||||||||||||||
$val3
Ending Number
@########.###
$val3
------====================------
.

#T# page number $%
format headerName =
¨¨¨¨¨'''''''''''''¨¨¨¨¨
header word page: @<<
$%
¨¨¨¨¨'''''''''''''¨¨¨¨¨
.

$val1 = "leftJustified";
$val2 = "rightJustified";
$val3 = 982.16;

#T# select() file handle STDOUT, $~ format special variable, format header $^, write()
select(STDOUT);
$~ = formatName;
$^ = headerName;

write();