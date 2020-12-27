#T# the following code shows how to graph a linear equation

#T# to graph a linear equation, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes to graph the linear equation
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect ratio of the axes
ax1.set_aspect('equal')

#T# create two points from the equation so that the line passes through them
p1 = (4, 3)
p2 = (7, 5)

#T# draw the line
ax1.axline(p1, p2)

#T# show the results
plt.show()