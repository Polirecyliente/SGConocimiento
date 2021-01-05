#T# the following code shows how to create a logical negation

#T# to create a logical negation, the sympy package is used
import sympy

#T# create the symbol that will be negated
p = sympy.Symbol('p')

#T# create the logical negation
expr1 = ~p           # ~p
expr2 = sympy.Not(p) # ~p