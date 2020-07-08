/*
    Namespaces
*/

#include <iostream>
using namespace std;

//T// create namespace with the namespace keyword
namespace scope1
{
    void fun1(){cout << "in scope1\n";}
}
namespace scope2
{
    void fun1(){cout << "in scope2\n";}
}

int main()
{
//T// call functions in the namespaces
    scope2::fun1();
    scope1::fun1();
    return 0;
}