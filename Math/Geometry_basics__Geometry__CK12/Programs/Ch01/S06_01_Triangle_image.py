#T# the following code shows how to draw a triangle

#T# to draw a triangle, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

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
p0 = (0, 0)
p1 = (3, 1)
p2 = (2, 3)

list1 = [p0[0], p1[0], p2[0], p0[0]] #| x coordinates
list2 = [p0[1], p1[1], p2[1], p0[1]] #| y coordinates

#T# plot the figure
plt.plot(list1, list2, 'k')
plt.scatter(list1, list2, s = 9, color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label1 = plt.annotate(r'$A$', p0, ha = 'right', va = 'top', size = 16)
label2 = plt.annotate(r'$B$', p1, ha = 'left', va = 'top', size = 16)
label3 = plt.annotate(r'$C$', p2, ha = 'center', va = 'bottom', size = 16)

#T# drag the labels if needed
label1.draggable()
label2.draggable()
label3.draggable()

#T# show the results
plt.show()