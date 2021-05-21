/*
    Storage classes
*/

#include <stdio.h>

int eA = 73;

//T// static
static int sA = 29;

//T// extern
extern void printExtern(int aI, int rI, int sI);

int main()
{
//T// auto
    auto int aA = 6;

//T// register
    register int rA = 27;
    printExtern(aA, rA, sA);
    return 0;
}