#T# the following code shows how to draw parallel lines

#T# to draw parallel lines, the pyplot module of the matplotlib package is used
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
p1 = (0, 5)
p2 = (0, 3)
p3 = (6, 2)
p4 = (7.5, 2)

run1 = 5
rise1 = 2
run2 = 2
rise2 = 6

p1_2 = (p1[0] + run1, p1[1] + rise1) #| second points of each line
p2_2 = (p2[0] + run1, p2[1] + rise1)
p3_2 = (p3[0] + run2, p3[1] + rise2)
p4_2 = (p4[0] + run2, p4[1] + rise2)

p1_markA = (p1[0] + run1/2.1, p1[1] + rise1/2.1) #| auxiliary points for the parallel line marks
p1_markB = (p1[0] + run1/2, p1[1] + rise1/2)

p2_markA = (p2[0] + run1/2.1, p2[1] + rise1/2.1)
p2_markB = (p2[0] + run1/2, p2[1] + rise1/2)

p3_mark1A = (p3[0] + run2/2.0, p3[1] + rise2/2.0)
p3_mark1B = (p3[0] + run2/1.9, p3[1] + rise2/1.9)
p3_mark2A = (p3[0] + run2/2.2, p3[1] + rise2/2.2)
p3_mark2B = (p3[0] + run2/2.1, p3[1] + rise2/2.1)

p4_mark1A = (p4[0] + run2/2.0, p4[1] + rise2/2.0)
p4_mark1B = (p4[0] + run2/1.9, p4[1] + rise2/1.9)
p4_mark2A = (p4[0] + run2/2.2, p4[1] + rise2/2.2)
p4_mark2B = (p4[0] + run2/2.1, p4[1] + rise2/2.1)

#T# set the axes size
ax1.axis([p1[0], p4_2[0] + .5, p3[1], p3_2[1]])

#T# plot the figure
line1 = mpatches.FancyArrowPatch(p1, p1_2, arrowstyle = '<->', mutation_scale = 12)
line2 = mpatches.FancyArrowPatch(p2, p2_2, arrowstyle = '<->', mutation_scale = 12)
line3 = mpatches.FancyArrowPatch(p3, p3_2, arrowstyle = '<->', mutation_scale = 12)
line4 = mpatches.FancyArrowPatch(p4, p4_2, arrowstyle = '<->', mutation_scale = 12)
ax1.add_patch(line1)
ax1.add_patch(line2)
ax1.add_patch(line3)
ax1.add_patch(line4)

mark1 = mpatches.FancyArrowPatch(p1_markA, p1_markB, arrowstyle = '->', mutation_scale = 20) #| parallel line marks
mark2 = mpatches.FancyArrowPatch(p2_markA, p2_markB, arrowstyle = '->', mutation_scale = 20)
mark3_1 = mpatches.FancyArrowPatch(p3_mark1A, p3_mark1B, arrowstyle = '->', mutation_scale = 20)
mark3_2 = mpatches.FancyArrowPatch(p3_mark2A, p3_mark2B, arrowstyle = '->', mutation_scale = 20)
mark4_1 = mpatches.FancyArrowPatch(p4_mark1A, p4_mark1B, arrowstyle = '->', mutation_scale = 20)
mark4_2 = mpatches.FancyArrowPatch(p4_mark2A, p4_mark2B, arrowstyle = '->', mutation_scale = 20)
ax1.add_patch(mark1)
ax1.add_patch(mark2)
ax1.add_patch(mark3_1)
ax1.add_patch(mark3_2)
ax1.add_patch(mark4_1)
ax1.add_patch(mark4_2)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label1 = plt.annotate(r'$k$', p1_2, ha = 'left', va = 'bottom', size = 16)
label2 = plt.annotate(r'$l$', p2_2, ha = 'left', va = 'bottom', size = 16)
label3 = plt.annotate(r'$m$', p3_2, ha = 'left', va = 'bottom', size = 16)
label4 = plt.annotate(r'$n$', p4_2, ha = 'left', va = 'bottom', size = 16)

#T# drag the labels if needed
label1.draggable()
label2.draggable()
label3.draggable()
label4.draggable()

#T# show the results
plt.show()