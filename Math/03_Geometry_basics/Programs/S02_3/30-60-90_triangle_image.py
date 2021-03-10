#T# the following code shows how to draw a 30-60-90 triangle

#T# to draw a 30-60-90 triangle, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

#T# import the math module to do calculations
import math

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'datalim')

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the variables that define the plot
o = (0, 0)
A = (.5, 0)
B = (1, 0)
C = (.5, math.sqrt(3)/2)

list_x_1 = [A[0], B[0], C[0], o[0], A[0], C[0]]
list_y_1 = [A[1], B[1], C[1], o[1], A[1], C[1]]

p_mid_oA = [(o[0] + A[0])/2, (o[1] + A[1])/2]
p_mid_AB = [(A[0] + B[0])/2, (A[1] + B[1])/2]
p_mid_BC = [(B[0] + C[0])/2, (B[1] + C[1])/2]
p_mid_Co = [(C[0] + o[0])/2, (C[1] + o[1])/2]

#T# plot the figure
plt.plot(list_x_1, list_y_1, 'o-k', markersize = 3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 16)
label_B = ax1.annotate(r'$B$', B, size = 16)
label_C = ax1.annotate(r'$C$', C, size = 16)
a_marker1 = ax1.annotate(r'$\urcorner$', A, size = 26)

s_marker1 = ax1.annotate(r'$|$', p_mid_oA, ha = 'center', va = 'center', size = 18)
s_marker2 = ax1.annotate(r'$|$', p_mid_AB, ha = 'center', va = 'center', size = 18)
s_marker3 = ax1.annotate(r'$|$', p_mid_BC, ha = 'center', va = 'center', size = 18, rotation = 120)
s_marker4 = ax1.annotate(r'$|$', p_mid_Co, ha = 'center', va = 'center', size = 18, rotation = 60)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
a_marker1.draggable()

#T# show the results
plt.show()