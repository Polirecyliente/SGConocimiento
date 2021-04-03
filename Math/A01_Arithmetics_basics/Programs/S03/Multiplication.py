#T# multiplication is made directly with the times * operator
a = 5; b = 3
num1 = a * b # 15

#T# the prod function returns the product of all elements in an array
import math
list1 = [5, 3]
num1 = math.prod(list1) # 15

#T# to multiply lists or arrays element-wise, the numpy package is used
import numpy as np

#T# the multiply function of the numpy package, multiplies two arrays element-wise, it supports array broadcasting
arr1 = np.array([[1, 2, 3, 4], [0, 1, 2, 3]])
arr2 = np.array([2, 2, 2, 2])
arr3 = np.multiply(arr1, arr2) # array([[2, 4, 6, 8], [0, 2, 4, 6]])

#T# the multiplication * operator can be used to multiply more than two numpy arrays in a single statement, it supports array broadcasting
arr1 = np.array([[1, 2, 3, 4], [0, 1, 2, 3]])
arr2 = np.array([2, 2, 2, 2])
arr3 = np.array([3, 3, 1, 1])
arr4 = arr1*arr2*arr3 # array([[ 6, 12,  6,  8], [ 0,  6,  4,  6]])