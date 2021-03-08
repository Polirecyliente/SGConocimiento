#T# the following code shows how to draw a perpendicular bisector to show the perpendicular bisector theorem

#T# to draw a perpendicular bisector to show the perpendicular bisector theorem, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

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
B = (1, 0)
C = (.5, 1.2)
D = ((A[0] + B[0])/2, (A[1] + B[1])/2)

C2 = (.5, 1.47)
D2 = (.5, -.27)

list1 = [A[0], B[0], C[0], A[0]] #| x coordinates
list2 = [A[1], B[1], C[1], A[1]] #| y coordinates

p_mid_AD = ((A[0] + D[0])/2, (A[1] + D[1])/2) #| auxiliary point for the markers
p_mid_DB = ((D[0] + B[0])/2, (D[1] + B[1])/2) #| auxiliary point for the markers

#T# plot the figure
ax1.plot(list1, list2, 'k')
ax1.plot([.5, .5], [0, 1.2], 'k')

line1 = mpatches.FancyArrowPatch(C2, D2, arrowstyle = '<->', mutation_scale = 12)
ax1.add_patch(line1)

ax1.scatter(list1, list2, s = 12, color = 'k')
ax1.scatter([.5, .5], [0, 1.2], s = 12, color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the markers
marker1 = MarkerStyle(r'$|$')
marker1._transform.scale(1, 2.6)

#T# plot the markers
ax1.plot([p_mid_AD[0], p_mid_DB[0]], [p_mid_AD[1], p_mid_DB[1]], 'k', marker = marker1)

#T# create the labels
label1 = ax1.annotate(r'$A$', A, ha = 'right', va = 'top', size = 16)
label2 = ax1.annotate(r'$B$', B, ha = 'left', va = 'top', size = 16)
label3 = ax1.annotate(r'$C$', C, ha = 'right', va = 'bottom', size = 16)
label4 = ax1.annotate(r'$D$', D, ha = 'right', va = 'top', size = 16)

#T# drag the labels if needed
label1.draggable()
label2.draggable()
label3.draggable()
label4.draggable()

#T# show the results
plt.show()