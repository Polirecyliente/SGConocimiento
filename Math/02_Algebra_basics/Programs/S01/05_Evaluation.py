#T# evaluation in an expression means substituting variables and constants for specific numeric values and then calculating the result

#T# to evaluate expressions, the sympy package is used
import sympy

#T# create an expression to evaluate
x = sympy.Symbol('x')
expr1 = x + 7
expr2 = 2 ** x

#T# the subs function from the sympy package is used to evaluate an expression
num1 = expr1.subs(x, 4) # 11 #| evaluates expr1 with x being 4
num1 = expr2.subs(x, 5) # 32

#T# an expression without symbols can be evaluated directly
num1 = 7 + 4 # 11

#T# an expression with more than one symbol (variable or constant) substituted can be evaluated with the evalf function
y = sympy.Symbol('y')
expr1 = 3*x + 4*y - 6
num1 = expr1.evalf(subs = {x:10, y:2}) # 32 #| 3*10 + 4*2 - 6 == 30 + 8 - 6 == 38 - 6, the subs kwarg contains a dictionary of the symbols being substituted and their values