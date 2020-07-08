#!/usr/local/bin/octave
%{
    Polynomials
%}

#T# represent polynomials as coefficient vectors, in the example P1 represents the polynomial x^4 + 7*x^3 - 5*x + 9
P1 = [1 7 0 -5 9];  

#T# evaluate a given value or set of values with polyval()
Val1 = polyval(P1,[4 1]);

Matr1 = [9 4;1 12];
#T# evaluate a given matrix as one value with polyvalm()
Val2 = polyvalm(P1,Matr1);

r1 = roots(P1);
#T# find a polynomial with a given set of roots with poly()
P2 = poly(r1);

x1 = [1 2 3 4 5 6];
y1 = [5.5 43.1 128 290.7 498.4 978.67];
#T# fit a polynomial of a given degree to a curve with polyfit()
P3 = polyfit(x1,y1,4);