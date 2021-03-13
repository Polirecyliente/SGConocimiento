#T# the following code shows how to draw a Cantor set with two iterations

#T# to draw a Cantor set with two iterations, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax_list1 = plt.subplots(1, 3)

#T# set the aspect of the axes
for it1 in fig1.axes:
    it1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in fig1.axes:
    for it2 in ['top', 'bottom', 'left', 'right']:
        it1.spines[it2].set_visible(False)
    it1.get_xaxis().set_visible(False)
    it1.get_yaxis().set_visible(False)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# title the axes
ypos = -2
ax_list1[0].set_title(r'$Stage\ 0$', y = ypos)
ax_list1[1].set_title(r'$Stage\ 1$', y = ypos)
ax_list1[2].set_title(r'$Stage\ 2$', y = ypos)

#T# create the variables that define the plot
list_x_0 = [0, 1]
list_y_0 = [0, 0]

list_x_1a = [0, 1/3]
list_y_1a = [0, 0]
list_x_1b = [2/3, 1]
list_y_1b = [0, 0]

list_x_2a = [0, (1/3)*1/3]
list_y_2a = [0, 0]
list_x_2b = [(1/3)*2/3, 1/3]
list_y_2b = [0, 0]
list_x_2c = [2/3, 2/3 + (1/3)*1/3]
list_y_2c = [0, 0]
list_x_2d = [2/3 + (1/3)*2/3, 1]
list_y_2d = [0, 0]

#T# plot the figure
ax_list1[0].plot(list_x_0, list_y_0, 'k')

ax_list1[1].plot(list_x_1a, list_y_1a, 'k')
ax_list1[1].plot(list_x_1b, list_y_1b, 'k')

ax_list1[2].plot(list_x_2a, list_y_2a, 'k')
ax_list1[2].plot(list_x_2b, list_y_2b, 'k')
ax_list1[2].plot(list_x_2c, list_y_2c, 'k')
ax_list1[2].plot(list_x_2d, list_y_2d, 'k')

#T# show the results
plt.show()