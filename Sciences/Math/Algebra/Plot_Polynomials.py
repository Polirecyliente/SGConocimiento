import argparse

import matplotlib.pyplot as plt
import numpy as np
import sympy

def main():
    """
    This program graphs the polynomial in the first argument, with x
    between the second and third arguments. Only recognizes the variable x.
"""
    parser = argparse.ArgumentParser()
    parser.add_argument("alg_expr",help="alg_expr for algebraic expression, this string is the polynomial to graph, e.g. 'x**2-10*x' including quotes")
    parser.add_argument("min_x",type=int,help="min_x for minimum x value, it's an integer")
    parser.add_argument("max_x",type=int,help="max_x for maximum x value, it's an integer")
    args = parser.parse_args()

    alg_expr = args.alg_expr
    min_x = args.min_x
    max_x = args.max_x

    plotPoly(alg_expr,min_x,max_x)

def plotPoly(alg_expr,min_x,max_x):
    alg_expr = sympy.Poly(alg_expr)
    xVals = np.linspace(min_x,max_x)
    yVals = []
    for xi in xVals:
        yVals.append(alg_expr.subs('x',xi))
    
    plt.plot(xVals,yVals)
    plt.show()

    return

if __name__ == '__main__':
    main()