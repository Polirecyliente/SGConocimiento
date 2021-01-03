#T# the following code shows how to draw a concave polygon

#T# to draw a concave polygon, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw arcs
import matplotlib.patches as mpatches

#T# import the math module to calculate angles and lengths
import math

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'datalim')

#T# hide the spines and the axes ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the endpoints of the segments that form the concave polygon
p1 = (0, 0)
p2 = (2, 0)
p3 = (4, 2)
p4 = (5, 5)
p5 = (1, 6)
p6 = (2, 4) #| this point makes it concave
p7 = (-1, 3)

#T# create the coordinates of these points
list1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p1[0]] #| x coordinates
list2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p1[1]] #| y coordinates

#T# calculate the angle of the point that makes the polygon concave
a_0_p5_p6 = math.atan2(p5[1] - p6[1], p5[0] - p6[0])
l_p5_p6 = math.sqrt((p5[1] - p6[1])**2 + (p5[0] - p6[0])**2)
l_p7_p6 = math.sqrt((p7[1] - p6[1])**2 + (p7[0] - p6[0])**2)
num1 = (p5[0] - p6[0])*(p7[0] - p6[0]) + (p5[1] - p6[1])*(p7[1] - p6[1])
a_p5_p6_p7_p6 = math.acos(num1/(l_p5_p6*l_p7_p6)) + a_0_p5_p6 - 2*math.pi

#T# plot the concave polygon and the arc of the point that makes the polygon concave
plt.plot(list1, list2, 'k')

arc1 = mpatches.Arc(p6, .7, .7, theta1 = math.degrees(a_p5_p6_p7_p6), theta2 = math.degrees(a_0_p5_p6))
ax1.add_patch(arc1)

#T# show the results
plt.show()