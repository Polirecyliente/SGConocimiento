/*
    Decision making
*/

#include <iostream>
using namespace std;

int main()
{
    int a = 1;
//T// if, else if, else statement
    if (a == 10)
    {
        cout << "in if executed\n";
    }
    else if (a < 10)
    {
        cout << "in else if executed\n";
    }
    else
    {
        cout << "in else executed\n";
    }

//T// switch, case, default statement
    switch (a)
    {
        case 1:
            cout << "in case 1 executed\n";
            break;
        case 's':
            cout << "in case s executed\n";
            break;
        default:
            cout << "in default executed\n";
    }

    return 0;
}