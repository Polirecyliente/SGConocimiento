%{
    CLI args
%}

#T# get a cell array containing the command line arguments with argv()
cellArgs1 = argv();

#T# access argument values by accessing the cell array
cellArgs1{2,1};

#T# get the number of arguments with nargin
nArgs1 = nargin;