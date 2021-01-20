#T# the following code shows how to draw two congruent triangles

#T# to draw two congruent triangles, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw arcs
import matplotlib.patches as mpatches

#T# the transforms module of the matplotlib package, is used to do affine transforms
import matplotlib.transforms as mtransforms

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

#T# create the vertices of one triangle, the other will be the same but rotated and translated
p1 = (0, 0)
p2 = (3, 1)
p3 = (-5, 4)

#T# create the coordinates of these points
list1_1 = [p1[0], p2[0], p3[0], p1[0]] #| x coordinates
list2_1 = [p1[1], p2[1], p3[1], p1[1]] #| y coordinates

#T# create auxiliary points for the segment markers
p_marker_1_2 = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
p_marker_1_3 = ((p1[0] + p3[0])/2, (p1[1] + p3[1])/2)
p_marker_2_3 = ((p2[0] + p3[0])/2, (p2[1] + p3[1])/2)

#T# plot the triangles and their vertices
ax1.plot(list1_1, list2_1, 'k')
ax1.scatter(list1_1, list2_1, s = 12, color = 'k')

trans1 = mtransforms.Affine2D()
trans1.rotate_deg(130).translate(5, 7)
trans1 = trans1 + ax1.transData
ax1.plot(list1_1, list2_1, 'k', transform = trans1)
ax1.scatter(list1_1, list2_1, s = 12, color = 'k', transform = trans1)

#T# plot the arcs for the angle markings
arc1_1 = mpatches.A

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1_1 = MarkerStyle(r'$|$')
marker2_1 = MarkerStyle(r'$||$')
marker3_1 = MarkerStyle(r'$|||$')

marker1_2 = MarkerStyle(r'$|$')
marker2_2 = MarkerStyle(r'$||$')
marker3_2 = MarkerStyle(r'$|||$')

#T# transform the markers to make them the correct shape and size
marker1_1._transform.scale(1, 2.2)
marker1_1._transform.rotate(.35)
marker2_1._transform.scale(1.6, 2.2)
marker2_1._transform.rotate(-.7)
marker3_1._transform.scale(1.6, 2.2)
marker3_1._transform.rotate(-.35)

marker1_2._transform.scale(1, 2.2)
marker1_2._transform.rotate(-.5)
marker2_2._transform.scale(1.6, 2.2)
marker2_2._transform.rotate(1.6)
marker3_2._transform.scale(1.6, 2.2)
marker3_2._transform.rotate(-1.2)

#T# plot the markers
plt.plot(p_marker_1_2[0], p_marker_1_2[1], 'k', marker = marker1_1)
plt.plot(p_marker_1_3[0], p_marker_1_3[1], 'k', marker = marker2_1)
plt.plot(p_marker_2_3[0], p_marker_2_3[1], 'k', marker = marker3_1)

plt.plot(p_marker_1_2[0], p_marker_1_2[1], 'k', marker = marker1_2, transform = trans1)
plt.plot(p_marker_1_3[0], p_marker_1_3[1], 'k', marker = marker2_2, transform = trans1)
plt.plot(p_marker_2_3[0], p_marker_2_3[1], 'k', marker = marker3_2, transform = trans1)

#T# show the results
plt.show()