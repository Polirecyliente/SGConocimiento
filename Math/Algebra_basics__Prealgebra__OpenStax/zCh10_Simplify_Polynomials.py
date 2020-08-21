import argparse
import sympy

def main():
    """
    This program simplifies an algebraic expression passed to the command line.
    It removes parentheses and adds like terms.
"""
    parser = argparse.ArgumentParser()
    parser.add_argument("alg_expr",help="alg_expr for algebraic expression, it's a string with the polynomial to simplify, e.g. '(x+4*x**2)*(3*x**3+7*x)' don't forget the quotes around. If correct it should output 12*x**5 + 3*x**4 + 28*x**3 + 7*x**2")

    args = parser.parse_args()
    alg_expr = args.alg_expr
    alg_expr = sympyPolyWrapper(alg_expr)
    print("The algebraic expression is:",alg_expr)
    
def sympyPolyWrapper(alg_expr):
    return sympy.Poly(alg_expr)

if __name__ == '__main__':
    main()