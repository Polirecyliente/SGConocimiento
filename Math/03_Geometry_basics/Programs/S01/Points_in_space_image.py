#T# the following code shows how to draw points in a two dimensional space

#T# to draw points in a two dimensional space, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# create the variables that define the plot
list1 = [3, 5, 6, 8] #| x coordinates
list2 = [7, 2, 5, 4] #| y coordinates

#T# plot the figure
plt.scatter(list1, list2)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
plt.text(list1[0] + 0.05, list2[0] - 0.1, r'$A$', ha = 'left', va = 'top')
plt.text(list1[1] + 0.0, list2[1] + 0.1, r'$B$', ha = 'center', va = 'bottom')
plt.text(list1[2] + 0.0, list2[2] - 0.13, r'$C$', ha = 'center', va = 'top')
plt.text(list1[3] - 0.03, list2[3] + 0.05, r'$D$', ha = 'right', va = 'bottom')

#T# show the results
plt.show()