#T# radicals are simplified like regular expressions, but their variables must be defined in the set of real numbers for the simplification to work

#T# to simplify expressions with radicals, the sympy package is used
import sympy

#T# create the variable, it must be created as a variable in the set of real numbers using the real kwarg with a value of True
x = sympy.Symbol('x', real = True) # x

#T# the sqrt function of the sympy package returns the square root of its argument
expr1 = sympy.sqrt(x) # sqrt(x)

#T# the Pow function of the sympy package returns its first argument raised to the power of the second
num1 = 2
expr1 = sympy.Pow(x, num1) # x**2

#T# the powsimp function simplifies expressions with exponents
x = sympy.Symbol('x')     # x
y = sympy.Symbol('y')     # y
a = sympy.Rational('1/2') # 1/2
b = sympy.Rational('1/3') # 1/3
expr1 = x**a * x**b                        # x**(5/6)
expr2 = x**a * y**a                        # sqrt(x)*sqrt(y)
expr3 = sympy.powsimp(expr1)               # x**(5/6)
expr3 = sympy.powsimp(expr2, force = True) # sqrt(x*y) #| the force kwarg must be set to True to show the simplification