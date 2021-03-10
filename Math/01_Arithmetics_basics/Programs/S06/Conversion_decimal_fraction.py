#T# floats can be converted into fractions, fractions are presented as decimals by performing the division

#T# to work with fractions, the sympy package is used
import sympy

#T# create a fraction to be converted into a float number
num1 = sympy.Rational(7, 4)      # 7/4

#T# the float representation of a fraction is the result of dividing the numerator over the denominator
num2 = num1.p/num1.q             # 1.75

#T# a float number is converted into a fraction with the Rational constructor
num3 = sympy.Rational(str(num2)) # 7/4