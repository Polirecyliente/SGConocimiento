import matplotlib.pyplot as plt
import numpy as np
import sympy
def plotPoly(alg_expr,min_x,max_x):
    """This program graphs the polynomial in the first argument, with x between the second and third arguments. Only recognizes the variable x. alg_expr for algebraic expression, this string is the polynomial to graph, e.g. 'x**2-10*x' including quotes. min_x for minimum x value, it's an integer. max_x for maximum x value, it's an integer"""
    alg_expr = sympy.Poly(alg_expr)
    xVals = np.linspace(min_x,max_x)
    yVals = []
    for xi in xVals:
        yVals.append(alg_expr.subs('x',xi))
    plt.plot(xVals,yVals)
    plt.show()
    return