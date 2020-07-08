/*
    Memory management
*/

#include <stdio.h>
#include <string.h>

//T// dynamic memory allocation and management functions are found in stdlib.h
#include <stdlib.h>

int main()
{
    char *strMall1;
//T// allocate memory in a given size with malloc(size), malloc(size) returns a void pointer that can be casted
    strMall1 = (char *)malloc(1*sizeof(char));

    strcpy(strMall1,"ab1ab2abcd3");
    printf("MSaved string is: %s\n",strMall1);

    char *strCall1;
//T// contiguous allocation can be done with calloc()
    strCall1 = calloc(5,sizeof(char));

    strcpy(strCall1,"cd1cd2cdef3");
    printf("CSaved string is: %s\n",strCall1);

//T// reallocate memory to a new size with realloc()
    strMall1 = realloc(strMall1,2);

    strcat(strMall1," Added characters tothe former strinZ. Added characters tothe former string. Added characters tothe former string. Added characters tothe former string. Added characters tothe former string. Added characters tothe former string. Added characters tothe former string. Added characters tothe former string.");
    printf("New string is: %s\n",strMall1);

//T// free or release memory with free()
    free(strMall1);
    printf("String after freeing is: %s\n",strMall1);
}