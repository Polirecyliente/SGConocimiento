/*
    Structures
*/

#include <iostream>
using namespace std;

int main()
{
//T// create structures with the struct keyword
    struct FirStru
    {
//T// members of the structure go inside curly brackets
        int mem1;
        char mem2;
//T// instances of the structure can be defined before semicolon
    } stru1, stru2;

//T// access structure's members with the dot operator .
    stru1.mem1 = 16;
    cout << "member one in structure one is " << stru1.mem1 << "\n";

//T// new instances of the structure can be defined with this syntax
    struct FirStru stru3;

    struct FirStru* stru3ptr;
    stru3ptr = &stru3;
//T// access members of a structure through a pointer with ->
    stru3ptr->mem1 = 78;
    cout << "member one through pointer is " << stru3ptr->mem1 << "\n";

    return 0;
}