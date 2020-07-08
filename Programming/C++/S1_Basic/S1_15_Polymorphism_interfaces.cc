/*
    Polymorphism, interfaces
*/

#include <iostream>
using namespace std;

class BaseCl1
{
    public:

//T// allow polymorphism with the virtual keyword
        virtual int polymorphF1()
        {
            return 3;
        }
//T// make an interface by declaring a pure virtual function = 0
        virtual int interfFun1(int a1) = 0;
};

class ChildCl1: public BaseCl1
{
    public:
        int polymorphF1()
        {
            return 27;
        }
//T// implement the functions of the interface
        int interfFun1(int arg1)
        {
            return 2*arg1;
        }
};

int main()
{
    BaseCl1* ptr1;
    ChildCl1 obj1;
    ptr1 = &obj1;

//T// call child function with parent pointer because of the virtual keyword
    cout << "func return: " << ptr1->polymorphF1() << endl;

    return 0;
}