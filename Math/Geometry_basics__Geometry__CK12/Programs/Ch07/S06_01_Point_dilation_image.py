#T# the following code shows how to draw a point dilation

#T# to draw a point dilation, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

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
A = (0, 0)
B = (2, 1)
C = (6, 3)

list_x_1 = [A[0], B[0]]
list_y_1 = [A[1], B[1]]

list_x_2 = [B[0], C[0]]
list_y_2 = [B[1], C[1]]

#T# plot the figure
ax1.plot(list_x_1, list_y_1, 'o-k', markersize = 3)
ax1.plot(list_x_2, list_y_2, 'o--k', markersize = 3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 18)
label_B = ax1.annotate(r'$B$', B, size = 18)
label_C = ax1.annotate(r'$C$', C, size = 18)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()

#T# show the results
plt.show()