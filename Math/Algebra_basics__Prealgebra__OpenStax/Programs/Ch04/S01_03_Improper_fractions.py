#T# improper fraction can be converted to and from mixed numbers

#T# to work with improper fractions and mixed numbers, the sympy package is used
import sympy

#T# create an improper fraction with the Rational constructor
num1 = sympy.Rational(7, 4) # 7/4

#T# the p, q attributes of a rational number contain the numerator and the denominator respectively
int1 = num1.p # 7 #| numerator
int2 = num1.q # 4 #| denominator

#T# to convert an improper fraction into a mixed number, the quotient as an integer and the remainder must be calculated
int3 = int1 // int2 # 1 #| quotient
int4 = int1 % int2  # 3 #| remainder

#T# a mixed number is written as quotient remainder/denominator
str1 = f'{int3} {int4}/{int2}'               # '1 3/4'

#T# to convert a mixed number into an improper fraction, the quotient is added to remainder/denominator
num2 = int3 + int4/int2                      # 1.75
num2 = sympy.Rational(str(int3 + int4/int2)) # 7/4