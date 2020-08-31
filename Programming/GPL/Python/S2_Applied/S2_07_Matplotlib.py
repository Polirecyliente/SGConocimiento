
#   Matplotlib

#T# Table of contents

#T# Basic usage
#T# Figures, axes
#T# Parts of a plot
#T# Annotations
#T# Coordinate systems
#T# Plot types
#T# Backends
#T# Interactive sessions

#T# Beginning of content

#T# Matplotlib is a package for plotting

#T# Basic usage

#T# import the matplotlib.pyplot module
import matplotlib.pyplot as plt

x = [4, 1]
y = [3, 5]
#T# plot a set of points with the plot function
# plt.plot(list1, list2)
#T# list1 and list2 must be the same size, list1 has the abscissa values, list2 has the ordinate values
plt.plot(x, y)

#T# save the plot with the savefig function
# plt.savefig("/path/to/save_file1")
plt.savefig("/tmp/fig1_file")

#T# show the created plot in a window with the show function
plt.show()

#T# a lot of matplotlib's functionality is done through kwargs in functions, and constructors, most of the kwargs are self explanatory, but explanations are included when neccessary

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
# plt.axes([rect1, label = 'label_string1'])
#T# rect1 is a list with measures [left_pos1, bottom_pos1, width1, height1], in axes coordinates
#T# the label kwarg serves to put a label to the axes, that acts as the name of the axes
ax1 = plt.axes(label = 'axes one') # type:plt.Axes
ax2 = plt.axes(label = 'axes two')
#T# ax2 overwrites ax1, so the only axes in fig1 is ax2

#T# add axes to a figure
# axes1 = fig1.add_axes([rect1])
#T# the axes axes1 is added to fig1, rect1 is a list with measures [left_pos1, bottom_pos1, width1, height1], in axes coordinates
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
#T# set the axis borders (in data coordinates) with the axis function
# axis1.axis([xmin, xmax, ymin, ymax])
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

#T# customize the grid with the kwargs of the grid function
#T# the which kwarg chooses the grid lines to affect, the major grid, minor grid, or both
#T# the dashes kwarg is an array of numbers, determining the length of a dash and the length of a space in turns, (dash_length1, space_length1, dash_length2, space_length2) and so on
ax1.grid(which = "minor", color = "r", alpha = 0.2)
ax1.grid(which = "major", color= "#FFFF66")
ax1.grid(axis = "x", linewidth = 4, dashes = [5, 10, 7, 7, 2, 1], linestyle = '--')

ax1.axis([0, 4, 0, 6])
#T# the twinx, twiny functions serve to create a second axis
ax2 = ax1.twiny()

#T# the ticks in the x, y axis can be set at particular values
# axes1.set_xtick(list1)
# axes1.set_ytick(list1)
#T# list1 is the list of values at which a tick mark will appear
ax2.set_xticks([-8, 0, 8, 16, 24])
#T# the ticks in ax2 appear as if multiplying the ticks in ax1 by 4

#T# create a figure, and a numpy n-dimensional array of axes, together in a tuple, with the subplots function
# plt.subplots(rowN, colN)
#T# rowN is the number of rows of subplots, and colN is the number of columns of subplots, a unique pair of axes is assigned to each subplot
fig1, axes_ndarr1 = plt.subplots(2, 3)

#T# access subplots in an axes ndarray
axes_ndarr1[0][2].plot([2, 4], [7, 12])
#T# this figure has 6 axes, and the plot goes in rwo 1, col 3

#T# set the margins of the axes as a proportion of the data interval with the margins function
# axes1.margins([xmargin1[, ymargin1]])
#T# without arguments, the function returns the current margins, with one argument it sets the margins for both the x, and y axis, xmargin1 is the margin for the x axis, ymargin1 is the margin for the y axis, both should be greater than zero but they can be a bit lower
axes_ndarr1[0][2].margins(0.5)
#T# the example leaves half the size of the data as the margin for all 4 sides of the affected plot

#T# Parts of a plot

