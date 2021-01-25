#T# the following code shows how to draw a geometric ray

#T# to draw a ray, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal')

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the variables that define the plot
p1 = (1, 4) #| endpoint
p2 = (7, 2) #| point inside the ray

rise1 = p2[1] - p1[1]
run1 = p2[0] - p1[0]

k1 = 1.3 #| factor to readjust the rise and run to change the length of the ray
rise1 = rise1*k1
run1 = run1*k1

list1 = [1, 7] #| x coordinates
list2 = [4, 2] #| y coordinates

#T# plot the figure
ray1 = mpatches.FancyArrowPatch((p1[0], p1[1]), (p1[0] + run1, p1[1] + rise1), arrowstyle = '->', mutation_scale = 12)
ax1.add_patch(ray1)
plt.scatter(list1, list2, color = 'k')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
plt.text(p1[0], p1[1] - 0.2, r'$A$', ha = 'center', va = 'top', size = 16)
plt.text(p2[0], p2[1] - 0.2, r'$B$', ha = 'center', va = 'top', size = 16)

#T# show the results
plt.show()