/*
    Loops
*/

#include <stdio.h>

int main()
{
    start:;
    int i = 0;
//T// do, while
    do
    {
        printf("i in do while costs %1$i\n",i);
        i += 1;
//T// for
        for (;i <= 12; i += 1)
        {
//T// break, continue, goto
            if (i >= 6) break;
            if (i == 4) continue;
            if (i == 10) goto start;
            printf("i in for costs %1$i\n",i);   
        }
    } while (i <= 9);
}