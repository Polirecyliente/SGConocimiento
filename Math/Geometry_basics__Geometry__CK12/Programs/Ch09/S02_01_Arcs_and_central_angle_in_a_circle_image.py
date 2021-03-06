#T# the following code shows how to draw a circle with a central angle and major and minor arcs

#T# to draw a circle with a central angle and major and minor arcs, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# import the math module to do calculations
import math

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
A = (0, 0)
r_A = 1

a_0_AB = math.pi/4.5
a_0_AC = math.pi/1.2
a_0_AD = math.pi*3/2.5

B = (A[0] + r_A*math.cos(a_0_AB), A[1] + r_A*math.sin(a_0_AB))
C = (A[0] + r_A*math.cos(a_0_AC), A[1] + r_A*math.sin(a_0_AC))
D = (A[0] + r_A*math.cos(a_0_AD), A[1] + r_A*math.sin(a_0_AD))

list_x_1 = [B[0], A[0], C[0]]
list_y_1 = [B[1], A[1], C[1]]

#T# plot the figure
circle1 = mpatches.Arc(A, 2*r_A, 2*r_A, linewidth = 1.5)
ax1.add_patch(circle1)

ax1.plot(list_x_1, list_y_1, 'o-k', markersize = 3)
ax1.plot(D[0], D[1], 'ok', markersize = 3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 16)
label_B = ax1.annotate(r'$B$', B, size = 16)
label_C = ax1.annotate(r'$C$', C, size = 16)
label_D = ax1.annotate(r'$D$', D, size = 16)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()

#T# show the results
ax1.autoscale()
plt.show()