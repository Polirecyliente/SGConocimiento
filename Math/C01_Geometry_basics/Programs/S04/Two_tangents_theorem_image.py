#T# the following code shows how to draw a diagram to show the two tangents theorem

#T# to draw a diagram to show the two tangents theorem, the pyplot module of the matplotlib package is used
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
B = (-3, 4)
C = (0, 1.5)

k_AC = 1

m_BC = (C[1] - B[1])/(C[0] - B[0])
m_perp_BC = -1/m_BC
A = (C[0] + k_AC, C[1] + k_AC*m_perp_BC)
r_A = math.sqrt((C[0] - A[0])**2 + (C[1] - A[1])**2)

m_AB = (B[1] - A[1])/(B[0] - A[0])
b_AB_A = A[1] - m_AB*A[0]
m_perp_AB = -1/m_AB
b_perp_AB_C = C[1] - m_perp_AB*C[0]
x_p_mid_CD = (b_perp_AB_C - b_AB_A)/(m_AB - m_perp_AB)
y_p_mid_CD = m_AB*x_p_mid_CD + b_AB_A
p_mid_CD = (x_p_mid_CD, y_p_mid_CD)
D = (C[0] + 2*(p_mid_CD[0] - C[0]), C[1] + 2*(p_mid_CD[1] - C[1]))

p_mid_BC = ((B[0] + C[0])/2, (B[1] + C[1])/2)
p_mid_BD = ((B[0] + D[0])/2, (B[1] + D[1])/2)
a_0_BC = math.atan2((C[1] - B[1]), (C[0] - B[0]))
a_0_BD = math.atan2((D[1] - B[1]), (D[0] - B[0]))

list_x_1 = [B[0], C[0]]
list_y_1 = [B[1], C[1]]

list_x_2 = [B[0], D[0]]
list_y_2 = [B[1], D[1]]

list_x_3 = [A[0], B[0]]
list_y_3 = [A[1], B[1]]

#T# plot the figure
ax1.plot(list_x_1, list_y_1, 'o-k', markersize = 3)
ax1.plot(list_x_2, list_y_2, 'o-k', markersize = 3)
ax1.plot(list_x_3, list_y_3, 'o--k', markersize = 3)

circle1 = mpatches.Arc(A, 2*r_A, 2*r_A, linewidth = 1.5)
ax1.add_patch(circle1)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 16)
label_B = ax1.annotate(r'$B$', B, size = 16)
label_C = ax1.annotate(r'$C$', C, size = 16)
label_D = ax1.annotate(r'$D$', D, size = 16)

ax1.annotate(r'$|$', p_mid_BC, ha = 'center', va = 'center', size = 18, rotation = math.degrees(a_0_BC))
ax1.annotate(r'$|$', p_mid_BD, ha = 'center', va = 'center', size = 18, rotation = math.degrees(a_0_BD))

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()

#T# show the results
ax1.autoscale()
plt.show()