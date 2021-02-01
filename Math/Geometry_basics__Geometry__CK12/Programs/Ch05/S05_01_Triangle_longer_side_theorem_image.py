#T# the following code shows how to draw a triangle to show the triangle longer side theorem

#T# to draw a triangle to show the triangle longer side theorem, the pyplot module of the matplotlib package is used
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
A, B, C = (0, 0), (4, 0), (-3, 4)

d_CA = math.sqrt((A[0] - C[0])**2 + (A[1] - C[1])**2)
a0_CB = math.atan2(B[1] - C[1], B[0]- C[0])

D = (C[0] + d_CA*math.cos(a0_CB), C[1] + d_CA*math.sin(a0_CB))

p_mid_AC = ((A[0] + C[0])/2, (A[1] + C[1])/2)
p_mid_CD = ((C[0] + D[0])/2, (C[1] + D[1])/2)

list_x = [C[0], A[0], B[0], D[0], A[0], D[0], C[0]] #| coordinates
list_y = [C[1], A[1], B[1], D[1], A[1], D[1], C[1]]

#T# plot the figure
ax1.plot(list_x, list_y, 'o-k', markersize = 3.5)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# plot the markers
ax1.annotate(r'$|$', (p_mid_AC[0], p_mid_AC[1]), ha = 'center', va = 'center', size = 18, rotation = -52)
ax1.annotate(r'$|$', (p_mid_CD[0], p_mid_CD[1]), ha = 'center', va = 'center', size = 18, rotation = -32)

#T# create the labels
label_A = ax1.annotate(r'$A$', A, ha = 'center', va = 'top', size = 18)
label_B = ax1.annotate(r'$B$', B, ha = 'center', va = 'top', size = 18)
label_C = ax1.annotate(r'$C$', C, ha = 'center', va = 'bottom', size = 18)
label_D = ax1.annotate(r'$D$', D, ha = 'center', va = 'top', size = 18)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()

#T# show the results
plt.show()