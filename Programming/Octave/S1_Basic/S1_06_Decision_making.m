#!/usr/local/bin/octave
%{
    Decision making
%}

a = 21;
#T# if, elseif, else, end statement
if a < 20
    disp("a is less than 20");
elseif a == 20
    disp("a is equal to 20");
else
    disp("a is greater than 20");
    disp("borr1");
    disp("borr2");
    if (a + 5) == 26
        disp("a is exactly one over 20");
    end
end

str = "str1";
s1 = struct2cell(struct("fld1",12,"fld2",34,"fld3","str1"));
#T# switch, case, otherwise, end statement
switch str
    case s1
        disp("found case");
    case 1
        disp("val 1");
    otherwise
        disp("no value detected");
end