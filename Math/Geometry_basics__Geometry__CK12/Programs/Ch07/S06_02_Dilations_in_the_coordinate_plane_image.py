#T# the following code shows how to draw a dilation of a triangle in the coordinate plane

#T# to draw a dilation of a triangle in the coordinate plane, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in ['top', 'right']:
    ax1.spines[it1].set_visible(False)

#T# position the spines and ticks
for it1 in ['bottom', 'left']:
    ax1.spines[it1].set_position(('data', 0))

#T# set the axes size
xmin1 = -8
xmax1 = 8
ymin1 = -8
ymax1 = 8
for it1 in fig1.axes:
    it1.axis([xmin1, xmax1, ymin1, ymax1])

#T# set the ticks labels
list1_1 = list(range(xmin1, xmax1 + 1, 1))
list2_1 = list(range(ymin1, ymax1 + 1, 1))
list1_2 = ['' if it1 == 0 else str(it1) for it1 in list1_1]
list2_2 = ['' if it1 == 0 else str(it1) for it1 in list2_1]
ax1.set_xticks(list1_1)
ax1.set_yticks(list2_1)
ax1.set_xticklabels(list1_2)
ax1.set_yticklabels(list2_2)

#T# draw the grid
ax1.grid(True, alpha = .3)

#T# create the variables that define the plot
A = (1, 2)
B = (.5, 1.3)
C = (1.8, 1.1)

Center = (-2, 3)
k = 2.5

D = Center

A2 = (Center[0] + k*(A[0] - Center[0]), Center[1] + k*(A[1] - Center[1]))
B2 = (Center[0] + k*(B[0] - Center[0]), Center[1] + k*(B[1] - Center[1]))
C2 = (Center[0] + k*(C[0] - Center[0]), Center[1] + k*(C[1] - Center[1]))

list_x_1 = [A[0], B[0], C[0], A[0]]
list_y_1 = [A[1], B[1], C[1], A[1]]

list_x_2 = [A2[0], B2[0], C2[0], A2[0]]
list_y_2 = [A2[1], B2[1], C2[1], A2[1]]

list_x_3 = [A2[0], A[0], D[0], B[0], B2[0], B[0], D[0], C[0], C2[0]]
list_y_3 = [A2[1], A[1], D[1], B[1], B2[1], B[1], D[1], C[1], C2[1]]

#T# plot the figure
ax1.plot(list_x_1, list_y_1, 'o-k', markersize = 3)
ax1.plot(list_x_2, list_y_2, 'o-k', markersize = 3)
ax1.plot(list_x_3, list_y_3, 'o--k', markersize = 3, alpha = .4)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 18)
label_B = ax1.annotate(r'$B$', B, size = 18)
label_C = ax1.annotate(r'$C$', C, size = 18)

label_D = ax1.annotate(r'$D$', D, size = 18)

label_A2 = ax1.annotate(r"$A'$", A2, size = 18)
label_B2 = ax1.annotate(r"$B'$", B2, size = 18)
label_C2 = ax1.annotate(r"$C'$", C2, size = 18)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()

label_D.draggable()

label_A2.draggable()
label_B2.draggable()
label_C2.draggable()

#T# show the results
plt.show()