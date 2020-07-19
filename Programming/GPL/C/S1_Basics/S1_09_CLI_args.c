/*
    CLI args
*/

#include <stdio.h>

int main(int argc, char* argv[])
{
//T// argv in position 0 always stores the name of the program
    printf("Program's name: %s\n",argv[0]);

//T// argc stores the arg count
    printf("The argument count is: %d\n",argc);

//T// access arguments in argv[]
    printf("First arg is: %s\n",argv[1]);
    return 0;
}