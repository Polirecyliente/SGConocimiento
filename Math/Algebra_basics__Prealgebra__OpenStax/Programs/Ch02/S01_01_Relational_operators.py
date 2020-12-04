#T# relational operators are used to do relational operations, i.e. operations in which there is testing of the values of numbers, by comparing them against each other

#T# the equality == operator compares if two numbers are equal
a = 5; b = 3
bool1 = a == b # False
a = 4; b = 4
bool1 = a == b # True

#T# the not equal != operator compares if two number are not equal
a = 5; b = 3
bool1 = a != b # True
a = 4; b = 4
bool1 = a != b # False

#T# the greater than > operator compares if the first number is greater than the second
a = 5; b = 3
bool1 = a > b # True
a = 4; b = 4
bool1 = a > b # False

#T# the less than < operator compares if the first number is less than the second
a = 3; b = 5
bool1 = a < b # True
a = 4; b = 4
bool1 = a < b # False

#T# the greater than or equal to >= operator compares if the first number is greater than or equal to the second
a = 5; b = 3
bool1 = a >= b # True
a = 4; b = 4
bool1 = a >= b # True
a = 3; b = 5
bool1 = a >= b # False

#T# the less than or equal to <= operator compares if the first number is less than or equal to the second
a = 3; b = 5
bool1 = a <= b # True
a = 4; b = 4
bool1 = a <= b # True
a = 5; b = 3
bool1 = a <= b # False

#T# to do relational operations with lists or arrays element-wise, the numpy package is used
import numpy as np

#T# the array_equal function from the numpy package, compares if two arrays are equal, with the same shape and the same elements
arr1 = np.array([[6, 9, 4, 4], [8, 1, 9, 10]])
arr2 = np.array([[6, 9, 4, 4], [8, 1, 9, 10]])
bool1 = np.array_equal(arr1, arr2) # True

#T# the equal function from the numpy package, compares if two arrays are equal element-wise, it supports array broadcasting
arr1 = np.array([[6, 9, 4, 4], [8, 1, 10, 8]])
arr2 = np.array([7, 3, 4, 8])
arr3 = np.equal(arr1, arr2)
# array([[False, False,  True, False], [False, False, False,  True]])

#T# the equality operator == can be used to compare if two numpy arrays are equal element-wise, it supports array broadcasting
arr1 = np.array([[6, 9, 4, 4], [8, 1, 10, 8]])
arr2 = np.array([7, 3, 4, 8])
arr3 = arr1 == arr2
# array([[False, False,  True, False], [False, False, False,  True]])

#T# the not_equal function from the numpy package, compares if two arrays are not equal element-wise, it supports array broadcasting
arr1 = np.array([[6, 9, 4, 4], [8, 1, 10, 8]])
arr2 = np.array([7, 3, 4, 8])
arr3 = np.not_equal(arr1, arr2)
# array([[ True,  True, False,  True], [ True,  True,  True, False]])

#T# the not equal != operator can be used to compare if two numpy arrays are not equal element-wise, it supports array broadcasting
arr1 = np.array([[6, 9, 4, 4], [8, 1, 10, 8]])
arr2 = np.array([7, 3, 4, 8])
arr3 = arr1 != arr2
# array([[ True,  True, False,  True], [ True,  True,  True, False]])

#T# the greater function from the numpy package, compares if the first array is greater than the second element-wise, it supports array broadcasting
arr1 = np.array([[6, 9, 4, 4], [8, 1, 10, 8]])
arr2 = np.array([7, 3, 4, 8])
arr3 = np.greater(arr1, arr2)
# array([[False,  True, False, False], [ True, False,  True, False]])

#T# the greater than > operator can be used to compare if the first numpy array is greater than the second element-wise, it supports array broadcasting
arr1 = np.array([[6, 9, 4, 4], [8, 1, 10, 8]])
arr2 = np.array([7, 3, 4, 8])
arr3 = arr1 > arr2
# array([[False,  True, False, False], [ True, False,  True, False]])

#T# the less function from the numpy package, compares if the first array is less than the second element-wise, it supports array broadcasting
arr1 = np.array([[6, 9, 4, 4], [8, 1, 10, 8]])
arr2 = np.array([7, 3, 4, 8])
arr3 = np.less(arr1, arr2)
# array([[ True, False, False,  True], [False,  True, False, False]])

#T# the less than < operator can be used to compare if the first numpy array is less than the second element-wise, it supports array broadcasting
arr1 = np.array([[6, 9, 4, 4], [8, 1, 10, 8]])
arr2 = np.array([7, 3, 4, 8])
arr3 = arr1 < arr2
# array([[ True, False, False,  True], [False,  True, False, False]])

#T# the greater_equal function from the numpy package, compares if the first array is greater than or equal to the second element-wise, it supports array broadcasting
arr1 = np.array([[6, 9, 4, 4], [8, 1, 10, 8]])
arr2 = np.array([7, 3, 4, 8])
arr3 = np.greater_equal(arr1, arr2)
# array([[False,  True,  True, False], [ True, False,  True,  True]])

#T# the greater than or equal to >= operator can be used to compare if the first numpy array is greater than or equal to the second element-wise, it supports array broadcasting
arr1 = np.array([[6, 9, 4, 4], [8, 1, 10, 8]])
arr2 = np.array([7, 3, 4, 8])
arr3 = arr1 >= arr2
# array([[False,  True,  True, False], [ True, False,  True,  True]])

#T# the less_equal function from the numpy package, compares if the first array is less than or equal to the second element-wise, it supports array broadcasting
arr1 = np.array([[6, 9, 4, 4], [8, 1, 10, 8]])
arr2 = np.array([7, 3, 4, 8])
arr3 = np.less_equal(arr1, arr2)
# array([[ True, False,  True,  True], [False,  True, False,  True]])

#T# the less than or equal to <= operator can be used to compare if the first numpy array is less than or equal to the second element-wise, it supports array broadcasting
arr1 = np.array([[6, 9, 4, 4], [8, 1, 10, 8]])
arr2 = np.array([7, 3, 4, 8])
arr3 = arr1 <= arr2
# array([[ True, False,  True,  True], [False,  True, False,  True]])