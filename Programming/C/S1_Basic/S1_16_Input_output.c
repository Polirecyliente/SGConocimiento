/*
    Input output
*/

#include <stdio.h>

int main ()
{
//T// getchar() and putchar()
//T// cleaner1 to clean input stream after getchar()
    char c1, cleaner1;
    c1 = getchar();
    putchar(c1);
    while ((cleaner1 = getchar()) != EOF && cleaner1 != '\n'){}

//T// fgets() and fputs()
    char s1[15];
    fgets(s1,50,stdin);
    fputs(s1,stdout);

//T// scanf() and printf()
    int i1;
    char s2[15];
    scanf("%s%d",s2,&i1);
    printf("i1:%d\ns2:%s\n",i1,s2);
    while((cleaner1 = getchar()) != EOF && cleaner1 != '\n'){}
    return 0;
}