#!/usr/local/bin/octave
%{
    Variables
%}

#T# variable initialization, matrices
A = [4 5 6;
     6,7,9]; 
x = sqrt(16); y = 2 * x;
longVariable = x + x + x...
+ x + x + x;

#T# who, whos, clear
who;
whos;
clear;

#T# format values: bank, long e, short e, "+", compact, loose, rat(rational)
format bank
x1 = 3.2
format rat 
x2 = 4.572 * 6.1;

#T# vectors
Vr = [1 3 8,12,9];
Vc = [1;3;8;12;9];