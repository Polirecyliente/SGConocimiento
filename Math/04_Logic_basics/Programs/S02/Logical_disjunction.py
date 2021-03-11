#T# the following code shows how to create a logical disjunction

#T# to create a logical disjunction, the sympy package is used
import sympy

#T# create the symbols that represent the logical statements
p = sympy.Symbol('p')
q = sympy.Symbol('q')

#T# create a logical disjunction between p and q
expr1 = p | q          # p | q
expr2 = sympy.Or(p, q) # p | q