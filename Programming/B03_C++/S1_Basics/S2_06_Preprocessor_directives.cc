/*
    Preprocessor directives
*/

//T// the #include directive includes headers
#include <iostream>

//T// the #define directive defines a constant or macro
#define PI 3.1415

//T// conditional compilation directives #if, #ifdef, #ifndef, #else, #endif
#ifndef NULL
    #define NULL 0
#endif

//T// stringize operator #, token pasting operator ##
#define strF(s1) #s1" -|-"#s1
#define pasteF(a,b) a##b

using namespace std;

int main()
{
    cout << "PI is " << PI << "\n";

    #ifdef PI
        cout << "str\n";
    #endif

    #if 0
        unreachable code
    #endif

    cout << strF(tokens) << "\n";
    cout << "num really is " << pasteF(P,I) << endl;

    return 0;
}