#T# the following code shows how to draw an isosceles triangle to show the base angles theorem

#T# to draw an isosceles triangle to show the base angles theorem, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

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
p1 = (0, 0)
p2 = (.5, 1.2)
p3 = (1, 0)

list1 = [p1[0], p2[0], p3[0], p1[0]] #| x coordinates
list2 = [p1[1], p2[1], p3[1], p1[1]] #| y coordinates

p_marker_1_2 = ((p2[0] + p1[0])/2, (p2[1] + p1[1])/2) #| auxiliary points for the segment markers
p_marker_2_3 = ((p2[0] + p3[0])/2, (p2[1] + p3[1])/2)

a_0_p2_p1 = math.atan2(p2[1] - p1[1], p2[0] - p1[0]) #| angles between the segments
a_0_p2_p3 = math.atan2(p2[1] - p3[1], p2[0] - p3[0])

#T# plot the figure
ax1.plot(list1, list2, 'k')
ax1.plot([.5, .5], [0, 1.2], 'k')
ax1.scatter(list1, list2, s = 12, color = 'k')
ax1.scatter([.5, .5], [0, 1.2], s = 12, color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$|$')
marker1._transform.scale(1, 2.6)
marker1._transform.rotate(a_0_p2_p1)

marker2 = MarkerStyle(r'$|$')
marker2._transform.scale(1, 2.6)
marker2._transform.rotate(a_0_p2_p3)

marker3 = MarkerStyle(r'$|$')
marker3._transform.scale(1, 1.5)
marker3._transform.rotate(a_0_p2_p1 + math.pi/2 + .2)

marker4 = MarkerStyle(r'$|$')
marker4._transform.scale(1, 1.5)
marker4._transform.rotate(a_0_p2_p3 + math.pi/2 - .18)

#T# plot the markers
ax1.plot(p_marker_1_2[0], p_marker_1_2[1], 'k', marker = marker1)
ax1.plot(p_marker_2_3[0], p_marker_2_3[1], 'k', marker = marker2)
ax1.plot(.47, 1.055, 'k', marker = marker3)
ax1.plot(.531, 1.055, 'k', marker = marker4)

#T# plot the angle arc
arc1 = mpatches.Arc(p2, .3, .3, theta1 = math.degrees(-a_0_p2_p3), theta2 = math.degrees(-a_0_p2_p1))
ax1.add_patch(arc1)

#T# place the labels
label1 = ax1.annotate(r'$A$', (0, 0), ha = 'right', va = 'top', size = 16)
label2 = ax1.annotate(r'$B$', (.5, 1.2), ha = 'center', va = 'bottom', size = 16)
label3 = ax1.annotate(r'$C$', (1, 0), ha = 'left', va = 'top', size = 16)
label4 = ax1.annotate(r'$D$', (.5, 0), ha = 'center', va = 'top', size = 16)

#T# drag the labels if needed
label1.draggable()
label2.draggable()
label3.draggable()
label4.draggable()

#T# show the results
plt.show()