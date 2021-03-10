#T# the following code shows how to draw an altitude of a triangle

#T# to draw an altitude of a triangle, the pyplot module of the matplotlib package is used
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
A, B, C = (0, 0), (4, 0), (-3, 4)
D = (-3, 0)

list_x = [C[0], A[0], B[0], C[0], D[0]] #| coordinates
list_y = [C[1], A[1], B[1], C[1], D[1]]

#T# plot the figure
ax1.plot(list_x, list_y, 'o-k', markersize = 3.5)
ax1.plot([A[0], D[0]], [A[1], D[1]], '--k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, ha = 'center', va = 'top', size = 18)
label_B = ax1.annotate(r'$B$', B, ha = 'center', va = 'top', size = 18)
label_C = ax1.annotate(r'$C$', C, ha = 'center', va = 'bottom', size = 18)
label_D = ax1.annotate(r'$D$', D, ha = 'center', va = 'top', size = 18)
label_aD = ax1.annotate(r'$\urcorner$', D, ha = 'left', va = 'bottom', size = 26)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()
label_aD.draggable()

#T# show the results
plt.show()