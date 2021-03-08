#T# the following code shows how to draw a few triangles to show the triangle inequality theorem

#T# to draw a few triangles to show the triangle inequality theorem, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax_list1 = plt.subplots(2, 2)

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
A1, B1, C1, D1 = (2, 1), (0, 0), (7, 0), (5, .5)

list_x1 = [A1[0], B1[0], C1[0], D1[0]]
list_y1 = [A1[1], B1[1], C1[1], D1[1]]

A2, B2, C2 = (2, 1), (0, 0), (3, 0)

list_x2 = [A2[0], B2[0], C2[0], A2[0]]
list_y2 = [A2[1], B2[1], C2[1], A2[1]]

A3, B3, C3, D3 = (1, 0), (0, 0), (7, 2), (6, 1)

list_x3 = [A3[0], B3[0], C3[0], D3[0]]
list_y3 = [A3[1], B3[1], C3[1], D3[1]]

A4, B4, C4 = (3, 1), (0, 0), (1, 0)

list_x4 = [A4[0], B4[0], C4[0], A4[0]]
list_y4 = [A4[1], B4[1], C4[1], A4[1]]

#T# plot the figure
ax_list1[0][0].plot(list_x1, list_y1, 'k')
ax_list1[1][0].plot(list_x2, list_y2, 'k')
ax_list1[0][1].plot(list_x3, list_y3, 'k')
ax_list1[1][1].plot(list_x4, list_y4, 'k')

#T# title the axes
ax_list1[0][0].set_title(r'$c \geq a + b$', y = 2)
ax_list1[1][0].set_title(r'$c < a + b$', y = 1.3)
ax_list1[0][1].set_title(r'$c \leq |a - b|$', y = 1.3)
ax_list1[1][1].set_title(r'$c > |a - b|$', y = 1.3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_a1 = ax_list1[0][0].annotate(r'$a$', A1, size = 18)
label_b1 = ax_list1[0][0].annotate(r'$b$', D1, size = 18)
label_c1 = ax_list1[0][0].annotate(r'$c$', C1, size = 18)

label_a2 = ax_list1[1][0].annotate(r'$a$', A2, size = 18)
label_b2 = ax_list1[1][0].annotate(r'$b$', B2, size = 18)
label_c2 = ax_list1[1][0].annotate(r'$c$', C2, size = 18)

label_a3 = ax_list1[0][1].annotate(r'$a$', A3, size = 18)
label_b3 = ax_list1[0][1].annotate(r'$b$', B3, size = 18)
label_c3 = ax_list1[0][1].annotate(r'$c$', C3, size = 18)

label_a4 = ax_list1[1][1].annotate(r'$a$', A4, size = 18)
label_b4 = ax_list1[1][1].annotate(r'$b$', B4, size = 18)
label_c4 = ax_list1[1][1].annotate(r'$c$', C4, size = 18)

#T# drag the labels if needed
label_a1.draggable()
label_b1.draggable()
label_c1.draggable()

label_a2.draggable()
label_b2.draggable()
label_c2.draggable()

label_a3.draggable()
label_b3.draggable()
label_c3.draggable()

label_a4.draggable()
label_b4.draggable()
label_c4.draggable()

#T# show the results
plt.show()