#T# the following code shows how to draw the rise and run between two points

#T# to draw the rise and run between two points, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

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

#T# create a point and the slope for the line, and three points for the rise and run
p1 = (0, 4/3)
m1 = 2/3

p1_1 = (1, 2)
p2_1 = (4, 2)
p3_1 = (4, 4)

#T# plot the line, and the rise and run
ax1.axline(p1, slope = m1)
ax1.plot([p1_1[0], p2_1[0], p3_1[0]], [p1_1[1], p2_1[1], p3_1[1]], 'k')

#T# label the rise and run
label1 = ax1.annotate('rise', p3_1)
label2 = ax1.annotate('run', p1_1)

#T# drag the labels into better positions after plotting them
label1.draggable()
label2.draggable()

#T# show the results
plt.show()