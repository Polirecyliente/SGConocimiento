/*
    Arrays
*/

#include <stdio.h>

int * dupArr2(int *);

int main()
{
//T// array initialization
    int iArr[3] = {0};
    double doubArr[] = {5.0, 3, 2.12};
    
//T// multidimensional arrays
    short sArr[][2][3] = {{{1,2,3},{1,2,3}},{{1,2,3},{1,2,3}}
    ,{{1,2,3},{1,2,3}},{{1,7,3},{1,2,3}}};
    int *a = dupArr2(iArr);
    for(int i = 0;i<3;i++) iArr[i] = a[i];
    return 0;
}
//T// array as return value and parameter in functions
int * dupArr2(int *aArr)
{
    static int inArr[3];
    inArr[2] = (aArr[2] + 3)*2;
    return inArr;
}