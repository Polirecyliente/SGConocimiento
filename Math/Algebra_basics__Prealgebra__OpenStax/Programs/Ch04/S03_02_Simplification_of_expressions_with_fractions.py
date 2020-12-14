#T# there are special functions to simplify expressions with fractions

#T# to simplify an expression with fractions, the sympy package is used
import sympy

#T# the ratsimp function from the sympy package, simplifies expressions with fractions
var1 = sympy.Symbol('x') # x
expr1 = 1/(2*var1) + 7/(var1**2) # 1/(2*x) + 7/x**2
expr2 = sympy.ratsimp(expr1)     # (x + 14)/(2*x**2)