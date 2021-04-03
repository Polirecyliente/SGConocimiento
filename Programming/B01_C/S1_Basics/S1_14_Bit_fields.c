/*
    Bit fields
*/

#include <stdio.h>

int main ()
{
//T// bit field definition
    struct st1
    {
        __uint8_t i1 : 3;
        __uint8_t i2 : 5;
    };
    struct st1 a;
    
//T// bit field assignment
    a.i1 = 9; // integer overflow
    return 0;
}