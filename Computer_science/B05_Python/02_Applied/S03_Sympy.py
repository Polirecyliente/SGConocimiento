
#   Sympy

#T# Table of contents

#C# Basic usage
#C# Data types
#C# - Numeric constants
#C# Functions
#C# - Iterator creation
#C# - Equation solving
#C# - Simplification
#C# - Arithmetic
#C# - Algebra
#C# - Logic

#T# Beginning of content

#C# Basic usage

# |-------------------------------------------------------------
#T# the sympy package is a CAS (Computer Algebra System)
import sympy

#T# create a symbol for a variable with the Symbol constructor
var1 = sympy.Symbol('x') # x #| the string arg can be more than one char in length
type(var1) # <class 'sympy.core.symbol.Symbol'>

#T# expressions can be created using symbols, these are simplified by default
expr1 = var1 + var1 # 2*x

#T# several symbols can be created together with the symbols function

# SYNTAX sympy.symbols('str1, str2')
#T# str1, str2, up to strN are the created symbols, this returns a tuple containing said symbols

tuple1 = sympy.symbols('x, sym1') # (x, sym1)

# SYNTAX sympy.symbols('int1:int2')
# SYNTAX sympy.symbols('char1:char2')
#T# this creates several symbols, in the ranges between int1 and int2 - 1, or between char1 and char2, several colons can be used but their nature is different in numbers and in characters

tuple1 = sympy.symbols('3:5')    # (3, 4)
tuple1 = sympy.symbols('c:e')    # (c, d, e)
tuple1 = sympy.symbols('var3:5') # (var3, var4)
tuple1 = sympy.symbols('9:11:3') # (90, 91, 92, 100, 101, 102) #| only 9:11 has its range interpreted as such (namely (9, 10)), because the rest, in this case 3, is interpreted as :3 which is the same as 0:3 or (0, 1, 2)
tuple1 = sympy.symbols('a:c:b')  # (aa, ab, ba, bb, ca, cb) #| with characters, the fist colon is interpreted as a:c, the second is :b which is the same as a:b
tuple1 = sympy.symbols('a:cd:f') # (ad, ae, af, bd, be, bf, cd, ce, cf) #| here two ranges are interpreted, a:c and d:f

#T# A symbol with several subscripts and superscripts can be created with the following syntax.

# SYNTAX sympy.symbols('symbol1^superscript1_subscript1^superscript2_subscript2')

tuple1 = sympy.symbols('var_1:5_1:3') # (var_1_1, var_1_2, var_2_1, var_2_2, var_3_1, var_3_2, var_4_1, var_4_2)
tuple1 = sympy.symbols('var_1:5^1:3') # (var_1^1, var_1^2, var_2^1, var_2^2, var_3^1, var_3^2, var_4^1, var_4^2)

#T# the subs function is used to substitute symbols and expressions for other symbols and expressions

# SYNTAX expr1.subs(expr2, expr3)
#T# expr1 is the expression in which the substitution takes place, expr2 and expr3 can be single symbols or any expression, each instance of expr2 will be substituted by expr3

#T# if expr2 is a symbol and expr3 is a number, expr2 is replaced with the value expr3 and the result is simplified

var1 = sympy.Symbol('x')                 # x
var2 = sympy.Symbol('y')                 # y
var3 = sympy.Symbol('z')                 # z
expr1 = var1 + var2                      # x + y
expr2 = expr1.subs(var1 + var2, var3)    # z
expr2 = expr1.subs(var1, var2 + var3)    # 2*y + z
int1 = expr1.subs(var1, 3).subs(var2, 4) # 7
bool1 = var1.subs(var1, True)            # True

# SYNTAX expr1.subs(dict1)
#T# same as before, but this syntax uses the dictionary dict1 to substitute its keys for its values in expr1

var1 = sympy.Symbol('x')            # x
var2 = sympy.Symbol('y')            # y
expr1 = var1 + var2                 # x + y
int1 = expr1.subs({var1:3, var2:4}) # 7

#T# another way to substitute several variables for numeric values in a single function call, is using the evalf function

# SYNTAX expr1.evalf(subs = {var1:val1, var2:val2})
#T# the subs kwarg receives a dictionary of symbols of variables mapped to numeric values, each variable is replaced with each value, up to varN:valN

