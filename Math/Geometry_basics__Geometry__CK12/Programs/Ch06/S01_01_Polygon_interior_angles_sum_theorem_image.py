#T# the following code shows how to draw a few polygons to show the polygon interior angles sum theorem

#T# to draw a few polygons to show the polygon interior angles sum theorem, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax_list1 = plt.subplots(1, 2)

#T# set the aspect of the axes
for it1 in fig1.axes:
    it1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in fig1.axes:
    for it2 in ['top', 'bottom', 'left', 'right']:
        it1.spines[it2].set_visible(False)
    it1.xaxis.set_visible(False)
    it1.yaxis.set_visible(False)

#T# create the variables that define the plot
p1_1 = (0, 0)
p2_1 = (4, 1)
p3_1 = (3, 4)
p4_1 = (.5, 2)

list_x1 = [p2_1[0], p3_1[0], p4_1[0], p1_1[0], p2_1[0], p4_1[0]]
list_y1 = [p2_1[1], p3_1[1], p4_1[1], p1_1[1], p2_1[1], p4_1[1]]

p1_2 = (0, 0)
p2_2 = (2, 0)
p3_2 = (4, 2)
p4_2 = (5, 5)
p5_2 = (3, 6)
p6_2 = (-2, 4)
p7_2 = (-1, 1)

list_x2 = [p1_2[0], p2_2[0], p3_2[0], p4_2[0], p5_2[0], p6_2[0], p7_2[0], p1_2[0], p3_2[0], p7_2[0], p4_2[0], p6_2[0]]
list_y2 = [p1_2[1], p2_2[1], p3_2[1], p4_2[1], p5_2[1], p6_2[1], p7_2[1], p1_2[1], p3_2[1], p7_2[1], p4_2[1], p6_2[1]]

#T# plot the figure
ax_list1[0].plot(list_x1, list_y1, 'k')
ax_list1[1].plot(list_x2, list_y2, 'k')

#T# show the results
plt.show()