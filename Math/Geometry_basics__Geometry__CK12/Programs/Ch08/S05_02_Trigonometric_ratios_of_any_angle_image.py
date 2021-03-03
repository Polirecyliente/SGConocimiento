#T# the following code shows how to draw right triangles to show the trigonometric ratios of any angle

#T# to draw right triangles to show the trigonometric ratios of any angle, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax_list1 = plt.subplots(2, 2)

#T# set the aspect of the axes
for it1 in fig1.axes:
    it1.set_aspect('equal', adjustable = 'datalim')

#T# hide the spines and ticks
for it1 in fig1.axes:
    for it2 in ['top', 'right']:
        it1.spines[it2].set_visible(False)

#T# position the spines and ticks
for it1 in fig1.axes:
    for it2 in ['top', 'bottom', 'left', 'right']:
        it1.spines[it2].set_position(('data', 0))

ax_list1[0][0].xaxis.set_ticks_position('bottom')
ax_list1[0][0].yaxis.set_ticks_position('left')
ax_list1[0][1].xaxis.set_ticks_position('bottom')
ax_list1[0][1].yaxis.set_ticks_position('right')
ax_list1[1][0].xaxis.set_ticks_position('top')
ax_list1[1][0].yaxis.set_ticks_position('right')
ax_list1[1][1].xaxis.set_ticks_position('top')
ax_list1[1][1].yaxis.set_ticks_position('left')

#T# create the variables that define the plot
A1 = (0, 0)
B1 = (2, 0)
C1 = (2, 3)

A2 = (0, 0)
B2 = (-2, 0)
C2 = (-2, 3)

A3 = (0, 0)
B3 = (-2, 0)
C3 = (-2, -3)

A4 = (0, 0)
B4 = (2, 0)
C4 = (2, -3)

list_x_1 = [A1[0], B1[0], C1[0], A1[0]]
list_y_1 = [A1[1], B1[1], C1[1], A1[1]]

list_x_2 = [A2[0], B2[0], C2[0], A2[0]]
list_y_2 = [A2[1], B2[1], C2[1], A2[1]]

list_x_3 = [A3[0], B3[0], C3[0], A3[0]]
list_y_3 = [A3[1], B3[1], C3[1], A3[1]]

list_x_4 = [A4[0], B4[0], C4[0], A4[0]]
list_y_4 = [A4[1], B4[1], C4[1], A4[1]]

#T# set the axes size
ax_list1[0][0].axis([-C1[0], C1[0], -C1[1], C1[1]])
ax_list1[0][1].axis([C2[0], -C2[0], -C2[1], C2[1]])
ax_list1[1][0].axis([C3[0], -C3[0], C3[1], -C3[1]])
ax_list1[1][1].axis([-C4[0], C4[0], C4[1], -C4[1]])

#T# plot the figure
ax_list1[0][0].plot(list_x_1, list_y_1, 'o-k', markersize = 3, clip_on = False)
ax_list1[0][1].plot(list_x_2, list_y_2, 'o-k', markersize = 3, clip_on = False)
ax_list1[1][0].plot(list_x_3, list_y_3, 'o-k', markersize = 3, clip_on = False)
ax_list1[1][1].plot(list_x_4, list_y_4, 'o-k', markersize = 3, clip_on = False)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_a1 = ax_list1[0][0].annotate(r'$a$', (1, 0), size = 16)
label_b1 = ax_list1[0][0].annotate(r'$b$', (1, 1), size = 16)
label_c1 = ax_list1[0][0].annotate(r'$c$', (1, 2), size = 16)
a_marker1 = ax_list1[0][0].annotate(r'$\ulcorner$', (1, 1), size = 18)

label_a2 = ax_list1[0][1].annotate(r'$a$', (1, 0), size = 16)
label_b2 = ax_list1[0][1].annotate(r'$b$', (1, 1), size = 16)
label_c2 = ax_list1[0][1].annotate(r'$c$', (1, 2), size = 16)
a_marker2 = ax_list1[0][1].annotate(r'$\urcorner$', (1, 1), size = 18)

label_a3 = ax_list1[1][0].annotate(r'$a$', (1, 0), size = 16)
label_b3 = ax_list1[1][0].annotate(r'$b$', (1, 1), size = 16)
label_c3 = ax_list1[1][0].annotate(r'$c$', (1, 2), size = 16)
a_marker3 = ax_list1[1][0].annotate(r'$\lrcorner$', (1, 1), size = 18)

label_a4 = ax_list1[1][1].annotate(r'$a$', (1, 0), size = 16)
label_b4 = ax_list1[1][1].annotate(r'$b$', (1, 1), size = 16)
label_c4 = ax_list1[1][1].annotate(r'$c$', (1, 2), size = 16)
a_marker4 = ax_list1[1][1].annotate(r'$\llcorner$', (1, 1), size = 18)

#T# drag the labels if needed
label_a1.draggable()
label_b1.draggable()
label_c1.draggable()
a_marker1.draggable()

label_a2.draggable()
label_b2.draggable()
label_c2.draggable()
a_marker2.draggable()

label_a3.draggable()
label_b3.draggable()
label_c3.draggable()
a_marker3.draggable()

label_a4.draggable()
label_b4.draggable()
label_c4.draggable()
a_marker4.draggable()

#T# show the results
plt.show()