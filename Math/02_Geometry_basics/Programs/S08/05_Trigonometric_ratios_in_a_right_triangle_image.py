#T# the following code shows how to draw a right triangle to show the trigonometric ratios

#T# to draw a right triangle to show the trigonometric ratios, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

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

list_x_1 = [A[0], B[0], C[0], A[0]]
list_y_1 = [A[1], B[1], C[1], A[1]]

#T# plot the figure
plt.plot(list_x_1, list_y_1, 'o-k', markersize = 3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 16)
label_B = ax1.annotate(r'$B$', B, size = 16)
label_C = ax1.annotate(r'$C$', C, size = 16)
label_a = ax1.annotate(r'$a$', (1, 0), size = 16)
label_b = ax1.annotate(r'$b$', (1, 1), size = 16)
label_c = ax1.annotate(r'$c$', (1, 2), size = 16)
a_marker1 = ax1.annotate(r'$\urcorner$', (1, 1), size = 28)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_a.draggable()
label_b.draggable()
label_c.draggable()
a_marker1.draggable()

#T# show the results
plt.show()