/*
    Unions
*/

#include <stdio.h>
#include <string.h>

int main ()
{
//T// union definition
    union oneType
    {
        int ui;
        char us[15];
    };
//T// union initialization and assignment
    union oneType u1;
    strcpy(u1.us,"str1");
    return 0;
}