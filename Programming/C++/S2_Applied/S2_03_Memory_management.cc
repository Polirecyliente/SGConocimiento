/*
    Memory management
*/

#include <iostream>
using namespace std;

int main()
{
    double* dptr1 = NULL;
//T// allocate memory to the heap with the new keyword
    dptr1 = new double;

//T// release memory from the heap with the delete keyword
    delete dptr1;
    
    return 0;
}