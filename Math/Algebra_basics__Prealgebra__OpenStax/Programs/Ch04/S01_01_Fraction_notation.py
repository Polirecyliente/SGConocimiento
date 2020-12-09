#T# fractions are nearly related to float numbers due to their non integer nature, they can be converted to and from floats

#T# fractions can also be stored as its own data type, in which the numerator and denominator are stored as integers

#T# fractions are also called rational numbers

#T# to create fractions (rational numbers), the sympy package is used
import sympy

#T# rational numbers are created with the Rational constructor, it admits a float number casted as string
num1 = sympy.Rational('3/4') # 3/4
num1 = sympy.Rational('0.2') # 1/5

#T# the Rational constructor can also create rational numbers with the following syntax

# SYNTAX sympy.Rational(num1, num2)
#T# num1 is the numerator, num2 is the denominator

num1 = sympy.Rational(5, 2) # 5/2

#T# the p, q attributes of a rational number contain the numerator and the denominator respectively
num1 = sympy.Rational(5, 2)
int1 = num1.p # 5
int1 = num1.q # 2

#T# the numerator, denominator getters of a rational number also contain the numerator and the denominator
num1 = sympy.Rational(5, 2)
int1 = num1.numerator()   # 5
int1 = num1.denominator() # 2