var1 = sympy.Symbol('x')                    # x
var2 = sympy.Symbol('y')                    # y
expr1 = var1 + var2                         # x + y
int1 = expr1.evalf(subs = {var1:3, var2:4}) # 7.00000000000000

#T# when a variable must be substituted with several values, it may be better to create a function, this is done with the lambdify function, it creates anonymous functions in the way of the lambda keyword

# SYNTAX sympy.lambdify(list1, expr1)
#T# this returns a function, expr1 is the expression being converted into a function, list1 is a list that contains the variables in expr1, each variable will be treated as an argument in the returned function

var1 = sympy.Symbol('x') # x
var2 = sympy.Symbol('y') # y
expr1 = var1 + var2      # x + y
func1 = sympy.lambdify([var1, var2], expr1) # <function _lambdifygenerated at 0x7f870a79d940>
int1 = func1(3, 4)  # 7

#T# regular strings can be converted to sympy expressions with the sympify function

# SYNTAX sympy.sympify(str1)
#T# str1 should contain any valid sympy expression

var1 = sympy.Symbol('x')    # x
str1 = '3*x**2 + 5*x + 20'
expr1 = sympy.sympify(str1) # 3*x**2 + 5*x + 20
int1 = expr1.subs(var1, 1)  # 28
# |-------------------------------------------------------------

#C# Data types

# |-------------------------------------------------------------
#T# float numbers are created with the Float constructor
flo1 = sympy.Float(5.3)     # 5.30000000000000

#T# the Float constructor also admits scientific notation, and creating numbers with a given amount of significant figures

# SYNTAX sympy.Float('float1Eint1', int2)
#T# float1 is a float number, int1 is the exponent of 10 that will multiply float1, they are separated with an 'E', int2 is the amount of significant figures

flo1 = sympy.Float('5.3E1')    # 53.0000000000000
flo1 = sympy.Float('5.3E1', 2) # 53.
flo1 = sympy.Float('5.8E1', 1) # 6.e+1

#T# rational numbers are created with the Rational constructor, it admits a float number casted as string
num1 = sympy.Rational('3/4') # 3/4
num1 = sympy.Rational('0.2') # 1/5

#T# the Rational constructor can also create rational numbers with the following syntax

# SYNTAX sympy.Rational(num1, num2)
#T# num1 is the numerator, num2 is the denominator

num1 = sympy.Rational(5, 2) # 5/2

#T# the p, q attributes of a rational number contain the numerator and the denominator respectively
num1 = sympy.Rational(5, 2)
int1 = num1.p # 5
int1 = num1.q # 2

#T# the numerator, denominator getters of a rational number also contain the numerator and the denominator
num1 = sympy.Rational(5, 2)
int1 = num1.numerator()   # 5
int1 = num1.denominator() # 2

#T# the Integer constructor accepts integer numbers, but also float numbers
int1 = sympy.Integer(3.7) # 3
int1 = sympy.Integer(5/2) # 2

#T# the Symbol constructor has several kwargs that determine the set of values the symbol constructed can have, these kwargs are turned on with the value True, and turned off with the value False
#T#     algebraic, the symbol admits values in the set of algebraic numbers
#T#     antihermitian, the symbol belongs to the field of antihermitian operators
#T#     commutative, the symbol is commutative with respect to multiplication
#T#     complex, the symbol admits values in the set of complex numbers
#T#     composite, the symbol admits values in the set of composite numbers
#T#     even, the symbol admits values in the set of even integers
#T#     finite, the symbol has its absolute value bounded
#T#     hermitian, the symbol belongs to the field of hermitian operators
#T#     imaginary, the symbol admits values in the set of imaginary numbers
#T#     infinite, the symbol has its absolute value arbitrarily large
#T#     integer, the symbol admits values in the set of integer numbers
#T#     irrational, the symbol admits values in the set of irrational numbers
#T#     negative, the symbol admits values in the set of negative numbers
#T#     nonnegative, the symbol admits values in the set of nonnegative numbers
#T#     nonpositive, the symbol admits values in the set of nonpositive numbers
#T#     nonzero, the symbol admits nonzero values
#T#     odd, the symbol admits values in the set of odd integers
#T#     positive, the symbol admits values in the set of positive numbers
#T#     prime, the symbol admits values in the set of prime numbers
#T#     rational, the symbol admits values in the set of rational numbers
#T#     real, the symbol admits values in the set of real numbers
#T#     transcendental, the symbol admits values in the set of transcendental numbers
#T#     zero, the symbol admits only the value 0

