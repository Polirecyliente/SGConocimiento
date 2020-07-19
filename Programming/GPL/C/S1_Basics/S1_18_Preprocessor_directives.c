/*
    Preprocessor directives
*/

//T// #include, #define, #undef, #error, #ifdef, #ifndef, #endif, #if, defined(), #elif, #else, a few stdio.h macros
#include <stdio.h>

#define VAR_FIRST __DATE__
#undef VAR_FIRST

#ifdef VAR_FIRST
# error "Variable must not be defined"
#endif

#ifndef VAR_FIRST
    #define VAR_SEC __STDC__
#endif

#if defined(VAR_SEC) && !defined(VAR_FIRST)
    #define VAR_INS __FILE__
#elif defined(VAR_FIRST)
    #define VAR_INS __LINE__
#else
    #define VAR_INS __TIME__
#endif

//T// stringize operator #, macro continuation operator, token pasting operator ##, #pragma, function in #define
#define Z1(b1,n) printf(#b1" or a non string: %d\n",c##n)
#define Z2(x) (x * x)
#pragma pack(1)

int main ()
{
    struct st1
    {
        int i1;
        char c1;
    }a;
    
    int b = 1, c5 = 9;
    Z1(b,5);
    printf("Square of five: %d\n",Z2(5));
    
    return 0;
}