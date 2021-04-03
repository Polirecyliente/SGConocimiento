#T# the following code shows how to create a biconditional statement

#T# to create a biconditional statement, the sympy package is used
import sympy

#T# create the symbols that represent the logical statements
p = sympy.Symbol('p')
q = sympy.Symbol('q')

#T# create the biconditional statement, a biconditional statement can be seen as a conditional statement and its converse
expr1 = (p >> q) & (q >> p) # (Implies(p, q)) & (Implies(q, p))