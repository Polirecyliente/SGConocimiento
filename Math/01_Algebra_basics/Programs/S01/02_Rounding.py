#T# The round function rounds to the nearest even, the second argument is the precision, if the precision is negative then the number is rounded to the left of the decimal point
num1 = round(1.5) # 2
num1 = round(2.5) # 2
num1 = round(23658, -2) # 23700
num1 = round(23650, -2) # 23600

#T# the ceil function rounds numbers up
import math
num1 = math.ceil(2.5)  #  3
num1 = math.ceil(-2.5) # -2

#T# the floor function rounds numbers down
import math
num1 = math.floor(2.5) #   2
num1 = math.floor(-2.5) # -3

#T# the trunc function truncates numbers
num1 = math.trunc(2.5)  # 2
num1 = math.trunc(-2.5) # -2