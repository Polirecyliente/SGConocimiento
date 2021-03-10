#T# the following code shows how to draw a triangle with an angle bisector, to show the proportionality in an angle bisector theorem

#T# to draw a triangle with an angle bisector, to show the proportionality in an angle bisector theorem, the pyplot module of the matplotlib package is used
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
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

#T# create the variables that define the plot
A = (8, 16)
B = (0, 0)
C = (4, 0)

a_ABC = math.atan2(A[1], A[0])
a_DBC = a_ABC/2

m_AC = (C[1] - A[1])/(C[0] - A[0])
m_BD = math.tan(a_DBC)
b_AC = A[1] - m_AC*A[0]
b_BD = B[1] - m_BD*B[0]
x_D = (b_BD - b_AC)/(m_AC - m_BD)
y_D = m_BD*x_D + b_BD
D = (x_D, y_D)

m_AB = (B[1] - A[1])/(B[0] - A[0])
m_CE = math.tan(a_DBC)
b_AB = A[1] - m_AB*A[0]
b_CE = C[1] - m_CE*C[0]
x_E = (b_CE - b_AB)/(m_AB - m_CE)
y_E = m_CE*x_E + b_CE
E = (x_E, y_E)

diam_arc1 = 3

a_marker1 = a_DBC/2
a_marker2 = a_DBC*3/2
p_marker1 = (diam_arc1/2*math.cos(a_marker1), diam_arc1/2*math.sin(a_marker1))
p_marker2 = (diam_arc1/2*math.cos(a_marker2), diam_arc1/2*math.sin(a_marker2))

p_mid_BD_1 = (B[0] + .55*(D[0] - B[0]), B[1] + .55*(D[1] - B[1]))
p_mid_BD_2 = (B[0] + .65*(D[0] - B[0]), B[1] + .65*(D[1] - B[1]))

p_mid_EC_1 = (E[0] + .55*(C[0] - E[0]), E[1] + .55*(C[1] - E[1]))
p_mid_EC_2 = (E[0] + .65*(C[0] - E[0]), E[1] + .65*(C[1] - E[1]))

list_x_1 = [A[0], B[0], C[0], A[0]]
list_y_1 = [A[1], B[1], C[1], A[1]]

list_x_2 = [B[0], D[0]]
list_y_2 = [B[1], D[1]]

list_x_3 = [B[0], E[0], C[0]]
list_y_3 = [B[1], E[1], C[1]]

#T# plot the figure
ax1.plot(list_x_1, list_y_1, 'o-k', markersize = 3)
ax1.plot(list_x_2, list_y_2, 'o-k', markersize = 3)
ax1.plot(list_x_3, list_y_3, 'o--k', markersize = 3)

arc1 = mpatches.Arc(B, diam_arc1, diam_arc1, theta2 = math.degrees(a_ABC))
ax1.add_patch(arc1)

mark1_1 = mpatches.FancyArrowPatch(p_mid_BD_1, p_mid_BD_2, arrowstyle = '->', mutation_scale = 16)
mark1_2 = mpatches.FancyArrowPatch(p_mid_EC_1, p_mid_EC_2, arrowstyle = '->', mutation_scale = 16)
ax1.add_patch(mark1_1)
ax1.add_patch(mark1_2)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 18)
label_B = ax1.annotate(r'$B$', B, size = 18)
label_C = ax1.annotate(r'$C$', C, size = 18)
label_D = ax1.annotate(r'$D$', D, size = 18)
label_E = ax1.annotate(r'$E$', E, size = 18)

marker1 = ax1.annotate(r'$|$', p_marker1, ha = 'center', va = 'center', size = 15, rotation = 90 + math.degrees(a_marker1))
marker2 = ax1.annotate(r'$|$', p_marker2, ha = 'center', va = 'center', size = 15, rotation = 90 + math.degrees(a_marker2))

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()
label_E.draggable()

#T# show the results
plt.show()