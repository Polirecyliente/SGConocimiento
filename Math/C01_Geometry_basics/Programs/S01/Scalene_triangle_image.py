#T# the following code shows how to draw an scalene triangle

#T# to draw an scalene triangle, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

#T# import the math module to do calculations
import math

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the projection of the axes to polar projection
ax1 = plt.subplot(1, 1, 1, projection = 'polar')

#T# set the aspect of the axes
ax1.set_aspect('equal')

#T# hide the spines and ticks
ax1.spines['polar'].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the variables that define the plot
p0 = (0, 0)
p1 = (0.2, 1)
p2 = (2.4, 2)

list1 = [p0[0], p1[0], p2[0], p0[0]] #| x coordinates
list2 = [p0[1], p1[1], p2[1], p0[1]] #| y coordinates

p0_p1_marker = (p1[0], p1[1]/2) #| auxiliary points for the segment markers
p0_p2_marker = (p2[0], p2[1]/2)
p1_p2_marker = (1.8, .76)

#T# plot the figure
plt.plot(list1, list2, 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$|$')
marker1._transform.scale(1, 2.2)
marker1._transform.rotate(p0_p1_marker[0] + .05)

marker2 = MarkerStyle(r'$||$')
marker2._transform.scale(1.6, 2.2)
marker2._transform.rotate(p0_p2_marker[0] - .05)

marker3 = MarkerStyle(r'$|||$')
marker3._transform.scale(1.6, 2.2)
marker3._transform.rotate(p1_p2_marker[0] + .9)

#T# plot the markers
plt.plot(p0_p1_marker[0], p0_p1_marker[1], 'k', marker = marker1)
plt.plot(p0_p2_marker[0], p0_p2_marker[1], 'k', marker = marker2)
plt.plot(p1_p2_marker[0], p1_p2_marker[1], 'k', marker = marker3)

#T# show the results
plt.show()