#T# the following code shows how to draw an isosceles triangle with its parts

#T# to draw an isosceles triangle with its parts, the pyplot module of the matplotlib package is used
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

#T# plot the markers
ax1.plot(p_marker_1_2[0], p_marker_1_2[1], 'k', marker = marker1)
ax1.plot(p_marker_2_3[0], p_marker_2_3[1], 'k', marker = marker2)

#T# create the labels
label1 = ax1.annotate(r'$Base\ angles$', (.97, .03), xytext = (.5, .13), ha = 'center', size = 16, arrowprops = {'arrowstyle': '->'})
label2 = ax1.annotate(r'$Base\ angles$', (.03, .03), xytext = (.5, .13), ha = 'center', size = 16, arrowprops = {'arrowstyle': '->'})
label3 = ax1.annotate(r'$Vertex\ angle$', (.5, 1.15), xytext = (.8, .8), size = 16, arrowprops = {'arrowstyle': '->', 'connectionstyle': 'arc3, rad = -.9'})
label_leg1 = ax1.annotate(r'$Leg$', p_marker_1_2, ha = 'right', va = 'center', size = 16)
label_leg2 = ax1.annotate(r'$Leg$', p_marker_2_3, ha = 'left', va = 'center', size = 16)
label_base1 = ax1.annotate(r'$Base$', (.5, -.1), ha = 'center', size = 16)

#T# drag the labels if needed
label1.draggable()
label2.draggable()
label3.draggable()
label_leg1.draggable()
label_leg2.draggable()

#T# show the results
plt.show()