
import math

#T# numpy is a library to find least common multiple (LCM), and 
#T# greatest common divisor (GCD)
import numpy

#T# calculate lcm and gcd with numpy.lcm(*numbersList),
#T# numpy.gcd(*numbersList)
def least_common_multiple(int_list1):
    return numpy.lcm(*int_list1)
def greatest_common_divisor(int_list1):
    return numpy.gcd(*int_list1)