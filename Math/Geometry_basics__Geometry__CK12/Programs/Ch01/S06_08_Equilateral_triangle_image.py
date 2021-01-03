#T# the following code shows how to draw an equilateral triangle

#T# to draw an equilateral triangle, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

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

#T# create the endpoints of the segments that form the equilateral triangle
p0 = (0, 0)
p1 = (1, 0)
p2 = (.5, math.sqrt(3)/2)

#T# create the coordinates of these points
list1 = [p0[0], p1[0], p2[0], p0[0]] #| x coordinates
list2 = [p0[1], p1[1], p2[1], p0[1]] #| y coordinates

#T# create auxiliary points for the segment markers
p1_p0_marker = ((p1[0] + p0[0])/2, (p1[1] + p0[1])/2)
p2_p0_marker = ((p2[0] + p0[0])/2, (p2[1] + p0[1])/2)
p2_p1_marker = ((p2[0] + p1[0])/2, (p2[1] + p1[1])/2)

#T# calculate the angles from the segments
a_0_p1_p0 = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
a_0_p2_p0 = math.atan2(p2[1] - p0[1], p2[0] - p0[0])
a_0_p2_p1 = math.atan2(p1[1] - p2[1], p1[0] - p2[0])

#T# plot the equilateral triangle
plt.plot(list1, list2, 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$|$')
marker2 = MarkerStyle(r'$|$')
marker3 = MarkerStyle(r'$|$')

#T# transform the markers to make them the correct shape and size
s1 = 2.6 #| scale factor for the markers
marker1._transform.scale(1, s1)
marker1._transform.rotate(a_0_p1_p0)
marker2._transform.scale(1, s1)
marker2._transform.rotate(a_0_p2_p0)
marker3._transform.scale(1, s1)
marker3._transform.rotate(a_0_p2_p1)

#T# plot the markers
plt.plot(p1_p0_marker[0], p1_p0_marker[1], 'k', marker = marker1)
plt.plot(p2_p0_marker[0], p2_p0_marker[1], 'k', marker = marker2)
plt.plot(p2_p1_marker[0], p2_p1_marker[1], 'k', marker = marker3)

#T# show the results
plt.show()