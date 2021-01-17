#T# the following code shows how to draw the slope of a line with different values

#T# to draw the slope of a line with different values, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to create bidirectional arrows
import matplotlib.patches as mpatches

#T# the numpy package is used to manage and use numpy arrays
import numpy as np

#T# create the figure and axes
fig1, axes1 = plt.subplots(2, 2)

#T# set the aspect of the axes
for it1 in fig1.axes:
    it1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in ['top', 'right']:
    for it2 in fig1.axes:
        it2.spines[it1].set_visible(False)

#T# position the spines and ticks
for it1 in ['bottom', 'left']:
    for it2 in fig1.axes:
        it2.spines[it1].set_position(('data', 0))
        
#T# set the axes size
xmin1 = -8
xmax1 = 8
ymin1 = -8
ymax1 = 8
for it1 in fig1.axes:
    it1.axis([xmin1, xmax1, ymin1, ymax1])

#T# set the ticks labels
list1_1 = list(range(xmin1, xmax1 + 1, 2))
list1_2 = list(range(ymin1, ymax1 + 1, 2))
list2_1 = ['' if it1 == 0 else str(it1) for it1 in list1_1]
list2_2 = ['' if it1 == 0 else str(it1) for it1 in list1_2]
for it1 in fig1.axes:
    it1.set_xticks(list1_1)
    it1.set_yticks(list1_2)
    it1.set_xticklabels(list2_1)
    it1.set_yticklabels(list2_2)

#T# set the ticks labels size
for it1 in fig1.axes:
    it1.tick_params(labelsize = 8)

#T# draw the grid
for it1 in fig1.axes:
    it1.grid(True, which = 'both', alpha = .3)
    it1.minorticks_on()

#T# place the arrowheads of the axes
for it1 in fig1.axes:
    it1.plot(0, 8.3, '^k', clip_on = False)
    it1.plot(0, -8.3, 'vk', clip_on = False)
    it1.plot(-8.3, 0, '<k', clip_on = False)
    it1.plot(8.3, 0, '>k', clip_on = False)

#T# set the title of each pair of axes
fig1.axes[0].set_title('Positive slope', y = 1.1)
fig1.axes[1].set_title('Negative slope', y = 1.1)
fig1.axes[2].set_title('Zero slope', y = 1.1)
fig1.axes[3].set_title('Undefined slope', y = 1.1)

#T# set the position of the subplots with regards to one another
fig1.tight_layout()

#T# create two points per line
p1_1 = (-8, -3)
p2_1 = (2, 5)

p1_2 = (.5, 7)
p2_2 = (8, 4)

p1_3 = (-6, 2)
p2_3 = (6, 2)

p1_4 = (-5, -6)
p2_4 = (-5, 6)

#T# plot the lines
line1 = mpatches.FancyArrowPatch(p1_1, p2_1, color = 'cornflowerblue', arrowstyle = '<->', mutation_scale = 16)
line2 = mpatches.FancyArrowPatch(p1_2, p2_2, color = 'cornflowerblue', arrowstyle = '<->', mutation_scale = 16)
line3 = mpatches.FancyArrowPatch(p1_3, p2_3, color = 'cornflowerblue', arrowstyle = '<->', mutation_scale = 16)
line4 = mpatches.FancyArrowPatch(p1_4, p2_4, color = 'cornflowerblue', arrowstyle = '<->', mutation_scale = 16)
fig1.axes[0].add_patch(line1)
fig1.axes[1].add_patch(line2)
fig1.axes[2].add_patch(line3)
fig1.axes[3].add_patch(line4)

#T# show the results
plt.show()