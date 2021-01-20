#T# the following code shows how to draw the remote interior angles of a triangle

#T# to draw the remote interior angles of a triangle, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw arcs and arrows
import matplotlib.patches as mpatches

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and the axes ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

#T# create the vertices of the triangle, and a point for the exterior angle
A, B, C = (1, 2), (8, 2), (6, 6)
D = (-1, 2)

#T# create the coordinates of the vertices
list1 = [A[0], B[0], C[0], A[0]] #| x coordinates
list2 = [A[1], B[1], C[1], A[1]] #| y coordinates

#T# plot the sides of the triangle
ax1.plot(list1, list2, 'k')

#T# plot the exterior angle side
line1 = mpatches.FancyArrowPatch(A, D, arrowstyle = '-', shrinkA = 0, shrinkB = 0, mutation_scale = 12, linewidth = 1.4)
ax1.add_patch(line1)

#T# plot the vertices and an endpoint on the exterior angle side
ax1.scatter(list1, list2, s = 12, color = 'k')
ax1.scatter(D[0], D[1], s = 12, color = 'k')

#T# plot the arc of the exterior angle and the arcs of the remote interior angles
arc1 = mpatches.Arc(A, 1, 1, theta1 = 39, theta2 = 180)
arc2 = mpatches.Arc(B, 1, 1, theta1 = 116.5, theta2 = 180)
arc3 = mpatches.Arc(C, 1, 1, theta1 = 218.5, theta2 = 296.5)
ax1.add_patch(arc1)
ax1.add_patch(arc2)
ax1.add_patch(arc3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# Name the vertices
label_A = ax1.annotate(r'$A$', (A[0], A[1]), ha = 'right', va = 'top', size = 18)
label_B = ax1.annotate(r'$B$', (B[0], B[1]), ha = 'left', va = 'top', size = 18)
label_C = ax1.annotate(r'$C$', (C[0], C[1]), ha = 'center', va = 'bottom', size = 18)
label_D = ax1.annotate(r'$D$', (D[0], D[1]), ha = 'center', va = 'bottom', size = 18)

#T# drag the labels into better positions after plotting them
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()

#T# show the result
plt.show()