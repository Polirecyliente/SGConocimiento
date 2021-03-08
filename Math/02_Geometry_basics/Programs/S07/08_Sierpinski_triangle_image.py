#T# the following code shows how to draw a Sierpinski triangle with two iterations

#T# to draw a Sierpinski triangle with two iterations, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# create the figure and axes
fig1, ax_list1 = plt.subplots(1, 3)

#T# set the aspect of the axes
for it1 in fig1.axes:
    it1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in fig1.axes:
    for it2 in ['top', 'bottom', 'left', 'right']:
        it1.spines[it2].set_visible(False)
    it1.get_xaxis().set_visible(False)
    it1.get_yaxis().set_visible(False)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# title the axes
ypos = -.4
ax_list1[0].set_title(r'$Stage\ 0$', y = ypos)
ax_list1[1].set_title(r'$Stage\ 1$', y = ypos)
ax_list1[2].set_title(r'$Stage\ 2$', y = ypos)

#T# create the variables that define the plot
A = (0.2, 1)
B = (0, 0)
C = (2.4, 2)

t1_1_A = ((B[0] + C[0])/2, (B[1] + C[1])/2)
t1_1_B = ((A[0] + C[0])/2, (A[1] + C[1])/2)
t1_1_C = ((A[0] + B[0])/2, (A[1] + B[1])/2)
tris1 = {'t1_1': (t1_1_A, t1_1_B, t1_1_C)} #| triangles that result from iteration 1

t1_2_A = ((t1_1_B[0] + t1_1_C[0])/2, (t1_1_B[1] + t1_1_C[1])/2)
t1_2_B = ((A[0] + t1_1_B[0])/2, (A[1] + t1_1_B[1])/2)
t1_2_C = ((A[0] + t1_1_C[0])/2, (A[1] + t1_1_C[1])/2)
t2_2_A = ((t1_1_A[0] + B[0])/2, (t1_1_A[1] + B[1])/2)
t2_2_B = ((t1_1_A[0] + t1_1_C[0])/2, (t1_1_A[1] + t1_1_C[1])/2)
t2_2_C = ((B[0] + t1_1_C[0])/2, (B[1] + t1_1_C[1])/2)
t3_2_A = ((t1_1_A[0] + C[0])/2, (t1_1_A[1] + C[1])/2)
t3_2_B = ((t1_1_B[0] + C[0])/2, (t1_1_B[1] + C[1])/2)
t3_2_C = ((t1_1_A[0] + t1_1_B[0])/2, (t1_1_A[1] + t1_1_B[1])/2)
tris2 = {'t1_2': (t1_2_A, t1_2_B, t1_2_C), 't2_2': (t2_2_A, t2_2_B, t2_2_C), 't3_2': (t3_2_A, t3_2_B, t3_2_C)}

list_x_1 = [A[0], B[0], C[0], A[0]]
list_y_1 = [A[1], B[1], C[1], A[1]]

#T# plot the figure
ax_list1[0].plot(list_x_1, list_y_1, 'k')
ax_list1[1].plot(list_x_1, list_y_1, 'k')
ax_list1[2].plot(list_x_1, list_y_1, 'k')

tris1_t1 = mpatches.Polygon(tris1['t1_1'], color = 'k')
ax_list1[1].add_patch(tris1_t1)
tris1_t1 = mpatches.Polygon(tris1['t1_1'], color = 'k')
ax_list1[2].add_patch(tris1_t1)

tris2_t1 = mpatches.Polygon(tris2['t1_2'], color = 'k')
ax_list1[2].add_patch(tris2_t1)
tris2_t2 = mpatches.Polygon(tris2['t2_2'], color = 'k')
ax_list1[2].add_patch(tris2_t2)
tris2_t3 = mpatches.Polygon(tris2['t3_2'], color = 'k')
ax_list1[2].add_patch(tris2_t3)

#T# show the results
plt.show()