#!/usr/local/bin/octave
%{
    Calculus
%}

pkg load symbolic;

#T# define symbolic variables with syms
syms x;
syms y;

#T# calculate limits with limit()
a = limit((x^2+x-6)/(x-2),x,2,'left');

#T# make derivatives with diff()
y = expand(diff((x^3+5*x^4),2));

#T# substitute a given value in a function with subs()
val1 = subs(y,2);

#T# solve for zero or solve a given equation with solve()
solucs1 = solve(x^2 + 6 == 5*x,x);

syms z(x);
DiffEq1 = diff(z,x) == 5*z;
#T# solve differential equations and their initial conditions with dsolve()
solDiff1 = dsolve(DiffEq1,z(3)==7);

#T# integrate functions with the not so well named int()
y = int(2*x^4);
area1 = int(x,4,9);