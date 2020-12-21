import sympy as sp
def factorizePoly(alg_expr):
    """alg_expr for algebraic expression, it's the string with the polynomial to factorize, e.g. 'x**2 - 10*x' including quotes"""
    facPoly = sp.factor(alg_expr)
    return facPoly