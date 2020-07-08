/*
    Constants, literals
*/

#include <iostream>
using namespace std;

//T// define constants with #define preprocessor directive
#define FIRC 12

int main()
{
//T// integer literals
    int a = 5;
    a = 923452u;
    a = 888838833l;
    a = 0XFEE;
    a = 013ul;
    cout << a << "\n";

//T// floating point literals
    float b = 1.335345;
    b = 34.2E-4;
    cout << b << "\n";

//T// boolean literals
    bool c = false;
    c = true;
    cout << c << "\n";

//T// character literals
//T// wide characters (UTF-16) begin with L
    wchar_t d = L'y';
    d = '\u02A0';
    cout << d << "\n";

//T// string literals
    string e = "fir str";
    cout << e << "\n";

//T// create constants with the const keyword
    const int SECC = 15;

    cout << FIRC << "\n";
    cout << SECC << "\n";

//T// the auto, register, static, and extern keywords are the same as in C

    return 0;
}