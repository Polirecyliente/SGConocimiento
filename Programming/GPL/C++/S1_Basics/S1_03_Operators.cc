/*
    Operators
*/

#include <iostream>
using namespace std;

int main()
{
    float f1 = 5, f2 = 7,f3;
    cout << "-|-\n";
//T// arithmetic operators
    f3 = f1 + f2;
    cout << f3 << "\n";
    f3 = f1 - f2;
    cout << f3 << "\n";
    f3 = f1*f2;
    cout << f3 << "\n";
    f3 = f1/f2;
    cout << f3 << "\n";
    f3 = (int)f2%(int)f1;
    cout << f3 << "\n";
    f3 = f1++;
    cout << f3 << "\n";
    f3 = f2--;
    cout << f3 << "\n";
    cout << f1 << " " << f2 << endl;

    cout << "-|-\n";
//T// relational operators
    bool b1 = (f1 == f2);
    cout << b1 << "\n";
    b1 = (f1 != f2);
    cout << b1 << "\n";
    b1 = (f1 > f2);
    cout << b1 << "\n";
    b1 = (f1 < f2);
    cout << b1 << "\n";
    b1 = (f1 >= f2);
    cout << b1 << "\n";
    b1 = (f1 <= f2);
    cout << b1 << endl;

    cout << "-|-\n";
    f1 = 0;
//T// logical operators
    b1 = (f1 && f2);
    cout << b1 << "\n";
    b1 = (f1 || f2);
    cout << b1 << "\n";
    b1 = !f1;
    cout << b1 << endl;

    f1 = 60, f2 = 13;
    cout << "-|-\n";
//T// bitwise operators
    f3 = (int)f1 & (int)f2;
    cout << f3 << "\n";
    f3 = (int)f1 | (int)f2;
    cout << f3 << "\n";
    f3 = (int)f1 ^ (int)f2;
    cout << f3 << "\n";
    f3 = ~(int)f1;
    cout << f3 << "\n";
    f3 = (int)f1 << 2;
    cout << f3 << "\n";
    f3 = (int)f1 >> 2;
    cout << f3 << endl;

    cout << "-|-\n";
//T// assignment operators
    f3 = f1;
    cout << f3 << "\n";
    f3 += f2;
    cout << f3 << "\n";
    f3 -= f1;
    cout << f3 << "\n";
    f3 *= 2;
    cout << f3 << "\n";
    f3 /= 13;
    cout << f3 << "\n";
    int i1 = 2;
    i1 %= 17;
    cout << i1 << "\n";
    i1 <<= 1;
    cout << i1 << "\n";
    i1 >>= 2;
    cout << i1 << "\n";
    i1 &= 2;
    cout << i1 << "\n";
    i1 ^= 4;
    cout << i1 << "\n";
    i1 |= 8;
    cout << i1 << "\n";

    cout << "-|-\n";
//T// ternary operator
    f3 = f1 > f2 ? 2*f1 : 3*f2;
    
    return 0;
}