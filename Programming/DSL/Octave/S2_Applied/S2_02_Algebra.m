#!/usr/local/bin/octave
%{
    Algebra
%}

#T# solve for the roots of polynomials with roots(), the first example rt1 is for the polynomial x - 7, the second rt2 is for 3*x^2 - 4*x - 1
rt1 = roots([1 -7]);
rt2 = roots([3 -4 -1]);

#T# solve systems of linear equations with left division \ or with inv(A)*b
# x = inv(A)*b

#T# load the symbolic package with pkg load
pkg load symbolic;

#T# create symbolic variables with sym()
x = sym('x');
y = sym('y');
z = sym('z');

#T# expand parentheses with expand()
y = expand((x+3)*(x-2));

#T# factorize terms with factor()
z = factor(x^4-2*x+3*x^4);