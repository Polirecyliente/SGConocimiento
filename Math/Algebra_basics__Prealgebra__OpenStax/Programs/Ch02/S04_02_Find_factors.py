#T# finding the factors of a number can serve to determine if a number is prime (only two factors) or composite (at least three factors)

#T# commonly all the sets of factors of a number can be found, for this the modulo operation is used, in a % b, if the result is 0 then b is a factor of a, and also a/b is a factor of a

#T# to work with arrays of pairs of factors, the numpy package is used
import numpy as np

#T# create the number whose factors are to be found, the number under test
num1 = 72

#T# create an array with the natural numbers from 2 up to the number under test minus 1
arr1 = np.arange(2, num1) #| creates an array from 2 to 71

#T# create an array to store the factor pairs
arr2 = np.array([[1, num1]]) #| this array is two dimensional so that the factor pairs are stored in the second dimension, the first factor pair is 1 and 72

#T# find all factor pairs and concatenate them in the array of factor pairs
for it1 in arr1:
    if (num1/it1 < it1): break #| there is no need to iterate if the quotient is less than the divisor, otherwise factor pairs are repeated
    if (num1 % it1 == 0):
        arr3 = np.array([[it1, num1/it1]])
        arr2 = np.concatenate((arr2, arr3))

#T# check the resulting factor pairs
arr2 # array([[ 1., 72.], [ 2., 36.], [ 3., 24.], [ 4., 18.], [ 6., 12.], [ 8.,  9.]])

#T# the list of factor pairs would be the same as the list of factors in general, except for squared numbers which have one repeated factor, for instance doing num1 = 25, makes arr2 = array([[ 1., 25.], [ 5.,  5.]])

#T# if the list of factor pairs of num1 only contains two numbers, then the number num1 is prime