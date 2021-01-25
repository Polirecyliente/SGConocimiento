#T# the following code shows how to draw the slope of the perpendicular line to a given line

#T# to draw the slope of the perpendicular line to a given line, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

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

#T# create the variables that define the plot
p1 = (0, 0)
m1 = 3

p2 = (0, 0)
m2 = -1/m1

#T# plot the figure
ax1.axline((p1[0], p1[1]), slope = m1)
ax1.axline((p1[0], p1[1]), slope = -m1, color = 'limegreen')
ax1.axline((p2[0], p2[1]), slope = m2, color = 'crimson')

#T# show the results
plt.show()