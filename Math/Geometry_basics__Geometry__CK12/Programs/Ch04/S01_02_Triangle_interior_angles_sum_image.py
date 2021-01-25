#T# the following code shows how to draw a triangle's interior angles to show their sum

#T# to draw a triangle's interior angles to show their sum, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

#T# create the variables that define the plot
A, B, C = (1, 2), (8, 2), (6, 6)
D = (8, 6)

list1 = [A[0], B[0], C[0], A[0]] #| x coordinates
list2 = [A[1], B[1], C[1], A[1]] #| y coordinates

#T# plot the figure
ax1.plot(list1, list2, 'k')
line1 = mpatches.FancyArrowPatch((0, 6), (9, 6), arrowstyle = '<->', mutation_scale = 12, linewidth = 1.4) #| parallel line to a side that passes through the vertex opposite to said side
ax1.add_patch(line1)

marker1 = mpatches.FancyArrowPatch((2.7, 6), (3, 6), arrowstyle = '->', mutation_scale = 26) #| parallel line marks
marker2 = mpatches.FancyArrowPatch((3, 2), (4, 2), arrowstyle = '->', mutation_scale = 26)
ax1.add_patch(marker1)
ax1.add_patch(marker2)

ax1.scatter(list1, list2, s = 12, color = 'k')
ax1.scatter(D[0], D[1], s = 12, color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', (A[0], A[1]), ha = 'right', va = 'top', size = 18)
label_B = ax1.annotate(r'$B$', (B[0], B[1]), ha = 'left', va = 'top', size = 18)
label_C = ax1.annotate(r'$C$', (C[0], C[1]), ha = 'center', va = 'bottom', size = 18)
label_D = ax1.annotate(r'$D$', (D[0], D[1]), ha = 'center', va = 'bottom', size = 18)

label_aA_1 = ax1.annotate(r'$1$', (A[0], A[1]), ha = 'left', va = 'bottom', size = 18)
label_aA_2 = ax1.annotate(r'$4$', (C[0], C[1]), ha = 'right', va = 'top', size = 18)
label_aB_1 = ax1.annotate(r'$2$', (B[0], B[1]), ha = 'right', va = 'bottom', size = 18)
label_aB_2 = ax1.annotate(r'$5$', (C[0], C[1]), ha = 'left', va = 'top', size = 18)
label_aC_1 = ax1.annotate(r'$3$', (C[0], C[1]), ha = 'center', va = 'top', size = 18)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()

label_aA_1.draggable()
label_aA_2.draggable()
label_aB_1.draggable()
label_aB_2.draggable()
label_aC_1.draggable()

#T# show the result
plt.show()