#T# the following code shows how to apply the law of syllogism from propositional logic

#T# to apply the law of syllogism from propositional logic, the sympy package is used
import sympy

#T# create the symbols that represent the logical statements
p = sympy.Symbol('p')
q = sympy.Symbol('q')
r = sympy.Symbol('r')

#T# apply the law of syllogism
expr1 = (p >> q) & (q >> r)
expr1.subs(p, True).subs(q, True) # r