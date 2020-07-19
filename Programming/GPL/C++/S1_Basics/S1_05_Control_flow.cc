/*
    Control flow
*/

//T// Contents
//T// Decision making
//T// Loops

#include <iostream>
using namespace std;

int main()
{

//T// Decision making

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

//T// Loops

    int i1 = 5;
//T// while loop
    while (i1 > 2)
    {
        if (i1 == 4)
        {
            i1--;
            continue;
        }
        cout << "iterW";
        i1--;
    }

//T// for loop
    for (i1; i1<6; i1++)
    {
        cout << "iterF";
    }

    LABL1:if(i1 == 1500) goto LABL2;

//T// do while loop
    do
    {
        cout << "iterD";

//T// break
        if (i1 == 6) break;
    } while (i1 > 0);

    i1 = 1500;
//T// goto
    goto LABL1;

    LABL2:cout << "endl\n";

    return 0;
}