#T# the following code shows how to draw a number line

#T# to draw a number line, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# hide the spines and ticks
for it1 in ['top', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.axes.get_yaxis().set_visible(False)

#T# position the spines and ticks
ax1.spines['bottom'].set_position(('data', 0))

#T# set the axes size
xmin = -2.5; xmax = 5.5
ax1.axis([xmin, xmax, -0.1, 0.1])

#T# plot the figure
plt.plot(-2.5, 0, 'k<', clip_on = False)
plt.plot(5.5, 0, 'k>', clip_on = False)

#T# show the results
plt.show()