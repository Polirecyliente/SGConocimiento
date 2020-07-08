#!/usr/bin/python3
#   Operators

a = 5; b = 3
#T# arithmetic operators: +, -, *, /, %, **, //
ari1 = a + b
ari1 = a - b
ari1 = a * b
ari1 = b/a
ari1 = b % a
ari1 = a ** b
ari1 = b//a # floor division

#T# relational operators: ==, !=, >, <, >=, <=
rel1 = (a == b)
rel1 = (a != b)
rel1 = (a > b)
rel1 = (a < b)
rel1 = (a >= b)
rel1 = (a <= b)

#T# assignment operators: =, +=, -=, *=, /=, %/, **=, //=
asg1 = a
asg1 += a
asg1 -= a
asg1 *= a
asg1 /= a
asg1 %= a
asg1 **= a
asg1 //= a

b1 = 0x00C98011; b2 = 0x00362057
#T# bitwise operators: &, |, ^, ~, <<, >>
bit1 = b1 & b2
bit1 = b1 | b2
bit1 = b1 ^ b2
bit1 = ~b1
bit1 = b1 << 4
bit1 = b1 >> 4

l1 = True; l2 = False
#T# logical operators: and, or, not
log1 = (l1 and l2)
log1 = (l1 or l2)
log1 = (not l2)

list1 = ['memb1','memb3','memb4']
#T# membership operators: in, not in
mem1 = 'memb3' in list1
mem1 = 'memb2' not in list1

b1 = 7; b2 = 7
#T# identity operators (compares id() of variables): is, is not
ide1 = (b1 is b2)
ide1 = (b1 is not b2)