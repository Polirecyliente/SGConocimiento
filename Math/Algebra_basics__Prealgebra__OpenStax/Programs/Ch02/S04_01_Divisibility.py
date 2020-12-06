#T# divisibility can be checked with the modulo % operator, in a % b, if the result is 0 then a is divisible by b

#T# even numbers are divisible by 2, odd numbers are not, so in a % 2, if the result is 0 then a is an even number, if the result is 1 then a is an odd number
num1 = 5 % 2 # 1 #| 5 is an odd number
num1 = 8 % 2 # 0 #| 8 is an even number

#T# to check for divisibility in arrays element-wise, the numpy package is used
import numpy as np

#T# create an array to check divisibility on its elements
arr1 = np.arange(1, 8) # array([1, 2, 3, 4, 5, 6, 7])

#T# check divisibility by 2
arr2 = arr1 % 2 # array([1, 0, 1, 0, 1, 0, 1]) #| every second number is divisible by 2

#T# check divisibility by 3
arr2 = arr1 % 3 # array([1, 2, 0, 1, 2, 0, 1]) #| every third number is divisible by 3