
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
#T# addition operation
num1 = a + b  # 8
#T# subtraction operation
num1 = a - b  # 2
#T# multiplication operation
num1 = a * b  # 15
#T# division operation
num1 = b/a    # 0.6
#T# modulo operation
num1 = b % a  # 3
#T# exponentiation operation
num1 = a ** b # 125
#T# floor division operation
num1 = b//a   # 0
#T# the floor division b//a returns the floor of b/a

#T# Relational operators

#T# equality operator
bool1 = (a == b) # False
#T# not equal operator
bool1 = (a != b) # True
#T# greater than operator
bool1 = (a > b)  # True
#T# less than operator
bool1 = (a < b)  # False
#T# greater than or equal to operator
bool1 = (a >= b) # True
#T# less than or equal to operator
bool1 = (a <= b) # False

#T# Assignment operators

#T# equals operator
num1 = a        # 5
#T# plus equals operator
num1 += a       # 10
#T# minus equals operator
num1 -= a       # 5
#T# times equals operator
num1 *= a       # 25
#T# divided by equals operator
num1 /= a       # 5.0
#T# modulo equals operator
num1 %= (a - 2) # 2.0
#T# raised to equals operator
num1 **= a      # 32.0
#T# floor divided by equals operator
num1 //= a      # 6.0

#T# Bitwise operators

a =  0b00000000110010011000000000010001 # is 0x00C98011 or 13205521
b =  0b00000000001101100010000001010111 # is 0x00362057 or 03547223
#T# and operator
#T#  0b00000000000000000000000000010001
num1 = a & b
#T# or operator
#T#  0b00000000111111111010000001010111
num1 = a | b
#T# xor operator
#T#  0b00000000111111111010000001000110
num1 = a ^ b
#T# not operator
#T# -0b00000000110010011000000000010010
num1 = ~a
#T# left shift operator
#T#  0b00001100100110000000000100010000
num1 = a << 4
#T# right shift operator
#T#  0b00000000000011001001100000000001
num1 = a >> 4

#T# Ternary operator

#T# use the ternary operator to assign one of two values to a variable depending on a condition
# var1 = val_true1 if condition1 else val_false1
#T# val_true1 is the value assigned if condition1 is true, otherwise the value assigned is val_false1
num1 = 5 if a > b else "retV" # 5
#T# the result is 5 since a is greater than b

#T# Logical operators

a = True; b = False
#T# logical and operator
bool1 = (a and b) # False
#T# logical or operator
bool1 = (a or b)  # True
#T# logical not operator
bool1 = (not b)   # True

#T# Membership operators

list1 = ['memb1','memb3','memb4']
#T# in operator
bool1 = 'memb3' in list1     # True
#T# not in operator
bool1 = 'memb2' not in list1 # True

#T# Identity operators

a = 7; b = 7
#T# is operator
bool1 = (a is b)     # True
#T# is not operator
bool1 = (a is not b) # False

#T# Operators over variables

#T# assign the same value to several variables
int1 = int2 = int3 = a # 7

#T# assign a different value to each variable with a tuple at each side
int1, int2, int3 = 72, 12, 55

#T# walrus operator :=, assigns and returns value
int2 = 5 if (int1 := int3) > 100 else int2 # 12
#T# int1 is 55, the value of int3

#T# delete statement
del int1, int2, int3