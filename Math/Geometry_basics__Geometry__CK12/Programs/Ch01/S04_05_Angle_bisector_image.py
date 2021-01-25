#T# the following code shows how to draw an angle bisector

#T# to draw an angle bisector, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

#T# the numpy package is used to facilitate drawing arcs in polar coordinates
import numpy as np

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
a1 = 1.1
a2 = 2*a1

#T# plot the figure
plt.polar([p0[0], a0], [p0[1], 1], 'k')
plt.polar([p0[0], a1], [p0[1], 1], 'k')
plt.polar([p0[0], a2], [p0[1], 1], 'k')
plt.scatter([p0[0], a0, a1, a2], [p0[1], 1, 1, 1], s = 9, color = 'k')

plt.polar(np.linspace(a0, a1, 30), .18*np.ones(30), 'k', linewidth = 1)
plt.polar(np.linspace(a1, a2, 30), .18*np.ones(30), 'k', linewidth = 1)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$|$')
marker1._transform.scale(1, 2.2)
marker1._transform.rotate(np.pi/2 + (a1 + a0)/2)

marker2 = MarkerStyle(r'$|$')
marker2._transform.scale(1, 2.2)
marker2._transform.rotate(np.pi/2 + (a2 + a1)/2)

#T# plot the markers
plt.plot([(a1 + a0)/2], [.18], 'k', marker = marker1)
plt.plot([(a2 + a1)/2], [.18], 'k', marker = marker2)

#T# create the labels
label1 = plt.annotate(r'$A$', p0, ha = 'right', va = 'top', size = 16)
label2 = plt.annotate(r'$B$', (a0, 1), ha = 'center', va = 'top', size = 16)
label3 = plt.annotate(r'$C$', (a1, 1), ha = 'left', va = 'top', size = 16)
label4 = plt.annotate(r'$D$', (a2, 1), ha = 'right', va = 'top', size = 16)

#T# drag the labels if needed
label1.draggable()
label2.draggable()
label3.draggable()
label4.draggable()

#T# show the results
plt.show()