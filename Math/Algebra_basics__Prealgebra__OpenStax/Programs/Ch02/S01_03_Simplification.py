#T# simplification is done over mathematical expressions and numbers, to show them in the most simplified manner, i.e. in their smallest size, with their smallest numbers, etcetera

#T# to simplify expressions and numbers, the sympy package is used
import sympy

#T# most expressions are simplified by default
x = sympy.Symbol('x')
expr1 = x * x * x * x * x    # x**5
expr1 = x + x * x + x        # x**2 + 2*x
num1 = sympy.Rational(18/12) # 3/2