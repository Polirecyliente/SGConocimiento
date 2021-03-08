#T# the following code shows how to draw an isosceles trapezoid to show the diagonals of an isosceles trapezoid theorem

#T# to draw an isosceles trapezoid to show the diagonals of an isosceles trapezoid theorem, the pyplot module of the matplotlib package is used
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
a2 = math.pi - a1

list_x1 = [A[0], B[0], C[0], D[0], A[0], C[0]]
list_y1 = [A[1], B[1], C[1], D[1], A[1], C[1]]

list_x2 = [B[0], D[0]]
list_y2 = [B[1], D[1]]

p_mid_AB_1 = (A[0] + .45*(B[0] - A[0]), A[1] + .45*(B[1] - A[1]))
p_mid_AB_2 = (A[0] + .50*(B[0] - A[0]), A[1] + .50*(B[1] - A[1]))

p_mid_CD_1 = (C[0] + .50*(D[0] - C[0]), C[1] + .50*(D[1] - C[1]))
p_mid_CD_2 = (C[0] + .45*(D[0] - C[0]), C[1] + .45*(D[1] - C[1]))

p_mid_BC = ((B[0] + C[0])/2, (B[1] + C[1])/2)
p_mid_AD = ((A[0] + D[0])/2, (A[1] + D[1])/2)

r = 1

#T# plot the figure
ax1.plot(list_x1, list_y1, 'k', marker = 'o', markersize = 3)
ax1.plot(list_x2, list_y2, 'k', marker = 'o', markersize = 3)

arc1_1 = mpatches.Arc(A, 2*r, 2*r, theta1 = 0, theta2 = math.degrees(a1))
arc1_2 = mpatches.Arc(A, 2.2*r, 2.2*r, theta1 = 0, theta2 = math.degrees(a1))
arc2_1 = mpatches.Arc(B, 2*r, 2*r, theta1 = 180 - math.degrees(a1), theta2 = 180)
arc2_2 = mpatches.Arc(B, 2.2*r, 2.2*r, theta1 = 180 - math.degrees(a1), theta2 = 180)
arc3_1 = mpatches.Arc(C, 2*r, 2*r, theta1 = 180, theta2 = 180 + math.degrees(a2))
arc3_2 = mpatches.Arc(C, 2.2*r, 2.2*r, theta1 = 180, theta2 = 180 + math.degrees(a2))
arc3_3 = mpatches.Arc(C, 2.4*r, 2.4*r, theta1 = 180, theta2 = 180 + math.degrees(a2))
arc4_1 = mpatches.Arc(D, 2*r, 2*r, theta1 = 360 - math.degrees(a2), theta2 = 360)
arc4_2 = mpatches.Arc(D, 2.2*r, 2.2*r, theta1 = 360 - math.degrees(a2), theta2 = 360)
arc4_3 = mpatches.Arc(D, 2.4*r, 2.4*r, theta1 = 360 - math.degrees(a2), theta2 = 360)

ax1.add_patch(arc1_1)
ax1.add_patch(arc1_2)
ax1.add_patch(arc2_1)
ax1.add_patch(arc2_2)
ax1.add_patch(arc3_1)
ax1.add_patch(arc3_2)
ax1.add_patch(arc3_3)
ax1.add_patch(arc4_1)
ax1.add_patch(arc4_2)
ax1.add_patch(arc4_3)

mark1 = mpatches.FancyArrowPatch(p_mid_AB_1, p_mid_AB_2, arrowstyle = '->', mutation_scale = 20)
mark2 = mpatches.FancyArrowPatch(p_mid_CD_1, p_mid_CD_2, arrowstyle = '->', mutation_scale = 20)

ax1.add_patch(mark1)
ax1.add_patch(mark2)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 18)
label_B = ax1.annotate(r'$B$', B, size = 18)
label_C = ax1.annotate(r'$C$', C, size = 18)
label_D = ax1.annotate(r'$D$', D, size = 18)

ax1.annotate(r'$|$', p_mid_AD, ha = 'center', va = 'center', size = 20, rotation = math.degrees(a1))
ax1.annotate(r'$|$', p_mid_BC, ha = 'center', va = 'center', size = 20, rotation = math.degrees(-a1))

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()

#T# show the results
plt.show()