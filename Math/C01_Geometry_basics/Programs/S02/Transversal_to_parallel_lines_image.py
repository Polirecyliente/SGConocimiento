#T# the following code shows how to draw a transversal line to two parallel lines

#T# to draw a transversal line to two parallel lines, the pyplot module of the matplotlib package is used
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
p1_1 = (-2, 0)
p2_1 = (7, 0)

p1_2 = (-3, 2)
p2_2 = (6, 2)

p1_3 = (2.5, -2) #| points for the transversal
p2_3 = (3.5, 5)

#T# set the axes size
num1 = min(p1_1[0], p2_1[0], p1_2[0], p2_2[0], p1_3[0], p2_3[0])
num2 = max(p1_1[0], p2_1[0], p1_2[0], p2_2[0], p1_3[0], p2_3[0])
num3 = min(p1_1[1], p2_1[1], p1_2[1], p2_2[1], p1_3[1], p2_3[1])
num4 = max(p1_1[1], p2_1[1], p1_2[1], p2_2[1], p1_3[1], p2_3[1])
ax1.axis([num1, num2, num3, num4])

#T# plot the figure
line1 = mpatches.FancyArrowPatch(p1_1, p2_1, arrowstyle = '<->', mutation_scale = 12)
line2 = mpatches.FancyArrowPatch(p1_2, p2_2, arrowstyle = '<->', mutation_scale = 12)
line3 = mpatches.FancyArrowPatch(p1_3, p2_3, arrowstyle = '<->', mutation_scale = 12) #| the transversal line
ax1.add_patch(line1)
ax1.add_patch(line2)
ax1.add_patch(line3)

mark1 = mpatches.FancyArrowPatch((3.9, 0), (5.5,0), arrowstyle = '->', mutation_scale = 20) #| parallel line marks
mark2 = mpatches.FancyArrowPatch((3.9, 2), (4.5,2), arrowstyle = '->', mutation_scale = 20)
ax1.add_patch(mark1)
ax1.add_patch(mark2)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label1 = plt.annotate(r'$m$', p2_1, ha = 'left', va = 'bottom', size = 16)
label2 = plt.annotate(r'$l$', p2_2, ha = 'left', va = 'bottom', size = 16)
label3 = plt.annotate(r'$t$', p2_3, ha = 'left', va = 'bottom', size = 16)

label_a1 = plt.annotate(r'$1$', (3, 2.5), ha = 'right', va = 'top', size = 16)
label_a2 = plt.annotate(r'$2$', (3.5, 2.5), ha = 'right', va = 'top', size = 16)
label_a3 = plt.annotate(r'$3$', (2.9, 1.9), ha = 'right', va = 'top', size = 16)
label_a4 = plt.annotate(r'$4$', (3.4, 1.9), ha = 'right', va = 'top', size = 16)
label_a5 = plt.annotate(r'$5$', (2.7, .45), ha = 'right', va = 'top', size = 16)
label_a6 = plt.annotate(r'$6$', (3.2, .45), ha = 'right', va = 'top', size = 16)
label_a7 = plt.annotate(r'$7$', (2.6, -.15), ha = 'right', va = 'top', size = 16)
label_a8 = plt.annotate(r'$8$', (3.1, -.15), ha = 'right', va = 'top', size = 16)

#T# drag the labels if needed
label1.draggable()
label2.draggable()
label3.draggable()

#T# show the results
plt.show()