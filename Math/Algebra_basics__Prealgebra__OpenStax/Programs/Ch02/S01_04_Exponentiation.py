#T# exponentiation is the operation of multiplying a number by itself several times

#T# the exponentiation ** operator can be used to raise the first number to the power of the second
num1 = 2 ** 4  # 16 #| 16 is 2 to the 4th power
num1 = 5 ** -1 # 0.2

#T# the pow function is used to raise the first number to the power of the second
num1 = pow(2, 4) # 16 #| 16 is 2 to the 4th power

#T# to raise a list or array to the power of another list or array element-wise, the numpy package is used
import numpy as np

#T# the power function raises the first array to the power of the second element-wise, it supports array broadcasting
arr1 = np.array([[2, 3, 2, 4], [3, 2, 2, 5]])
arr2 = np.array([6, 4, 5, 2])
arr3 = np.power(arr1, arr2)
# array([[ 64,  81,  32,  16], [729,  16,  32,  25]])

#T# the exponentiation ** operator can be used to raise the first array to the power of the second element-wise, it supports array broadcasting
arr1 = np.array([[2, 3, 2, 4], [3, 2, 2, 5]])
arr2 = np.array([6, 4, 5, 2])
arr3 = arr1 ** arr2
# array([[ 64,  81,  32,  16], [729,  16,  32,  25]])