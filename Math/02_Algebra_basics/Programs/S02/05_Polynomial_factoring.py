#T# the following code shows how to do polynomial factoring

#T# to do polynomial factoring, the sympy package is used
import sympy

#T# create the variable of the polynomial
x = sympy.Symbol('x') # x

#T# create the polynomial to do polynomial factoring to it
P1 = 3*x**2 + 6*x  # 3*x**2 + 6*x

#T# the factor function of the sympy package expresses a polynomial as a product of its factors
P2 = sympy.factor(P1) # 3*x*(x + 2)