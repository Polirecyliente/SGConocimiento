#T# the following code shows how to make simple logical statements

#T# to make logical statements, the sympy package is used
import sympy

#T# a simple logical statement is created as a symbol
p = sympy.Symbol('p')
q = sympy.Symbol('q')

#T# the logical values True and False can be substituted into the symbols
p.subs(p, sympy.S.true)  # True
q.subs(q, sympy.S.false) # False