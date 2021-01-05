#T# the following code shows how to compute the truth table of a given logical statement

#T# to compute the truth table of a given logical statement, the sympy package is used
import sympy

#T# create the symbols with which to build the the logical statement whose truth table is to be computed
p = sympy.Symbol('p')
q = sympy.Symbol('q')
r = sympy.Symbol('r')

#T# create the logical statement
expr1 = p & (~q | r)

#T# create the rows of the truth table
product1 = sympy.cartes([sympy.S.true, sympy.S.false], repeat = 3)
list1 = list(product1)
# [(True, True, True),
#  (True, True, False),
#  (True, False, True),
#  (True, False, False),
#  (False, True, True),
#  (False, True, False),
#  (False, False, True),
#  (False, False, False)]

list2 = [] #| store here the rows of the truth table of the logical statement
for it1 in list1:
    list2.append(expr1.subs(dict(zip([p, q, r], it1))))

list2
# [True,
#  False,
#  True,
#  True,
#  False,
#  False,
#  False,
#  False]