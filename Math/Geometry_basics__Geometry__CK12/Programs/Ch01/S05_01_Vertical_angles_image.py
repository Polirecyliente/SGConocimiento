#T# the following code shows how to draw vertical angles in the intersection of two lines

#T# to draw vertical angles, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw arrows
import matplotlib.patches as mpatches

#T# the numpy package is used to facilitate drawing arcs in polar coordinates
import numpy as np

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the projection of the axes to polar projection
ax1 = plt.subplot(1, 1, 1, projection = 'polar')

#T# set the aspect of the axes
ax1.set_aspect('equal')

#T# hide the spine and axes ticks
ax1.spines['polar'].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the vertex and two angles (one angle for each of the two lines in the intersection)
p0 = (0, 0)
a1 = 0.22
a2 = 1.10

#T# plot the lines and the arcs of the angles
line1 = mpatches.FancyArrowPatch((a1 + np.pi, 1), (a1, 1), arrowstyle = '<->', mutation_scale = 12, linewidth = 1.3)
line2 = mpatches.FancyArrowPatch((a2 + np.pi, 1), (a2, 1), arrowstyle = '<->', mutation_scale = 12, linewidth = 1.3)
ax1.add_patch(line1)
ax1.add_patch(line2)

plt.polar(np.linspace(0, 2*np.pi, 30), .18*np.ones(30), 'k', linewidth = 1)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# label the angles
label1 = plt.annotate(r'$\alpha_1$', ((a1 + a2)/2, .18), ha = 'left', va = 'bottom', size = 16)
label2 = plt.annotate(r'$\alpha_2$', ((a1 + a2)/2 + np.pi, .18), ha = 'right', va = 'top', size = 16)
label3 = plt.annotate(r'$\beta_1$', ((a2 + a1 + np.pi)/2, .18), ha = 'right', va = 'bottom', size = 16)
label4 = plt.annotate(r'$\beta_2$', ((a2 + a1 + np.pi)/2 + np.pi, .18), ha = 'left', va = 'top', size = 16)

#T# drag the labels into better positions after plotting them
label1.draggable()
label2.draggable()
label3.draggable()
label4.draggable()

#T# show the results
plt.show()