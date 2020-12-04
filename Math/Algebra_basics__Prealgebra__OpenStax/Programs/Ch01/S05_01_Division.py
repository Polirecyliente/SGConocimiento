#T# division is made directly with the divided by / operator
a = 3; b = 15
num1 = b/a # 5.0

#T# to divide lists or arrays element-wise, the numpy package is used
import numpy as np

#T# the divide function from the numpy package, divides the first array by the second, element-wise, it supports array broadcasting 
arr1 = np.array([[12, 24, 12, 6], [21, 18, 15, 12]])
arr2 = np.array([3, 3, 3, 3])
arr3 = np.divide(arr1, arr2) # array([[4., 8., 4., 2.], [7., 6., 5., 4.]])

#T# the division / operator can be used to divide one numpy array by more than one other array, element-wise, it supports array broadcasting
arr1 = np.array([[12, 24, 12, 6], [21, 18, 15, 12]])
arr2 = np.array([3, 3, 3, 3])
arr3 = np.array([2, 2, 1, 1])
arr4 = arr1/arr2/arr3 # array([[2. , 4. , 4. , 2. ], [3.5, 3. , 5. , 4. ]])