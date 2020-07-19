%{
    Sets
%}

#T# Let A,B,C sets be:
A = [111 12 13 123];
B = [222 12 23 123];
C = [333 13 23 123];

#T# join sets with union()
unionA_B = union(A,B)

#T# meet sets with intersect()
intersB_C = intersect(B,C)