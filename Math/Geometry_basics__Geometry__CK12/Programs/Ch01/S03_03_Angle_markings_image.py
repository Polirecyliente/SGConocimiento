#T# the following code shows how to draw angle markings with arc marks

#T# to draw arc marks, the pyplot module of the matplotlib package is used
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

#T# create one point and five angles to draw five rays with a common vertex
p0 = (0, 0)
a0 = 0
a1 = np.pi/8
a2 = 2*a1
a3 = a2 + np.pi/2 + .15
a4 = np.pi + .5

#T# plot the angles with their arc marks
list_patches1 = []
ray1 = mpatches.FancyArrowPatch(p0, (a0, 1), arrowstyle = '->', mutation_scale = 12)
list_patches1.append(ray1)
ray2 = mpatches.FancyArrowPatch(p0, (a1, 1), arrowstyle = '->', mutation_scale = 12)
list_patches1.append(ray2)
ray3 = mpatches.FancyArrowPatch(p0, (a2, 1), arrowstyle = '->', mutation_scale = 12)
list_patches1.append(ray3)
ray4 = mpatches.FancyArrowPatch(p0, (a3, 1), arrowstyle = '->', mutation_scale = 12)
list_patches1.append(ray4)
ray5 = mpatches.FancyArrowPatch(p0, (a4, 1), arrowstyle = '->', mutation_scale = 12)
list_patches1.append(ray5)
plt.scatter(p0[0], p0[1], s = 6, color = 'k')
for it1 in list_patches1:
    ax1.add_patch(it1)

plt.polar(np.linspace(a0, a4, 30), 0.200*np.ones((30)), 'k', linewidth = 1)
plt.polar(np.linspace(a0, a2, 30), 0.215*np.ones((30)), 'k', linewidth = 1)
plt.polar(np.linspace(a3, a4, 30), 0.215*np.ones((30)), 'k', linewidth = 1)
plt.polar(np.linspace(a3, a4, 30), 0.230*np.ones((30)), 'k', linewidth = 1)
plt.polar([(a0 + a1)/2, (a0 + a1)/2], [.16, .26], 'k', linewidth = 1)
plt.polar([(a1 + a2)/2, (a1 + a2)/2], [.16, .26], 'k', linewidth = 1)

#T# show the results
plt.show()