#!/usr/local/bin/octave
%{
    Input output
%}

cd '/home/jul/SGConocimiento/Octave/S1_Basic/'
file1 = 'S1_11_Aux01.csv';

delimiter1 = ' ';
headerline1 = 1;
#T# import data with importdata()
fStruct1 = importdata(file1,delimiter1,headerline1);

#T# headers in imported data
fStruct1{1,1};

#T# get actual data imported
for k = [2:10]
    fStruct1{k,1};
end

#T# open a file handle with fopen()
fH1 = fopen(file1,'a+');

#T# get a line of bytes from a file with fgetl()
lineHeaders1 = fgetl(fH1);

#T# get a line including newline with fgets()
lineData1 = fgets(fH1);

#T# read byte by byte from a file with fread()
tenBytes1 = char(fread(fH1,10));

#T# rewind cursor to the beginning of the file with frewind()
frewind(fH1);
lineHeaders2 = fgetl(fH1);

#T# scan data from a file with fscanf()
scanned1 = fscanf(fH1,"\"%d");

#T# position the cursor at a given offset from a place with fseek()
fseek(fH1,-15,SEEK_END);
lineData2 = fgetl(fH1);

#T# get cursor position in a file with ftell()
pos1 = ftell(fH1);
frewind(fH1)

#T# print data to a file with fprintf()
fprintf(fH1,'HelloNewLine');

#T# write data to a file with fwrite()
fwrite(fH1,'WrittenText');

#T# detect if cursor is at end of file with feof()
n1 = feof(fH1);

#T# close a file handle with fclose()
fclose(fH1);