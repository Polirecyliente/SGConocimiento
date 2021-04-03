#T# the following code shows how to draw a median of a triangle

#T# to draw a median of a triangle, the pyplot module of the matplotlib package is used
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
D = ((A[0] + B[0])/2, (A[1] + B[1])/2)

list1 = [C[0], A[0], B[0], C[0], D[0]]
list2 = [C[1], A[1], B[1], C[1], D[1]]

p_mid_AD = ((A[0] + D[0])/2, (A[1] + D[1])/2) #| auxiliary points for the markers
p_mid_DB = ((D[0] + B[0])/2, (D[1] + B[1])/2)

list1_1 = [p_mid_AD[0], p_mid_DB[0]] #| coordinates of the markers
list2_1 = [p_mid_AD[1], p_mid_DB[1]]

#T# plot the figure
ax1.plot(list1, list2, 'k')

#T# plot the points
ax1.scatter(list1, list2, s = 12, color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$|$')
marker1._transform.scale(1.6, 2.2)

#T# plot the markers
ax1.plot(list1_1, list2_1, 'k', marker = marker1)

#T# create the labels
label_A = ax1.annotate(r'$A$', A, ha = 'right', va = 'top', size = 18)
label_B = ax1.annotate(r'$B$', B, ha = 'left', va = 'top', size = 18)
label_C = ax1.annotate(r'$C$', C, ha = 'center', va = 'bottom', size = 18)
label_D = ax1.annotate(r'$D$', D, ha = 'right', va = 'top', size = 18)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()

#T# show the result
plt.show()