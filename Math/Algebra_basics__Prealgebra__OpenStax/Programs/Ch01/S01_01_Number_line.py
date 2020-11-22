#T# this programs draws a number line

#T# import the pyplot module of the matplotlib package
import matplotlib.pyplot as plt

#T# create the figure and the axes
fig1 = plt.Figure()
ax1 = plt.axes()

#T# set the limits of the number line
xmin = -2.5; xmax = 5.5
ax1.axis([xmin, xmax, 0, 0])

#T# leave the number line alone
for iter1 in ['top', 'left', 'right']:
    ax1.spines[iter1].set_visible(False)
ax1.axes.get_yaxis().set_visible(False)

#T# put the arrow tips
ax1.spines['bottom'].set_position(('data', 0))
plt.plot(-2.5, 0, 'k<', clip_on = False)
plt.plot(5.5, 0, 'k>', clip_on = False)

#T# show the result
plt.show()