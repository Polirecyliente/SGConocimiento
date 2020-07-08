/*
    Referencing
*/

#include <stdio.h>

int main()
{
//T// pointer initialization
//T// create a null value with the NULL keyword
    double *p = NULL, d1=76;
    p = &d1;

//T// array of pointers
    int i1 = 5, *q[2] = {&i1,&i1};
    p++;
    q[0]--;

//T// pointer to pointer
    char *r, **pr = &r, c1 = 'h';
    r = &c1;

//T// pointer accessing
    double pd1 = p[-1], pd2 = *(p - 1);
    p--;
    *p = 5; // now d1 = 5
    p[0] = 3;
    *(p + 0) = 2;
    //r = "wjty"; // if used, all the following assignments will segfault
    *r = 'y';
    r[0] = 'm';
    *(r + 0) = 'k';
    return 0;
}