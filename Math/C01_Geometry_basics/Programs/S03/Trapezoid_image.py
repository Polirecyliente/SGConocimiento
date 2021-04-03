#T# the following code shows how to draw a trapezoid

#T# to draw a trapezoid, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

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
B = (6, 0)
C = (3, 3)
D = (1, 3)

list_x1 = [A[0], B[0], C[0], D[0], A[0]]
list_y1 = [A[1], B[1], C[1], D[1], A[1]]

p_mid_AB_1 = (A[0] + .45*(B[0] - A[0]), A[1] + .45*(B[1] - A[1]))
p_mid_AB_2 = (A[0] + .50*(B[0] - A[0]), A[1] + .50*(B[1] - A[1]))

p_mid_CD_1 = (C[0] + .55*(D[0] - C[0]), C[1] + .55*(D[1] - C[1]))
p_mid_CD_2 = (C[0] + .50*(D[0] - C[0]), C[1] + .50*(D[1] - C[1]))

#T# plot the figure
ax1.plot(list_x1, list_y1, 'k')

mark1 = mpatches.FancyArrowPatch(p_mid_AB_1, p_mid_AB_2, arrowstyle = '->', mutation_scale = 20)
mark2 = mpatches.FancyArrowPatch(p_mid_CD_1, p_mid_CD_2, arrowstyle = '->', mutation_scale = 20)

ax1.add_patch(mark1)
ax1.add_patch(mark2)

#T# show the results
plt.show()