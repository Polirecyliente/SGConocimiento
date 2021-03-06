#T# the following code shows how to draw a segment bisector at an arbitrary angle

#T# to draw a segment bisector at an arbitrary angle, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

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
p1 = (-1.3, 0)
p2 = (1.3, 0)
p3 = (.3, -1)
p4 = (-.3, 1)

p5 = (.24, -.8) #| auxiliary points
p6 = (-.24, .8)

list1 = [p0[0], p1[0], p2[0]] #| x coordinates of the segment
list2 = [p0[1], p1[1], p2[1]] #| y coordinates of the segment

list3 = [p3[0], p4[0]] #| x coordinates of the bisector
list4 = [p3[1], p4[1]] #| y coordinates of the bisector

#T# plot the figure
plt.plot(list1, list2, 'k')
plt.scatter(list1, list2, s = 6, color = 'k')
plt.scatter([p5[0], p6[0]], [p5[1], p6[1]], s = 6, color = 'k')

line1 = mpatches.FancyArrowPatch(p3, p4, arrowstyle = '<->', mutation_scale = 12, linewidth = 1.3)
ax1.add_patch(line1)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$|$')
marker1._transform.scale(1, 2.2)

#T# plot the markers
plt.plot([(p1[0] + p0[0])/2, (p2[0] + p0[0])/2], [(p1[1] + p0[1])/2, (p2[1] + p0[1])/2], 'k', marker = marker1)

#T# create the labels
label1 = plt.annotate(r'$A$', p1, ha = 'center', va = 'bottom', size = 16)
label2 = plt.annotate(r'$B$', p0, ha = 'right', va = 'top', size = 16)
label3 = plt.annotate(r'$C$', p2, ha = 'center', va = 'bottom', size = 16)
label4 = plt.annotate(r'$D$', p6, ha = 'left', va = 'bottom', size = 16)
label5 = plt.annotate(r'$E$', p5, ha = 'left', va = 'bottom', size = 16)

#T# drag the labels if needed
label1.draggable()
label2.draggable()
label3.draggable()
label4.draggable()
label5.draggable()

#T# show the results
plt.show()