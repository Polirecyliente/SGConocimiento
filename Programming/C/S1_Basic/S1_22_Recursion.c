/*
    Recursion
*/

#include <stdio.h>

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
//T// call the recursive function
    int a1 = recursiveF1(4);
    printf("\nResult is %d\n",a1);
    return 0;
}