fig1 = plt.figure() # type: plt.Figure
#T# put the title of the figure, in the top side, with the suptitle function
fig1.suptitle("Title string")

ax1 = plt.axes() # type: plt.Axes
#T# put the title of the axes, in the top side, with the set_title function
ax1.set_title('Axes title string')

#T# basic formatting of a plot
# plt.plot(x, y, 'basic_formatting_string1', kwargs)
#T# the 'basic_formatting_string1' is a string whose characters have formatting meaning, these characters can have one of three meanings, marker shape, line style, or color, and the order should be marker_char1-line_char1-color_char1
#T# marker shape
#T#     '.' point
#T#     ',' literal pixel
#T#     'o' circle
#T#     'v' down triangle
#T#     '^' up triangle
#T#     '<' left triangle
#T#     '>' right triangle
#T#     '1' Y down
#T#     '2' Y up
#T#     '3' Y left
#T#     '4' Y right
#T#     's' square
#T#     'p' pentagon
#T#     '*' star
#T#     'h' hexagon one
#T#     'H' hexagon two
#T#     '+' plus
#T#     'x' x
#T#     'D' diamond
#T#     'd' thin diamond
#T#     '|' vertical line
#T#     '_' horizontal line
#T# line style
#T#     '-' solid
#T#     '--' dashed
#T#     '-.' dash dot
#T#     ':' dotted
#T# color
#T#     'r' red
#T#     'g' green
#T#     'b' blue
#T#     'c' cyan
#T#     'm' magenta
#T#     'y' yellow
#T#     'k' black
#T#     'w' white
#T# the clip_on kwarg is a boolean, that sets whether or not to the plot clips at the axes borders, so when False, the plot outside of the axes will be rendered
plt.plot([3, 7], [-1, 5], 'w')

#T# parts of the axes

#T# each of the four sides of the axes is called a spine

#T# the spines attribute of an axes object is used to access each spine individually, using the spines attribute as a dictionary. The spine names are: 'left', 'bottom', 'right', 'top'
ax1.spines['top'].set_visible(False)
#T# the set_visible function of the spines is used the set their visibility

#T# the ticks can be modified with the tick_params function
# axes1.tick_params(kwargs)
#T# the direction kwarg is used to set the direction, in or out the axes, in which to draw the ticks, its values can be, 'in', 'out', 'inout'
ax1.tick_params(direction = 'inout')

#T# Annotations

#T# annotations are ways to annotate an image, like text, arrows

fig1 = plt.Figure() # type: plt.Figure
ax1 = plt.axes() # type: plt.Axes
#T# the text function serves to put text in the image
# plt.text(width_coord1, height_coord1, 'text_string1', kwargs)
#T# width_coord1, height_coord1 are the horizontal, and verical coordinates, 'text_string1' is the string that will be displayed
#T# the ha, va kwargs are for horizontal, and vertical alignment, ha can have the values, 'left', 'center', 'right, va can have the values, 'bottom', 'center', 'top'
plt.text(1, 1, 'text in the image')

#T# the annotate function serves to put annotations in the image
# plt.annotate('text_string1', xy_tuple1[, xy_text_tuple1], kwargs)
#T# 'text_string1' is the string that will be displayed, xy_tuple1 is a tuple with the x, y coordinates of the annotation, xy_text_tuple1 is a tuple with the x, y coordinates for the text of the annotation
#T# the arrowprops kwarg is a dictionary with the properties (also kwargs) of the arrow that connects the point of annotation with its text
ax1.annotate('annotation in the image', (.4, .8), (.5, .7), arrowprops = {'arrowstyle': '->'})

#T# Coordinate systems

#T# there are four coordinate systems

plt.clf()
fig1 = plt.Figure() # type: plt.Figure
ax1 = plt.axes([.1, .2, .4, .6]) # type: plt.Axes
ax1.axis([-4, 6, 2, 5])

#T# the display coordinates are the pixel coordinates of the display, measured from the bottom left corner of the display

#T# the display coordinates are set using the transform kwarg with a value of None
plt.text(1, 1, 'diplay coords', transform = None)

