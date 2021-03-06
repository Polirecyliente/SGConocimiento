#T# the following code shows how to draw two concentric circles

#T# to draw two concentric circles, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

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
r1 = 1
r2 = .6

list_x_1 = [A[0]]
list_y_1 = [A[1]]

#T# plot the figure
circle1 = mpatches.Arc(A, 2*r1, 2*r1, linewidth = 1.5)
circle2 = mpatches.Arc(A, 2*r2, 2*r2, linewidth = 1.5)
ax1.add_patch(circle1)
ax1.add_patch(circle2)

ax1.plot(list_x_1, list_y_1, 'ok', markersize = 3.5)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', A, size = 16)

#T# drag the labels if needed
label_A.draggable()

#T# show the results
ax1.autoscale()
plt.show()