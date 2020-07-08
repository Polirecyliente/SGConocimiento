/*
    File input output
*/

#include <iostream>

//T// include the library to manipulate files fstream
#include <fstream>

using namespace std;

int main()
{
//T// create a file handle of sorts with an fstream object, an ofstream object is for output to the file
    ofstream ofh1;

    string fname1 = 
    "/home/jul/PolirecylBases/tutos/C++/Section2/Section2_1Debug";
//T// open a file with the open() function
    ofh1.open(fname1,ios::out|ios::trunc);
    
//T// write data to a file with <<
    ofh1 << "Info " << "written to file" << endl;

//T// close a file with the close() function
    ofh1.close();

//T// an ifstream object is for input from the file
    ifstream ifh1;

    ifh1.open(fname1);
    string str1;

//T// read data from a file with >>
    ifh1 >> str1;
    ifh1 >> str1;

    cout << "Found data in file:\n" << str1 << "\n";

//T// get cursor position with tellg() and set it with seekg()
    cout << "Tell: " << ifh1.tellg() << "\n";
    ifh1.seekg(15,ios::cur);

    ifh1.close();

    return 0;
}