#!/usr/local/bin/octave
%{
    Builtin functions
%}

#T# create an array of zeros with zeros()
Z = zeros(4,5,2);

#T# create an array of ones with ones()
A = ones(3,9,2);

#T# create an identity array with eye()
A = eye(2,12);

#T# create an array of random numbers with rand()
A = rand(3,2,2,4);

#T# create a magic square matrix with magic()
A = magic(20);

A = [1 3;2 5];
B = [9 4;8 2];
#T# concatenate arrays along a given dimension with cat()
C = cat(1,A,B);

#T# array functions
n1 = length(Z);
n1 = size(Z);
n1 = ndims(Z);
n1 = numel(Z);
n1 = iscolumn(Z(:,1,1));
n1 = isempty(Z);
n1 = ismatrix(Z(:,:,1));
n1 = isrow(Z(1,:,1));
n1 = isscalar(Z(1,1,1));
n1 = isvector(Z(:,1,1));
D = blkdiag(C,A,B);
D = ctranspose(A);
D = circshift(C,2);
D = diag(A);
D = flip(C,2);
D = fliplr(A);
D = flipud(A);
D = rot90(A);
n1 = issorted(A(1,:));
D = sort(C);
D = squeeze(C);
D = transpose(C);

#T# create cell arrays with cell(), or with {}
B = cell(2,3);
B = {"a",1;32,"b"};

#T# access cell array elements with (), or their values with {}
C = B(2,1);
n1 = B{2,1};

#T# Octave commands

#T# exist, help, lookfor
a = 5;
exist a;
help global;
lookfor global;

#T# cd, dir, pwd, date, what, delete, path, type
cd ../;
dir;
currentWorkDir = pwd;
toDay = date;
cd ./S1_Basic;
save S1_08_Aux02.mat;
what;
delete S1_08_Aux02.mat;
path;
type toDay;

#T# disp(), fopen(), fscanf(), fclose(), fprintf(), input
disp("Mssg1");
fi1 = fopen("S1_1_Basic_syntax.m");
s1  = fscanf(fi1,"%s");
fclose(fi1);
fprintf(stdout,"%s","Line1","\nLine2");
input k1;

#T# cat(), find(), length(), linspace(), logspace(), min(), max(), prod()
A = [3 4 5;
     1 7 9];
B = [5 1 2 8;
     6 0 4 1];
C = cat(2,A,B);
K2 = find(B);
k3 = length(B);
K4 = linspace(20,100,3);
K5 = logspace(2,3,10);
[k6,k6Index] = max([2:5]);
[k7,k7Index] = min([2:5]);
K8 = prod(A,2);

#T# reshape(), size(), sort(), eye(), ones(), zeros(), cross(), dot(), det()
A2 = reshape(A,3,2);
K9 = size(A);
[K10,K10Indexes] = sort(B);
K11 = sum(B);
K12 = eye(3);
K13 = ones(3,2,"uint8");
K14 = zeros(3,2,"uint8");
K15 = cross([0 1 0],[1 0 0]);
k16 = dot(B(1,:),B(2,:));
k17 = det(K12);

#T# inv(), pinv(), rank(), rref()
K18 = inv(K12);
K19 = pinv(K12);
k20 = rank(A);
K21 = rref(A);

#T# figure, axes(), get(), plot() axis(), fplot(), grid, print(), title()
fig1 = figure;
ax1 = axes("parent",fig1);
ax1Type = get(ax1,"type");
plot(ax1,A);
axis(ax1,[0 4 2 4]);
figure;
fplot(@sin,[0 2*pi]);
grid;
print(fig1,"S1_08_Aux01.svg","-landscape");
title(ax1,"OutOfBoundsImg");

#T# xlabel(), ylabel(), close, gtext(), hold(), legend(), refresh(), set()
xlabel(ax1,"LabelXax");
ylabel(ax1,"LabelYax");
close;
gtext("textByMouse");
hold(ax1,"off");
legend(ax1,"legAx","location","northwest");
refresh(fig1);
set(fig1,"name","OneNawn");

#T# subplot(), text()
subplot(2,1,2,ax1);
text(2,3.5,"textByCoordinate");

#T# quit
quit;