#T# the following code shows how to draw the circumcenter of a triangle

#T# to draw the circumcenter of a triangle, the pyplot module of the matplotlib package is used
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
A, B, C = (1, 2), (8, 2), (3.5, 7)

mid_AB = ((A[0] + B[0])/2, (A[1] + B[1])/2)
mid_AC = ((A[0] + C[0])/2, (A[1] + C[1])/2)
mid_BC = ((B[0] + C[0])/2, (B[1] + C[1])/2)

m_AB = (B[1] - A[1])/(B[0] - A[0])
m_AC = (C[1] - A[1])/(C[0] - A[0])
m_BC = (C[1] - B[1])/(C[0] - B[0])

m_perp_AC = -1/m_AC
m_perp_BC = -1/m_BC

p_perp_AB = (mid_AB[0], mid_AB[1] + 3.3)
p_perp_AC = (mid_AC[0] + 4.24, mid_AC[1] + 4.24*m_perp_AC)
p_perp_BC = (mid_BC[0] - 2.35, mid_BC[1] - 2.35*m_perp_BC)

G = (mid_AB[0], mid_AC[1] + m_perp_AC*(mid_AB[0] - mid_AC[0])) #| circumcenter

d_AG = math.sqrt((G[0] - A[0])**2 + (G[1] - A[1])**2)

list_x_1 = [A[0], B[0], C[0], A[0]]
list_y_1 = [A[1], B[1], C[1], A[1]]

list_x_2 = [mid_AB[0], mid_AC[0], mid_BC[0], G[0]]
list_y_2 = [mid_AB[1], mid_AC[1], mid_BC[1], G[1]]

#T# plot the figure
ax1.plot(list_x_1, list_y_1, 'k')

ax1.scatter(list_x_1, list_y_1, s = 12, color = 'k')
ax1.scatter(list_x_2, list_y_2, s = 12, color = 'k')

ax1.plot([mid_AB[0], p_perp_AB[0]], [mid_AB[1], p_perp_AB[1]], 'k')
ax1.plot([mid_AC[0], p_perp_AC[0]], [mid_AC[1], p_perp_AC[1]], 'k')
ax1.plot([mid_BC[0], p_perp_BC[0]], [mid_BC[1], p_perp_BC[1]], 'k')

arc1 = mpatches.Arc(G, 2*d_AD, 2*d_AD)
ax1.add_patch(arc1)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, ha = 'right', va = 'top', size = 16)
label_B = ax1.annotate(r'$B$', B, ha = 'left', va = 'top', size = 16)
label_C = ax1.annotate(r'$C$', C, ha = 'center', va = 'bottom', size = 16)
label_D = ax1.annotate(r'$D$', mid_AB, ha = 'center', va = 'top', size = 16)
label_E = ax1.annotate(r'$E$', mid_AC, ha = 'right', va = 'bottom', size = 16)
label_F = ax1.annotate(r'$F$', mid_BC, ha = 'left', va = 'bottom', size = 16)
label_G = ax1.annotate(r'$G$', G, ha = 'right', va = 'center', size = 16)

label_angle1 = ax1.annotate(r'$\urcorner$', mid_AB, size = 26)
label_angle2 = ax1.annotate(r'$\urcorner$', mid_AC, size = 26, rotation = 245)
label_angle3 = ax1.annotate(r'$\urcorner$', mid_BC, size = 26, rotation = -137)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()
label_E.draggable()
label_F.draggable()
label_G.draggable()

label_angle1.draggable()
label_angle2.draggable()
label_angle3.draggable()

#T# show the result
plt.show()