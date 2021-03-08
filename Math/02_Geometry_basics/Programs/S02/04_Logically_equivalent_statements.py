#T# the following code shows how to check if two logical statements are logically equivalent

#T# to check if two logical statements are logically equivalent, the sympy package is used
import sympy

#T# create the symbols to create logical statements with them
p = sympy.Symbol('p')
q = sympy.Symbol('q')

#T# create two logical statements to test if they are logically equivalent
expr1 = p >> q
expr2 = q >> p #| the converse of expr1

#T# the Equivalent constructor creates a test to see if its arguments are logically equivalent to each other, to carry out the test the logical variables should be substituted for specific logical values
expr3 = sympy.Equivalent(expr1, expr2) # Equivalent(Implies(p, q), Implies(q, p))

bool1 = expr3.subs({p:True, q:True})  # True
bool2 = expr3.subs({p:False, q:True}) # False 
#| expr1 and expr2 are not equivalent in all cases, which means that they are not logically equivalent