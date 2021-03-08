#T# the following code shows how to draw a circle to show examples of segments and lines of circles

#T# to draw a circle to show examples of segments and lines of circles, the pyplot module of the matplotlib package is used
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
A = (0, 0)
r = 1

a_B = math.pi/5
B = (r*math.cos(a_B), r*math.sin(a_B)) #| radius

a_C = math.pi*4.8/5
a_D = a_C + math.pi
C = (r*math.cos(a_C), r*math.sin(a_C)) #| diameter
D = (r*math.cos(a_D), r*math.sin(a_D))

a_E = math.pi*4/5
a_F = math.pi*2/5
E = (r*math.cos(a_E), r*math.sin(a_E)) #| chord
F = (r*math.cos(a_F), r*math.sin(a_F))

a_G = 3.72
a_H = 5.935
G = (r*math.cos(a_G), r*math.sin(a_G)) #| secant
H = (r*math.cos(a_H), r*math.sin(a_H))
G1 = (-1.3, -.6)
H1 = (1.3, -.3)

a_I = math.pi*3.2/2
I = (r*math.cos(a_I), r*math.sin(a_I)) #| tangent

m_AI = (I[1] - A[1])/(I[0] - A[0])
m_perp_AI = -1/m_AI
b_perp_AI = I[1] - m_perp_AI*I[0]

x_I1 = -.6
y_I1 = m_perp_AI*x_I1 + b_perp_AI
x_I2 = 1.15
y_I2 = m_perp_AI*x_I2 + b_perp_AI
I1 = (x_I1, y_I1)
I2 = (x_I2, y_I2)

list_x_1 = [A[0], B[0]]
list_y_1 = [A[1], B[1]]

list_x_2 = [C[0], D[0]]
list_y_2 = [C[1], D[1]]

list_x_3 = [E[0], F[0]]
list_y_3 = [E[1], F[1]]

list_x_4 = [G[0], H[0]]
list_y_4 = [G[1], H[1]]

#T# plot the figure
circle1 = mpatches.Arc(A, 2*r, 2*r, linewidth = 1.5)
ax1.add_patch(circle1)

ax1.plot(list_x_1, list_y_1, 'o-k', markersize = 3)
ax1.plot(list_x_2, list_y_2, 'o-k', markersize = 3)
ax1.plot(list_x_3, list_y_3, 'o-k', markersize = 3)
ax1.plot(list_x_4, list_y_4, 'o-k', markersize = 3)
line1 = mpatches.FancyArrowPatch(G1, H1, arrowstyle = '<->', mutation_scale = 12, linewidth = 1.5)
ax1.add_patch(line1)
ax1.plot(I[0], I[1], 'o-k', markersize = 3)
line2 = mpatches.FancyArrowPatch(I1, I2, arrowstyle = '<->', mutation_scale = 12, linewidth = 1.5)
ax1.add_patch(line2)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 16)
label_radius = ax1.annotate(r'$radius$', (-1, 1), size = 16)
label_diameter = ax1.annotate(r'$diameter$', (0, 1), size = 16)
label_chord = ax1.annotate(r'$chord$', (1, 1), size = 16)
label_secant = ax1.annotate(r'$secant$', (-1, -1), size = 16)
label_tangent = ax1.annotate(r'$tangent$', (0, -1), size = 16)

#T# drag the labels if needed
label_A.draggable()
label_radius.draggable()
label_diameter.draggable()
label_chord.draggable()
label_secant.draggable()
label_tangent.draggable()

#T# show the results
ax1.autoscale()
plt.show()