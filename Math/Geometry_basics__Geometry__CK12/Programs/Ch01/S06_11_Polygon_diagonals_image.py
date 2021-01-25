#T# the following code shows how to draw the diagonals of a polygon

#T# to draw the diagonals of a polygon, the pyplot module of the matplotlib package is used
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
p1 = (0, 0)
p2 = (2, 0)
p3 = (4, 2)
p4 = (5, 5)
p5 = (3, 6)
p6 = (-2, 4)
p7 = (-1, 1)

list1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p1[0]] #| x coordinates
list2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p1[1]] #| y coordinates

#T# plot the figure
plt.plot(list1, list2, 'k')

str1 = '#427BDF'
plt.plot([p1[0], p3[0]], [p1[1], p3[1]], color = str1) #| diagonals
plt.plot([p1[0], p4[0]], [p1[1], p4[1]], color = str1)
plt.plot([p1[0], p5[0]], [p1[1], p5[1]], color = str1)
plt.plot([p1[0], p6[0]], [p1[1], p6[1]], color = str1)

plt.plot([p2[0], p4[0]], [p2[1], p4[1]], color = str1)
plt.plot([p2[0], p5[0]], [p2[1], p5[1]], color = str1)
plt.plot([p2[0], p6[0]], [p2[1], p6[1]], color = str1)
plt.plot([p2[0], p7[0]], [p2[1], p7[1]], color = str1)

plt.plot([p3[0], p5[0]], [p3[1], p5[1]], color = str1)
plt.plot([p3[0], p6[0]], [p3[1], p6[1]], color = str1)
plt.plot([p3[0], p7[0]], [p3[1], p7[1]], color = str1)
plt.plot([p3[0], p1[0]], [p3[1], p1[1]], color = str1)

plt.plot([p4[0], p6[0]], [p4[1], p6[1]], color = str1)
plt.plot([p4[0], p7[0]], [p4[1], p7[1]], color = str1)
plt.plot([p4[0], p1[0]], [p4[1], p1[1]], color = str1)
plt.plot([p4[0], p2[0]], [p4[1], p2[1]], color = str1)

plt.plot([p5[0], p7[0]], [p5[1], p7[1]], color = str1)
plt.plot([p5[0], p1[0]], [p5[1], p1[1]], color = str1)
plt.plot([p5[0], p2[0]], [p5[1], p2[1]], color = str1)
plt.plot([p5[0], p3[0]], [p5[1], p3[1]], color = str1)

plt.plot([p6[0], p1[0]], [p6[1], p1[1]], color = str1)
plt.plot([p6[0], p2[0]], [p6[1], p2[1]], color = str1)
plt.plot([p6[0], p3[0]], [p6[1], p3[1]], color = str1)
plt.plot([p6[0], p4[0]], [p6[1], p4[1]], color = str1)

plt.plot([p7[0], p2[0]], [p7[1], p2[1]], color = str1)
plt.plot([p7[0], p3[0]], [p7[1], p3[1]], color = str1)
plt.plot([p7[0], p4[0]], [p7[1], p4[1]], color = str1)
plt.plot([p7[0], p5[0]], [p7[1], p5[1]], color = str1)

#T# show the results
plt.show()