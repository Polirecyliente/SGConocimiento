/*
    Structures
*/

#include <stdio.h>
#include <string.h>

//T// structure with tag
struct Books
{
    char title[50];
    int book_id;
};
//T// structure as parameter
void printBook(struct Books bookParam)
{
    printf("Title:%s\nID:%d\n",bookParam.title,bookParam.book_id);
}

int main()
{
//T// structure without tag
    struct
    {
        char t[3];
        int b;
    } x1 = {'f',5} , x2 = {'s',10};

//T// member assignment
    struct Books Book1, Book2;
    strcpy(Book1.title, "book1TitleString");
    Book1.book_id = 5;

//T// pointers to structures
    struct Books *P1;
    P1 = &Book1;
    strcpy(P1->title,"modifiedstring");
    printBook(Book1);
    return 0;
}