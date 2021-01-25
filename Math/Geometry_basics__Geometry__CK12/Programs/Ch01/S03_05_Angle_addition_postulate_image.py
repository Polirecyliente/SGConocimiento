#T# the following code shows how to draw a diagram of the angle addition postulate

#T# to draw a diagram of the angle addition postulate, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# import the pi constant from the math module
from math import pi

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the projection of the axes to polar projection
ax1 = plt.subplot(1, 1, 1, projection = 'polar')

#T# set the aspect of the axes
ax1.set_aspect('equal')

#T# hide the spines and ticks
ax1.spines['polar'].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the variables that define the plot
p0 = (0, 0)
a0 = 0
a1 = pi*1/6
a2 = a1 + pi*3/12

#T# plot the figure
ray1 = mpatches.FancyArrowPatch(p0, (a0, 1), arrowstyle = '->', mutation_scale = 12)
ray2 = mpatches.FancyArrowPatch(p0, (a1, 1), arrowstyle = '->', mutation_scale = 12)
ray3 = mpatches.FancyArrowPatch(p0, (a2, 1), arrowstyle = '->', mutation_scale = 12)
ax1.add_patch(ray1)
ax1.add_patch(ray2)
ax1.add_patch(ray3)
plt.scatter([p0[0], a0, a1, a2], [p0[1], .8, .8, .8], s = 6, color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
plt.text(a2 + .02, .8, r'$A$', ha = 'right', va = 'center', size = 16)
plt.text(a1 + .04, .8, r'$B$', ha = 'right', va = 'center', size = 16)
plt.text(a0 - .03, .8, r'$C$', ha = 'center', va = 'top', size = 16)
plt.text(pi*5/4, .02, r'$D$', ha = 'right', va = 'top', size = 16)

#T# show the results
plt .show()