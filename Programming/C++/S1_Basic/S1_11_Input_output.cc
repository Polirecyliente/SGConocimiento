/*
    Input output
*/

#include <iostream>
using namespace std;

int main()
{
//T// use the standard output stream with cout
//T// << is the stream inserter operator
    cout << "in standard output stream\n";

    int i1;
    char c1;
//T// use the standard input stream with cin
//T// >> is the stream extraction operator
    cin >> i1 >> c1;

//T// use the unbuffered standard error stream with cerr
    cerr << "in unbuffered standard error stream\n";

//T// use the buffered standard error stream with clog
    clog << "in buffered standard error stream\n";
    
    return 0;
}