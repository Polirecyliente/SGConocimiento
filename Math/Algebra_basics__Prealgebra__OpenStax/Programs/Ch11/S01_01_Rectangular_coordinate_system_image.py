#T# the following code shows a rectangular coordinate system with its quadrants

#T# to show the rectangular coordinate system, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes in which to plot the rectangular coordinate system
fig1 = plt.Figure()
ax1 = plt.axes()

#T# set the aspect ratio
ax1.set_aspect('equal')

#T# show the grid
ax1.grid(True)

#T# set the positions and visibility of the spines
ax1.spines['left'].set_position(('data', 0))
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

#T# set the axes limits
ax1.axis([-2, 2, -2, 2])

#T# put the arrow tips
plt.plot(-2.04, 0, 'k<', clip_on = False)
plt.plot(2.04, 0, 'k>', clip_on = False)
plt.plot(0, -2.04, 'kv', clip_on = False)
plt.plot(0, 2.04, 'k^', clip_on = False)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# annotate the axes and the quadrants
plt.text(2, 0.05, r'$x$', va = 'bottom')
plt.text(0.1, 2, r'$y$', ha = 'left')
plt.text(1, 1, r'$I$', ha = 'center', va = 'center', size = 15)
plt.text(-1, 1, r'$II$', ha = 'center', va = 'center', size = 15)
plt.text(-1, -1, r'$III$', ha = 'center', va = 'center', size = 15)
plt.text(1, -1, r'$IV$', ha = 'center', va = 'center', size = 15)

#T# show the results
plt.show()