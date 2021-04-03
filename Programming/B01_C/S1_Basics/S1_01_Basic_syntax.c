/*
	Basic syntax
*/

//T// Contents
//T// Basic syntax
//T// Variables, constants, literals

//T// compile any C file /path/to/file1.c in a terminal with
// gcc /path/to/file1.c -o /path/to/exec1
//T// run the compiled executable in a terminal with
// /path/to/exec1

//T// include directive
#include <stdio.h>

//T// define directive
#define LENGTH1 10

//T// main function, (), {}
int main ()
{
//T// int, identifiers, ",", ";"
	int a,b,c;

//T// =, 0x, 0octal, u, +
	a = 0x5p-2,b = 03u,c = a + b;

//T// printf, escapes \n and modifiers %d
	printf("Hello World!\nNum:%d\n",c);

//T// Variables, constants, literals

//T// const keyword
    const int LENGTH2 = 5;

//T// return keyword
	return 0;
}