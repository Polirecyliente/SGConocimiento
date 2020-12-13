#T# repeating decimals can be converted into fractions, and when starting with a fraction, the repeating part of its repeating decimal can be found if the fraction is a repeating decimal

#T# to work with repeating decimals and fractions, the sympy package is used
import sympy

#T# create a repeating decimal, any repeating decimal has two parts, an unique part (which may be zero), and a repeating part
num1 = 894.57    #| unique part of the repeating decimal number
num2 = 448132653 #| repeating part of the repeating decimal number
#| the repeating decimal itself is 894.57448132653448132653448132653448132653

#T# get the amount of digits after decimal point in the unique number
num1_1 = len(str(num1).split('.')[1]) # 2

#T# get the amount of digits in the repeated number
num2_1 = len(str(num2))               # 9

#T# the calculation of the fraction is based on subtracting the repeating part of the number to get rid of it, and for this, two multiples of the number are created and the smaller is subtracted from the larger one, after this the fraction can be found

#T# calculate the numerator, it's all the unique digits and one time the repeated digits, both put to the left of the decimal point, minus the unique digits also put to the left of the decimal point
num3 = int(num1*10**(num1_1 + num2_1) + num2 - num1*10**num1_1)
# 89457448132653 - 89457 == 89457448043196

#T# calculate the denominator, it's the subtraction of the powers of ten that were needed to create the numerator
num4 = int(10**(num1_1 + num2_1) - 10**num1_1)
# 100000000000 - 100 == 99999999900

#T# create a fraction with the numerator and denominator, using the Rational constructor
num5 = sympy.Rational(num3, num4) # 2484929112311/2777777775

#T# now to do the opposite process, long division is used to calculate the remainder and quotient in iterations, once a remainder repeats itself in the iterations, that means that the repeating part of the decimal number is found

#T# create a list to store the quotients, and one to store the remainders of the iterations
list1 = []
list2 = []

#T# create the numerator and the denominator of the fraction whose repeating part wants to be found
num1 = 2484929112311
num2 = 2777777775

#T# create the loop to do the long division
bool1 = False
while bool1 == False:
    num3 = num1//num2 #| quotient of the iteration
    num4 = num1%num2  #| remainder of the iteration
    if num4 in list2:
        bool1 = True
    list1.append(num3)
    list2.append(num4)
    num1 = 10*num4    #| dividend for the next iteration

#T# list1 contains the quotients of each iteration, and list2 the remainders of each iteration
list1 # [894, 5, 7, 4, 4, 8, 1, 3, 2, 6, 5, 3]
list2 # [1595781461, 2068925735, 1244812925, 1337018150, 2259070400, 368481800, 907040225, 737068925, 1815133700, 1484670350, 957814625, 1244812925] #| the remainder 1244812925 is repeated at index 2 and at the last element

#T# get the index with the first occurrence of the remainder, the second occurrence is always the last element in list2
num5 = list2.index(num4) # 2

#T# the index is augmented by 1 to avoid repeating the remainder, because num5 is supposed to signal the index from which all remainders are unique
num5 += 1 # 3

#T# cast the elements in list1 into a list of strings, to concatenate the numbers
list3 = [str(it1) for it1 in list1]

#T# the result is shown as int1.unique1(repeating1) where int1 is the integer part, unique1 is the unique part of the decimals, and repeating1 is inside parentheses to indicate the repeating part of the decimal number
str1 = list3[0] + '.' + ''.join(list3[1:num5]) + '(' + ''.join(list3[num5:]) + ')' # '894.57(448132653)'