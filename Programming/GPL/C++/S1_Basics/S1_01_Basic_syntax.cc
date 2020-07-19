/*
    Basic syntax
*/

//T// Contents
//T// Basic syntax
//T// Variables, constants, literals

//T// compile any C file /path/to/file1.c in a terminal with
// g++ /path/to/file1.c -o /path/to/exec1
//T// run the compiled executable in a terminal with
// /path/to/exec1

//T// preprocessor directives
#include <iostream>

//T// define constants with #define preprocessor directive
#define FIRC 12

//T// using namespace statement
using namespace std;

//T// variable declaration
extern int extr1;

//T// main()
int main()

//T// block of code {}
{

//T// program statements
    cout << "Hello World\n";

//T// keywords and identifiers
    int var_num1 = 5;

//T// Variables, constants, literals

//T// variable declaration and definition
    int a,b;

//T// variable initialization
    a = 10;

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