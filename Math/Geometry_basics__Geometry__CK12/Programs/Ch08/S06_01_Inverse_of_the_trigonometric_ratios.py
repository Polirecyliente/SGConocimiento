#T# the following code shows how to calculate the inverse of the trigonometric ratios

#T# to calculate the inverse of the trigonometric ratios, the math module is used
import math

#T# the asin function returns the arc sine in radians of a number
flo1 = math.asin(1/math.sqrt(2)) # 0.7853... == math.pi/4

#T# the acos function returns the arc cosine in radians of a number
flo1 = math.acos(-1) # 3.1415... == math.pi

#T# the atan function returns the arc tangent in radians of a number
flo1 = math.atan(1) # 0.7853 == math.pi/4

#T# the atan2 function returns the arc tangent in radians by taking the triangle legs as arguments
# SYNTAX math.atan2(opposite_leg1, adjacent_leg1)
flo1 = math.atan2(0, -1) # 3.1415... == math.pi