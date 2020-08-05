
#   Operators

#T# Table of contents

#T# Arithmetic operators
#T# Relational operators
#T# Assignment operators
#T# Bitwise operators
#T# Ternary operator
#T# Logical operators
#T# Membership operators
#T# Identity operators
#T# Operators over variables

#T# Beginning of content

#T# Arithmetic operators

a = 5; b = 3
num1 = a + b
num1 = a - b
num1 = a * b
num1 = b/a
num1 = b % a
num1 = a ** b
num1 = b//a # floor division

#T# Relational operators

bool1 = (a == b)
bool1 = (a != b)
bool1 = (a > b)
bool1 = (a < b)
bool1 = (a >= b)
bool1 = (a <= b)

#T# Assignment operators

num1 = a
num1 += a
num1 -= a
num1 *= a
num1 /= a
num1 %= a
num1 **= a
num1 //= a

#T# Bitwise operators

a = 0b00000000110010011000000000010001 # is 0x00C98011 or 13205521
b = 0b00000000001101100010000001010111 # is 0x00362057 or 03547223

#T#  0b00000000000000000000000000010001
num1 = a & b
#T#  0b00000000111111111010000001010111
num1 = a | b
#T#  0b00000000111111111010000001000110
num1 = a ^ b
#T# -0b00000000110010011000000000010010
num1 = ~a
#T#  0b00001100100110000000000100010000
num1 = a << 4
#T#  0b00000000000011001001100000000001
num1 = a >> 4

#T# Ternary operator

#T# in this operator, true_out1 if condition1 else false_out1, where true_out1 is the output if condition1 is true, otherwise the output is false_out1, in the following the result is 5 since a is greater than b
num1 = 5 if a > b else "retV"

#T# Logical operators

a = True; b = False
bool1 = (a and b)
bool1 = (a or b)
bool1 = (not b)

#T# Membership operators

list1 = ['memb1','memb3','memb4']
bool1 = 'memb3' in list1
bool1 = 'memb2' not in list1

#T# Identity operators

a = 7; b = 7
bool1 = (a is b)
bool1 = (a is not b)

#T# Operators over variables

#T# assign the same value to several variables
int1 = int2 = int3 = a

#T# assign a different value to each variable
int1, int2, int3 = 72, 12, 55

#T# walrus operator :=, assigns and returns value
int2 = 5 if (int1 := int3) > 100 else int2

#T# delete statement
del int1, int2, int3