/*
    Exception handling
*/

#include <iostream>
using namespace std;

//T// create a custom exception inheriting the class exception
struct custExc1: public exception
{
    const char* what () const throw ()
    {
        return "from custom exception";
    }
};

int excThrower1(int a1)
{
//T// throw an exception with the throw keyword
    if (a1 == 6) throw "Custom Exc Mssg: Arg number";
    return 21;
}

int main()
{
    int i1 = -3;
//T// handle exceptions with a try catch block
    try
    {
        i1 = excThrower1(6);
        cout << "i1 value is " << i1 << "\n";
    } catch (const char* excMsg)
    {
        cout << "Exception\n" << excMsg << ". i1 value is " << i1 << "\n";
//T// catch any exception with ellipsis ...
    } catch (...)
    {
        cout << "Overall Exception, i1 value is " << i1 << "\n";
    }

    try
    {
        throw custExc1();

//T// catch exceptions of a given class
    } catch (custExc1& exc1)
    {
//T// get the message of the exception with what()
        cout << "Caught own exception, " << exc1.what() << "\n";
    }

    return 0;
}