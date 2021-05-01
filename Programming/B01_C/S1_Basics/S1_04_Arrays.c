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

int * dupArr2(int *);

//T// array as return value and parameter in functions
int * dupArr2(int *aArr)
{
    static int inArr[3];
    inArr[2] = (aArr[2] + 3)*2;
    return inArr;
}