#T# the following code shows how to draw an angle from two rays

#T# to draw an angle from two rays, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw arrows and arcs
import matplotlib.patches as mpatches

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal')

#T# hide the spines and the axes ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# import the math module to calculate the angle between the rays
import math

#T# create three points, i.e. one single endpoint and two points each on its own distinct ray
p1 = (3, 2)
p2 = (0, 0)
p3 = (4, 0)

#T# create two auxiliary points to lengthen the rays
p4 = (4.5, 3)
p5 = (6, 0)

#T# create the coordinates of the points
list1 = [3, 0, 4] #| x coordinates
list2 = [2, 0, 0] #| y coordinates

#T# set the axes size
ax1.axis([-1, 7, -1, 5.5])

#T# plot the rays and the arc of the angle
ray1 = mpatches.FancyArrowPatch(p2, p4, arrowstyle = '->', mutation_scale = 12)
ray2 = mpatches.FancyArrowPatch(p2, p5, arrowstyle = '->', mutation_scale = 12)
ax1.add_patch(ray1)
ax1.add_patch(ray2)
plt.scatter(list1, list2, color = 'k')

arc1 = mpatches.Arc(p2, 1, 1, theta1 = 0, theta2 = math.degrees(math.atan2(p1[1], p1[0])))
ax1.add_patch(arc1)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# label the points and the angle
plt.text(p1[0] - 0.05, p1[1] + 0.05, r'$A$', ha = 'right', va = 'bottom', size = 16)
plt.text(p2[0] - 0.1, p2[1] - 0.1, r'$B$', ha = 'right', va = 'top', size = 16)
plt.text(p3[0] - 0.0, p3[1] - 0.1, r'$C$', ha = 'center', va = 'top', size = 16)

plt.text(p2[0] + 0.53, p2[1], r'$\theta$', ha = 'left', va = 'bottom', size = 16)

#T# show the results
plt.show()