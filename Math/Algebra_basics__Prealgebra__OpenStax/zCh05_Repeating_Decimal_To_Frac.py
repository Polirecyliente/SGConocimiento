import sys
import math
from fractions import Fraction
from decimal import Decimal

argv = sys.argv

def main(argv):
    """Converts a repeating decimal to a fraction.

    Input the repeating decimal as two arguments: arg1 is the part you 
    want unique, and arg2 is the part you want repeated. Example usage:
    python3 Repeating_Decimal_To_Frac.py 894.57 448132653
    This represents the decimal 894.57448132653448132653448132653448132653
    If correct, it should output the fraction 2484929112311/2777777775"""

    num,den = repeDecToFrac(argv[1],argv[2])
    print("The fraction of the repeating decimal is:",Fraction(num,den))

def repeDecToFrac(unique,repe):
    """returns the numerator and denominator of the repeating decimal with
    parts unique (arg1), and repeated (arg2)"""
    unique = Decimal(unique)
    repe = Decimal(repe)
#T# uniqueDecimals is the amount of numbers after decimal point in the unique number
    uniqueDecimals = abs(unique.as_tuple().exponent)
#T# repePositions is the amount of numbers in the repeated number
    repePositions = math.floor(math.log10(repe)) + 1
    small10 = 10**uniqueDecimals
    big10 = 10**(uniqueDecimals+repePositions)
    small10unique = unique*small10
    big10unique = unique*big10+repe
    num = int(big10unique - small10unique)
    den = int(big10 - small10)

    numden = (num,den)
    return numden

if __name__ == '__main__':
    main(argv)