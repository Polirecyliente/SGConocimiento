#!/usr/local/bin/octave
%{
    Functions
%}

cd "/home/jul/SGConocimiento/Octave/S1_Basic"
#T# call user defined functions
[a b c] = S1_10_Aux01(3,4.5,5);
help S1_10_Aux01;

#T# create anonymous functions
anonFun1 = @(arg1,arg2) arg1+(arg2 * 3);
resultAnon1 = anonFun1(2,3);

#T# share variables across this script and functions with the global keyword
global gVar1;
gVar1 = 12;
[a b c] = S1_10_Aux01(3,4.5,5);