/*
    typedef
*/

#include <stdio.h>
 
int main( ) 
{
//T// typedef a struct
    typedef struct
    {
        int i1;
        char c1;
    } tyst1;

//T// typedef use
    tyst1 a;
    a.i1 = 5;
    a.c1 = 'e';
   return 0;
}