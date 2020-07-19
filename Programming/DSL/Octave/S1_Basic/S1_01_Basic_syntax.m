#!/usr/local/bin/octave
%{
    Basic syntax
%}

#T# definitions, calculations, suppress output with semicolon ;
a = 2 + 2;
b = 7/0;
Carr1 = [3 4 14;6 25 13];

#T# cd to change dir to working dir
cd "/home/jul/SGConocimiento/Octave/S1_Basic/"

#T# save variables to a file with save file1.mat
save S1_01_Aux01.mat;

#T# load variables in file1.mat with load file1.mat
# load S1_01_Aux01.mat;

#T# save a particular array in ascii delimited style
save S1_01_Aux02.out Carr1 -ascii;

#T# show an Octave's file content with the type keyword
type S1_01_Aux02.out