var1 = sympy.Symbol('x', commutative = True)
var1 = sympy.Symbol('x', complex = True)
var1 = sympy.Symbol('x', integer = True)
var1 = sympy.Symbol('x', odd = True)
var1 = sympy.Symbol('x', real = True)

#T# the Poly constructor is used to create polynomials
var1 = sympy.Symbol('x') # x
P1 = sympy.Poly(3*var1**2 + 5*var1 + 8) # Poly(3*x**2 + 5*x + 8, x, domain='ZZ')

#C# - Numeric constants

# |-----
#T# The numbers 0, 1, 1/2 have a sympy constant
num1 = sympy.S.Zero # 0
num1 = sympy.S.One  # 1
num1 = sympy.S.Half # 1/2

#T# the NaN constant stands for Not a Number
num1 = sympy.S.NaN # nan

#T# infinity is represented with a constant
num1 = sympy.S.Infinity # oo #| represents infinity

#T# the imaginary unit is square root of -1
num1 = sympy.S.ImaginaryUnit # I

#T# the boolean values True and False have sympy constants
bool1 = sympy.S.true  # True
bool1 = sympy.S.false # False
# |-----

# |-------------------------------------------------------------

#C# Functions

# |-------------------------------------------------------------
import sympy

#C# - Iterator creation

# |-----
#T# the cartes function is an alias for the product function of the itertools module which is part of the Python standard library
product1 = sympy.cartes([1, 0], repeat = 2)
list1 = list(product1) # [(1, 1), (1, 0), (0, 1), (0, 0)]
# |-----

#C# - Equation solving

# |-----
#T# the Eq constructor is used to create equations, the first argument is equal to the second
var1 = sympy.Symbol('x') # x
eq1 = sympy.Eq(11, var1 + 7) # Eq(11, x + 7)

#T# the solve function is a generic function used to solve the equation in the first argument, for the variable in the second, it returns a list with the found solutions
var1 = sympy.Symbol('x') # x
eq1 = sympy.Eq(var1**2, 9) # Eq(x**2, 9)
num1 = sympy.solve(eq1, var1) # [-3, 3]

#T# the solveset function is used to solve the equation in the first argument, for the variable in the second
var1 = sympy.Symbol('x') # x
eq1 = sympy.Eq(11, var1 + 7) # Eq(11, x + 7)
num1 = sympy.solveset(eq1, var1) # FiniteSet(4) #| the solution is x == 4

#T# the linsolve function is used to solve systems of linear equations, it takes a list of equations in the first argument, and a list of variables in the second
var1, var2 = sympy.symbols('x, y') # x, y
eq1 = sympy.Eq(11, var1 + 7)   # Eq(11, x + 7)
eq2 = sympy.Eq(3*var1, 2*var2) # Eq(3*x, 2*y)
list1 = [eq1, eq2]   # [Eq(11, x + 7), Eq(3*x, 2*y)]
list2 = [var1, var2] # [x, y]
nums1 = sympy.linsolve(list1, list2) # FiniteSet((4, 6)) #| 4 is the solution of var1, and 6 is the solution of var2
# |-----

#C# - Simplification

# |-----
#T# the simplify function is a function for general simplification, it is avoided in favor of one of the more specific simplification functions
var1 = sympy.Symbol('x')
expr1 = sympy.simplify(var1 + var1) # 2*x

#T# the ratsimp function simplifies expressions with fractions
var1 = sympy.Symbol('x') # x
expr1 = 1/(2*var1) + 7/(var1**2) # 1/(2*x) + 7/x**2
expr2 = sympy.ratsimp(expr1)     # (x + 14)/(2*x**2)

#T# the powsimp function simplifies expressions with exponents
var1 = sympy.Symbol('x') # x
var2 = sympy.Symbol('y') # y
num1 = sympy.Symbol('a') # a
num2 = sympy.Symbol('b') # b
expr1 = var1**num1 * var1**num2            # x**a*x**b
expr2 = var1**num1 * var2**num1            # x**a*y**a
expr3 = sympy.powsimp(expr1)               # x**(a + b)
expr3 = sympy.powsimp(expr2, force = True) # (x*y)**a #| the force kwarg must be set to True to show the simplification

