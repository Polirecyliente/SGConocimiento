#T# the following code shows how to draw a few right angles as an example of the right angle theorem

#T# to draw a few right angles as an example of the right angle theorem, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

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
p1_1 = (2, 0)
p2_1 = (0, 0) #| vertex
p3_1 = (0, 3)

p1_2 = (1, 6)
p2_2 = (-1, 4) #| vertex
p3_2 = (-3, 6)

list1_1 = [p1_1[0], p2_1[0], p3_1[0]] #| x coordinates
list2_1 = [p1_1[1], p2_1[1], p3_1[1]] #| y coordinates

list1_2 = [p1_2[0], p2_2[0], p3_2[0]] #| x coordinates
list2_2 = [p1_2[1], p2_2[1], p3_2[1]] #| y coordinates

#T# plot the figure
plt.plot(list1_1, list2_1, 'k')
plt.plot(list1_2, list2_2, 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$\ulcorner$')
marker1._transform.rotate_deg(-90)
marker1._transform.translate(.1, .35)
marker2 = MarkerStyle(r'$\ulcorner$')
marker2._transform.rotate_deg(-45)
marker2._transform.translate(-.2, .3)

#T# plot the markers
plt.scatter(p2_1[0], p2_1[1], s = 250, color = 'k', marker = marker1, linewidths = 0.1)
plt.scatter(p2_2[0], p2_2[1], s = 250, color = 'k', marker = marker2, linewidths = 0.1)

#T# show the results
plt.show()