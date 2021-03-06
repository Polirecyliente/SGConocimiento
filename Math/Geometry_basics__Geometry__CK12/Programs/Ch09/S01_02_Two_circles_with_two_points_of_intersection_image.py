#T# the following code shows how to draw two circles with two points of intersection

#T# to draw two circles with two points of intersection, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

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
A = (-.3, -1)
B = (.9, -.5)

C1 = (0, 1)
C2 = (.4, -1.8)

p_mid_AB = ((A[0] + B[0])/2, (A[1] + B[1])/2)
m_AB = (B[1] - A[1])/(B[0] - A[0])
m_perp_AB = -1/m_AB
b_perp_AB = p_mid_AB[1] - m_perp_AB*p_mid_AB[0]

p_mid_AC1 = ((A[0] + C1[0])/2, (A[1] + C1[1])/2)
m_AC1 = (C1[1] - A[1])/(C1[0] - A[0])
m_perp_AC1 = -1/m_AC1
b_perp_AC1 = p_mid_AC1[1] - m_perp_AC1*p_mid_AC1[0]

p_mid_AC2 = ((A[0] + C2[0])/2, (A[1] + C2[1])/2)
m_AC2 = (C2[1] - A[1])/(C2[0] - A[0])
m_perp_AC2 = -1/m_AC2
b_perp_AC2 = p_mid_AC2[1] - m_perp_AC2*p_mid_AC2[0]

x_center1 = (b_perp_AC1 - b_perp_AB)/(m_perp_AB - m_perp_AC1)
y_center1 = m_perp_AB*x_center1 + b_perp_AB
center1 = (x_center1, y_center1)
r1 = math.sqrt((A[0] - x_center1)**2 + (A[1] - y_center1)**2)

x_center2 = (b_perp_AC2 - b_perp_AB)/(m_perp_AB - m_perp_AC2)
y_center2 = m_perp_AB*x_center2 + b_perp_AB
center2 = (x_center2, y_center2)
r2 = math.sqrt((A[0] - x_center2)**2 + (A[1] - y_center2)**2)

list_x_1 = [A[0], B[0]]
list_y_1 = [A[1], B[1]]

#T# plot the figure
circle1 = mpatches.Arc(center1, 2*r1, 2*r1, linewidth = 1.5)
circle2 = mpatches.Arc(center2, 2*r2, 2*r2, linewidth = 1.5)
ax1.add_patch(circle1)
ax1.add_patch(circle2)

ax1.plot(list_x_1, list_y_1, 'ok', markersize = 3.5)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 16)
label_B = ax1.annotate(r'$B$', B, size = 16)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()

#T# show the results
ax1.autoscale()
plt.show()