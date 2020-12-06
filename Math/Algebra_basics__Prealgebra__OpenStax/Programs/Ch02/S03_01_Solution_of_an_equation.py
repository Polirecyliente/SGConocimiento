#T# an equation with a variable can have a set of solutions, these solutions are the values of the variable that make the equation true

#T# to solve algebraic equations, the sympy package is used
import sympy

#T# the Eq constructor of the sympy package is used to create equations, the first argument is equal to the second
x = sympy.Symbol('x')
eq1 = sympy.Eq(11, x + 7) # Eq(11, x + 7)

#T# the solveset function of the sympy package is used to solve the equation in the first argument, for the variable in the second
eq1 = sympy.Eq(11, x + 7) # Eq(11, x + 7) #| this shows the subtraction property of equality
num1 = sympy.solveset(eq1, x) # FiniteSet(4) #| the solution is x == 11 - 7 == 4
eq1 = sympy.Eq(11, x - 7) # Eq(11, x - 7) #| this shows the addition property of equality
num1 = sympy.solveset(eq1, x) # FiniteSet(18) #| the solution is x == 11 + 7 == 18