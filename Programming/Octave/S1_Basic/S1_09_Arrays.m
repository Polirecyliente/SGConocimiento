#!/usr/local/bin/octave
%{
    Arrays
%}

#T# vectors

#T# row vector
V1 = [4 12 29 7];

#T# column vector
V1 = [4;12;29;7];

#T# referencing vector elements with colon :
subV1 = V1(1:2);

V2 = [5 + 2i;3 - 4i;1 + 2i;9i];
#T# vector addition and subtraction
V3 = V1 + V2;
V3 = V1 - V2;

#T# scalar multiplication
V3 = 5 * V2;

#T# transpose
V3 = V2';

#T# appending vectors
V3 = [V1,V2];
V3 = [V1;V2];

#T# vector norm: vecnorm()
V3 = vecnorm(V1,2);

#T# dot product: dot()
V3 = dot(V1,V2);

#T# creating vectors with colon operator [::]
V3 = [1:2:20];

#T# matrices

#T# create a matrix
A = [2 12 3;3 2 4];

#T# select a matrix element with (), all elements with :, also range with :
a1_2 = A(1,2);
aALL_3 = A(:,3);
aALL_1to2 = A(:,1:2);

#T# null assignment with []
A(:,2) = [];
B = A([1;1;2;1],:);

B = 2*A;
#T# addition and subtraction of matrices
C = A + B;
C = A - B;

#T# left division, right division
C = A/B;
C = A\B;

d = 4;
#T# scalar operations with matrices
C = d*A;

#T# matrix transpose with '
C = A';

#T# append matrices in []
C = [A B];
C = [A;B];

#T# matrix multiplication with *
C = A*B;

#T# get a matrix determinant with det()
c = det(A);

#T# get a matrix inverse with inv()
C = inv(A);

#T# create multidimensional arrays
A = [2 3;1 6];
A(:,:,2) = [1 0;9 8];