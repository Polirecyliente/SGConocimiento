#T# prime factorization consists of finding the prime numbers that multiplied together produce a given number, in the case that the given number is prime itself then the two prime factors are 1 and itself

#T# define a function to calculate the prime factors of a number recursively
def func1(num1):
    num1 = int(num1)

#T# create a list to store the prime number gotten in each recursion
    list1 = []

#T# create the range of numbers from 2 to num1, num1 is included in case it is prime
    list2 = range(2, num1 + 1)

#T# check the numbers in the range for the first prime number
    for it1 in list2:

#T# if num1 is divisible by it1 then it1 is prime because it's the first number (after 1) by which num1 is divisible
        if (num1 % it1 == 0):
            list1.append(it1)

#T# recurse to find and append the first prime factor of the quotient num1/it1 which is smaller than num1, so that recursion can end
            list1 += func1(num1/it1)

#T# skip the remaining iterations of the for loop, this guarantees that no other factors of num1 are included, which may not be prime
            break
    return list1

#T# check the prime factors of a number
num1 = 60
list1 = func1(num1) # [2, 2, 3, 5]

#T# the multiplicity of the prime factors can be calculated by counting the amount of repetitions of each prime factor, for this the unique function from the numpy package is used
import numpy as np

tuple1 = np.unique(list1, return_counts = True)
# (array([2, 3, 5]), array([2, 1, 1])) #| the multiplicity of each prime number is in the second array