#T# the following code shows how to draw the shortest distance between a point and a line

#T# to draw the shortest distance between a point and a line, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw arrows
import matplotlib.patches as mpatches

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in ['top', 'right']:
    ax1.spines[it1].set_visible(False)

#T# position the spines and ticks
for it1 in ['bottom', 'left']:
    ax1.spines[it1].set_position(('data', 0))

#T# set the axes size
xmin1 = -8
xmax1 = 8
ymin1 = -8
ymax1 = 8
for it1 in fig1.axes:
    it1.axis([xmin1, xmax1, ymin1, ymax1])

#T# set the ticks labels
list1_1 = list(range(xmin1, xmax1 + 1, 1))
list2_1 = list(range(ymin1, ymax1 + 1, 1))
list1_2 = ['' if it1 == 0 else str(it1) for it1 in list1_1]
list2_2 = ['' if it1 == 0 else str(it1) for it1 in list2_1]
ax1.set_xticks(list1_1)
ax1.set_yticks(list2_1)
ax1.set_xticklabels(list1_2)
ax1.set_yticklabels(list2_2)

#T# draw the grid
ax1.grid(True, alpha = .3)

#T# create the point, and two points for the line
p1 = (1, 6)

p1_1 = (-7, -2)
p2_1 = (7, 5)

#T# calculate the slope of the line, and the slope of the perpendicular line
m1 = (p2_1[1] - p1_1[1])/(p2_1[0] - p1_1[0])
m2 = -1/m1

#T# calculate the y-intercepts of both lines
b1 = p1_1[1] - m1*p1_1[0]
b2 = p1[1] - m2*p1[0]

#T# calculate the point of intersection between the line and the perpendicular line
x2 = (b2 - b1)/(m1 - m2)
y2 = m1*x2 + b1
p2 = (x2, y2)

#T# plot the points and the line
ax1.scatter([p1[0], p2[0]], [p1[1], p2[1]], s = 6, color = 'k')
line1 = mpatches.FancyArrowPatch(p1_1, p2_1, arrowstyle = '<->', mutation_scale = 16)
ax1.add_patch(line1)

#T# plot the perpendicular line
ax1.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the perpendicular mark
marker1 = MarkerStyle(r'$\urcorner$')
marker1._transform.rotate_deg(26)
marker1._transform.translate(.16, .23)

#T# place the perpendicular mark
ax1.scatter(p2[0], p2[1], s = 250, color = 'k', marker = marker1, linewidths = .1)

#T# label the points and the line
label1 = ax1.annotate(r'$A$', p1, ha = 'center', va = 'bottom', size = 16)
label2 = ax1.annotate(r'$B$', p2, ha = 'center', va = 'top', size = 16)
label3 = ax1.annotate(r'$l$', p2_1, ha = 'left', va = 'center', size = 16)
label4 = ax1.annotate(r'$y = m_1x + b_1$', p2_1, ha = 'center', va = 'top', size = 16)

#T# drag the labels into better positions after plotting them
label1.draggable()
label2.draggable()
label3.draggable()
label4.draggable()

#T# show the results
plt.show()