#T# the following code shows how to draw a dart shape

#T# to draw a dart shape, the pyplot module of the matplotlib package is used
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
A = (0, 0)
B = (2, -1)
C = (0, 2)
D = (-2, -1)

a0_AB = math.atan2(B[1] - A[1], B[0] - A[0])
a0_BC = math.atan2(C[1] - B[1], C[0] - B[0])

p_mid_AB = ((A[0] + B[0])/2, (A[1] + B[1])/2)
p_mid_BC = ((B[0] + C[0])/2, (B[1] + C[1])/2)
p_mid_CD = ((C[0] + D[0])/2, (C[1] + D[1])/2)
p_mid_AD = ((A[0] + D[0])/2, (A[1] + D[1])/2)

list_x1 = [A[0], B[0], C[0], D[0], A[0]]
list_y1 = [A[1], B[1], C[1], D[1], A[1]]

#T# plot the figure
ax1.plot(list_x1, list_y1, 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
ax1.annotate(r'$|$', p_mid_AB, ha = 'center', va = 'center', size = 20, rotation = math.degrees(a0_AB))
ax1.annotate(r'$|$', p_mid_AD, ha = 'center', va = 'center', size = 20, rotation = math.degrees(-a0_AB))
ax1.annotate(r'$||$', p_mid_BC, ha = 'center', va = 'center', size = 20, rotation = math.degrees(a0_BC))
ax1.annotate(r'$||$', p_mid_CD, ha = 'center', va = 'center', size = 20, rotation = math.degrees(-a0_BC))

#T# show the results
plt.show()