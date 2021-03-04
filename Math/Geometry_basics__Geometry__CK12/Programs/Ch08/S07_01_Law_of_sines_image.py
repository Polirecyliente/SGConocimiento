#T# the following code shows how to draw two triangles to show the law of sines

#T# to draw two triangles to show the law of sines, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# import the math module to do calculations
import math

#T# create the figure and axes
fig1, ax_list1 = plt.subplots(1, 2)

#T# set the aspect of the axes
for it1 in fig1.axes:
    it1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in fig1.axes:
    for it2 in ['top', 'bottom', 'left', 'right']:
        it1.spines[it2].set_visible(False)
        it1.xaxis.set_visible(False)
        it1.yaxis.set_visible(False)

#T# create the variables that define the plot
A = (0, 0)
B = (4, 0)
C = (3, 3)

D1 = (3, 0)

m_AC = (C[1] - A[1])/(C[0] - A[0])
m_perp_AC = -1/m_AC

b_AC = A[1] - m_AC*A[0]
b_perp_AC = B[1] - m_perp_AC*B[0]

x_D2 = (b_perp_AC - b_AC)/(m_AC - m_perp_AC)
y_D2 = m_AC*x_D2 + b_AC
D2 = (x_D2, y_D2)

a_0_BD2 = math.atan2(D2[1] - B[1], D2[0] - B[0])

list_x_1 = [A[0], B[0], C[0], A[0]]
list_y_1 = [A[1], B[1], C[1], A[1]]

list_x_2a = [D1[0], C[0]]
list_y_2a = [D1[1], C[1]]

list_x_2b = [D2[0], B[0]]
list_y_2b = [D2[1], B[1]]

#T# plot the figure
ax_list1[0].plot(list_x_1, list_y_1, 'o-k', markersize = 3)
ax_list1[1].plot(list_x_1, list_y_1, 'o-k', markersize = 3)

ax_list1[0].plot(list_x_2a, list_y_2a, 'o-k', markersize = 3)

ax_list1[1].plot(list_x_2b, list_y_2b, 'o-k', markersize = 3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A1 = ax_list1[0].annotate(r'$A$', A, size = 16)
label_A2 = ax_list1[1].annotate(r'$A$', A, size = 16)
label_B1 = ax_list1[0].annotate(r'$B$', B, size = 16)
label_B2 = ax_list1[1].annotate(r'$B$', B, size = 16)
label_C1 = ax_list1[0].annotate(r'$C$', C, size = 16)
label_C2 = ax_list1[1].annotate(r'$C$', C, size = 16)
label_D1 = ax_list1[0].annotate(r'$D_1$', D1, size = 16)
label_D2 = ax_list1[1].annotate(r'$D_2$', D2, size = 16)
label_a1 = ax_list1[0].annotate(r'$a$', (0, 1), size = 16)
label_a2 = ax_list1[1].annotate(r'$a$', (0, 1), size = 16)
label_b1 = ax_list1[0].annotate(r'$b$', (1, 1), size = 16)
label_b2 = ax_list1[1].annotate(r'$b$', (1, 1), size = 16)
label_c1 = ax_list1[0].annotate(r'$c$', (2, 1), size = 16)
label_c2 = ax_list1[1].annotate(r'$c$', (2, 1), size = 16)
label_h1 = ax_list1[0].annotate(r'$h_1$', (3, 1), size = 16)
label_h2 = ax_list1[1].annotate(r'$h_2$', (3, 1), size = 16)
a_marker1 = ax_list1[0].annotate(r'$\ulcorner$', (2, 0), size = 24)
a_marker2 = ax_list1[1].annotate(r'$\ulcorner$', (2, 0), size = 24, rotation = math.degrees(a_0_BD2))

#T# drag the labels if needed
label_A1.draggable()
label_A2.draggable()
label_B1.draggable()
label_B2.draggable()
label_C1.draggable()
label_C2.draggable()
label_D1.draggable()
label_D2.draggable()
label_a1.draggable()
label_a2.draggable()
label_b1.draggable()
label_b2.draggable()
label_c1.draggable()
label_c2.draggable()
label_h1.draggable()
label_h2.draggable()
a_marker1.draggable()
a_marker2.draggable()

#T# show the results
plt.show()