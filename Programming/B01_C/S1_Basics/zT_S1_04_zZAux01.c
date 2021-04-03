#include <stdio.h>
extern int eA;
void printExtern(int aA, int rA, int sA)
{   
    printf("auto:%d\nremote:%d\nstatic:%d\nextern:%d\n",aA,rA,sA,eA);
}