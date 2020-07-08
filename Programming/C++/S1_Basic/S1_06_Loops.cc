/*
    Loops
*/

#include <iostream>
using namespace std;

int main()
{
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