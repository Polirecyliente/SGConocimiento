#T# the following code shows how to draw two circles and their two common internal tangents

#T# to draw two circles and their two common internal tangents, the pyplot module of the matplotlib package is used
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
C1 = (-2, 2.5)
D1 = (2.2, -1.12)

C2 = (-3, -.75)
D2 = (2.6, .46)

m_C1D1 = (D1[1] - C1[1])/(D1[0] - C1[0])
b_C1D1_C1 = C1[1] - m_C1D1*C1[0]

m_C2D2 = (D2[1] - C2[1])/(D2[0] - C2[0])
b_C2D2_C2 = C2[1] - m_C2D2*C2[0]

x_E = (b_C2D2_C2 - b_C1D1_C1)/(m_C1D1 - m_C2D2)
y_E = m_C1D1*x_E + b_C1D1_C1
E = (x_E, y_E)

d_C1C2 = math.sqrt((C2[0] - C1[0])**2 + (C2[1] - C1[1])**2)
d_C1E = math.sqrt((E[0] - C1[0])**2 + (E[1] - C1[1])**2)
d_C2E = math.sqrt((E[0] - C2[0])**2 + (E[1] - C2[1])**2)
k_AC1 = d_C1E/(d_C1E + d_C2E)
A = (C1[0] + k_AC1*(C2[0] - C1[0]), C1[1] + k_AC1*(C2[1] - C1[1]))

m_perp_C1D1 = -1/m_C1D1
b_perp_C1D1_A = A[1] - m_perp_C1D1*A[0]
x_p_tang_A = (b_C1D1_C1 - b_perp_C1D1_A)/(m_perp_C1D1 - m_C1D1)
y_p_tang_A = m_perp_C1D1*x_p_tang_A + b_perp_C1D1_A
p_tang_A = (x_p_tang_A, y_p_tang_A)
r_A = math.sqrt((p_tang_A[0] - A[0])**2 + (p_tang_A[1] - A[1])**2)

d_D1D2 = math.sqrt((D2[0] - D1[0])**2 + (D2[1] - D1[1])**2)
d_D1E = math.sqrt((E[0] - D1[0])**2 + (E[1] - D1[1])**2)
d_D2E = math.sqrt((E[0] - D2[0])**2 + (E[1] - D2[1])**2)
k_BD1 = d_D1E/(d_D1E + d_D2E)
B = (D1[0] + k_BD1*(D2[0] - D1[0]), D1[1] + k_BD1*(D2[1] - D1[1]))

m_perp_C2D2 = -1/m_C2D2
b_perp_C2D2_B = B[1] - m_perp_C2D2*B[0]
x_p_tang_B = (b_C2D2_C2 - b_perp_C2D2_B)/(m_perp_C2D2 - m_C2D2)
y_p_tang_B = m_perp_C2D2*x_p_tang_B + b_perp_C2D2_B
p_tang_B = (x_p_tang_B, y_p_tang_B)
r_B = math.sqrt((p_tang_B[0] - B[0])**2 + (p_tang_B[1] - B[1])**2)

list_x_1 = [C1[0], D1[0]]
list_y_1 = [C1[1], D1[1]]

list_x_2 = [C2[0], D2[0]]
list_y_2 = [C2[1], D2[1]]

list_x_3 = [A[0], B[0]]
list_y_3 = [A[1], B[1]]

#T# plot the figure
ax1.plot(list_x_1, list_y_1, 'o-k', markersize = 3)
ax1.plot(list_x_2, list_y_2, 'o-k', markersize = 3)
ax1.plot(list_x_3, list_y_3, 'o--k', markersize = 3)

circle1 = mpatches.Arc(A, 2*r_A, 2*r_A, linewidth = 1.5)
circle2 = mpatches.Arc(B, 2*r_B, 2*r_B, linewidth = 1.5)
ax1.add_patch(circle1)
ax1.add_patch(circle2)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 16)
label_B = ax1.annotate(r'$B$', B, size = 16)
label_C1 = ax1.annotate(r'$C_1$', C1, size = 16)
label_D1 = ax1.annotate(r'$D_1$', D1, size = 16)
label_C2 = ax1.annotate(r'$C_2$', C2, size = 16)
label_D2 = ax1.annotate(r'$D_2$', D2, size = 16)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C1.draggable()
label_C2.draggable()
label_D1.draggable()
label_D2.draggable()

#T# show the results
ax1.autoscale()
plt.show()