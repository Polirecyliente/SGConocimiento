/*
    Data types
*/

#include <stdio.h>

//T// void keyword
void fvoid1(){}

int main ()
{
//T// char, it can be unsigned but defaults to signed
    char c1 = 128;

//T// unsigned modifier
    unsigned char c2 = 128;

//T// Unicode characters, char*
    char* s1 = "\u02A0";

//T// signed modifier
    signed int i1 = 2147483648;

//T// short modifier
    short i2 = 18;

//T// long modifier
    long i3 = 14;
    long long i4 = 9;

//T// float
    float f1 = 3.1;

//T// double
    double f2 = 9.12;
    long double f3 = 0.2;
    printf("Sizes in Bytes\nInt:\t\t%1$lu\nShort \
int:\t%2$lu\n%3$s\n",

//T// sizeof()
    sizeof(int),sizeof(short),s1);

//T// Casting

    int a = 5, b = 17;
//T// cast operator (type)
    double div1 = ((double) a)/b;

    return 0;   
}