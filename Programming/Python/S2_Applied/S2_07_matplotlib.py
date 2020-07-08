#!/usr/bin/python3
#   matplotlib

#T# matplotlib is a library for plotting

#T# import the matplotlib module
#T# the pylab module mixes pyplot and numpy
import pylab

x = [4,1]
y = [3,5]
#T# plot a set of points with plot(x,y)
# pylab.plot(x,y)

#T# show the plot with show()
# pylab.show()

#T# create a bar plot with bar(x,y)
# pylab.bar(x,y)
# pylab.show()

z = [4,7,4,4]
#T# plot a histogram with hist(z)
# pylab.hist(z)
# pylab.show()

#T# create a scatter plot with scatter(x,y)
# pylab.scatter(x,y)
# pylab.show()

x2 = [0,3]
y2 = [0,0]
#T# create a figure with figure()
fig1 = pylab.figure(facecolor='#ffefd6')

#T# create the axes with axes()
ax1 = pylab.axes(frameon=False)

#T# set the axis borders with axis([xmin,xmax,ymin,ymax])
ax1.axis([-7,5,-0.5,0.5])

#T# manipulate the axes through the axes object
ax1.axes.get_yaxis().set_visible(False)
ax1.set_aspect('equal')
ax1.axhline(y=0,color='#000000')
ax1.grid(True)

#T# plot an arrow with arrow(x,y,dx,dy)
ax1.arrow(0,0.1,3,0,width=0.12,color='#9977ee',length_includes_head=True)

#T# customize the arrow with its constructor
# pylab.arrow(0,0,3,5,width=0.2,length_includes_head=True,shape="left",overhang=0.2,linestyle='--',fill=False,facecolor="#FF99DD",edgecolor="#33FF99",hatch='/',zorder=3,alpha=0.7)

#T# customize the grid with its kwargs
#T# activate the minor grid ticks with minorticks_on()
# ax1.grid(b=True,which="minor",color="r",alpha=0.2)
# ax1.grid(b=True,which="major",color="#FFFF66")
# ax1.grid(axis="x",linewidth=4,dashes=(1.1,2.3),linestyle='--')
pylab.minorticks_on()

#T# create a second axis with twinx() or twiny()
ax1.axis([0,4,0,6])
ax2 = ax1.twiny()
ax2.axis([-24*2/3,24*2,0,6])
ax2.set_xticks([-16,-8,0,8,16,24,32,40,48])
ax1.set_aspect("equal")

#T# create a rectangle with pyplot.Rectangle(), customize it with its constructor
# rec1 = plt.Rectangle((0,0),3,5,fill=False,alpha=0.3,hatch='*',linewidth=4,edgecolor='#99DD33',facecolor="#4499EF",linestyle=":")

pylab.show()

#T# save the plot with savefig()
fig1.savefig("tempFig1",transparent=True)

#T# matplotlib concepts

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

#T# start an interactive plotting session with ion() turn it off with ioff()
plt.ion()

x = np.linspace(0,24,13)
y = [5,8,3]

#T# create an empty figure with no axes with plt.figure()
fig1 = plt.figure()

#T# put the title of the figure in the superior side with suptitle("Title")
fig1.suptitle("strings of titles")

#T# create a tuple of figure and a set of axes with plt.subplots(nrow,ncol)
fig1, axList = plt.subplots(2,3)
print(type(axList))

#T# all plotting functions work on a np.array
#T# access subplots in an axes list
out1 = axList[1][2].plot([2,4],[7,12])

#T# zoom in or out with axis.margins(zVal), out if zVal > 0
axList[1][2].margins(0.07)

#T# there are two types of backends: interactive and non interactive, interactive shows windows, and non interactive saves image to a format

#T# if an interactive session doesn't update a plot, it is redrawn with draw()
plt.draw()

# plt.show()