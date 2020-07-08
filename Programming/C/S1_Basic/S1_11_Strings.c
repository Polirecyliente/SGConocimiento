/*
    Strings
*/

#include <stdio.h>
#include <string.h>

int main()
{
//T// string as char array
    char s1[12] = "str1\u02A1", s2[] = "str2";

//T// string manipulation functions
    strcpy(s1, s2);
    strcat(s1, s2);
    int a = strlen(s1);
    s1[0] = 'a', s2[0] = 'Z';
    int b = strcmp(s1, s2);
    char c1 = 'r';
    char *A = strchr(s2,c1);
    char *s3 = "tr";
    char *B = strstr(s2,s3);
    return 0;
}