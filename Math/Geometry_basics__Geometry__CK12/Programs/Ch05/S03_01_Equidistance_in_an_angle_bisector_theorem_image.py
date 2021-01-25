#T# the following code shows how to draw an angle to show the equidistance in an angle bisector theorem

#T# to draw an angle to show the equidistance in an angle bisector theorem, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# to transform the markers of a plot, import the MarkerStyle constructor
from matplotlib.markers import MarkerStyle

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'box')