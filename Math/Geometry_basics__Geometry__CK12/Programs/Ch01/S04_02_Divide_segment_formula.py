#T# the following code shows how to divide a segment into subsegments and get the location of any given endpoint of a subsegment

#T# define the points of the segment to be divided
p1 = (2, 1)
p2 = (29, 10)

#T# define n as the number of subsegments in which to divide the segment, and k as the number of the endpoint whose location will be calculated (starting the count from p1 as endpoint 0)
n = 9 #| number of subsegments
k = 4 #| k-th endpoint

#T# calculate the location of the k-th endpoint
p_k = (p1[0] + k/n*(p2[0] - p1[0]), p1[1] + k/n*(p2[1] - p1[1])) # (14.0, 5.0)
#| p_k = (2 + 4/9*(29 - 2), 1 + 4/9*(10 - 1))
#| p_k = (2 + 4/9*27, 1 + 4/9*9)
#| p_k = (2 + 4*3, 1 + 4)