
#   Operators

#T# Table of contents

#C# Arithmetic operators
#C# Relational operators
#C# Assignment operators
#C# Bitwise operators
#C# Ternary operator
#C# Logical operators
#C# Grouping operators
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

#T# change sign operator (the same as the subtraction operator)
a = 5
num1 = -a     # -5

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
num1 = 0xA & 0x3 # 0x2

#T# or operator
num1 = 0xA | 0x3 # 0xB

#T# xor operator
num1 = 0xA ^ 0x3 # 0x9

#T# not operator
num1 = ~0xA # 0x5 #| the output is -0xB which is 0x5 in bits

#T# left shift operator
num1 = 0x3 << 1 # 0x6

#T# right shift operator
num1 = 0xE >> 1 # 0x7
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
bool1 = (a or b) # True

#T# logical not operator
a = False
bool1 = (not a) # True
# |-------------------------------------------------------------

#C# Grouping operators

# |-------------------------------------------------------------
#T# the basic grouping operator is the parenthesis pair ()
num1 = ((3 + 4) * 5) + 1 # 36 #| ((7) * 5) + 1 == 35 + 1
# |-------------------------------------------------------------

#C# Membership operators

# |-------------------------------------------------------------
#T# the in keyword is the basic membership operator
list1 = ['memb1', 'memb3', 'memb4']
bool1 = 'memb3' in list1     # True

#T# not in operator
list1 = ['memb1', 'memb3', 'memb4']
bool1 = 'memb2' not in list1 # True
# |-------------------------------------------------------------

#C# Identity operators

# |-------------------------------------------------------------
#T# the is keyword is the basic identity operator
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