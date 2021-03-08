#T# the following code shows how to draw skew lines

#T# to draw skew lines, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the numpy package is used to create two dimensional arrays, needed to plot planes in 3D
import numpy as np

#T# create the figure
fig1 = plt.figure()

#T# create the axes with a 3d projection
ax1 = fig1.add_subplot(1, 1, 1, projection = '3d')

#T# set the aspect of the 3d axes
ax1.set_box_aspect([1, 1, 1])

#T# turn off the 3D box visibility
ax1.set_axis_off()

#T# create the variables that define the plot
arr1_1 = np.array([[2, 2], [2, 2]]) #| x coordinates of plane 1
arr2_1 = np.array([[3, 5], [3, 5]]) #| y coordinates of plane 1
arr3_1 = np.array([[0, 0], [6, 6]]) #| z coordinates of plane 1

arr1_2 = np.array([[0, 0], [4, 4]]) #| x coordinates of plane 2
arr2_2 = np.array([[3, 5], [3, 5]]) #| y coordinates of plane 2
arr3_2 = np.array([[1, 1], [5, 5]]) #| z coordinates of plane 2

list1_1 = [2, 2]     #| x coordinates of the skew line 1
list2_1 = [3.5, 3.5] #| y coordinates of the skew line 1
list3_1 = [0, 6]     #| z coordinates of the skew line 1

list1_2 = [0, 4]     #| x coordinates of the skew line 2
list2_2 = [3.5, 4.5] #| y coordinates of the skew line 2
list3_2 = [1, 5]     #| z coordinates of the skew line 2

#T# plot the figure
ax1.plot_surface(arr1_1, arr2_1, arr3_1, cmap = 'Accent', zorder = 1)
ax1.plot_surface(arr1_2, arr2_2, arr3_2, cmap = 'terrain', zorder = 1)

ax1.plot(list1_1, list2_1, list3_1, color = 'mediumblue', linewidth = 3, zorder = 4) #| skew lines
ax1.plot(list1_2, list2_2, list3_2, color = 'crimson', linewidth = 3, zorder = 4)

#T# show the results
plt.show()