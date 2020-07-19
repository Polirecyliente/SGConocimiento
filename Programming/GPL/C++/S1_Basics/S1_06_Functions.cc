/*
    Functions
*/

#include <iostream>
using namespace std;

//T// function declaration
char func1(char,char*,char &, int arg4 = 12);

//T// create inline functions with the inline keyword
inline int inlFun1(int a){return 3*a;}

int main()
{
    char c1,c2,c3;
    c2 = 'b';
    c3 = 'l';
//T// function call
    c1 = func1('h',&c2,c3);

    cout << "inline return from 7 is " << inlFun1(7) << "\n";
    return 0;
}

//T// function definition
//T// arg1 call by value, arg2 call by pointer, arg3 call by reference,
//T// arg4 default value
char func1(char arg1, char* arg2, char &arg3, int arg4)
{
    char retC = arg3;
    cout << "called from the func1 " << arg1 << retC << *arg2 
        << arg4 << endl;
    return retC;
}