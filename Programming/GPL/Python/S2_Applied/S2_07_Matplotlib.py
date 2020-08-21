
#   Matplotlib

#T# Table of contents

#T# Basics
#T# Figures, axes
#T# Plot types

#T# Beginning of content

#T# Matplotlib is a package for plotting

#T# Basics

#T# import the matplotlib.pyplot module
import matplotlib.pyplot as plt

x = [4,1]
y = [3,5]
#T# plot a set of points with the plot function
# plt.plot(list1, list2)
#T# list1 and list2 must be the same size, list1 has the abscissa values, list2 has the ordinate values
plt.plot(x,y)

#T# save the plot with the savefig function
# plt.savefig("/path/to/save_file1")
plt.savefig("/tmp/fig1_file")

#T# show the created plot in a window with the show function
plt.show()

#T# Figures, axes

#T# fig_id1, is an identification for a figure, it can be a figure object, or a string with the name of the figure

#T# to get autocompletion for figures or axes, type hints must be used

#T# create a figure with the figure constructor, it returns a figure object
# plt.figure("figure_name1")
#T# the argument "figure_name1" is the figure identification, and the figure title
fig1 = plt.figure() # type: plt.Figure
fig2 = plt.figure("Second figure")

#T# each figure has a number attribute with a unique number among the figures, get a list of these numbers with the get_fignums function
list1 = plt.get_fignums() # [1, 2]

#T# get the current figure with the gcf function
current_fig1 = plt.gcf() # type: plt.Figure
int1 = current_fig1.number # 2

#T# close a given figure with the close function
# plt.close(fig_id1)
#T# without argument, the current figure is closed
plt.close()

#T# clear the current figure with the clf function
plt.clf()

#T# select a figure to make it the current figure with the figure function
# plt.figure(fig1.number)
#T# the number attribute of the fig1 figure object is used to select fig1 as the current figure
plt.figure(fig1.number)

#T# create the axes with the axes constructor, it returns an axes object
# plt.axes(label = 'label_string1')
#T# the label kwarg serves to put a label to the axes, that acts as the name of the axes
ax1 = plt.axes(label = 'axes one') # type:plt.Axes
ax2 = plt.axes(label = 'axes two')
#T# ax2 overwrites ax1, so the only axes in fig1 is ax2

#T# add axes to a figure
# axes1 = fig1.add_axes([rect1])
#T# the axes axes1 is added to fig1, rect1 is a list with measures [left_pos1, bottom_pos1, width1, height1]
ax1 = fig1.add_axes([0, 0, 1, 1], label = 'new axes one')

#T# the axes attribute of a figure object has a list of the axes in the figure
axes_in_fig1 = fig1.axes
int1 = len(axes_in_fig1) # 2

#T# get the current axes with the gca function
current_axes1 = plt.gca()

#T# the _label attribute of an axes object contains its label
axes_label1 = current_axes1._label # 'new axes one'

#T# clear the current axes with the cla function
plt.cla()

#T# select a set of axes to make them the current axes with the sca function
# plt.sca(axes1)
plt.sca(ax1)

ax1 = plt.axes() # type: plt.Axes
#T# set the axis borders with the axis function
# axis1.axis([xmin,xmax,ymin,ymax])
#T# the list inside the axis function contains the limits in x, y
ax1.axis([-7, 5, -0.5, 0.5])

#T# manipulate the axes through the axes object

#T# the x, y axis can be returned as an object
# xaxis1 = axes1.axes.get_xaxis()
# yaxis1 = axes1.axes.get_yaxis()
ax1_yaxis = ax1.axes.get_yaxis()

#T# the visibility of an axis can be changed
# axis1.set_visible(bool1)
#T# bool1 sets the visibility of the axis axis1
ax1_yaxis.set_visible(False)

#T# set the aspect ratio of the x, and y axis
# axes1.set_aspect('aspect_string1')
#T# 'aspect_string1' can have a few values such as 'auto', 'equal'
ax1.set_aspect('equal')

#T# draw a horizontal line with the axhline function
# axes1.axhline([y = flo1])
#T# the y kwarg is for the ordinate position (flo1) of the line
ax1.axhline()

#T# the grid can be drawn with the grid function
# axes1.grid(bool1)
#T# bool1 sets the presence of the grid in the axes axes1
ax1.grid(True)

#T# activate the minor grid ticks
plt.minorticks_on()

#T# customize the grid with the kwargs of the grid function, most of the kwargs are self explanatory
#T# the which kwarg chooses the grid lines to affect, the major grid, minor grid, or both
#T# the dashes kwarg is an array of numbers, determining the length of a dash and the length of a space in turns, (dash_length1, space_length1, dash_length2, space_length2) and so on
ax1.grid(which = "minor", color = "r", alpha = 0.2)
ax1.grid(which = "major", color= "#FFFF66")
ax1.grid(axis = "x", linewidth=4, dashes=[5, 10, 7, 7, 2, 1], linestyle='--')

ax1.axis([0,4,0,6])
#T# the twinx, twiny functions serve to create a second axis
ax2 = ax1.twiny()

#T# the ticks in the x, y axis can be set at particular values
# axes1.set_xtick(list1)
# axes1.set_ytick(list1)
#T# list1 is the list of values at which a tick mark will appear
ax2.set_xticks([-8,0,8,16,24])
#T# the ticks in ax2 appear as if multiplying the ticks in ax1 by 4

#T# Plot types

x = ['categ1', 'categ2']
y = [3,5]
#T# create a bar plot with the bar function
# plt.bar(list1, list2)
#T# list1 contains the categories so it can be a list of strings, list2 has the value of the bar for each category
plt.bar(x,y)

z = [4, 7.6, 4, 4, 4.36, 4]
#T# plot a histogram with the hist function
# plt.hist(list1)
#T# the values are in list1, near values are put in the same bar
plt.hist(z)
#T# in the example, 4.36 is the minimum value away from 4 that by default produces a new bar

x = [4,1]
#T# create a scatter plot with the scatter function
# plt.scatter(list1, list2)
#T# each dot in the scatter plot comes from each value in list1 paired with each value in list2 in the same position of the lists
plt.scatter(x,y)

#T# create a rectangle with the Rectangle constructor
# plt.Rectangle(origin_tuple1, width1, height1)
#T# origin_tuple1 is a two element tuple with the x, y coordinates of the rectangle's bottom left corner, width1 is a number with the width, height1 is a number with the height
plt.Rectangle((2,1),3,5)
#plt.Rectangle((2,1),3,5,fill=False,alpha=0.3,hatch='*',linewidth=4,edgecolor='#99DD33',facecolor="#4499EF",linestyle=":")

#T# plot an arrow with arrow(x,y,dx,dy)
ax1.arrow(0,0.1,3,0,width=0.12,color='#9977ee',length_includes_head=True)

#T# customize the arrow with its constructor
# plt.arrow(0,0,3,5,width=0.2,length_includes_head=True,shape="left",overhang=0.2,linestyle='--',fill=False,facecolor="#FF99DD",edgecolor="#33FF99",hatch='/',zorder=3,alpha=0.7)

#T# matplotlib concepts

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

#T# get the current backend in use
str1 = plt.get_backend() # TkAgg

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