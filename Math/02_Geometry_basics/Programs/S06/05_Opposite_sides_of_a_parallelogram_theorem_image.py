#T# the following code shows how to draw a parallelogram to show the opposite sides of a parallelogram theorem

#T# to draw a parallelogram to show the opposite sides of a parallelogram theorem, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

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
B = (5, 0)
C = (8, 2.4)
D = (3, 2.4)

list_x1 = [A[0], B[0], C[0], D[0], A[0]]
list_y1 = [A[1], B[1], C[1], D[1], A[1]]

p_mid_AB_1 = (A[0] + .45*(B[0] - A[0]), A[1] + .45*(B[1] - A[1]))
p_mid_AB_2 = (A[0] + .50*(B[0] - A[0]), A[1] + .50*(B[1] - A[1]))

p_mid_BC_1 = (B[0] + .45*(C[0] - B[0]), B[1] + .45*(C[1] - B[1]))
p_mid_BC_2 = (B[0] + .50*(C[0] - B[0]), B[1] + .50*(C[1] - B[1]))
p_mid_BC_3 = (B[0] + .50*(C[0] - B[0]), B[1] + .50*(C[1] - B[1]))
p_mid_BC_4 = (B[0] + .55*(C[0] - B[0]), B[1] + .55*(C[1] - B[1]))

p_mid_CD_1 = (C[0] + .55*(D[0] - C[0]), C[1] + .55*(D[1] - C[1]))
p_mid_CD_2 = (C[0] + .50*(D[0] - C[0]), C[1] + .50*(D[1] - C[1]))

p_mid_DA_1 = (D[0] + .50*(A[0] - D[0]), D[1] + .50*(A[1] - D[1]))
p_mid_DA_2 = (D[0] + .45*(A[0] - D[0]), D[1] + .45*(A[1] - D[1]))
p_mid_DA_3 = (D[0] + .55*(A[0] - D[0]), D[1] + .55*(A[1] - D[1]))
p_mid_DA_4 = (D[0] + .50*(A[0] - D[0]), D[1] + .50*(A[1] - D[1]))

#T# plot the figure
ax1.plot(list_x1, list_y1, 'k', marker = 'o', markersize = 3)
ax1.plot([A[0], C[0]], [A[1], C[1]], 'k', linestyle = '--')

mark1 = mpatches.FancyArrowPatch(p_mid_AB_1, p_mid_AB_2, arrowstyle = '->', mutation_scale = 20)
mark2 = mpatches.FancyArrowPatch(p_mid_CD_1, p_mid_CD_2, arrowstyle = '->', mutation_scale = 20)
mark3_1 = mpatches.FancyArrowPatch(p_mid_BC_1, p_mid_BC_2, arrowstyle = '->', mutation_scale = 20)
mark3_2 = mpatches.FancyArrowPatch(p_mid_BC_3, p_mid_BC_4, arrowstyle = '->', mutation_scale = 20)
mark4_1 = mpatches.FancyArrowPatch(p_mid_DA_1, p_mid_DA_2, arrowstyle = '->', mutation_scale = 20)
mark4_2 = mpatches.FancyArrowPatch(p_mid_DA_3, p_mid_DA_4, arrowstyle = '->', mutation_scale = 20)
ax1.add_patch(mark1)
ax1.add_patch(mark2)
ax1.add_patch(mark3_1)
ax1.add_patch(mark3_2)
ax1.add_patch(mark4_1)
ax1.add_patch(mark4_2)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = plt.annotate(r'$A$', A, ha = 'center', va = 'top', size = 18)
label_B = plt.annotate(r'$B$', B, ha = 'center', va = 'top', size = 18)
label_C = plt.annotate(r'$C$', C, ha = 'center', va = 'bottom', size = 18)
label_D = plt.annotate(r'$D$', D, ha = 'center', va = 'bottom', size = 18)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()

#T# show the results
plt.show()