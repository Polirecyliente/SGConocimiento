#T# the remainder is calculated using the modulo % operator
b = 5; a = 3
num1 = b % a  # 2

#T# to calculate the remainder between lists or arrays element-wise, the numpy package is used
import numpy as np

#T# the remainder function of the numpy package calculates the remainder of the division of the first array by the second, element-wise, it supports array broadcasting
arr1 = np.array([[12, 13, 9, 11], [8, 8, 7, 12]])
arr2 = np.array([7, 7, 5, 6])
arr3 = np.remainder(arr1, arr2) # array([[5, 6, 4, 5], [1, 1, 2, 0]])

#T# the remainder % operator can be used to calculate the remainder from a sequence of numpy arrays
arr1 = np.array([[12, 13, 9, 11], [8, 8, 7, 12]])
arr2 = np.array([7, 7, 5, 6])
arr3 = np.array([3, 3, 3, 3])
arr4 = arr1 % arr2 % arr3 # array([[2, 0, 1, 2], [1, 1, 2, 0]])