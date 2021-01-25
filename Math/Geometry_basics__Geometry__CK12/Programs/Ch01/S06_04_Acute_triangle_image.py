#T# the following code shows how to draw an acute triangle

#T# to draw an acute triangle, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# import the math module to do calculations
import math

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'datalim')

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the variables that define the plot
p0 = (0, 0)
p1 = (2, 1)
p2 = (-0.5, 2)

list1 = [p0[0], p1[0], p2[0], p0[0]] #| x coordinates
list2 = [p0[1], p1[1], p2[1], p0[1]] #| y coordinates

a1_0 = math.degrees(math.atan2(p1[1] - p0[1], p1[0] - p0[0])) #| angles from the segments
a0_1 = a1_0 + 180
a2_0 = math.degrees(math.atan2(p2[1] - p0[1], p2[0] - p0[0]))
a0_2 = a2_0 + 180
a2_1 = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0]))
a1_2 = a2_1 + 180

#T# plot the figure
plt.plot(list1, list2, 'k')
arc1 = mpatches.Arc(p0, .6, .6, theta1 = a1_0, theta2 = a2_0)
arc2 = mpatches.Arc(p1, .6, .6, theta1 = a2_1, theta2 = a0_1)
arc3 = mpatches.Arc(p2, .6, .6, theta1 = a0_2, theta2 = a1_2)
ax1.add_patch(arc1)
ax1.add_patch(arc2)
ax1.add_patch(arc3)

#T# show the results
plt.show()