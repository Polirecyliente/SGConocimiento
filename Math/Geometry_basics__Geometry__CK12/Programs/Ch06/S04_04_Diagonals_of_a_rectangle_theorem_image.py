#T# the following code shows how to draw a rectangle to show the diagonals of a rectangle theorem

#T# to draw a rectangle to show the diagonals of a rectangle theorem, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the variables that define the plot
A = (0, 0)
B = (5, 0)
C = (5, 2.4)
D = (0, 2.4)
E = (2.5, 1.2)

list_x1 = [A[0], B[0], C[0], D[0], A[0]]
list_y1 = [A[1], B[1], C[1], D[1], A[1]]

#T# plot the figure
ax1.plot(list_x1, list_y1, 'k', marker = 'o', markersize = 3)
ax1.plot([A[0], E[0], C[0]], [A[1], E[1], C[1]], 'k', marker = 'o', markersize = 3)
ax1.plot([B[0], D[0]], [B[1], D[1]], 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 18)
label_B = ax1.annotate(r'$B$', B, size = 18)
label_C = ax1.annotate(r'$C$', C, size = 18)
label_D = ax1.annotate(r'$D$', D, size = 18)
label_E = ax1.annotate(r'$E$', E, size = 18)

label_a1 = ax1.annotate(r'$\urcorner$', A, ha = 'left', va = 'bottom', size = 30, rotation = 0)
label_a2 = ax1.annotate(r'$\ulcorner$', B, ha = 'right', va = 'bottom', size = 30, rotation = 0)
label_a3 = ax1.annotate(r'$\llcorner$', C, ha = 'right', va = 'top', size = 30, rotation = 0)
label_a4 = ax1.annotate(r'$\lrcorner$', D, ha = 'left', va = 'top', size = 30, rotation = 0)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()
label_E.draggable()

label_a1.draggable()
label_a2.draggable()
label_a3.draggable()
label_a4.draggable()

#T# show the results
plt.show()