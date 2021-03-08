#T# the following code shows how to draw an obtuse triangle

#T# to draw an obtuse triangle, the pyplot module of the matplotlib package is used
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
p2 = (-1.8, 2)

list1 = [p0[0], p1[0], p2[0], p0[0]] #| x coordinates
list2 = [p0[1], p1[1], p2[1], p0[1]] #| y coordinates

a1 = math.degrees(math.atan2(p1[1], p1[0])) #| angles from the segments of the obtuse angle
a2 = math.degrees(math.atan2(p2[1], p2[0]))

#T# plot the figure
plt.plot(list1, list2, 'k')
arc1 = mpatches.Arc(p0, .6, .6, theta1 = a1, theta2 = a2)
ax1.add_patch(arc1)

#T# show the results
plt.show()