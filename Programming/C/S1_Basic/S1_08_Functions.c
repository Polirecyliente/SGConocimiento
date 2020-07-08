/*
    Functions
*/

#include <stdio.h>

//T// function declaration
char chpint(char *, int);

int main()
{
    char ch1 = 'A', ch2;
    int i1 = 12;
    ch2 = chpint(&ch1,i1);
    printf("ch2:%1$c\nch1:%2$c\n",ch2,ch1);
}
//T// function definition, call by ref, by val
char chpint(char *c, int i)
{
    char ret = *c + i;
    *c = 'H';
    return ret;
}