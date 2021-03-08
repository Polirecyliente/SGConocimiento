#T# complex fractions are simplified as normal, but they have a small caveat when simplified with the sympy package

#T# to simplify complex fractions, the sympy package is used
import sympy

#T# a complex fraction can't be written directly into the Rational constructor
num1 = sympy.Rational('(2/3)/(5/4)') # TypeError: invalid input: (2/3)/(5/4)
num1 = sympy.Rational('2/3/5/4')     # TypeError: invalid input: 2/3/5/4
num1 = sympy.Rational((2/3)/(5/4))   # 4803839602528529/9007199254740992 #| the value is correct, but the form is undesirable
num1 = sympy.Rational(2/3/5/4)       # 4803839602528529/144115188075855872 #| this is an undesirable form, and also the fraction value is itself wrong

#T# instead, two rational numbers should be created separately, one for the fraction in the numerator, and other for the fraction in the denominator
num1 = sympy.Rational('2/3')     # 2/3
num2 = sympy.Rational('5/4')     # 5/4
num3 = sympy.Rational(num1/num2) # 8/15