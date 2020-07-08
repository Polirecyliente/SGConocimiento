#!/usr/local/bin/octave
%{
    Fourier, Laplace
%}

pkg load symbolic;
syms x y s;
#T# make Laplace transforms with laplace()
LTransf1 = laplace(x);
LTransf2 = laplace(sin(x*y));

#T# make inverse Laplace transforms with ilaplace()
invLT1 = ilaplace(1/s^3);
invLT2 = ilaplace(LTransf1);

#T# make Fourier transforms with fourier()
FTrans1 = fourier(exp(-2*x^2));

#T# make inverse Fourier transforms with ifourier()
invFT1 = ifourier(FTrans1);