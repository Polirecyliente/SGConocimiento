#T# the following code shows how to divide polynomials

#T# to divide a polynomial by another, the sympy package is used
import sympy

#T# create the variable of the polynomials
x = sympy.Symbol('x') # x

#T# create two polynomials to divide
P1 = 3*x**2 - 5*x + 8
P2 = 2*x - 7

#T# the div function of the sympy package divides a polynomial by another, it returns a tuple with the quotient and the remainder
tuple1 = sympy.div(P1, P2) # (3*x/2 + 11/4, 109/4)