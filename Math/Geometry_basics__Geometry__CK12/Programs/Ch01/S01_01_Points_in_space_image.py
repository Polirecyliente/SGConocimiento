#T# the following code shows how to draw points in a two dimensional space

#T# to draw points in a two dimensional space, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes to draw the points
fig1 = plt.Figure()
ax1 = plt.axes()

#T# create the points to draw
list1 = [3, 5, 6, 8] #| list of the x coordinates of the points
list2 = [7, 2, 5, 4] #| list of the y coordinates of the points

#T# plot the points
plt.scatter(list1, list2)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# label the points
plt.text(list1[0] + 0.05, list2[0] - 0.1, r'$A$', ha = 'left', va = 'top')
plt.text(list1[1] + 0.0, list2[1] + 0.1, r'$B$', ha = 'center', va = 'bottom')
plt.text(list1[2] + 0.0, list2[2] - 0.13, r'$C$', ha = 'center', va = 'top')
plt.text(list1[3] - 0.03, list2[3] + 0.05, r'$D$', ha = 'right', va = 'bottom')

#T# show the results
plt.show()