import sys

#T# sympy is an API that allows to solve equations, among other things
import sympy

argv = sys.argv

def main(argv):
    """If used with an argument attempt to solve. With several, take the
    first as the equation, and the rest as values to evaluate. In eval,
    only the left hand side expression will be evaluated."""
    if len(argv) == 1:
        print(
f"""
{__file__} can be used to eval an expression, or solve an equation for an
'x' variable. Only 'x' is understood. No spaces allowed in the expression
or equation.

For evaluating an expression:
Usage: python3 {__file__} expr val1 [val2] [valN]
Example: python3 {__file__} 3*x+7 4
This evaluates to 19, since 3*4+7 = 19

For solving an equation:
Usage: python3 {__file__} lhs=rhs
Example: python3 {__file__} 3*x+7=19
This solves x = 4
""",file=sys.stderr)
        exit(1)

    exprss = argv[1].split('=')
    if len(exprss) == 2:
        lhs_expr = exprss[0]
        rhs_expr = exprss[1]
    elif len(exprss) == 1:
        lhs_expr = exprss[0]
#T# evaluate all args after eq or expr
    if len(argv) > 2:
        vals = argv[2:]
        print("Evaluation(s) of the expression:",evalVals(lhs_expr,vals))
    if len(argv) == 2:
        print("Solution to the equation is:",solveEq(lhs_expr,rhs_expr))

def evalVals(expr,vals):
#T# parse string as expression with sympify(strExpression)
    expr = sympy.sympify(expr)
#T# use expression1.subs('var1',numberEvaled) to evaluate expression1 by
#T# substition of numberEvaled in var1
    evals = [expr.subs('x',vals[i1]) for i1 in range(0,len(vals))]
    return evals

def solveEq(lhs_expr,rhs_expr):
    lhs_expr = sympy.sympify(lhs_expr)
    rhs_expr = sympy.sympify(rhs_expr)
#T# use Eq(lhs,rhs) to create an equation where lhs = rhs
    eq = sympy.Eq(lhs_expr,rhs_expr)
#T# solve the equation eq1 with respect to var1 with solve(eq1,var1)
    soluc = sympy.solve(eq,'x')
    return soluc
    

if __name__ == '__main__':
    main(argv)