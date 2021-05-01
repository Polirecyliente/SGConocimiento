/*
    Functions
*/

//T// Contents
//T// Functions
//T// varargs
//T// Recursion

//T// include the stdarg.h header to be able to use list of args
#include <stdarg.h>
#include <stdio.h>

//T// function declaration
char chpint(char *, int);

//T// varargs

//T// varargs means variable arguments, which is a feature of functions

//T// create a function with a variable number of arguments, first arg is an int with the arg count, second arg indicates the actual arguments with an ellipsis
void varArgsFunc1(int func_argc, ...)
{
//T// define a variable of type va_list to store args
    va_list varArgsList;

//T// start the list of args with va_start()
    va_start(varArgsList,func_argc);

    for(int i = 0;i < func_argc;i++)
    {
//T// va_arg() access each arg in the list specifying their type
        printf("argument %d is %s\n",i,va_arg(varArgsList,char*));
    }

//T// clean memory from the arguments with va_end()
    va_end(varArgsList);

}

//T// Recursion

//T// define a recursive function
int recursiveF1(int n1)
{
//T// the first part of the recursion executes
    printf("Recursion Pre-iteration\n");

//T// an exit condition is given to avoid an infinite loop
    if (n1 <= 1) return 1;

//T// the function calls itself
    int retV = n1 * recursiveF1(n1 - 1);

//T// the last part of the recursion executes
    printf("Recursion Post-iteration\n");
    return retV;
}

int main()
{
    char ch1 = 'A', ch2;
    int i1 = 12;
    ch2 = chpint(&ch1,i1);
    printf("ch2:%1$c\nch1:%2$c\n",ch2,ch1);

//T// call the defined function with the first arg always the arg count
    varArgsFunc1(3,"str1","Second2","last");

//T// call the recursive function
    int a1 = recursiveF1(4);
    printf("\nResult is %d\n",a1);


    return 0;
}

//T// function definition, call by ref, by val
char chpint(char *c, int i)
{
    char ret = *c + i;
    *c = 'H';
    return ret;
}

// functions can be declared and called, before being defined