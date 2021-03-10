#T# the following code shows how to draw an isosceles trapezoid

#T# to draw an isosceles trapezoid, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# import the math module to do calculations
import math

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
B = (12, 0)
C = (9, 6)
D = (3, 6)

a1 = math.atan2(D[1] - A[1], D[0] - A[0])

list_x1 = [A[0], B[0], C[0], D[0], A[0]]
list_y1 = [A[1], B[1], C[1], D[1], A[1]]

p_mid_AB_1 = (A[0] + .45*(B[0] - A[0]), A[1] + .45*(B[1] - A[1]))
p_mid_AB_2 = (A[0] + .50*(B[0] - A[0]), A[1] + .50*(B[1] - A[1]))

p_mid_CD_1 = (C[0] + .50*(D[0] - C[0]), C[1] + .50*(D[1] - C[1]))
p_mid_CD_2 = (C[0] + .45*(D[0] - C[0]), C[1] + .45*(D[1] - C[1]))

p_mid_BC = ((B[0] + C[0])/2, (B[1] + C[1])/2)
p_mid_AD = ((A[0] + D[0])/2, (A[1] + D[1])/2)

#T# plot the figure
ax1.plot(list_x1, list_y1, 'k')

mark1 = mpatches.FancyArrowPatch(p_mid_AB_1, p_mid_AB_2, arrowstyle = '->', mutation_scale = 20)
mark2 = mpatches.FancyArrowPatch(p_mid_CD_1, p_mid_CD_2, arrowstyle = '->', mutation_scale = 20)

ax1.add_patch(mark1)
ax1.add_patch(mark2)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
ax1.annotate(r'$|$', p_mid_AD, ha = 'center', va = 'center', size = 20, rotation = math.degrees(a1))
ax1.annotate(r'$|$', p_mid_BC, ha = 'center', va = 'center', size = 20, rotation = math.degrees(-a1))

#T# show the results
plt.show()