#T# the following code shows how to draw an angle to show the equidistance in an angle bisector theorem

#T# to draw an angle to show the equidistance in an angle bisector theorem, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

#T# import the math module to do calculations
import math

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

#T# create the variables that define the plot
A = (1.9, 3.8)
B = (0, 0)
C = (4, 0)

a_ABC = math.atan2(A[1], A[0])
a_DBC = a_ABC/2

D = (2.6, 2.6*math.tan(a_DBC))
D2 = (3.6, 3.6*math.tan(a_DBC))

E = (2.6*math.cos(a_ABC), 2.6*math.sin(a_ABC))
F = (2.6*math.cos(0), 2.6*math.sin(0))

a_marker1 = a_DBC/2
a_marker2 = a_DBC*3/2
p_marker1 = (.5*math.cos(a_marker1), .5*math.sin(a_marker1))
p_marker2 = (.5*math.cos(a_marker2), .5*math.sin(a_marker2))

list_x_1a = [A[0], B[0], C[0]]
list_y_1a = [A[1], B[1], C[1]]
list_x_1b = [B[0], D2[0]]
list_y_1b = [B[1], D2[1]]
list_x_1c = [E[0], D[0], F[0]]
list_y_1c = [E[1], D[1], F[1]]

list_x_2 = [A[0], B[0], C[0], D[0], E[0], F[0]]
list_y_2 = [A[1], B[1], C[1], D[1], E[1], F[1]]

#T# plot the figure
ax1.plot(list_x_1a, list_y_1a, 'k')
ax1.plot(list_x_1b, list_y_1b, 'k')
ax1.plot(list_x_1c, list_y_1c, 'k')
ax1.scatter(list_x_2, list_y_2, s = 12, color = 'k')

arc1 = mpatches.Arc(B, 1, 1, theta2 = math.degrees(a_ABC))
ax1.add_patch(arc1)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'|')
marker1._transform.scale(1, 2)
marker1._transform.rotate(math.pi/2 + a_marker1)

marker2 = MarkerStyle(r'|')
marker2._transform.scale(1, 2)
marker2._transform.rotate(math.pi/2 + a_marker2)

#T# plot the markers
ax1.plot(p_marker1[0], p_marker1[1], 'k', marker = marker1)
ax1.plot(p_marker2[0], p_marker2[1], 'k', marker = marker2)

#T# create the labels
label_A = ax1.annotate(r'$A$', A, ha = 'right', va = 'bottom', size = 16)
label_B = ax1.annotate(r'$B$', B, ha = 'right', va = 'top', size = 16)
label_C = ax1.annotate(r'$C$', C, ha = 'left', va = 'top', size = 16)
label_D = ax1.annotate(r'$D$', D, ha = 'left', va = 'top', size = 16)
label_E = ax1.annotate(r'$E$', E, ha = 'right', va = 'center', size = 16)
label_F = ax1.annotate(r'$F$', F, ha = 'center', va = 'top', size = 16)

label_a_E = ax1.annotate(r'$\lrcorner$', E, ha = 'center', size = 26, rotation = math.degrees(a_ABC))
label_a_F = ax1.annotate(r'$\urcorner$', F, size = 26)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()
label_E.draggable()
label_F.draggable()
label_a_E.draggable()
label_a_F.draggable()

#T# show the results
plt.show()