#T# the following code shows how to draw perpendicular lines

#T# to draw perpendicular lines, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal')

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the variables that define the plot
p0 = (0, 0)
p1 = (2, 0)
p2 = (-2, 0)
p3 = (0, 2)
p4 = (0, -2)

p5 = (3, 0) #| auxiliary points
p6 = (-3, 0)
p7 = (0, 3)
p8 = (0, -3)

list1 = [0, 2, -2, 0, 0] #| x coordinates
list2 = [0, 0, 0, 2, -2] #| y coordinates

#T# set the axes size
ax1.axis([-4, 4, -4, 4])

#T# plot the figure
line1 = mpatches.FancyArrowPatch(p5, p6, arrowstyle = '<->', mutation_scale = 12)
line2 = mpatches.FancyArrowPatch(p7, p8, arrowstyle = '<->', mutation_scale = 12)
ax1.add_patch(line1)
ax1.add_patch(line2)

plt.scatter(list1, list2, color = 'k', s = 6)

plt.plot([.2, .2, .0], [.0, .2, .2], 'k', linewidth = .5)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
plt.text(p0[0], p0[1] - 0.1, r'$A$', ha = 'left', va = 'top', size = 16)
plt.text(p1[0], p1[1] - 0.1, r'$B$', ha = 'center', va = 'top', size = 16)
plt.text(p2[0], p2[1] - 0.1, r'$C$', ha = 'center', va = 'top', size = 16)
plt.text(p3[0], p3[1] + 0.0, r'$D$', ha = 'left', va = 'top', size = 16)
plt.text(p4[0], p4[1] + 0.0, r'$E$', ha = 'left', va = 'top', size = 16)

plt.text(p5[0] + 0.0, p5[1] + 0.0, r'$l$', ha = 'center', va = 'bottom', size = 16)
plt.text(p7[0] + 0.05, p7[1] + 0.1, r'$m$', ha = 'left', va = 'center', size = 16)

#T# show the results
plt.show()