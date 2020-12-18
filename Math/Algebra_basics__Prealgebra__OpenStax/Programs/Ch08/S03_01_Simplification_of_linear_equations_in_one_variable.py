#T# linear equations in one variable contain only one variable and its exponent is 1, said variable can be repeated accross several different terms

#T# to simplify linear equations in one variable, the sympy package is used
import sympy

#T# the simplify function is used to simplify linear equations in one variable
x = sympy.Symbol('x')              # x
eq1 = sympy.Eq(6*x - 11, -3*x + 7) # Eq(6*x - 11, 7 - 3*x)
eq2 = sympy.simplify(eq1)          # Eq(x, 2)
#| when simplifying a linear equation in one variable, the simplification incidentally solves for the variable, the solution in this case is x = 2