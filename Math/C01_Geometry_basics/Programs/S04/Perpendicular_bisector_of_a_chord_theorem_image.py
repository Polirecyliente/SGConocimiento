#T# the following code shows how to draw a diagram to show the perpendicular bisector of a chord theorem

#T# to draw a diagram to show the perpendicular bisector of a chord theorem, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# import the math module to do calculations
import math

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
r_A = 1

a_0_AB = math.pi/3.7
a_BAC = math.pi/3.5
a_0_AC = a_0_AB + a_BAC

B = (r_A*math.cos(a_0_AB), r_A*math.sin(a_0_AB))
C = (r_A*math.cos(a_0_AC), r_A*math.sin(a_0_AC))

a_mid_AB_AC = (a_0_AB + a_0_AC)/2
D = (r_A*math.cos(a_mid_AB_AC), r_A*math.sin(a_mid_AB_AC))
E = (r_A*math.cos(a_mid_AB_AC + math.pi), r_A*math.sin(a_mid_AB_AC + math.pi))

F = ((B[0] + C[0])/2, (B[1] + C[1])/2)
p_mid_BF = ((B[0] + F[0])/2, (B[1] + F[1])/2)
p_mid_CF = ((C[0] + F[0])/2, (C[1] + F[1])/2)

list_x_1 = [B[0], A[0], C[0], B[0]]
list_y_1 = [B[1], A[1], C[1], B[1]]

list_x_2 = [D[0], F[0], E[0]]
list_y_2 = [D[1], F[1], E[1]]

#T# plot the figure
circle1 = mpatches.Arc(A, 2*r_A, 2*r_A, linewidth = 1.5)
ax1.add_patch(circle1)

ax1.plot(list_x_1, list_y_1, 'o-k', markersize = 3)
ax1.plot(list_x_2, list_y_2, 'o-k', markersize = 3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 16)
label_B = ax1.annotate(r'$B$', B, size = 16)
label_C = ax1.annotate(r'$C$', C, size = 16)
label_D = ax1.annotate(r'$D$', D, size = 16)
label_E = ax1.annotate(r'$E$', E, size = 16)
label_F = ax1.annotate(r'$F$', F, size = 16)

ax1.annotate(r'$|$', p_mid_BF, ha = 'center', va = 'center', size = 16, rotation = math.degrees(a_mid_AB_AC) + 90)
ax1.annotate(r'$|$', p_mid_CF, ha = 'center', va = 'center', size = 16, rotation = math.degrees(a_mid_AB_AC) + 90)

a_marker1 = ax1.annotate(r'$\llcorner$', F, size = 24, rotation = math.degrees(a_mid_AB_AC))

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()
label_E.draggable()
label_F.draggable()
a_marker1.draggable()

#T# show the results
ax1.autoscale()
plt.show()