#T# the expand function expands the product of polynomials and combines like terms
var1 = sympy.Symbol('x') # x
expr1 = var1**2 + 3*var1 + 2
expr2 = 5*var1 + 6
expr3 = sympy.expand(expr1*expr2)
# 5*x**3 + 21*x**2 + 28*x + 12

#T# the factor function expresses a polynomial as a product of its factors
var1 = sympy.Symbol('x') # x
expr1 = 3*var1**2 + 6*var1  # 3*x**2 + 6*x
expr2 = sympy.factor(expr1) # 3*x*(x + 2)

#T# the div function divides a polynomial by another, it returns a tuple with the quotient and the remainder
var1 = sympy.Symbol('x') # x
expr1 = 3*var1**2 -5*var1 + 8
expr2 = 2*var1 - 7
expr3 = sympy.div(expr1, expr2) # (3*x/2 + 11/4, 109/4)
# |-----

#C# - Arithmetic

# |-----
#T# the sqrt function returns the square root of its argument
var1 = sympy.Symbol('x') # x
expr1 = sympy.sqrt(var1) # sqrt(x)

#T# the Pow function returns its first argument raised to the power of the second
var1 = sympy.Symbol('x')      # x
num1 = 2
expr1 = sympy.Pow(var1, num1) # x**2
# |-----

#C# - Algebra

# |-----
#T# the gcd function calculates the greatest common divisor, or greatest common factor, of two expressions
var1 = sympy.Symbol('x')        # x
expr1 = 3*var1**2 + 6*var1      # 3*x**2 + 6*x
expr2 = 9*var1                  # 9*x
expr3 = sympy.gcd(expr1, expr2) # 3*x
# |-----

#C# - Logic

# |-----
#T# the logic and operator is the ampersand &
var1 = sympy.Symbol('p')
var2 = sympy.Symbol('q')
expr1 = var1 & var2 # p & q
expr1.subs({var1:sympy.S.true, var2:sympy.S.false}) # False
expr1.subs({var1:sympy.S.true, var2:sympy.S.true})  # True

#T# the And constructor is equivalent to the logic and
var1 = sympy.Symbol('p')
var2 = sympy.Symbol('q')
expr1 = sympy.And(var1, var2) # p & q

#T# the logic or operator is the vartical bar |
var1 = sympy.Symbol('p')
var2 = sympy.Symbol('q')
expr1 = var1 | var2 # p | q

#T# the Or constructor is equivalent to the logic or
var1 = sympy.Symbol('p')
var2 = sympy.Symbol('q')
expr1 = sympy.Or(var1, var2) # p | q

#T# a logical negation can be created with the ~ operator
var1 = sympy.Symbol('p')
expr1 = ~var1 # ~p

#T# the Not constructor creates a logical negation
var1 = sympy.Symbol('p')
expr1 = sympy.Not(var1) # ~p

#T# a conditional statement can be created with the >> operator
var1 = sympy.Symbol('p')
var2 = sympy.Symbol('q')
expr1 = var1 >> var2 # Implies(p, q) #| p implies q

#T# the Implies constructor creates a conditional statement
var1 = sympy.Symbol('p')
var2 = sympy.Symbol('q')
expr1 = sympy.Implies(var1, var2) # Implies(p, q) #| p implies q

#T# the Equivalent constructor creates a test to see if its arguments are logically equivalent to each other, to carry out the test the logical variables should be substituted for specific logical values
var1 = sympy.Symbol('p')
var2 = sympy.Symbol('q')
expr1 = var1 >> var2
expr2 = var2 >> var1 #| the converse of expr1
expr3 = sympy.Equivalent(expr1, expr2) # Equivalent(Implies(p, q), Implies(q, p))
bool1 = expr3.subs({var1:True, var2:True})  # True
bool2 = expr3.subs({var1:False, var2:True}) # False #| expr1 and expr2 are not equivalent in all cases, which means that they are not logically equivalent
# |-----

# |-------------------------------------------------------------