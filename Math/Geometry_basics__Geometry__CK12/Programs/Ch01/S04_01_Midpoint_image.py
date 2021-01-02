#T# the following code shows how to draw the midpoint of a segment

#T# to draw the midpoint of a segment, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal')

#T# hide the spines and axes ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the coordinates of the midpoint and endpoints of the segment
list1 = [0, 2, 4] #| x coordinates
list2 = [0, 0, 0] #| y coordinates
list3 = [1, 3] #| x coordinates of the markers
list4 = [0, 0] #| y coordinates of the markers

#T# plot the segment with its midpoint
plt.plot(list1, list2, 'o-k')
plt.plot(list3, list4, 'k', marker = '|')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# label the points of the segment
label1 = plt.annotate(r'$A$', (list1[0], list2[0]), ha = 'center', va = 'top', size = 16)
label2 = plt.annotate(r'$B$', (list1[1], list2[1]), ha = 'center', va = 'top', size = 16)
label3 = plt.annotate(r'$C$', (list1[2], list2[2]), ha = 'center', va = 'top', size = 16)

#T# drag the labels into better positions after plotting them
label1.draggable()
label2.draggable()
label3.draggable()

#T# show the results
plt.show()