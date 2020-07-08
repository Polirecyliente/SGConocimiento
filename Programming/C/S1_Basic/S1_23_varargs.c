/*
    varargs
*/

//T// functions with variable arguments

#include <stdio.h>

//T// include the stdarg.h header to be able to use list of args
#include <stdarg.h>

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

int main()
{
//T// call the defined function with the first arg always the arg count
    varArgsFunc1(3,"str1","Second2","last");
    return 0;
}