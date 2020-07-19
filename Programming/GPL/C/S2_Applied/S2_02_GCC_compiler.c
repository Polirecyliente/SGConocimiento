/*
    GCC compiler
*/

//T// create an executable from a source code with the gcc command, the -o kwarg for output, takes the output filename as argument
// gcc sourceFile.c -o execFile

//T// to save the intermediate files: source code (.c), preprocessed (.i), assembly (.s), object code (.o), and executable, use the -save-temps flag
// gcc -save-temps sourceFile.c -o execFile

//T// preprocess a source code (.c) to (.i) with the -E flag
// gcc -E sourceFile.c -o preprocFile.i

//T// compile up to assembly language (.s) with the -S flag
// gcc -S sourceFile.c -o assemblyFile.s

//T// compile up to object code (.o) with the -c flag,
// gcc -c sourceFile.c -o objFile.o

//T// shared libraries

//T// compile the object files for a shared library with the -fPIC flag, -fPIC stands for Position Independent Code
// gcc -fPIC -c libraryFuncs1.c
// gcc -fPIC -c libraryFuncs2.c

//T// compile a shared library object with the -shared flag
// gcc -shared -o libNewFuncs.so libraryFuncs1.o libraryFuncs2.o

//T// compile an executable that uses a custom .so file with the -L/path/to/custom/libDir and -llibraryName kwargs
// gcc -o execFile sourceFile.c -L. -lNewFuncs

//T// set the environment variable LD_LIBRARY_PATH to include the path to the directory of the custom library, in bash it would be
// export LD_LIBRARY_PATH=/path/to/custom/libDir:${LD_LIBRARY_PATH}

//T// see the symbol table from an object file with nm objFile.o
// nm objFile.o

//T// compile to 32bit executables with the -m32 flag
// gcc -m32 sourceFile.c -o execFile

#include <stdio.h>

int main(void)
{
    printf("Hello, world!\n");
    return 0;
}