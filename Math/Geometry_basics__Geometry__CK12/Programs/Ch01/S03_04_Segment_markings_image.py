#T# the following code shows how to draw segment markings with hash marks

#T# to draw segment markings with hash marks, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

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
p1_1 = [0, 1]
p1_2 = [1, 1]
p2_1 = [2, 1]
p2_2 = [5, 1]
p3_1 = [0, 0]
p3_2 = [2, 0]
p4_1 = [3, 0]
p4_2 = [5, 0]

p1 = [0.5, 1] #| midpoints of the segments
p2 = [3.5, 1]
p3 = [1.0, 0]
p4 = [4.0, 0]

list1 = [0, 1, 2, 5, 0, 2, 3, 5] #| x coordinates of the endpoints of the segments
list2 = [1, 1, 1, 1, 0, 0, 0, 0] #| y coordinates of the endpoints of the segments

#T# set the axes size
ax1.axis([-1, 6, -1, 2])

#T# plot the figure
plt.plot([p1_1[0], p1_2[0]], [p1_1[1], p1_2[1]], 'k')
plt.plot([p2_1[0], p2_2[0]], [p2_1[1], p2_2[1]], 'k')
plt.plot([p3_1[0], p3_2[0]], [p3_1[1], p3_2[1]], 'k')
plt.plot([p4_1[0], p4_2[0]], [p4_1[1], p4_2[1]], 'k')
plt.scatter(list1, list2, s = 6, color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$|$')
marker1._transform.scale(1.6, 1.4)

marker2 = MarkerStyle(r'$||$')
marker2._transform.scale(1.6, 1.4)

marker3 = MarkerStyle(r'$|||$')
marker3._transform.scale(1.6, 1.4)

#T# plot the markers
plt.plot(p1[0], p1[1], 'k', marker = marker1)
plt.plot(p2[0], p2[1], 'k', marker = marker2)
plt.plot(p3[0], p3[1], 'k', marker = marker3)
plt.plot(p4[0], p4[1], 'k', marker = marker3)

#T# show the results
plt.show()