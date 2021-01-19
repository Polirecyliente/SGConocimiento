#T# the following code shows how to draw the exterior angles of a triangle

#T# to draw the exterior angles of a triangle, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to create bidirectional arrows
import matplotlib.patches as mpatches

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'datalim')

#T# hide the spines and the axes ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create two points per line in each of the sides of the triangle
p1_1 = (-2, 1)
p2_1 = (7, 3)

p1_2 = (-3, 4)
p2_2 = (6, -1)

p1_3 = (4.5, -2)
p2_3 = (5.5, 5)

#T# set the axes size
num1 = min(p1_1[0], p2_1[0], p1_2[0], p2_2[0], p1_3[0], p2_3[0])
num2 = max(p1_1[0], p2_1[0], p1_2[0], p2_2[0], p1_3[0], p2_3[0])
num3 = min(p1_1[1], p2_1[1], p1_2[1], p2_2[1], p1_3[1], p2_3[1])
num4 = max(p1_1[1], p2_1[1], p1_2[1], p2_2[1], p1_3[1], p2_3[1])
ax1.axis([num1, num2, num3, num4])

#T# plot the lines
line1 = mpatches.FancyArrowPatch(p1_1, p2_1, shrinkA = 65, shrinkB = 72, arrowstyle = '<-', mutation_scale = 12)
line2 = mpatches.FancyArrowPatch(p1_2, p2_2, shrinkA = 181, arrowstyle = '->', mutation_scale = 12)
line3 = mpatches.FancyArrowPatch(p1_3, p2_3, shrinkA = 66, shrinkB = 35, arrowstyle = '->', mutation_scale = 12)
ax1.add_patch(line1)
ax1.add_patch(line2)
ax1.add_patch(line3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# label the angles
label_1 = ax1.annotate(r'$1$', (0, 1), size = 16)
label_2 = ax1.annotate(r'$2$', (1, 1), size = 16)
label_3 = ax1.annotate(r'$3$', (2, 1), size = 16)
label_4 = ax1.annotate(r'$4$', (3, 1), size = 16)
label_5 = ax1.annotate(r'$5$', (4, 1), size = 16)
label_6 = ax1.annotate(r'$6$', (5, 1), size = 16)

#T# drag the labels into better positions after plotting them
label_1.draggable()
label_2.draggable()
label_3.draggable()
label_4.draggable()
label_5.draggable()
label_6.draggable()

#T# show the results
plt.show()