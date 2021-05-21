/*
    Headers
*/

//T// include local headers
#include <stdio.h>
#include "S1_19_zZAux01.h"

int main(void)
{
    puts(str1);
    return 0;
}

// #T# Headers can be compiled like regular source code files, the compiled header has the file extension `.gch`. This makes a difference when a header includes a header that includes a header and so on. The compiled header already has its headers included in it.
// # SYNTAX gcc header1.h -o header1.h.gch