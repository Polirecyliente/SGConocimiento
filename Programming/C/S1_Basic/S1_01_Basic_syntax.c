/*
	Basic syntax
*/

//T// include directive
#include <stdio.h>

//T// main function, (), {}
int main ()
{
//T// int, identifiers, ",", ";"
	int a,b,c;

//T// =, 0x, 0octal, u, +
	a = 0x5p-2,b = 03u,c = a + b;

//T// printf, escapes \n and modifiers %d
	printf("Hello World!\nNum:%d\n",c);

//T// return keyword
	return 0;
}