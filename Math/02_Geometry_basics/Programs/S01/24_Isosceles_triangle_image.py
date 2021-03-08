#T# the following code shows how to draw an isosceles triangle

#T# to draw an isosceles triangle, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

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
p1 = (.5, 1.2)
p2 = (1, 0)

list1 = [p0[0], p1[0], p2[0], p0[0]] #| x coordinates
list2 = [p0[1], p1[1], p2[1], p0[1]] #| y coordinates

p1_p0_marker = ((p1[0] + p0[0])/2, (p1[1] + p0[1])/2) #| auxiliary points for the segment markers
p1_p2_marker = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

a_0_p1_p0 = math.atan2(p1[1] - p0[1], p1[0] - p0[0]) #| angles from the segments
a_0_p1_p2 = math.atan2(p1[1] - p2[1], p1[0] - p2[0])

#T# plot the figure
plt.plot(list1, list2, 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$|$')
marker1._transform.scale(1, 2.6)
marker1._transform.rotate(a_0_p1_p0)

marker2 = MarkerStyle(r'$|$')
marker2._transform.scale(1, 2.6)
marker2._transform.rotate(a_0_p1_p2)

#T# plot the markers
plt.plot(p1_p0_marker[0], p1_p0_marker[1], 'k', marker = marker1)
plt.plot(p1_p2_marker[0], p1_p2_marker[1], 'k', marker = marker2)

#T# show the results
plt.show()