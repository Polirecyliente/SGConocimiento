#T# the following code shows how to draw the orthocenter of a triangle

#T# to draw the orthocenter of a triangle, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax_list1 = plt.subplots(1, 3)

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
A1, B1, C1 = (0, 0), (4, 0), (-3, 4)
D1 = (-3, 0)

m_C1B1 = (B1[1] - C1[1])/(B1[0] - C1[0])
m_perp_C1B1 = -1/m_C1B1
m_C1A1 = (A1[1] - C1[1])/(A1[0] - C1[0])
m_perp_C1A1 = -1/m_C1A1

list_x1 = [C1[0], A1[0], B1[0], C1[0]]
list_y1 = [C1[1], A1[1], B1[1], C1[1]]

A2, B2, C2 = (0, 0), (4, 0), (0, 3)

m_C2B2 = (B2[1] - C2[1])/(B2[0] - C2 [0])
m_perp_C2B2 = -1/m_C2B2

list_x2 = [C2[0], A2[0], B2[0], C2[0]]
list_y2 = [C2[1], A2[1], B2[1], C2[1]]

A3, B3, C3 = (0, 0), (4, 0), (3, 3)
D3 = (3, 0)

m_A3C3 = (C3[1] - A3[1])/(C3[0] - A3[0])
m_perp_A3C3 = -1/m_A3C3
m_B3C3 = (C3[1] - B3[1])/(C3[0] - B3[0])
m_perp_B3C3 = -1/m_B3C3

list_x3 = [C3[0], A3[0], B3[0], C3[0]]
list_y3 = [C3[1], A3[1], B3[1], C3[1]]

#T# set the axes size
f1 = 1.8

ax_list1[0].axis([min(A1[0], B1[0], C1[0]) - f1, max(A1[0], B1[0], C1[0]) + f1, min(A1[1], B1[1], C1[1]) - f1 - 6, max(A1[1], B1[1], C1[1]) + f1])

ax_list1[1].axis([min(A2[0], B2[0], C2[0]) - f1, max(A2[0], B2[0], C2[0]) + f1, min(A2[1], B2[1], C2[1]) - f1, max(A2[1], B2[1], C2[1]) + f1])

ax_list1[2].axis([min(A3[0], B3[0], C3[0]) - f1, max(A3[0], B3[0], C3[0]) + f1, min(A3[1], B3[1], C3[1]) - f1, max(A3[1], B3[1], C3[1]) + f1])

#T# title the axes
ax_list1[0].set_title(r'$Obtuse\ triangle$', y = 1)
ax_list1[1].set_title(r'$Right\ triangle$', y = 1)
ax_list1[2].set_title(r'$Acute\ triangle$', y = 1)

#T# plot the figure
ax_list1[0].plot(list_x1, list_y1, 'o-k', markersize = 3.5)

ax_list1[0].axline(A1, slope = m_perp_C1B1, alpha = .7)

ax_list1[0].axline(A1, C1, color = 'k', linestyle = '--')
ax_list1[0].axline(B1, slope = m_perp_C1A1, alpha = .7)

ax_list1[0].axline(A1, B1, color = 'k', linestyle = '--')
ax_list1[0].axline(C1, D1, alpha = .7)

ax_list1[1].plot(list_x2, list_y2, 'o-k', markersize = 3.5)

ax_list1[1].axline(A2, slope = m_perp_C2B2, alpha = .7)

ax_list1[1].axline(A2, B2, alpha = .7)

ax_list1[1].axline(A2, C2, alpha = .7)

ax_list1[2].plot(list_x3, list_y3, 'o-k', markersize = 3.5)

ax_list1[2].axline(A3, slope = m_perp_B3C3, alpha = .7)

ax_list1[2].axline(B3, slope = m_perp_A3C3, alpha = .7)

ax_list1[2].axline(C3, D3, alpha = .7)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_a1_1 = ax_list1[0].annotate(r'$\llcorner$', A1, ha = 'center', va = 'top', size = 18, rotation = -33)
label_a2_1 = ax_list1[0].annotate(r'$\urcorner$', B1, ha = 'center', va = 'top', size = 18, rotation = -55)
label_a3_1 = ax_list1[0].annotate(r'$\urcorner$', C1, ha = 'center', va = 'bottom', size = 18, rotation = 0)

label_a1_2 = ax_list1[1].annotate(r'$\llcorner$', A2, ha = 'left', va = 'top', size = 18, rotation = -40)
label_a2_2 = ax_list1[1].annotate(r'$\urcorner$', B2, ha = 'right', va = 'bottom', size = 18, rotation = 0)

label_a1_3 = ax_list1[2].annotate(r'$\llcorner$', A3, ha = 'left', va = 'bottom', size = 18, rotation = -70)
label_a2_3 = ax_list1[2].annotate(r'$\llcorner$', B3, ha = 'right', va = 'top', size = 18, rotation = 45)
label_a3_3 = ax_list1[2].annotate(r'$\urcorner$', C3, ha = 'right', va = 'top', size = 18, rotation = 0)

#T# drag the labels if needed
label_a1_1.draggable()
label_a2_1.draggable()
label_a3_1.draggable()

label_a1_2.draggable()
label_a2_2.draggable()

label_a1_3.draggable()
label_a2_3.draggable()
label_a3_3.draggable()

#T# show the results
plt.show()