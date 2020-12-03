
#   Sympy

#T# Table of contents

#C# Basic usage
#C# Data types
#C# --- Numeric constants

#T# Beginning of content

#C# Basic usage

# |-------------------------------------------------------------
#T# the sympy package is a CAS (Computer Algebra System)
import sympy

#T# create a symbol for a variable with the Symbol constructor
var1 = sympy.Symbol('x') #| the string arg can be more than one char in length
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

#T# the subs function is used to substitute symbols and expressions for other symbols and expressions

# SYNTAX expr1.subs(expr2, expr3)
#T# expr1 is the expression in which the substitution takes place, expr2 and expr3 can be single symbols or any expression, each instance of expr2 will be substituted by expr3

#T# if expr2 is a symbol and expr3 is a number, expr2 is replaced with the value expr3 and the result is simplified

var1 = sympy.Symbol('x')
var2 = sympy.Symbol('y')
var3 = sympy.Symbol('z')
expr1 = var1 + var2                      # x + y
expr2 = expr1.subs(var1 + var2, var3)    # z
expr2 = expr1.subs(var1, var2 + var3)    # 2*y + z
int1 = expr1.subs(var1, 3).subs(var2, 4) # 7

#T# to substitute several variables for numeric values in a single function, the evalf function can be used

# SYNTAX expr1.evalf(subs = {var1:val1, var2:val2})
#T# the subs kwarg receives a dictionary of symbols of variables mapped to numeric values, each variable is replaced with each value, up to varN:valN

var1 = sympy.Symbol('x')
var2 = sympy.Symbol('y')
expr1 = var1 + var2                         # x + y
int1 = expr1.evalf(subs = {var1:3, var2:4}) # 7.00000000000000

#T# when a variable must be substituted with several values, it may be better to create a function, this is done with the lambdify function, it creates anonymous functions in the way of the lambda keyword

# SYNTAX sympy.lambdify(list1, expr1)
#T# this returns a function, expr1 is the expression being converted into a function, list1 is a list that contains the variables in expr1, each variable will be treated as an argument in the returned function

var1 = sympy.Symbol('x')
var2 = sympy.Symbol('y')
expr1 = var1 + var2 # x + y
func1 = sympy.lambdify([var1, var2], expr1) # <function _lambdifygenerated at 0x7f870a79d940>
int1 = func1(3, 4)  # 7

#T# regular strings can be converted to sympy expressions with the sympify function

# SYNTAX sympy.sympify(str1)
#T# str1 should contain any valid sympy expression

var1 = sympy.Symbol('x')
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

#T# rational numbers are created with the Rational constructor, it admits fractions and float numbers
num1 = sympy.Rational(3/4)   # 3/4
num1 = sympy.Rational('0.2') # 1/5

#T# the Rational constructor can also create rational numbers with the following syntax

# SYNTAX sympy.Rational(num1, num2)
#T# num1 is the numerator, num2 is the denominator

num1 = sympy.Rational(5, 2) # 5/2

#T# the p, q attributes of a rational number contain the numerator and the denominator respectively
num1 = sympy.Rational(5, 2)
int1 = num1.p # 5
int1 = num1.q # 2

#T# the Integer constructor accepts integer numbers, but also rational and float numbers
int1 = sympy.Integer(3.7) # 3
int1 = sympy.Integer(5/2) # 2

#C# --- Numeric constants

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