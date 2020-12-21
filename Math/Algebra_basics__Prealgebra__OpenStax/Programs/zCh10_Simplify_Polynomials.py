import sympy
def sympyPolyWrapper(alg_expr):
    """This program simplifies an algebraic expression passed to the command line It removes parentheses and adds like terms. alg_expr for algebraic expression, it's a string with the polynomial to simplify, e.g. '(x+4*x**2)*(3*x**3+7*x)' don't forget the quotes around. If correct it should output 12*x**5 + 3*x**4 + 28*x**3 + 7*x**2"""
    return sympy.Poly(alg_expr)