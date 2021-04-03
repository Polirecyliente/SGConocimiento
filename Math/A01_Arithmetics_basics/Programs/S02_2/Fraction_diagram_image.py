#T# this program draws a fraction diagram, which is a diagram to show a fraction or related fractions

#T# import the pyplot module of the matplotlib package
import matplotlib.pyplot as plt

#T# create the figure and two sets of axes
fig1, ax_arr1 = plt.subplots(2, 1)
ax1 = ax_arr1[0] # type: plt.Axes
ax2 = ax_arr1[1] # type: plt.Axes

#T# set the limits of the axes
xmin = -1; xmax = 4
ymin = 0; ymax = 1
ax1.axis([xmin, xmax, ymin, ymax])
ax2.axis([xmin, xmax, ymin, ymax])

#T# leave the number lines alone
for it1 in ['top', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
    ax2.spines[it1].set_visible(False)
ax1.get_yaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)

#T# create the rectangles that show the fractions
rect1_1 = plt.Rectangle((0, -.04), 1, .08, alpha = .4, clip_on = False) # Exterior rectangle
rect1_2 = plt.Rectangle((0, -.04), 2/3, .08, alpha = .6, facecolor = '#DA31F8', hatch = '***', edgecolor = '#EB7142', clip_on = False) # Interior rectangle
rect2_1 = plt.Rectangle((0, -.12), 3, .24, alpha = .4, clip_on = False) # Exterior rectangle
rect2_2 = plt.Rectangle((0, -.12), 2, .24, alpha = .6, facecolor = '#DA31F8', hatch = '*', edgecolor = '#EB7142', clip_on = False) # Interior rectangle
ax1.add_patch(rect1_1)
ax1.add_patch(rect1_2)
ax2.add_patch(rect2_1)
ax2.add_patch(rect2_2)

#T# set the tick marks of the fractions
ax1.tick_params(direction = 'inout')
ax2.tick_params(direction = 'inout')
ax1.set_xticks([0, 2/3, 1, 2, 3])
ax1.set_xticklabels(['0', '2/3', '1', '2', '3'])
ax2.set_xticks([0, 1, 2, 3])

#T# show the result
plt.show()