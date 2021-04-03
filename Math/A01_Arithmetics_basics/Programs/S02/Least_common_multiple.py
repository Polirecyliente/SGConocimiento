#T# the common multiples of a given set of numbers, are themselves multiples of the least common multiple of said set

#T# to calculate the least common multiple, the numpy package is used
import numpy as np

#T# the lcm function from the numpy package calculates the least common multiple of two numbers
num1 = 8
num2 = 12
num3 = np.lcm(num1, num2) # 24

#T# the reduce function from the lcm module of the numpy package calculates the least common multiple of a set of numbers inside a one dimensional array
arr1 = np.array([2, 5, 2, 1])
num1 = np.lcm.reduce(arr1) # 10