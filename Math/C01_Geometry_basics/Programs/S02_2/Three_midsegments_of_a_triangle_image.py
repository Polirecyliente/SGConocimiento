#T# the following code shows how to draw a triangle with is three midsegments

#T# to draw a triangle with its three midsegments, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

#T# create the variables that define the plot
A, B, C = (1, 2), (8, 2), (3.5, 7)
D = ((A[0] + C[0])/2, (A[1] + C[1])/2)
E = ((B[0] + C[0])/2, (B[1] + C[1])/2)
F = ((A[0] + B[0])/2, (A[1] + B[1])/2)

list1 = [A[0], B[0], C[0], A[0], D[0], E[0], F[0], D[0]]
list2 = [A[1], B[1], C[1], A[1], D[1], E[1], F[1], D[1]]

p_mid_AD = ((A[0] + D[0])/2, (A[1] + D[1])/2) #| auxiliary points for the markers
p_mid_DC = ((D[0] + C[0])/2, (D[1] + C[1])/2)
p_mid_BE = ((B[0] + E[0])/2, (B[1] + E[1])/2)
p_mid_EC = ((E[0] + C[0])/2, (E[1] + C[1])/2)
p_mid_AF = ((A[0] + F[0])/2, (A[1] + F[1])/2)
p_mid_FB = ((F[0] + B[0])/2, (F[1] + B[1])/2)

list1_1 = [p_mid_AD[0], p_mid_DC[0]] #| coordinates of the markers
list2_1 = [p_mid_AD[1], p_mid_DC[1]]

list1_2 = [p_mid_BE[0], p_mid_EC[0]]
list2_2 = [p_mid_BE[1], p_mid_EC[1]]

list1_3 = [p_mid_AF[0], p_mid_FB[0]]
list2_3 = [p_mid_AF[1], p_mid_FB[1]]

#T# plot the figure
ax1.plot(list1, list2, 'k')

ax1.scatter(list1, list2, s = 12, color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$|$')
marker1._transform.scale(2, 2.4)
marker1._transform.rotate_deg(63)

marker2 = MarkerStyle(r'$||$')
marker2._transform.scale(2, 2.4)
marker2._transform.rotate_deg(-48)

marker3 = MarkerStyle(r'$|||$')
marker3._transform.scale(2.4, 2.4)
marker3._transform.rotate_deg(0)

#T# plot the markers
ax1.plot(list1_1, list2_1, 'k', marker = marker1)
ax1.plot(list1_2, list2_2, 'k', marker = marker2)
ax1.plot(list1_3, list2_3, 'k', marker = marker3)

#T# create the labels
label_A = ax1.annotate(r'$A$', (A[0], A[1]), ha = 'right', va = 'top', size = 18)
label_B = ax1.annotate(r'$B$', (B[0], B[1]), ha = 'left', va = 'top', size = 18)
label_C = ax1.annotate(r'$C$', (C[0], C[1]), ha = 'center', va = 'bottom', size = 18)
label_D = ax1.annotate(r'$D$', (D[0], D[1]), ha = 'right', va = 'center', size = 18)
label_E = ax1.annotate(r'$E$', (E[0], E[1]), ha = 'left', va = 'center', size = 18)
label_F = ax1.annotate(r'$F$', (F[0], F[1]), ha = 'center', va = 'top', size = 18)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()
label_E.draggable()
label_F.draggable()

#T# show the result
plt.show()