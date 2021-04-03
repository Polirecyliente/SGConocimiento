#T# the following code shows how to get the greatest common factor of two expressions

#T# to find the greatest common factor of two expressions, the sympy package is used
import sympy

#T# create the variable of the expressions
x = sympy.Symbol('x')           # x

#T# create the expressions whose greatest common factor wants to be found
expr1 = 3*x**2 + 6*x            # 3*x**2 + 6*x
expr2 = 9*x                     # 9*x

#T# the gcd function of the sympy package calculates the greatest common factor of two expressions
expr3 = sympy.gcd(expr1, expr2) # 3*x