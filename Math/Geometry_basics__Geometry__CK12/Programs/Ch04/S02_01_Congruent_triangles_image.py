#T# the following code shows how to draw two congruent triangles

#T# to draw two congruent triangles, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and the axes ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

#T# create the vertices of each triangle
p1_1 = (0, 0)
p2_1 = (3, 1)
p3_1 = (-5, 4)

p1_2 = ()
p2_2 = ()
p3_2 = ()

#T# create the coordinates of these points
list1_1 = [p1_1[0], p2_1[0], p3_1[0], p1_1[0]] #| x coordinates
list2_1 = [p1_1[1], p2_1[1], p3_1[1], p1_1[1]] #| y coordinates

#T# create auxiliary points for the segment markers
#p0_p1_marker = (p1[0], p1[1]/2)
#p0_p2_marker = (p2[0], p2[1]/2)
p1_p2_marker = (1.8, .76)

#T# plot the triangles
plt.plot(list1_1, list2_1, 'k')
plt.show(); quit()
#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$|$')
marker2 = MarkerStyle(r'$||$')
marker3 = MarkerStyle(r'$|||$')

#T# transform the markers to make them the correct shape and size
marker1._transform.scale(1, 2.2)
marker1._transform.rotate(p0_p1_marker[0] + .05)
marker2._transform.scale(1.6, 2.2)
marker2._transform.rotate(p0_p2_marker[0] - .05)
marker3._transform.scale(1.6, 2.2)
marker3._transform.rotate(p1_p2_marker[0] + .9)

#T# plot the markers
plt.plot(p0_p1_marker[0], p0_p1_marker[1], 'k', marker = marker1)
plt.plot(p0_p2_marker[0], p0_p2_marker[1], 'k', marker = marker2)
plt.plot(p1_p2_marker[0], p1_p2_marker[1], 'k', marker = marker3)

#T# show the results
plt.show()