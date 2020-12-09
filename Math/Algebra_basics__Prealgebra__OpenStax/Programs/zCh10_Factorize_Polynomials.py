import argparse

# TODO gcd

import sympy as sp

def main():
    """
    This program attempts to factorize the polynomial fed to it.
"""
    parser = argparse.ArgumentParser()
    parser.add_argument("alg_expr",help="alg_expr for algebraic expression, it's the string with the polynomial to factorize, e.g. 'x**2 - 10*x' including quotes")
    args = parser.parse_args()

    alg_expr = args.alg_expr

    print("The factorized polynomial is:",factorizePoly(alg_expr))

def factorizePoly(alg_expr):
    facPoly = sp.factor(alg_expr)
    return facPoly

if __name__ == '__main__':
    main()