#T# addition is made directly with the plus + operator
a = 5; b = 3
num1 = a + b # 8

#T# the sum function returns the sum of all elements in an array
list1 = [5, 3]
num1 = sum(list1) # 8

#T# to add lists or arrays element-wise, the numpy package is used
import numpy as np

#T# the add function from the numpy package, adds two arrays element-wise, it supports array broadcasting
arr1 = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
arr2 = np.array([4, 3, 2, 1])
arr3 = np.add(arr1, arr2) # array([[5, 5, 5, 5], [7, 7, 7, 7]])

#T# the plus + operator can be used to add more than two numpy arrays in a single statement, it supports array broadcasting
arr1 = np.array([[1, 2, 3, 4], [0, 1, 2, 3]])
arr2 = np.array([4, 3, 2, 1])
arr3 = np.array([2, 3, 4, 5])
arr4 = arr1 + arr2 + arr3 # array([[ 7,  8,  9, 10], [ 6,  7,  8,  9]])