
import math

#T# In this file:
#T# - Function to calculate the least common multiple (LCM), from API numpy
#T# - Function to calculate the greatest common divisor (GCD), from API numpy
#T# - Function to calculate prime factors, from GNU lib
#T# - Function to calculate all pairs of factors of a number (own)

#T# numpy is a library to find least common multiple (LCM), and 
#T# greatest common divisor (GCD)
import numpy


#T# TODO a function to calculate prime factors

def all_factor_pairs(num):
    allFactors = []
    maxDivisor = math.floor(math.sqrt(num))
    for i in range(1,maxDivisor + 1):
        if num % i == 0:
            allFactors.append(int(i))
            allFactors.append(int(num/i))
    return allFactors

#T# calculate lcm and gcd with numpy.lcm(*numbersList),
#T# numpy.gcd(*numbersList)
def least_common_multiple(int_list1):
    return numpy.lcm(*int_list1)
def greatest_common_divisor(int_list1):
    return numpy.gcd(*int_list1)

def main():
    """On a whole positive number, calculate all pairs of factors,
    prime factors, least common multiple, and greatest common divisor"""
    
    nums = [3,5,1]

    return 0