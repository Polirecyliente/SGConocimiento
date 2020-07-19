/*
    Input output
*/

#include <stdio.h>

int main ()
{
//T// getchar() and putchar()
//T// cleaner1 to clean input stream after getchar()
    char c1, cleaner1;
    printf("insert a char\n");
    c1 = getchar();
    putchar(c1);
    while ((cleaner1 = getchar()) != EOF && cleaner1 != '\n'){}

//T// fgets() and fputs()
    char s1[15];
    printf("insert a char\n");
    fgets(s1,50,stdin);
    fputs(s1,stdout);

//T// scanf() and printf()
    int i1;
    char s2[15];
    printf("insert a char, then a digit\n");
    scanf("%s%d",s2,&i1);
    printf("i1:%d\ns2:%s\n",i1,s2);
    while((cleaner1 = getchar()) != EOF && cleaner1 != '\n'){}

//T// File IO

//T// fopen(), fclose()
    char file1Path[] = "/tmp/jul/zPR/fopenF";
    FILE *file1 = fopen(file1Path,"w");
    int cloSta = fclose(file1);

//T// fputc(), fputs(), fprintf()
    file1 = fopen(file1Path,"r+");
    int c1Sta = fputc('h',file1);
    int s1Sta = fputs("Added wordings.\nMore to come.\nFinal line.",file1);
    
//T// rewind(), fgetc(), fgets(), fscanf()
//T// rewind to start reading the file at the beginning
    rewind(file1);
    int c2 = fgetc(file1);
    char s3[20], s4[20];
    fgets(s3,20,file1);
    fscanf(file1,"%s",s4);
    fclose(file1);
    printf("c2:%c\ns3:%s\ns4:%s\n",c2,s3,s4);

    return 0;
}