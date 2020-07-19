/*
    Arrays
*/

//T// include the string library
#include <string.h>
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

//T// Strings

//T// string as char array
    char s1[12] = "str1\u02A1", s2[] = "str2";

//T// string manipulation functions
    strcpy(s1, s2);
    strcat(s1, s2);
    int a1 = strlen(s1);
    s1[0] = 'a', s2[0] = 'Z';
    int b = strcmp(s1, s2);
    char c1 = 'r';
    char *A = strchr(s2,c1);
    char *s3 = "tr";
    char *B = strstr(s2,s3);

    return 0;
}

//T// array as return value and parameter in functions
int * dupArr2(int *aArr)
{
    static int inArr[3];
    inArr[2] = (aArr[2] + 3)*2;
    return inArr;
}