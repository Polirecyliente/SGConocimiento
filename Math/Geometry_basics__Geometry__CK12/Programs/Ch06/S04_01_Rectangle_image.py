#T# the following code shows how to draw a rectangle

#T# to draw a rectangle, the pyplot module of the matplotlib package is used
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

list_x1 = [A[0], B[0], C[0], D[0], A[0]]
list_y1 = [A[1], B[1], C[1], D[1], A[1]]

#T# plot the figure
ax1.plot(list_x1, list_y1, 'k')

#T# create the labels
label_a1 = ax1.annotate(r'$\urcorner$', A, size = 30, rotation = 0)
label_a2 = ax1.annotate(r'$\ulcorner$', B, size = 30, rotation = 0)
label_a3 = ax1.annotate(r'$\llcorner$', C, size = 30, rotation = 0)
label_a4 = ax1.annotate(r'$\lrcorner$', D, size = 30, rotation = 0)

#T# drag the labels if needed
label_a1.draggable()
label_a2.draggable()
label_a3.draggable()
label_a4.draggable()

#T# show the results
plt.show()