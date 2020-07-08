/*
    File input output
*/

#include <stdio.h>

int main ()
{
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
    char s2[20], s3[20];
    fgets(s2,20,file1);
    fscanf(file1,"%s",s3);
    fclose(file1);
    printf("c2:%c\ns2:%s\ns3:%s\n",c2,s2,s3);
    return 0;
}