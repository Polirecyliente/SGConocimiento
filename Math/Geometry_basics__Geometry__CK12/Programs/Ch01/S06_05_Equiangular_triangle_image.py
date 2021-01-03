#T# the following code shows how to draw an equiangular triangle

#T# to draw an equiangular triangle, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw arcs
import matplotlib.patches as mpatches

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

#T# import the math module to calculate arctangents
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

#T# create the endpoints of the segments that form the equiangular triangle
p0 = (0, 0)
p1 = (1, 0)
p2 = (.5, math.sqrt(3)/2)

#T# create the coordinates of these points
list1 = [p0[0], p1[0], p2[0], p0[0]] #| x coordinates
list2 = [p0[1], p1[1], p2[1], p0[1]] #| y coordinates

#T# calculate the angles from the segments
a1_0 = math.degrees(math.atan2(p1[1] - p0[1], p1[0] - p0[0]))
a0_1 = a1_0 + 180
a2_0 = math.degrees(math.atan2(p2[1] - p0[1], p2[0] - p0[0]))
a0_2 = a2_0 + 180
a2_1 = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0]))
a1_2 = a2_1 + 180

#T# create the diameter of the angle arcs, and auxiliary points for the angle markers
l1 = .4 #| diameter of the angle arcs
p0_marker = (p0[0] + l1/2*math.cos(math.pi/6), p0[1] + l1/2*math.sin(math.pi/6))
p1_marker = (p1[0] - l1/2*math.cos(math.pi/6), p1[1] + l1/2*math.sin(math.pi/6))
p2_marker = (p2[0], p2[1] - l1/2)

#T# plot the equiangular triangle and the angle marks
plt.plot(list1, list2, 'k')

arc1 = mpatches.Arc(p0, l1, l1, theta1 = a1_0, theta2 = a2_0)
arc2 = mpatches.Arc(p1, l1, l1, theta1 = a2_1, theta2 = a0_1)
arc3 = mpatches.Arc(p2, l1, l1, theta1 = a0_2, theta2 = a1_2)
ax1.add_patch(arc1)
ax1.add_patch(arc2)
ax1.add_patch(arc3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$|$')
marker2 = MarkerStyle(r'$|$')
marker3 = MarkerStyle(r'$|$')

#T# transform the markers to make them the correct shape and size
marker1._transform.scale(1, 2.2)
marker1._transform.rotate_deg((a1_0 + a2_0)/2 + 90)
marker2._transform.scale(1, 2.2)
marker2._transform.rotate_deg((a0_1 + a2_1)/2 + 90)
marker3._transform.scale(1, 2.2)
marker3._transform.rotate_deg((a1_2 + a0_2)/2 + 90)

#T# plot the markers
plt.plot(p0_marker[0], p0_marker[1], 'k', marker = marker1)
plt.plot(p1_marker[0], p1_marker[1], 'k', marker = marker2)
plt.plot(p2_marker[0], p2_marker[1], 'k', marker = marker3)

#T# show the results
plt.show()