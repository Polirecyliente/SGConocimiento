/*
    Data types
*/

#include <iostream>

using namespace std;

int main()
{
    int n;
//T// sizeof()
    n = sizeof(int);

//T// characters: [signed|unsigned] char
    char a1 = 'a';
    cout << "char:" << a1 << " \t\t\t" << sizeof(char) << "B" << "\n";
    unsigned char a2 = 'c';
    cout << "unsigned char:" << a2 << " \t" 
    << sizeof(unsigned char) << "B" << "\n";
    signed char a3 = 'x';
    cout << "signed char:" << a3 << " \t\t" 
    << sizeof(signed char) << "B" << "\n";

//T// boolean: bool
    bool b1 = true;
    cout << "bool:" << b1 << " \t\t\t" << sizeof(bool) << "B" << "\n";

//T// integers: [signed|unsigned] [short|long|long long] int
    int i1 = 12;
    cout << "int:" << i1 << " \t\t\t" << sizeof(int) << "B" << "\n";
    signed short int i2 = -6;
    cout << "signed short int:" << i2 << " \t" 
    << sizeof(signed short int) << "B" << "\n";
    unsigned long int i3 = 72;
    cout << "unsigned long int:" << i3 << " \t"
    << sizeof(unsigned long int) << "B" << "\n";
    long long int i4 = 999;
    cout << "long long int:" << i4 << " \t" 
    << sizeof(long long int) << "B" << "\n";

//T// floating point: float, [long] double
    float f1 = 5.1;
    cout << "float:" << f1 << " \t\t" << sizeof(float) << "B" << "\n";
    double f2 = 10.2;
    cout << "double:" << f2 << " \t\t" << sizeof(double) << "B" << "\n";
    long double f3 = 20.4;
    cout << "long double:" << f3 << " \t" 
    << sizeof(long double) << "B" << "\n";

    wchar_t wc1 = 'l';
    cout << "wchar_t:" << wc1 << " \t\t" << sizeof(wchar_t) << "B" << endl;

//T// type definition: typedef
    typedef int centimeters;
    centimeters measure1;

//T// enumerated type: enum
    enum label_t {label1 = 1031,label2,label3,label4};
    label_t lbl1 = label4;

//T// array syntax
    double arr1[] = {5.12 , 4.12 , 29.1};
    arr1[2] = 31.9;
    cout << "arr el2 is " << arr1[1] << "\n";

//T// multidimensional arrays
    int arr2[3][5];
    int arr3[3][2] = {{3,2},{1,4},{5,5}};

    return 0;
}