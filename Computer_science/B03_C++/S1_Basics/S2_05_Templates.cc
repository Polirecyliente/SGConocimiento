/*
    Templates
*/

#include <iostream>
using namespace std;

//T// create a template with the template keyword, and establish the name for a type with the typename keyword
template <typename T1> T1 const& funcTempl1(T1 const& arg1)
{
    return arg1;
}


int main()
{
    string s1 = "str1";
    int i1 = 8;
    cout << "s1 is " << funcTempl1(s1) << "\n";
    cout << "i1 is " << funcTempl1(i1) << "\n";
    return 0;
}