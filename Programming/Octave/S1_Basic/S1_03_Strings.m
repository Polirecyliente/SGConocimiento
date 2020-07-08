#!/usr/local/bin/octave
%{
    Strings
%}

A = [3.2 1;-5.62 3];
#T# numeric data types: double, single, and int
B = double(A);

#T# use printf() to print formatted to the stdout, get maximum and minimum ints that can be stored with intmax(), intmin()
printf("Min int64 %d, Max uint64 %d\n",intmin('int64'),intmax('uint64'));

#T# get maximum and minimum real numbers with realmax(), realmin()
printf("Min single %d, Max double %d\n",
realmin('single'),realmax('double'));

#T# convert numbers to cell array with num2cell()
A = num2cell(A);

#T# create strings with ''
str1 = 'Example String';

C = [65 95 80;66 100 97];
#T# cast numbers as characters, and create arrays of strings with char()
char(C);
B = char("one1","doubStr2","tripStr3Leng");

#T# concatenate strings with strcat()
C = strcat(B(1,:),B(2,:),B(3,:));

#T# convert strings to a cell array with cellstr()
B = cellstr(B);

#T# string functions
str2 = ["Start",blanks(5),"End"];
n1 = iscellstr(B);
n1 = ischar(B{2,1});
str2 = sprintf("formated %s saved into char array\n","string");
str2 = strjoin(B);
N1 = isletter(B{3,1});
N1 = isspace(B{3,1});
C = sscanf("3 92 5",'%d');
n1 = strfind("stringToBeMatched","Match");
str2 = strrep("stringToBeReplaced","Replac","Chang");
str2 = strsplit("stringadividedainasplits","a");
[str2,remain1] = strtok("stringabutainatokens","a");
str2 = validatestring("doubStr2",B);
n1 = strcmp("anotherStr","anotherStr");
n1 = strncmpi("onestrDiff","oNEStrExtra",5);
str2 = deblank("    leadSpaces and trailing        ");
str2 = strtrim("    leadSpaces and trailing        ");
str2 = lower("With CAPs");
str2 = upper("with noCaps");