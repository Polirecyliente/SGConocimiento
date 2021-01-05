#T# the following code shows how to apply the law of contrapositive from propositional logic

#T# to apply the law of contrapositive from propositional logic, the sympy package is used
import sympy

#T# create the symbols that represent the logical statements
p = sympy.Symbol('p') #| antecedent
q = sympy.Symbol('q') #| consequent

#T# apply the law of contrapositive
expr1 = p >> q
expr1.subs(q, False) # ~p