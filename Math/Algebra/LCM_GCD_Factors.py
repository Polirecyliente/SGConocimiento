import sys
import math
import subprocess

#T# In this file:
#T# - Function to calculate the least common multiple (LCM), from API numpy
#T# - Function to calculate the greatest common divisor (GCD), from API numpy
#T# - Function to calculate prime factors, from GNU lib
#T# - Function to calculate all pairs of factors of a number (own)

#T# numpy is a library to find least common multiple (LCM), and 
#T# greatest common divisor (GCD)
import numpy

argv = sys.argv

def main(argv):
    """On a whole positive number, calculate all pairs of factors,
    prime factors, least common multiple, and greatest common divisor"""
    if len(argv) == 2:
        num = int(argv[1])
        print("The own list of factors is:",ownAllFactors(num))
#T# calculate prime factors with GNU's factor(number)
#T# the number arg in factor(number) must be a string
        print("GNU's factor() list of prime factors is:",subprocess.run(["factor",argv[1]],capture_output=True))

    if len(argv) > 2:
        nums = list(map(int,argv[1:]))
#T# calculate lcm and gcd with numpy.lcm(*numbersList),
#T# numpy.gcd(*numbersList)
        print("Numpy's LCM is",numpy.lcm(*nums))
        print("Numpy's GCD is",numpy.gcd(*nums))
    return 0

def ownAllFactors(num):
    allFactors = []
    maxDivisor = math.floor(math.sqrt(num))
    for i in range(1,maxDivisor + 1):
        if num % i == 0:
            allFactors.append(int(i))
            allFactors.append(int(num/i))
    return allFactors

if __name__ == '__main__':
    main(argv)