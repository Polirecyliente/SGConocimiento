#T# the following code shows how to draw a point of concurrency

#T# to draw a point of concurrency, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

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
p1 = (0, 0)
m1 = 3
m2 = .3
m3 = -9

#T# plot the figure
ax1.axline((p1[0], p1[1]), slope = m1, color = 'k')
ax1.axline((p1[0], p1[1]), slope = m2, color = 'k')
ax1.axline((p1[0], p1[1]), slope = m3, color = 'k')
ax1.scatter(p1[0], p1[1], s = 18, color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', p1, ha = 'left', va = 'top', size = 16)

#T# drag the labels if needed
label_A.draggable()

#T# show the results
plt.show()