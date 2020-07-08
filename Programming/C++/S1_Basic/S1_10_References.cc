/*
    References
*/

#include <iostream>
using namespace std;

int gVar1;
int& lhsFun1();

int main()
{
    int var1;
//T// create a reference with & on a variable
    int& ref1 = var1;

    ref1 = 3;
    cout << "var1 val: " << var1 << "\n";

    gVar1 = 5;
    cout << "gVar1 before: " << gVar1 << "\n";
//T// functions can be used as left hand side values with references
    lhsFun1() = 92;
    cout << "gVar1 after: " << gVar1 << endl;

    return 0;
}

int& lhsFun1()
{
    return gVar1;
}