//T// relational operators: ==, !=, >, <, >=, <=
    p = (A != B);
    p = (A > B);
    p = (A < B);
    p = (A >= B);
    p = (A <= B);
    
    _Bool q = 1, r = 0;
//T// logical operators: &&, ||, !
    p = (q && r);
    p = (q || r);
    p = !q;

    int b1 = 0x00C98011, b2 = 0x00362057, b3;
//T// bitwise operators: &, |, ^, ~, <<, >>
    b3 = b1 & b2; //0X00000011 -> 17
    b3 = b1 | b2; //0X00FFA057 -> 16752727
    b3 = b1 ^ b2; //0X00FFA046 -> 16752710
    b3 = ~b1;     //0XFF367FEE or 0xFFFFFFFFFF367FEE
                  // -> 4281761774 or 18446744073696346094
    b3 = b1 << 3; //0X064C0088 -> 105644168
    b3 = b1 >> 1; //0X0064C008 -> 6602760

//T// assignment operators: =, +=, -=, *=, /=, %=, &=, |=, ^=, <<=, >>=
    C = A + B;
    C += A;
    C -= A;
    C *= A;
    C /= A;
    C %= A;
    b3 &= b1;
    b3 |= b1;
    b3 ^= b1;
    b3 <<= 2;
    b3 >>= 2;

//T// ternary operator: ?, :
    A = p ? 12 : -12;