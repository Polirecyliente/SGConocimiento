#T# the following code shows how to draw a transversal line

#T# to draw a transversal line, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
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

#T# create the variables that define the plot
p1_1 = (-2, 1)
p2_1 = (7, 3)

p1_2 = (-3, 4)
p2_2 = (6, -1)

p1_3 = (4.5, -2) #| points for the transversal
p2_3 = (5.5, 5)

#T# set the axes size
num1 = min(p1_1[0], p2_1[0], p1_2[0], p2_2[0], p1_3[0], p2_3[0])
num2 = max(p1_1[0], p2_1[0], p1_2[0], p2_2[0], p1_3[0], p2_3[0])
num3 = min(p1_1[1], p2_1[1], p1_2[1], p2_2[1], p1_3[1], p2_3[1])
num4 = max(p1_1[1], p2_1[1], p1_2[1], p2_2[1], p1_3[1], p2_3[1])
ax1.axis([num1, num2, num3, num4])

#T# plot the figure
line1 = mpatches.FancyArrowPatch(p1_1, p2_1, arrowstyle = '<->', mutation_scale = 12)
line2 = mpatches.FancyArrowPatch(p1_2, p2_2, arrowstyle = '<->', mutation_scale = 12)
line3 = mpatches.FancyArrowPatch(p1_3, p2_3, color = 'lime', arrowstyle = '<->', mutation_scale = 12) #| the transversal line
ax1.add_patch(line1)
ax1.add_patch(line2)
ax1.add_patch(line3)

#T# show the results
plt.show()