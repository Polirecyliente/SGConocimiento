/*
    OOP
*/

//T// OOP stands for Object Oriented Programming

#include <iostream>
using namespace std;

//T// create a class with the class keyword
class GCl1
{
    public:
        int memFun1();
//T// funcs or classes have full access to the class with the friend keyword
        friend int friFun1(GCl1);
        friend class Cl1;

//T// make static members with the static keyword
        static int statI1;
    private:
        int globPriv1;
};

//T// access static members with the :: operator
int GCl1::statI1 = 32;

int friFun1(GCl1 objP)
{
    return 2*objP.globPriv1;
}

//T// class functions can be defined through the scope resolution operator ::
int GCl1::memFun1()
{
    return 5;
}

class GCl2
{
    protected:
        int protGCl2 = 44;
};
//T// create child classes with a class derivation list
class ChildGCl1: public GCl1, private GCl2
{
    public:
        int getPr2(){return this->protGCl2;}
};

int main()
{
//T// classes may be local,
    class Cl1
    {
//T// public members go under the public: label
        public:

//T// members of the class
            int memC1;
            int memFun1();

//T// create the constructor with the same name as the class,
//T// constructors can use initializer lists
            Cl1(int pr1): privMem1(pr1)
            {
                cout << "Creation successful\n";
            }

//T// create a copy constructor with this syntax
            Cl1(const Cl1 &copiedObj)
            {
                cout << "in copy constructor\n";

//T// get a pointer to the object itself with the this keyword
                this->privMem1 = copiedObj.privMem1;
            }

//T// create the destructor with tilde ~ and the class name
            ~Cl1()
            {
                cout << "Destruction successful\n";
            }

            int getPvM()
            {
                return privMem1;
            }

//T// private members can only be seen inside the class or its friends
        private:
            int privMem1;

//T// protected members are visible to child classes only
        protected:
            int protMem1;
    };

//T// create instances of the class
    Cl1 obj1(93);

//T// access members of the class with .
    obj1.memC1 = 71;
    cout << "class member is " << obj1.memC1 << "\n";
    cout << "private member is " << obj1.getPvM() << "\n";

    int i1;
    GCl1 obj2;
//T// call a class member function
    i1 = obj2.memFun1();
    cout << "i1 is " << i1 << "\n";

//T// create a copy of an object
    Cl1 obj3(obj1);
    cout << "obj3 private member is " << obj3.getPvM() << "\n";

    ChildGCl1 obj4;
    cout << "obj4 private member is " << obj4.getPr2() << "\n";

    return 0;
}