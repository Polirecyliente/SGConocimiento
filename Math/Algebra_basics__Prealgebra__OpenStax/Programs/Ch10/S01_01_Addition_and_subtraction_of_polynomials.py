#T# the following code shows how to add and subtract polynomials

#T# to do addition and subtraction of polynomials, the sympy package is used
import sympy

#T# create the variables of the polynomials
x = sympy.Symbol('x') # x
y = sympy.Symbol('y') # y

#T# create two polynomials to add and subtract
P1 = 3*x**2*y + 5*x*y + 4*y**2 + 9
P2 = 7*x**2*y + 8*x*y + 2*y**2 + 12

#T# add and subtract with them directly
P3 = P1 + P2
#  10*x**2*y + 13*x*y + 6*y**2 + 21
P3 = P1 - P2
#   -4*x**2*y - 3*x*y + 2*y**2 - 3