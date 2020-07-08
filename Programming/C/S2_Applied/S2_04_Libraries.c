/*
    Libraries
*/

//T// calling functions from a user made library

//T// this program just calls functions in libS2_04_Aux02.so library. To find out how to compile .so files, and executables that use them see S2_02_GCC_compiler.c, but as a summary, execute for each of the source files of the library
// gcc -fPIC -c libraryFuncsN.c
//T// then execute this to create the library
// gcc -shared -o libS2_04_Aux02.so libraryFuncsN.o

//T// create a header file S2_04_Aux01.h with declarations for the library functions
// int S2_04_LibFun1(int, int);
// int S2_04_LibFun2(int, int);

// #include "S2_04_Aux01.h"
#include <stdio.h>

int main()
{
    int val1 = 0;
    int val2 = 0;
//T// calling custom library functions
    val1 = S2_04_LibFun1(3,10);
    val2 = S2_04_LibFun2(2,4);

    printf("val1 is: %d\nval2 is: %d\n",val1,val2);
    return 0;
}