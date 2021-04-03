#T# the following code shows how to draw two similar triangles to make an indirect measurement

#T# to draw two similar triangles to make an indirect measurement, the pyplot module of the matplotlib package is used
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
B = (4, 0)
C = (5, 3)
D = (10, 0)
E = (12.5, 7.5)

list_x1 = [B[0], D[0], E[0], C[0], A[0], B[0], C[0]]
list_y1 = [B[1], D[1], E[1], C[1], A[1], B[1], C[1]]

#T# plot the figure
ax1.plot(list_x1, list_y1, 'o-k', markersize = 3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 18)
label_B = ax1.annotate(r'$B$', B, size = 18)
label_C = ax1.annotate(r'$C$', C, size = 18)
label_D = ax1.annotate(r'$D$', D, size = 18)
label_E = ax1.annotate(r'$E$', E, size = 18)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()
label_E.draggable()

#T# show the results
plt.show()