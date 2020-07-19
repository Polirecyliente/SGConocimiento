#!/usr/local/bin/octave
%{
    Operators
%}

A1 = [3 6 2;9 8 1;0 5 7];
B1 = [2 1 4;3 1 5;2 6 3];
A2 = [1.2 2.5;9.12 -3.824];

#T# arithmetic operators
C1 = A1 + B1;
C1 = A1 - B1;
C1 = A1 * B1;
C1 = A1 .* B1;
C1 = B1/A1;
C1 = B1./A1;
C1 = A1\B1;
C1 = A1.\B1;
C1 = A1^-3;
C1 = A1.^-3;
C1 = A1';
C1 = A1.';

#T# arithmetic functions
C1 = uplus(-A1);
C1 = plus(A1,B1);
C1 = uminus(-A1);
C1 = minus(A1,B1);
C1 = mtimes(A1,B1);
C1 = times(A1,B1);
C1 = mrdivide(B1,A1);
C1 = rdivide(B1,A1);
C1 = mldivide(A1,B1);
C1 = ldivide(A1,B1);
C1 = mpower(A1,-3);
C1 = power(A1,-3);
C1 = cumprod(A1,2);
C1 = cumsum(A1,2);
C1 = diff(A1,1,2);
C1 = prod(A1,2,'native');
C1 = sum(A1,2,'native');
C1 = ceil(A2);
C1 = fix(A2);
C1 = floor(A2);
C1 = round(A2);
C1 = idivide(B1,A1,'ceil');
C1 = mod(B1,A1);
C1 = rem(B1,A1);

A1(3,3)=3;
#T# relational operators
C2 = (A1 < B1);
C2 = (A1 <= B1);
C2 = (A1 > B1);
C2 = (A1 >= B1);
C2 = (A1 == B1);
C2 = (A1 ~= B1);

#T# relational functions
C2 = lt(A1,B1);
C2 = le(A1,B1);
C2 = gt(A1,B1);
C2 = ge(A1,B1);
C2 = eq(A1,B1);
C2 = ne(A1,B1);
C2 = isequal(A1,B1);

a1 = 5; b1 = 0;
#T# logical operators
C3 = (A1 & B1);
C3 = (A1 | B1);
C3 = (~A1);
C3 = (a1 && b1);
C3 = (a1 || b1);

#T# logical functions
C3 = and(A1,B1);
C3 = or(A1,B1);
C3 = not(A1);
C3 = xor(A1,B1);
C3 = all(A1,2);
C3 = any(A1,2);
C3 = false(2,3);
C3 = true(2,3);
[C3a,C3b,C3c] = find(A1,5,'first');
C3 = islogical(A1);
C3 = logical(A1);

#T# bitwise functions
C4 = dec2hex(bitand(a1,b1));
C4 = dec2hex(bitcmp(a1));
C4 = bitget(a1,24:-1:1);
C4 = dec2hex(bitor(a1,b1));
C4 = dec2hex(bitset(a1,24,0));
C4 = dec2hex(bitshift(a1,-1));
C4 = dec2hex(bitxor(a1,b1));
C4 = dec2hex(swapbytes(uint32(a1)));

#T# set functions
C5 = intersect(A1,B1);
C5 = ismember(A1,B1);
C5 = issorted(B1(:,2));
C5 = setdiff(A1,B1);
C5 = setxor(A1,B1);
C5 = union(A1,B1);
C5 = unique(B1);

#T# continue string in next line operator
C6 = "Str\
 1";

#T# continue statement in next line operator
C7 = [2,3,52,34,45,36,74,7,...
54,6,4]