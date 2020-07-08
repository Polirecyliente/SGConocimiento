/*
    Decision making
*/

#include <stdio.h>

int main()
{
    int a = 20;
//T// if, else if, else
    if (a < 20)
    {
        printf("Executed because a < 20\n");
    } else if (a == 20)
    {
        printf("Executed when a = 20\n");
        if (sizeof(a) == 4)
        {
            printf("a is 20 and occupies 4 bytes\n");
        }
    } else
    {
        printf("Executed when a > 20\n");
    }
    
//T// switch, case, break
    switch(a)
    {
        case 20 :
            printf("a = 20\n");
        case 21 :
            printf("... or maybe 21?\n");
            switch(sizeof(a))
            {case 4 : printf("Either case it has 4 bytes\n");}
            break;
        case 22 :
            printf("No, a is 22");
            break;
        default :
            printf("The value of a couldn't be determined");
    }
    return 0;
}