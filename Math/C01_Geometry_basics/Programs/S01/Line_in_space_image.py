#T# the following code shows how to draw a line in a two dimensional space

#T# to draw a line in a two dimensional space, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the variables that define the plot
p1 = (4, 3)
p2 = (7, 5)

rise1 = p2[1] - p1[1]
run1 = p2[0] -p1[0]

k1 = 3 #| factor to readjust the rise and run to make the line fit on the plot with better proportions (i.e. to make a shorter arrow)
rise1 = rise1/k1
run1 = run1/k1

#T# plot the figure
line1 = mpatches.FancyArrowPatch((p1[0] - run1, p1[1] - rise1), (p2[0] + run1, p2[1] + rise1), arrowstyle = '<->', mutation_scale = 12)
ax1.add_patch(line1)
plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
plt.text(p1[0] - 0.05, p1[1] + 0.05, r'$P$', ha = 'right', va = 'bottom', size = 16)
plt.text(p2[0] - 0.05, p2[1] + 0.05, r'$Q$', ha = 'right', va = 'bottom', size = 16)
plt.text(p2[0] + run1, p2[1] + rise1, r'$g$', ha = 'left', va = 'top', size = 16)

#T# show the results
plt.show()