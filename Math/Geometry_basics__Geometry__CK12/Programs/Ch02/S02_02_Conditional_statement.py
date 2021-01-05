#T# the following code shows how to create a conditional statement

#T# to create a conditional statement, the sympy package is used
import sympy

#T# create the symbols of the conditional statement
p = sympy.Symbol('p')
q = sympy.Symbol('q')

#T# create the conditional statement, p implies q
expr1 = p >> q              # Implies(p, q)
expr2 = sympy.Implies(p, q) # Implies(p, q)