/*
    Referencing
*/

#include <iostream>
using namespace std;

int main()
{
    int a1 = 5;
//T// get the address of a variable with &
    cout << "address is " << &a1 << "\n";

//T// create pointers with *
    int* iptr1;
    iptr1 = &a1;

//T// access value pointed to by a pointer with *
    cout << "pointer value is " << iptr1 << "\n";
    cout << "pointed value by pointer is " << *iptr1 << "\n";

//T// use the NULL constant to create null pointers
    char* cptr1 = NULL;
    if (!cptr1) cout << "pointer is null\n";

//T// get next or former address from a pointer with ++ or --
    iptr1++;
    cout << "next address from iptr1 is " << iptr1 << "\n";

    return 0;
}