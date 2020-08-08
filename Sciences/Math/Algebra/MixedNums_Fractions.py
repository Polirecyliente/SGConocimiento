import sys
import math
from decimal import Decimal

#T# import numpy for the gcd
import numpy

#T# In this file:
#T# - Function to represent a decimal number as mixed number and 
#T# as a fraction, from fractions module

#T# the fractions module allows to reduce fractions with the Fraction()
#T# constructor
from fractions import Fraction

argv = sys.argv

def main(argv):
    """Only works on positive numbers, to get the representation of a negative
    number, pass it positive here and change the sign of the answer"""
#T# if the number is a float, print its mixed number and proper or improper fraction
    numFlo = float(eval(argv[1]))
    print("Python's fractions.Fraction() mixed number and fraction representations are:",pyMixedNumAndFrac(numFlo))

def pyMixedNumAndFrac(numFlo):
    '''shallt be used on positive numbers only'''
    pyMixNumAndFrac = []
    
#T# reduce a fraction with Fraction(numerator,denominator)
#T# can alse convert a float to a fraction with Fraction(str(floatNumber))
    fracNum = Fraction(Decimal(str(numFlo))).limit_denominator()
#T# get numerator and denominator with the homonym fraction attributes
    quotient = fracNum.numerator // fracNum.denominator
    rem = fracNum.numerator % fracNum.denominator
    div = fracNum.denominator
    
    mixNum = str(quotient) + '+' + str(rem) + '/' + str(div)
    fracNum = str(fracNum)
    pyMixNumAndFrac.append(mixNum)
    pyMixNumAndFrac.append(fracNum)

    return pyMixNumAndFrac

if __name__ == '__main__':
    main(argv)