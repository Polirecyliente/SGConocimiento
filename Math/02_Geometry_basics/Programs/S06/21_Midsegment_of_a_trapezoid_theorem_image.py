#T# the following code shows how to draw a trapezoid to show the midsegment of a trapezoid theorem

#T# to draw a trapezoid to show the midsegment of a trapezoid theorem, the pyplot module of the matplotlib package is used
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
B = (6, 0)
C = (3, 3)
D = (1, 3)
E = ((A[0] + D[0])/2, (A[1] + D[1])/2)
F = ((B[0] + C[0])/2, (B[1] + C[1])/2)
G = (D[0] + 2*(F[0] - D[0]), D[1] + 2*(F[1] - D[1]))

list_x1 = [E[0], A[0], B[0], C[0], D[0], E[0], F[0]]
list_y1 = [E[1], A[1], B[1], C[1], D[1], E[1], F[1]]

list_x2 = [D[0], G[0], B[0]]
list_y2 = [D[1], G[1], B[1]]

p_mid_AE = ((A[0] + E[0])/2, (A[1] + E[1])/2)
p_mid_DE = ((D[0] + E[0])/2, (D[1] + E[1])/2)
p_mid_BF = ((B[0] + F[0])/2, (B[1] + F[1])/2)
p_mid_CF = ((C[0] + F[0])/2, (C[1] + F[1])/2)

a0_AD = math.atan2(D[1] - A[1], D[0] - A[0])
a0_BC = math.atan2(C[1] - B[1], C[0] - B[0])

p_mid_AB_1 = (A[0] + .45*(B[0] - A[0]), A[1] + .45*(B[1] - A[1]))
p_mid_AB_2 = (A[0] + .50*(B[0] - A[0]), A[1] + .50*(B[1] - A[1]))

p_mid_DC_1 = (D[0] + .45*(C[0] - D[0]), D[1] + .45*(C[1] - D[1]))
p_mid_DC_2 = (D[0] + .50*(C[0] - D[0]), D[1] + .50*(C[1] - D[1]))

p_mid_EF_1 = (E[0] + .45*(F[0] - E[0]), E[1] + .45*(F[1] - E[1]))
p_mid_EF_2 = (E[0] + .50*(F[0] - E[0]), E[1] + .50*(F[1] - E[1]))

#T# plot the figure
ax1.plot(list_x1, list_y1, 'k', marker = 'o', markersize = 3)
ax1.plot(list_x2, list_y2, '--k', marker = 'o', markersize = 3)

mark1 = mpatches.FancyArrowPatch(p_mid_AB_1, p_mid_AB_2, arrowstyle = '->', mutation_scale = 20)
mark2 = mpatches.FancyArrowPatch(p_mid_DC_1, p_mid_DC_2, arrowstyle = '->', mutation_scale = 20)
mark3 = mpatches.FancyArrowPatch(p_mid_EF_1, p_mid_EF_2, arrowstyle = '->', mutation_scale = 20)

ax1.add_patch(mark1)
ax1.add_patch(mark2)
ax1.add_patch(mark3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = plt.annotate(r'$A$', A, size = 18)
label_B = plt.annotate(r'$B$', B, size = 18)
label_C = plt.annotate(r'$C$', C, size = 18)
label_D = plt.annotate(r'$D$', D, size = 18)
label_E = plt.annotate(r'$E$', E, size = 18)
label_F = plt.annotate(r'$F$', F, size = 18)
label_G = plt.annotate(r'$G$', G, size = 18)

plt.annotate(r'$|$', p_mid_AE, ha = 'center', va = 'center', size = 20, rotation = math.degrees(a0_AD))
plt.annotate(r'$|$', p_mid_DE, ha = 'center', va = 'center', size = 20, rotation = math.degrees(a0_AD))
plt.annotate(r'$||$', p_mid_BF, ha = 'center', va = 'center', size = 20, rotation = math.degrees(a0_BC))
plt.annotate(r'$||$', p_mid_CF, ha = 'center', va = 'center', size = 20, rotation = math.degrees(a0_BC))

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()
label_E.draggable()
label_F.draggable()
label_G.draggable()

#T# show the results
plt.show()