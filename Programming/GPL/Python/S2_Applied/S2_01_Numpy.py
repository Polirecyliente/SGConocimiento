
#   Numpy

#T# Table of contents

#C# Numpy arrays
#C# --- Array data types

#T# Beginning of content

#C# Numpy arrays

# |-------------------------------------------------------------
#T# arrays are one of the main aspects of the numpy package, numpy does not support jagged arrays for its operations
import numpy as np
arr1 = np.array(('a', 'b', 'c')) # array(['a', 'b', 'c'], dtype='<U1')
arr1 = np.array([1, 2, 3])   # array([1, 2, 3])
arr1 = np.array([[1, 2], [3, 4]]) # array([[1, 2], [3, 4]])
arr1 = np.array([[1, 2, 3], [4, 5], [6]]) # array([list([1, 2, 3]), list([4, 5]), list([6])], dtype=object) #| this jagged array can't be operated like normal numpy arrays

#T# the ndarray class stands for N-dimensional array, and it's the basic numpy class
type(arr1) # <class 'numpy.ndarray'>

#T# the ndim attribute of ndarray objects contains the number of dimensions of the array
arr1 = np.array([[1, 2], [3, 4]]) # array([[1, 2], [3, 4]])
int1 = arr1.ndim # 2

#T# the number of dimensions of an array can be set using a the ndmin kwarg
arr1 = np.array([1, 2], ndmin = 3) # array([[[1, 2]]])

#T# numpy arrays can be accessed and sliced like regular arrays, but also using a single list of indexes and slices

# SYNTAX arr1[int1, int2:int3]
#T# the list can have up to intN, int1 is the index in the outer dimension, int2:int3 is the slice in the next inner dimension, and so on, one dimension of arr1 per element of the list

#T# in the regular array indexing syntax, the first bracket pair indexes over the whole array, and any consecutive bracket pair indexes over the resulting array from previous bracket pairs

#T# in numpy arrays, each index in the list of indexes corresponds to a specific dimension, so the list of indexes acts as an ordered list of coordinates, where the first coordinate is the outer dimension or first dimension, the second coordinate is the second dimension, and so on

#T# dimensions can be omitted in the ordererd list, doing so makes the omitted dimensions default to all their values, e.g. in a numpy array arr1 of 5 dimensions, doing arr1[0], is the same as doing arr1[0, :, :, :, :]

arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
arr2 = arr1[0:2, 1] # array([[ 4,  5,  6],  [10, 11, 12]]) #| the 0:2 slice is in the outer dimension which is [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], the 1 index is in the second dimension which is [4, 5, 6] for the first element of the second dimension, and [10, 11, 12] for the second element of the second dimension
arr1[0:2, 1, 1:3]   # array([[ 5,  6], [11, 12]])
arr1[0:2, 1, 2]     # array([ 6, 12])

#T# any variable created by indexing or slicing a numpy array contains the data of said array by reference, this means that the original data can be modified through these variables, these variables are called views of the original data
arr1 = np.array([1, 2, 3])
arr2 = arr1[1:3] # array([2, 3])
arr2[0] = 50
arr1 # array([ 1, 50,  3])

#T# a view of a numpy array can be created with the view function as well
arr1 = np.array([1, 2, 3])
arr2 = arr1.view() # array([1, 2, 3])

#T# views are identified with the base attribute, it contains the original numpy array, and for the variable with the original numpy array, the base attribute contains None
arr1 = np.array([1, 2, 3])
arr2 = arr1[1:3].view() # array([2, 3])
var1 = arr1.base # None
var1 = arr2.base # array([1, 2, 3])

#T# variables can also be created to hold the contents of a numpy array by value, this is called a copy of the original data, this is done with the copy function
arr1 = np.array([1, 2, 3])
arr2 = arr1[1:3].copy()
arr2[0] = 50
arr1 # array([1, 2, 3])

#T# the shape of an array is defined as the amount of elements in each dimension, and so it can be represented by an ordered tuple, the ndarray objects have the shape attribute with such tuple
arr1 = np.array([[[1, 2, 3, 4]], [[5, 6, 7, 8]]])
tuple1 = arr1.shape # (2, 1, 4) 
#| there are 2 elements in the first dimension, namely [[1, 2, 3, 4]] and [[5, 6, 7, 8]], there is 1 element in the second dimension (be it [1, 2, 3, 4] or [5, 6, 7, 8]), and there are 4 elements in the third dimension

#T# the shape of an array can be changed with the reshape function

# SYNTAX array1.reshape(int1, int2, int3)
#T# array1 is a numpy array, int1, int2, int3, up to intN are the new amount of elements in each dimension, int1 for the first dimension, int2 for the second, and so on

#T# a caveat is that to guarantee that the resulting array is not jagged, the product of all the integers, int1*int2*int3, must be equal to the total number of elements in array1, this means that int1, int2, int3, up to intN are factors of said total number of elements

#T# one of the int values can be left unknown, this is done with the -1 literal value, the size for a dimension with a value of -1 is calculated

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr2 = arr1.reshape(1, 12) # array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]]) #| same as the original
arr2 = arr1.reshape(2, 6) # array([[ 1,  2,  3,  4,  5,  6], [ 7,  8,  9, 10, 11, 12]])
arr2 = arr1.reshape(3, 4) # array([[ 1,  2,  3,  4], [ 5,  6,  7,  8], [ 9, 10, 11, 12]])
arr2 = arr1.reshape(4, 3) # array([[ 1,  2,  3], [ 4,  5,  6], [ 7,  8,  9], [10, 11, 12]])
arr2 = arr1.reshape(6, 2) # array([[ 1,  2], [ 3,  4], [ 5,  6], [ 7,  8], [ 9, 10], [11, 12]])
arr2 = arr1.reshape(12, 1) # array([[ 1], [ 2], [ 3], [ 4], [ 5], [ 6], [ 7], [ 8], [ 9], [10], [11], [12]])
arr2 = arr1.reshape(2, 3, -1) # array([[[ 1,  2], [ 3,  4], [ 5,  6]], [[ 7,  8], [ 9, 10], [11, 12]]])
tuple1 = arr2.shape # (2, 3, 2)

#C# --- Array data types

# |-----
#T# there are a few data types that numpy arrays support, indicated by a single char
#T#     b, boolean
#T#     c, complex
#T#     f, float
#T#     i, integer
#T#     M, datetime
#T#     m, timedelta (# TODO)
#T#     O, object
#T#     S, string
#T#     U, unicode string
#T#     u, unsigned integer
#T#     V, void (# TODO)
arr1 = np.array(['str1']) # array(['str1'], dtype='<U4'), U4 means unicode string with 4 chars

#T# the dtype attribute of an ndarray object contains the array data type of said object
arr1 = np.array([1, 2])
dtype1 = arr1.dtype # dtype('int64')

#T# the dtype attribute can be set directly in the array constructor through the dtype kwarg
arr1 = np.array([1, 2], dtype = 'f8') #| the number in 'f8' stands for the amount of bytes, so 'f8' is for 8 byte float numbers
dtype1 = arr1.dtype # dtype('float64')

#T# the astype function creates a copy of a numpy array, and it allows changing the data type of the array
arr1 = np.array([1.4, 2.4])
arr2 = arr1.astype('i') # array([1, 2], dtype=int32) #| the argument 'i' changes the data type to integer, any of the other types can be used
# |-----

# |-------------------------------------------------------------