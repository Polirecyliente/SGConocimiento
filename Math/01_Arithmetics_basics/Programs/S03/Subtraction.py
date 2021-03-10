#T# subtraction is made directly with the minus - operator
a = 5; b = 8
num1 = b - a # 3

#T# to subtract lists or arrays element-wise, the numpy package is used
import numpy as np

#T# the subtract function from the numpy package, subtracts the second array from the first, element-wise, it supports array broadcasting
arr1 = np.array([[1, 2, 3, 4], [6, 5, 4, 3]])
arr2 = np.array([4, 3, 2, 1])
arr3 = np.subtract(arr1, arr2) # array([[-3, -1,  1,  3], [ 2,  2,  2,  2]])

#T# the minus - operator can be used to subtract more than one numpy array from another in a single statement, it supports array broadcasting
arr1 = np.array([[1, 2, 3, 4], [6, 5, 4, 3]])
arr2 = np.array([4, 3, 2, 1])
arr3 = np.array([-3, -1, 1, 3])
arr4 = arr1 - arr2 - arr3 # array([[ 0,  0,  0,  0], [ 5,  3,  1, -1]])