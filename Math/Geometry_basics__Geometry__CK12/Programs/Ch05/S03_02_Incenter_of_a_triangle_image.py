#T# the following code shows how to draw the incenter of a triangle

#T# to draw the incenter of a triangle, the pyplot module of the matplotlib package is used
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

a0_AB = math.atan2(B[1] - A[1], B[0] - A[0])
a0_AC = math.atan2(C[1] - A[1], C[0] - A[0])
a0_BA = math.atan2(A[1] - B[1], A[0] - B[0])
a0_BC = math.atan2(C[1] - B[1], C[0] - B[0])
a0_CA = math.atan2(A[1] - C[1], A[0] - C[0])
a0_CB = math.atan2(B[1] - C[1], B[0] - C[0])

a0_mid_BAC = (a0_AB + a0_AC)/2
a0_mid_ABC = (a0_BA + a0_BC)/2
a0_mid_ACB = (a0_CA + a0_CB)/2

m_mid_BAC = math.tan(a0_mid_BAC)
m_mid_ABC = math.tan(a0_mid_ABC)
m_mid_ACB = math.tan(a0_mid_ACB)

b_mid_BAC = A[1] - m_mid_BAC*A[0]
b_mid_ABC = B[1] - m_mid_ABC*B[0]

x_incenter = (b_mid_ABC - b_mid_BAC)/(m_mid_BAC - m_mid_ABC)
y_incenter = m_mid_BAC*x_incenter + b_mid_BAC
G = (x_incenter, y_incenter) #| incenter

d_AG = math.sqrt((G[0] - A[0])**2 + (G[1] - A[1])**2)
d_BG = math.sqrt((G[0] - B[0])**2 + (G[1] - B[1])**2)
d_CG = math.sqrt((G[0] - C[0])**2 + (G[1] - C[1])**2)

d_AD = d_AG*math.cos(a0_mid_BAC - a0_AB)
D = (d_AD*math.cos(a0_AB) + A[0], d_AD*math.sin(a0_AB) + A[1])

d_CE = d_CG*math.cos(a0_mid_ACB - a0_CA)
E = (d_CE*math.cos(a0_CA) + C[0], d_CE*math.sin(a0_CA) + C[1])

d_BF = d_BG*math.cos(a0_mid_ABC - a0_BC)
F = (d_BF*math.cos(a0_BC) + B[0], d_BF*math.sin(a0_BC) + B[1])

d_DG = math.sqrt((G[0] - D[0])**2 + (G[1] - D[1])**2)

list_x_1 = [A[0], B[0], C[0], A[0]]
list_y_1 = [A[1], B[1], C[1], A[1]]

list_x_2 = [A[0], B[0], C[0], D[0], E[0], F[0], G[0]]
list_y_2 = [A[1], B[1], C[1], D[1], E[1], F[1], G[1]]

#T# plot the figure
ax1.plot(list_x_1, list_y_1, 'k')
ax1.plot([A[0], G[0]], [A[1], G[1]], 'k')
ax1.plot([B[0], G[0]], [B[1], G[1]], 'k')
ax1.plot([C[0], G[0]], [C[1], G[1]], 'k')
ax1.plot([D[0], G[0]], [D[1], G[1]], 'k')
ax1.plot([E[0], G[0]], [E[1], G[1]], 'k')
ax1.plot([F[0], G[0]], [F[1], G[1]], 'k')

ax1.scatter(list_x_2, list_y_2, s = 12, color = 'k')

arc1 = mpatches.Arc(G, 2*d_DG, 2*d_DG)
ax1.add_patch(arc1)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, ha = 'right', va = 'top', size = 16)
label_B = ax1.annotate(r'$B$', B, ha = 'left', va = 'top', size = 16)
label_C = ax1.annotate(r'$C$', C, ha = 'center', va = 'bottom', size = 16)
label_D = ax1.annotate(r'$D$', D, ha = 'center', va = 'top', size = 16)
label_E = ax1.annotate(r'$E$', E, ha = 'right', va = 'bottom', size = 16)
label_F = ax1.annotate(r'$F$', F, ha = 'left', va = 'bottom', size = 16)
label_G = ax1.annotate(r'$G$', G, ha = 'right', va = 'center', size = 16)

label_angle1 = ax1.annotate(r'$\urcorner$', D, size = 26)
label_angle2 = ax1.annotate(r'$\urcorner$', E, size = 26, rotation = 245)
label_angle3 = ax1.annotate(r'$\urcorner$', F, size = 26, rotation = -137)

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