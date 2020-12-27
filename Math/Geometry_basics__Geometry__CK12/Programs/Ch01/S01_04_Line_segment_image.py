#T# the following code shows how to draw a line segment

#T# to draw a line segment, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal')

#T# hide the spines and scales
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the endpoints of the line segment
p1 = (2, 3)
p2 = (5, 4)

#T# create the coordinates of the endpoints of the line segment
list1 = [2, 5] #| x coordinates of the endpoints
list2 = [3, 4] #| y coordinates of the endpoints

#T# plot the line segment
plt.plot(list1, list2, 'k')
plt.scatter(list1, list2, color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# label the endpoints
plt.text(p1[0], p1[1] - 0.08, r'$A$', ha = 'center', va = 'top', size = 16)
plt.text(p2[0], p2[1] - 0.08, r'$B$', ha = 'center', va = 'top', size = 16)

#T# show the results
plt.show()