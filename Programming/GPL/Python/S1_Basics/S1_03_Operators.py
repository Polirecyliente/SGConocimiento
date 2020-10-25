
#   Operators

#T# Table of contents

#C# Arithmetic operators
#C# Relational operators
#C# Assignment operators
#C# Bitwise operators
#C# Ternary operator
#C# Logical operators
#C# Membership operators
#C# Identity operators
#C# Operators over variables

#T# Beginning of content

#C# Arithmetic operators

# |-------------------------------------------------------------
#T# addition operation
a = 5; b = 3
num1 = a + b  # 8

#T# subtraction operation
a = 5; b = 3
num1 = a - b  # 2

#T# multiplication operation
a = 5; b = 3
num1 = a * b  # 15

#T# division operation
a = 5; b = 3
num1 = b/a    # 0.6

#T# modulo operation
a = 5; b = 3
num1 = b % a  # 3

#T# exponentiation operation
a = 5; b = 3
num1 = a ** b # 125

#T# floor division operation
a = 5; b = 3
num1 = b//a   # 0
#T# the floor division b//a returns the floor of b/a
# |-------------------------------------------------------------

#C# Relational operators

# |-------------------------------------------------------------
#T# equality operator
a = 5; b = 3
bool1 = (a == b) # False

#T# not equal operator
a = 5; b = 3
bool1 = (a != b) # True

#T# greater than operator
a = 5; b = 3
bool1 = (a > b)  # True

#T# less than operator
a = 5; b = 3
bool1 = (a < b)  # False

#T# greater than or equal to operator
a = 5; b = 3
bool1 = (a >= b) # True

#T# less than or equal to operator
a = 5; b = 3
bool1 = (a <= b) # False
# |-------------------------------------------------------------

#C# Assignment operators

# |-------------------------------------------------------------
#T# equals operator
num1 = 0; a = 5
num1 = a   # 5

#T# plus equals operator
num1 = 5; a = 5
num1 += a  # 10

#T# minus equals operator
num1 = 10; a = 5
num1 -= a  # 5

#T# times equals operator
num1 = 5; a = 5
num1 *= a  # 25

#T# divided by equals operator
num1 = 25; a = 5
num1 /= a  # 5.0

#T# modulo equals operator
num1 = 5; a = 3
num1 %= a  # 2.0

#T# raised to equals operator
num1 = 2; a = 5
num1 **= a # 32.0

#T# floor divided by equals operator
num1 = 32; a = 5
num1 //= a # 6.0
# |-------------------------------------------------------------

#C# Bitwise operators

# |-------------------------------------------------------------
#T# and operator
a =  0b00000000110010011000000000010001 # is 0x00C98011 or 13205521
b =  0b00000000001101100010000001010111 # is 0x00362057 or 03547223
#    0b00000000000000000000000000010001
num1 = a & b

#T# or operator
a =  0b00000000110010011000000000010001 # is 0x00C98011 or 13205521
b =  0b00000000001101100010000001010111 # is 0x00362057 or 03547223
#    0b00000000111111111010000001010111
num1 = a | b

#T# xor operator
a =  0b00000000110010011000000000010001 # is 0x00C98011 or 13205521
b =  0b00000000001101100010000001010111 # is 0x00362057 or 03547223
#    0b00000000111111111010000001000110
num1 = a ^ b

#T# not operator
a =  0b00000000110010011000000000010001 # is 0x00C98011 or 13205521
#   -0b00000000110010011000000000010010
num1 = ~a

#T# left shift operator
a =  0b00000000110010011000000000010001 # is 0x00C98011 or 13205521
#    0b00001100100110000000000100010000
num1 = a << 4

#T# right shift operator
a =  0b00000000110010011000000000010001 # is 0x00C98011 or 13205521
#    0b00000000000011001001100000000001
num1 = a >> 4
# |-------------------------------------------------------------

#C# Ternary operator

# |-------------------------------------------------------------
#T# use the ternary operator to assign one of two values to a variable depending on a condition

# SYNTAX var1 = val_true1 if condition1 else val_false1
#T# val_true1 is the value assigned if condition1 is true, otherwise the value assigned is val_false1

a = 10; b = 3
num1 = 5 if a > b else "retV" # 5
#T# the result is 5 since a is greater than b
# |-------------------------------------------------------------

#C# Logical operators

# |-------------------------------------------------------------
#T# logical and operator
a = True; b = False
bool1 = (a and b) # False

#T# logical or operator
a = True; b = False
bool1 = (a or b)  # True

#T# logical not operator
b = False
bool1 = (not b)   # True
# |-------------------------------------------------------------

#C# Membership operators

# |-------------------------------------------------------------
#T# in operator
list1 = ['memb1', 'memb3', 'memb4']
bool1 = 'memb3' in list1     # True

#T# not in operator
list1 = ['memb1', 'memb3', 'memb4']
bool1 = 'memb2' not in list1 # True
# |-------------------------------------------------------------

#C# Identity operators

# |-------------------------------------------------------------
#T# is operator
a = 7; b = 7
bool1 = (a is b)     # True

#T# is not operator
a = 7; b = 7
bool1 = (a is not b) # False
# |-------------------------------------------------------------

#C# Operators over variables

# |-------------------------------------------------------------
#T# assign the same value to several variables
a = 7
int1 = int2 = int3 = a # 7

#T# assign a different value to each variable with a tuple at each side
int1, int2, int3 = 72, 12, 55

#T# walrus operator :=, assigns and returns value
int1 = 72; int2 = 12; int3 = 55
int2 = 5 if (int1 := int3) > 100 else int2 # int1 == 55; int2 == 12; int3 == 55

#T# delete statement
del int1, int2, int3
# |-------------------------------------------------------------