#T# the following code shows how to multiply polynomials

#T# to multiply polynomials, the sympy package is used
import sympy

#T# create the variable of the polynomials
x = sympy.Symbol('x') # x

#T# create two polynomials to multiply
P1 = x**2 + 3*x + 2
P2 = 5*x + 6

#T# the expand function of the sympy package is used to do polynomial multiplication, it expands the product of polynomials and combines like terms
P3 = sympy.expand(P1*P2)
# 5*x**3 + 21*x**2 + 28*x + 12