#T# the following code shows how to draw an interior angle of a polygon

#T# to draw an interior angle of a polygon, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw arcs
import matplotlib.patches as mpatches

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'datalim')

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the endpoints of the segments that form the polygon
p1 = (0, 0)
p2 = (2, 0)
p3 = (4, 2)
p4 = (5, 5)
p5 = (3, 6)
p6 = (-2, 4)
p7 = (-1, 1)

#T# create the coordinates of these points
list1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p1[0]] #| x coordinates
list2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p1[1]] #| y coordinates

#T# plot the polygon
ax1.plot(list1, list2, 'k')

#T# plot the arc of the interior angle
arc1 = mpatches.Arc(p1, 1, 1, theta1 = 0, theta2 = 135)
ax1.add_patch(arc1)

#T# plot the vertex of the interior angle
ax1.scatter(p1[0], p1[1], s = 6, color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# label the vertex of the interior angle
label1 = ax1.annotate(r'$A$', p1, ha = 'right', va = 'top', size = 16)

#T# show the results
plt.show()