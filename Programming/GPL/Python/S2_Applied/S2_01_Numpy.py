
#   Numpy

#T# Table of contents

#C# Numpy arrays
#C# --- Array data types
#C# --- Array operations

#T# Beginning of content

# |-------------------------------------------------------------
#T# numpy has an specific function to get help for names in the namespace of numpy, it's the numpy.info function which is used as the builtin help function from Python, this is important because numpy ufuncs are written in C, an so the help function can't show their help
import numpy as np
np.info(np.array) #| shows the numpy help for np.array
# |-------------------------------------------------------------

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
#T#     m, timedelta, provides time intervals to operate with datetimes
#T#     O, object
#T#     S, string
#T#     U, unicode string
#T#     u, unsigned integer
#T#     V, void, flexible data type to accommodate for any of the others
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

#C# --- Array operations

# |-----
#T# numpy arrays can be iterated like regular arrays, but also with the nditer function, this has the difference that the nditer function iterates over each individual element, and so nested arrays are not necessary
arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for it1 in np.nditer(arr1):
    it1
#T# the former prints
# array(1)
# array(2)
# array(3)
# array(4)
# array(5)
# array(6)
# array(7)
# array(8)
# array(9)
# array(10)
# array(11)
# array(12)

#T# the ndenumerate function returns an iterable object of tuples, where each tuple contains the index of each element in the numpy array, and the element itself

# SYNTAX np.ndenumerate(array1)
#T# each element in the numpy array array1 has an index, this can be retrieved with this syntax

#T# as array1 can have several dimensions, the index also has several dimensions, and so the index returned by the ndenumerate function is also a tuple whose elements indicate the index in each dimension, starting from the outer dimension or first dimension

#T# as an example, if an element of value 5 is located in index 3 of the first dimension and index 1 of the second, its index tuple will be (3, 1), and its tuple in the ndenumerate object would be ((3, 1), 5)

arr1 = np.array([[0, 1], [1, 1], [1, 1], [1, 5]])
for it1 in np.ndenumerate(arr1):
    it1
#T# the former outputs
# ((0, 0), 0)
# ((0, 1), 1)
# ((1, 0), 1)
# ((1, 1), 1)
# ((2, 0), 1)
# ((2, 1), 1)
# ((3, 0), 1)
# ((3, 1), 5)

#T# in numpy, the words dimension and axis are almost synonyms, axis is the same as dimension - 1, dimensions count from 1, axes count from 0

#T# numpy arrays can be joined along a given dimension or axis using the axis kwarg of the concatenate function, the axis kwarg starts counting dimensions at 0, this means that the first dimension is axis 0

# SYNTAX np.concatenate((array1, array2), axis = int1)
#T# the tuple argument accepts up to arrayN, array1 and array2 are the numpy arrays to concatenate, int1 is the axis in which the arrays will be concatenated

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.concatenate((arr1, arr2), axis = 0) # array([[1, 2], [3, 4], [5, 6], [7, 8]])
arr3 = np.concatenate((arr1, arr2), axis = 1) # array([[1, 2, 5, 6], [3, 4, 7, 8]])

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5], [6]])
arr3 = np.concatenate((arr1, arr2), axis = 0)
arr3 = np.concatenate((arr1, arr2), axis = 1)

#T# numpy arrays can be stacked, thereby creating an extra dimension to contain the stacked arrays, this is done with the stack function

# SYNTAX np.stack((array1, array2), axis = int1)
#T# array1, array2, up to arrayN are the arrays to be stacked, int1 is the axis in which the stacking will be made, all arrays must have the same shape

#T# int1 applies from the perspective of the new extra dimension that is an outer dimension enclosing the stacked arrays, so an axis of int1 equal to 0 represents the first dimension which is the extra dimension itself

#T# if int1 is 0 then each numpy array, array1, array2, up to arrayN, now counts as an element of the stacked array, so they are stacked directly on top of each other, in the order specified by the tuple argument

#T# if int1 is 1 then now the elements of the first dimension (their axis 0) of the numpy arrays, are stacked, and so if int1 is N then the elements in the Nth dimension of the numpy arrays, are stacked

#T# all the former means that the maximum value of int1 is 1 plus the biggest axes number of any of the arrays, array1, array2, up to arrayN, in this particular case, each individual element of each array is stacked with the individual elements of the other arrays, this forms new arrays in the most inner dimension that are always the size of the number of arrays stacked

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.array([[9, 10], [11, 12]])

arr4 = np.stack((arr1, arr2, arr3), axis = 0)
#T# arr4 stacks like the following
# array([[[ 1,  2], [ 3,  4]], [[ 5,  6], [ 7,  8]], [[ 9, 10], [11, 12]]])

arr4 = np.stack((arr1, arr2, arr3), axis = 1)
#T# arr4 stacks like the following
# array([[[ 1,  2], [ 5,  6], [ 9, 10]],
#        [[ 3,  4], [ 7,  8], [11, 12]]])

arr4 = np.stack((arr1, arr2, arr3), axis = 2)
#T# arr4 stacks like the following
# array([[[ 1,  5,  9],
#         [ 2,  6, 10]],
#        [[ 3,  7, 11],
#         [ 4,  8, 12]]])

#T# by stacking arrays, new arrays with different shapes can be acquired, except for dimensions with a shape value of 1, to get extra dimensions with a shape value of 1 use the following syntax

# SYNTAX array1 = np.array([[[[array1]]]])
#T# array1 is the array being manipulated, the number of square bracket pairs [] can be more than 4 or less than 4, according to the amount of extra dimensions wanted with a shape value of 1

arr1 = np.array([1, 2])
tuple1 = arr1.shape # (2,)
arr1 = np.array([[arr1]]) # array([[[1, 2]]])
tuple1 = arr1.shape # (1, 1, 2)

#T# the vstack function is not so much a function for stacking, as it is a function to concatenate along axis 0 (first dimension)

# SYNTAX np.vstack((array1, array2))
#T# array1, array2, up to arrayN are the arrays being concatenated along axis 0

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8], [9, 10]])
arr3 = np.vstack((arr1, arr2))
# array([[ 1,  2], [ 3,  4], [ 5,  6], [ 7,  8], [ 9, 10]])
arr3 = np.concatenate((arr1, arr2), axis = 0) #| same as before
# array([[ 1,  2], [ 3,  4], [ 5,  6], [ 7,  8], [ 9, 10]])

#T# the hstack function is not so much a function for stacking, as it is a function to concatenate along axis 1 (second dimension)

# SYNTAX np.hstack((array1, array2))
#T# array1, array2, up to arrayN are the arrays being concatenated along axis 1

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5], [6]])
arr3 = np.hstack((arr1, arr2))
# array([[1, 2, 5], [3, 4, 6]])
arr3 = np.concatenate((arr1, arr2), axis = 1) #| same as before
# array([[1, 2, 5], [3, 4, 6]])

#T# the dstack function is not so much a function for stacking, as it is a function to concatenate along axis 2 (third dimension)

# SYNTAX np.dstack((array1, array2))
#T# array1, array2, up to arrayN are the arrays being concatenated along axis 2

arr1 = np.array([[[1, 2]], [[3, 4]]])
arr2 = np.array([[[5]], [[6]]])
arr3 = np.dstack((arr1, arr2))
# array([[[1, 2, 5]], [[3, 4, 6]]])
arr3 = np.concatenate((arr1, arr2), axis = 2) #| same as before
# array([[[1, 2, 5]], [[3, 4, 6]]])
# |-----

# |-------------------------------------------------------------




# TODO ellipsis notation arr1[...]