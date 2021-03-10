#T# the following code shows how to draw a right triangle

#T# to draw a right triangle, the pyplot module of the matplotlib package is used
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
p1 = (2, 0)
p2 = (0, 3)

list1 = [p0[0], p1[0], p2[0], p0[0]] #| x coordinates
list2 = [p0[1], p1[1], p2[1], p0[1]] #| y coordinates

#T# plot the figure
plt.plot(list1, list2, 'k')
plt.plot([.13, .13, 0], [0, .13, .13], 'k', linewidth = .6)

#T# show the results
plt.show()