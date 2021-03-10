#T# the following code shows how to draw a rhombus

#T# to draw a rhombus, the pyplot module of the matplotlib package is used
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
d1 = 5
a1 = math.radians(68)

A = (0, 0)
B = (d1, 0)
C = (d1 + d1*math.cos(a1), d1*math.sin(a1))
D = (d1*math.cos(a1), d1*math.sin(a1))

list_x1 = [A[0], B[0], C[0], D[0], A[0]]
list_y1 = [A[1], B[1], C[1], D[1], A[1]]

p_mid_AB = ((A[0] + B[0])/2, (A[1] + B[1])/2)
p_mid_BC = ((B[0] + C[0])/2, (B[1] + C[1])/2)
p_mid_CD = ((C[0] + D[0])/2, (C[1] + D[1])/2)
p_mid_DA = ((D[0] + A[0])/2, (D[1] + A[1])/2)

#T# plot the figure
ax1.plot(list_x1, list_y1, 'k')

#T# create the labels
label_mid1 = ax1.annotate(r'$|$', p_mid_AB, ha = 'center', va = 'center', size = 17, rotation = 0)
label_mid2 = ax1.annotate(r'$|$', p_mid_BC, ha = 'center', va = 'center', size = 17, rotation = math.degrees(a1))
label_mid3 = ax1.annotate(r'$|$', p_mid_CD, ha = 'center', va = 'center', size = 17, rotation = 0)
label_mid4 = ax1.annotate(r'$|$', p_mid_DA, ha = 'center', va = 'center', size = 17, rotation = math.degrees(a1))

#T# drag the labels if needed
label_mid1.draggable()
label_mid2.draggable()
label_mid3.draggable()
label_mid4.draggable()

#T# show the results
plt.show()