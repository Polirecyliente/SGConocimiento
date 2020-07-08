/*
    Error handling
*/

#include <stdio.h>

//T// header with errno, perror()
#include <errno.h>

//T// header with strerror()
#include <string.h>

//T// header with EXIT_SUCCESS and EXIT_FAILURE
#include <stdlib.h>

//T// implement errno
extern int errno;

int main()
{
    FILE *f1;
    f1 = fopen("nofile","r");
    if (f1 == NULL)
    {
//T// call perror(), strerror(errno)
        perror("Print from perror()");
        fprintf(stderr,"Contents of strerror(errno) %s\n",strerror(errno));

//T// return EXIT_FAILURE on failure
        return EXIT_FAILURE;
    }
    else
    {
        fclose(f1);
    }
    
//T// return EXIT_SUCCESS on success
    return EXIT_SUCCESS;
}