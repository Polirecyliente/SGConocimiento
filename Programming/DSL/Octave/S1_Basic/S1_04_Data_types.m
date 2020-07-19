#!/usr/local/bin/octave
%{
    Data types
%}

#T# integer types, the u prefix stands for unsigned, the suffix is the number of bits to store the number
n1 = int8(-2);
n2 = uint8(255);
n3 = int16(-31500);
n4 = uint16(64000);
n5 = int32(-2000000000);
n6 = uint32(4000000000);
n7 = int64(-9000000000000000000);
n8 = uint64(18000000000000000000);

#T# single(), double(), logical(), char()
format long
n9 = single(876.543210987654321098);
n10 = double(654321.098765432109876);
n11 = logical(false);
n12 = char('charArrayAKAString');

#T# cell(), struct(), function handle @
cell1 = cell(3,2,4);
struct1 = struct("uint32_1",n6,"char_1",n12);
fhandle1 = @sin;

#T# data type conversion functions, e.g. int2str(), mat2str(), unicode2native(), hex2dec() struct2cell()
A1 = [4,6 2; 2 9 0];
str1 = int2str(A1);
str2 = mat2str(A1);
N13 = unicode2native("á");
str3 = native2unicode([hex2dec("e2") hex2dec("8c") hex2dec("a4")]);
cell2 = struct2cell(struct1);

#T# boolean functions that determine type, e.g. isa(), iscell(), islogical(), class()
n14 = isa(n1,"numeric");
n15 = iscell(cell2);
n16 = islogical(n11);
str4 = class(n5);

A = [3.2 1;-5.62 3];
#T# casting
B = double(A);
B = single(A);
B = int64(A);
B = uint64(A);
B = int32(A);
B = uint32(A);
B = int16(A);
B = uint16(A);
B = int8(A);
B = uint8(A);