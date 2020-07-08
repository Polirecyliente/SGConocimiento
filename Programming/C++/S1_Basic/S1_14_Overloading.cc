/*
    Overloading
*/

//T// overloading of functions and operators

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

//T// function overload
void funOv(int);
void funOv(double);

//T// operator overload with the operator keyword
string operator+(const string& arg1,const string& arg2)
{
    string retV = "";
    retV.append(arg1);
    retV.append(" -|- ");
    retV.append(arg2);
    return retV;
}

int main()
{
    int i1 = 5;
    double d1 = 64.1;
//T// call overloaded functions
    funOv(i1);
    funOv(d1);

    string s1 = "str1";
    string s2 = "str2";
    cout << "sum overload: " << s1 + s2 << "\n";

    return 0;
}

void funOv(int i)
{
    cout << "First " << i << "\n";
}
void funOv(double d)
{
    cout << "Second " << d << "\n";
}