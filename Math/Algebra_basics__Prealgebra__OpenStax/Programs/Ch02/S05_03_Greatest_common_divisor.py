#T# when two numbers have no common divisor, their common divisor is then 1

#T# to calculate the greatest common divisor, the numpy package is used
import numpy as np

#T# the gcd function from the numpy package calculates the greatest common divisor of two numbers
num1 = 8
num2 = 12
num3 = np.gcd(num1, num2) # 4

#T# the reduce function from the gcd module of the numpy package calculates the greatest common divisor of a set of numbers inside a one dimensional array
arr1 = np.array([12, 18, 36, 60])
num1 = np.gcd.reduce(arr1) # 6