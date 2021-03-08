#T# the following code shows how to create a logical conjunction

#T# to create a logical conjunction, the sympy package is used
import sympy

#T# create the symbols that represent the logical statements
p = sympy.Symbol('p')
q = sympy.Symbol('q')

#T# create a logical conjunction between p and q
expr1 = p & q           # p & q
expr2 = sympy.And(p, q) # p & q