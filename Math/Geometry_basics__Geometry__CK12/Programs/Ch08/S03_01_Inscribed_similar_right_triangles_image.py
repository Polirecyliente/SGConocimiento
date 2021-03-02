#T# the following code shows how to draw a right triangle with its two inscribed similar right triangles

#T# to draw a right triangle with its two inscribed similar right triangles, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

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
B = (2, 0)
C = (0, 3)

aC = math.atan2(B[0], C[1])
lD = B[0]*math.cos(aC)
D = (lD*math.cos(aC), lD*math.sin(aC))

list_x_1 = [A[0], B[0], C[0], A[0], D[0]]
list_y_1 = [A[1], B[1], C[1], A[1], D[1]]

#T# plot the figure
plt.plot(list_x_1, list_y_1, 'o-k', markersize = 3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 16)
label_B = ax1.annotate(r'$B$', B, size = 16)
label_C = ax1.annotate(r'$C$', C, size = 16)
label_D = ax1.annotate(r'$D$', D, size = 16)
a_marker1 = ax1.annotate(r'$\urcorner$', (1, 1), size = 28)
a_marker2 = ax1.annotate(r'$\llcorner$', (1, 1.5), size = 24, rotation = math.degrees(aC))

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()
a_marker1.draggable()
a_marker2.draggable()

#T# show the results
plt.show()