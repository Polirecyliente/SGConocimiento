#T# the following code shows how to draw a regular polygon

#T# to draw a regular polygon, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# import the math module to do calculations
import math

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the variables that define the plot
n = 7
a = math.pi - (n - 2)*math.pi/n
d = 1.2

p1 = (0, 0)
p2 = (p1[0] + d, p1[1])
p3 = (p2[0] + d*math.cos(1*a), p2[1] + d*math.sin(1*a))
p4 = (p3[0] + d*math.cos(2*a), p3[1] + d*math.sin(2*a))
p5 = (p4[0] + d*math.cos(3*a), p4[1] + d*math.sin(3*a))
p6 = (p5[0] + d*math.cos(4*a), p5[1] + d*math.sin(4*a))
p7 = (p6[0] + d*math.cos(5*a), p6[1] + d*math.sin(5*a))

list_x1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p1[0]]
list_y1 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p1[1]]

#T# plot the figure
ax1.plot(list_x1, list_y1, 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_d1 = ax1.annotate(r'$d$', p1, ha = 'right', va = 'top', size = 18)
label_d2 = ax1.annotate(r'$d$', p2, ha = 'right', va = 'top', size = 18)
label_d3 = ax1.annotate(r'$d$', p3, ha = 'right', va = 'top', size = 18)
label_d4 = ax1.annotate(r'$d$', p4, ha = 'right', va = 'top', size = 18)
label_d5 = ax1.annotate(r'$d$', p5, ha = 'right', va = 'top', size = 18)
label_d6 = ax1.annotate(r'$d$', p6, ha = 'right', va = 'top', size = 18)
label_d7 = ax1.annotate(r'$d$', p7, ha = 'right', va = 'top', size = 18)

label_a1 = ax1.annotate(r'$\theta$', p1, ha = 'left', va = 'bottom', size = 18)
label_a2 = ax1.annotate(r'$\theta$', p2, ha = 'left', va = 'bottom', size = 18)
label_a3 = ax1.annotate(r'$\theta$', p3, ha = 'left', va = 'bottom', size = 18)
label_a4 = ax1.annotate(r'$\theta$', p4, ha = 'left', va = 'bottom', size = 18)
label_a5 = ax1.annotate(r'$\theta$', p5, ha = 'left', va = 'bottom', size = 18)
label_a6 = ax1.annotate(r'$\theta$', p6, ha = 'left', va = 'bottom', size = 18)
label_a7 = ax1.annotate(r'$\theta$', p7, ha = 'left', va = 'bottom', size = 18)

#T# drag the labels if needed
label_d1.draggable()
label_d2.draggable()
label_d3.draggable()
label_d4.draggable()
label_d5.draggable()
label_d6.draggable()
label_d7.draggable()

label_a1.draggable()
label_a2.draggable()
label_a3.draggable()
label_a4.draggable()
label_a5.draggable()
label_a6.draggable()
label_a7.draggable()

#T# show the results
plt.show()