#T# the data coordinates are between the values of x, y, in the plot, so its limits are given by the limits of x (xmin, xmax), y (ymin, ymax)

#T# the get_xlim, get_ylim functions return the limits of x, y from a given axes
tuple1 = ax1.get_xlim() # (-4.0, 6.0)
tuple1 = ax1.get_ylim() # (2.0, 5.0)

#T# the transData attribute of an axes object serves to set the coordinates to data coordinates
plt.text(1, 1, 'data coords', transform = ax1.transData)

#T# the axes coordinates are a proportional location in the axes, in the horizontal axis 0 means to the left of the axes, 1 to the right, in the vertical axis 0 means the bottom, 1 is the top

#T# the transAxes attribute of an axes object serves to set the coordinates to axes coordinates
plt.text(1, 1, 'axes coords', transform = ax1.transAxes)

#T# the figure coordinates are a proportional location in the figure, in the horizontal axis 0 means to the left of the figure, 1 to the right, in the vertical axis 0 means the bottom, 1 is the top

#T# the transFigure attribute of a figure object serves to set the coordinates to figure coordinates
plt.text(.9, .9, 'figure coords', transform = fig1.transFigure)

#T# Plot types

x = ['categ1', 'categ2']
y = [3, 5]
#T# create a bar plot with the bar function
# plt.bar(list1, list2)
#T# list1 contains the categories so it can be a list of strings, list2 has the value of the bar for each category
plt.bar(x, y)

z = [4, 7.6, 4, 4, 4.36, 4]
#T# plot a histogram with the hist function
# plt.hist(list1)
#T# the values are in list1, near values are put in the same bar
plt.hist(z)
#T# in the example, 4.36 is the minimum value away from 4 that by default produces a new bar

x = [4, 1]
#T# create a scatter plot with the scatter function
# plt.scatter(list1, list2)
#T# each dot in the scatter plot comes from each value in list1 paired with each value in list2 in the same position of the lists
plt.scatter(x, y)

#T# plot an arrow with the arrow function
# plt.arrow(x_pos1, y_pos1, x_delta1, y_delta1, kwargs)
#T# x_pos1, y_pos1 are the x, y coordinates of the arrow's origin, x_delta1 is the distance in the x axis traveled by the arrow, and y_delta1 is the homologous for the y axis
#T# the shape kwarg can have one of the values, 'full', 'left', or 'right', to determine the side, or sides of the arrow to draw
plt.arrow(0, 0, 3, 5, width = 0.2, length_includes_head = True, shape = "left", overhang = 0.2, linestyle = '--', fill = False, facecolor = "#FF99DD", edgecolor = "#33FF99", hatch = '/', zorder = 3, alpha = 0.7)

#T# patches

#T# patches are basic shapes, added through an axes object
# axes1.add_patch(plt.Patch1)
#T# this adds Patch1 to be drawn in axes1

#T# create a rectangle with the Rectangle constructor
# plt.Rectangle(origin_tuple1, width1, height1, kwargs)
#T# origin_tuple1 is a two element tuple with the x, y coordinates of the rectangle's bottom left corner, width1 is a number with the width, height1 is a number with the height
ax1.add_patch(plt.Rectangle((0, 0), 3, 5, fill = True, alpha = 0.3, hatch = '*', linewidth = 4, edgecolor = '#99DD33', facecolor = "#4499EF", linestyle = ":"))

#T# Backends

#T# there are two types of backends: interactive and non interactive, interactive shows windows with figures, and non interactive saves images to a file, with a given format

import matplotlib

#T# get the current backend in use
str1 = plt.get_backend() # Qt5Agg

#T# set the current backend with the use function
# matplotlib.use('backend_string1')
# matplotlib.use('TkAgg')

#T# Interactive sessions

#T# start an interactive plotting session with the ion function
# plt.ion()
plt.ion()

#T# end an interactive plotting session with the ioff function
# plt.ioff()

#T# if the interactive session doesn't update a plot, it is redrawn with the draw function
plt.draw()