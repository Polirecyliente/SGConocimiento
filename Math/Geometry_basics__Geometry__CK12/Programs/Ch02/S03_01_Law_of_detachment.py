#T# the following code shows how to apply the law of detachment from propositional logic

#T# to apply the law of detachment from propositional logic, the sympy package is used
import sympy

#T# create the symbols that represent the logical statements
p = sympy.Symbol('p') #| antecedent
q = sympy.Symbol('q') #| consequent

#T# apply the law of detachment
expr1 = p >> q #| conditional statement
expr1.subs(p, True) # q #| the result is the consequent