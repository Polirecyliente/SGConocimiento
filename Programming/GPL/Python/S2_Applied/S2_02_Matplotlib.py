
#   Matplotlib

#T# Table of contents

#C# Basic usage
#C# Figures, axes
#C# --- Figure basics
#C# --- Figure management
#C# --- Axes creation
#C# --- Axes management
#C# --- Axis
#C# --- Grids
#C# --- Figures and axes together
#C# Parts of a plot
#C# --- Titles
#C# --- Spines
#C# --- Ticks
#C# Annotations
#C# --- Latex symbols
#C# Coordinate systems
#C# Plot types
#C# --- Patches
#C# Backends
#C# Interactive sessions
#C# Configuration

#T# Beginning of content

# |-------------------------------------------------------------
#T# Matplotlib is a package for plotting
# |-------------------------------------------------------------

#C# Basic usage

# |-------------------------------------------------------------
#T# import the matplotlib.pyplot module
import matplotlib.pyplot as plt

#T# plot a set of points with the plot function

# SYNTAX plt.plot(list1, list2)
#T# list1 and list2 must be the same size, list1 has the abscissa values, list2 has the ordinate values, the plot can be modified using kwargs

#T# a few of the plot kwargs are
#T#     color, accepts a hexadecimal string that starts with a hash, such as '#A178B9'

x = [4, 1]
y = [3, 5]
plt.plot(x, y)

#T# save the plot with the savefig function
plt.savefig("/tmp/fig1_file")

#T# show the created plot in a window with the show function
plt.show()

#T# a lot of matplotlib's functionality is done through kwargs in functions, and constructors, most of the kwargs are self explanatory, but explanations are included when neccessary
# |-------------------------------------------------------------

#C# Figures, axes

# |-------------------------------------------------------------

#C# --- Figure basics

# |-----
#T# fig_id1, is an identification for a figure, it can be a figure object, or a string with the name of the figure

#T# to get autocompletion for figures or axes, type hints must be used

#T# create a figure with the figure constructor, it returns a figure object

# SYNTAX plt.figure("figure_name1", kwargs1)
#T# the argument "figure_name1" is the figure identification, and the figure title, kwargs1 are the kwarg value pairs

#T# the figsize kwarg is a tuple of two numbers, that sets the horizontal and vertical size of the figure

fig1 = plt.figure() # type: plt.Figure
fig2 = plt.figure("Second figure", figsize = (2, 1))

#T# each figure has a number attribute with a unique number among the figures, get a list of these numbers with the get_fignums function
list1 = plt.get_fignums() # [1, 2]
# |-----

#C# --- Figure management

# |-----
#T# get the current figure with the gcf function
current_fig1 = plt.gcf() # type: plt.Figure

#T# the number attribute of a figure stores the figure number
int1 = current_fig1.number # 2

#T# close a given figure with the close function

# SYNTAX plt.close(fig_id1)
#T# fig_id1 represents a figure object, without argument, the current figure is closed

plt.close()

#T# clear the current figure with the clf function
plt.clf()

#T# select a figure to make it the current figure with the figure function

# SYNTAX plt.figure(fig1.number)
#T# the number attribute of the fig1 figure object is used to select fig1 as the current figure

plt.figure(fig1.number)
# |-----

#C# --- Axes creation

# |-----
#T# create the axes with the axes constructor, it returns an axes object

# SYNTAX plt.axes(rect1, label = 'label_string1')
#T# the arguments are optional, rect1 is a list with measures [left_pos1, bottom_pos1, width1, height1], in axes coordinates

#T# the label kwarg serves to put a label to the axes, that acts as the name of the axes

ax1 = plt.axes(label = 'axes one') # type:plt.Axes
ax2 = plt.axes(label = 'axes two')
#T# ax2 overwrites ax1, so the only axes in fig1 is ax2

#T# add axes to a figure

# SYNTAX axes1 = fig1.add_axes([rect1])
#T# the axes1 is added to fig1, rect1 is the same as before

ax1 = fig1.add_axes([0, 0, 1, 1], label = 'new axes one')
# |-----

#C# --- Axes management

# |-----
#T# the axes attribute of a figure object has a list of the axes in the figure
fig1, axes1 = plt.subplots(2, 1)
axes_in_fig1 = fig1.axes
int1 = len(axes_in_fig1) # 2

#T# the figure attribute of an axes object contains the figure of the axes object
fig1 = ax1.figure # <Figure size 640x480 with 1 Axes>

#T# get the current axes with the gca function
current_axes1 = plt.gca()

#T# the _label attribute of an axes object contains its label
axes_label1 = current_axes1._label # 'new axes one'

#T# clear the current axes with the cla function
plt.cla()

#T# select a set of axes to make them the current axes with the sca function
plt.sca(ax1)

#T# set the aspect ratio of the x, and y axes

# SYNTAX axes1.set_aspect('aspect_string1')
#T# this changes the axes1 aspect, 'aspect_string1' can have a few values such as 'auto', 'equal'

ax1.set_aspect('equal')

# SYNTAX axes1.set_aspect('aspect_string1', adjustable = str1)
#T# same as before, the adjustable kwarg sets what is adjusted to get to the aspect ratio, str1 can be 'box' (adjusts the box of the axes) or 'datalim' (adjusts the data limits)

p1 = (4, 3)
p2 = (7, 5)
ax1.axline(p1, p2)
ax1.set_aspect('equal', adjustable = 'datalim')

#T# draw a horizontal line with the axhline function

# SYNTAX axes1.axhline(y = flo1)
#T# the line is drawn in axes1, the y kwarg is for the ordinate position flo1 of the line, the y kwarg is optional and if omitted it defaults to 0

ax1.axhline()

#T# draw a vertical line with the axvline function

# SYNTAX axes1.axvline(x = flo1)
#T# the line is drawn in axes1, the x kwarg is for the abscissa position flo1 of the line, the x kwarg is optional and if omitted it defaults to 0

ax1.axvline()

#T# draw a line in a given inclination with the axline function

# SYNTAX axes1.axline((x1, y1), (x2, y2))
# SYNTAX axes1.axline((x1, y1), slope = num1)
#T# these syntaxes represent a line given two points, and a line given a point and the slope, the tuples (x1, y1) and (x2, y2) are the points where the line passes, num1 is the slope, a line is created with one of these syntaxes

ax1.axline((4, 3), (7, 5))
ax1.axline((5, 3), slope = 1.5)

#T# set the margins of the axes as a proportion of the data interval with the margins function

# SYNTAX axes1.margins(xmargin1, ymargin1)
#T# the arguments are optional, without arguments, the function returns the current margins, with one argument it sets the margins for both the x, and y axis

#T# xmargin1 is the margin for the x axis, ymargin1 is the margin for the y axis, they can have any value greater than -0.5, a bigger value makes the plot look smaller (as if zoomed out)

#T# if the margin is negative then a portion of the data is left outside of the plot, with a margin of -0.5 the whole data would disappear because half the data is left out on one side and the other half on the other side

ax1.margins(0.5)
#T# this leaves half the size of the data as the margin for all 4 sides, half the size in x at the left and right, half the size in y at the top and bottom

#T# the get_xlim, get_ylim functions return the limits of x, y from a given set of axes
tuple1 = ax1.get_xlim() # (0.0, 1.0)
tuple1 = ax1.get_ylim() # (0.0, 1.0)
# |-----

#C# --- Axis

# |-----
#T# set the axis borders (in data coordinates) with the axis function

# SYNTAX axis1.axis([xmin, xmax, ymin, ymax])
#T# the list inside the axis function contains the limits in x, y

ax1 = plt.axes() # type: plt.Axes
ax1.axis([-7, 5, -0.5, 0.5])

#T# the x, y axis can each be returned as an object

# SYNTAX xaxis1 = axes1.axes.get_xaxis()
#T# xaxis1 is the x axis of axes1

# SYNTAX yaxis1 = axes1.axes.get_yaxis()
#T# yaxis1 is the y axis of axes1

ax1_yaxis = ax1.axes.get_yaxis()

#T# the x, y axis can each be accessed as an attribute of a pair of axes
ax1_xaxis = ax1.xaxis
ax1_yaxis = ax1.yaxis

#T# the visibility of an axis can be changed

# SYNTAX axis1.set_visible(bool1)
#T# bool1 sets the visibility of axis1

ax1_yaxis.set_visible(False)

#T# the twinx, twiny functions serve to create a second axis in x, y respectively
ax1.axis([0, 4, 0, 6])
ax2 = ax1.twiny()
# |-----

#C# --- Grids

# |-----
#T# the grid can be drawn with the grid function

# SYNTAX axes1.grid(bool1)
#T# bool1 sets the presence of the grid in axes1

ax1.grid(True)

#T# activate the minor grid ticks with the minorticks_on function
ax1.minorticks_on()

#T# customize the grid with the kwargs of the grid function

# SYNTAX axes1.grid(kwargs1)
#T# this sets the grid of axes1, by setting kwargs1 which are the kwarg value pairs

#T# the which kwarg chooses the grid lines to affect, it can be "major", "minor", or "both"

#T# the dashes kwarg is an array of numbers, determining the length of a dash and the length of a space in turns, dash_length1, space_length1, dash_length2, space_length2, up to dash_lengthN, space_lengthN

ax1.grid(which = "minor", color = "r", alpha = 0.2)
ax1.grid(which = "major", color= "#FFFF66")
ax1.grid(axis = "x", linewidth = 4, dashes = [5, 10, 7, 7, 2, 1], linestyle = '--')
# |-----

#C# --- Figures and axes together

# |-----
#T# create a figure, and a numpy n-dimensional array of axes, together in a tuple, with the subplots function

# SYNTAX plt.subplots(rows1, cols1)
#T# rows1 is the number of rows, and cols1 is the number of columns of subplots, a unique pair of axes is assigned to each subplot

fig1, axes_ndarr1 = plt.subplots(2, 3)

#T# access subplots in an axes ndarray
axes_ndarr1[0][2].plot([2, 4], [7, 12])
#T# this figure has 6 axes, and the plot goes in rwo 1, col 3

#T# set the transparency (or alpha value) and the color of the figure and the axes with the set_facecolor function, it interprets colors as a hex value, the last two hex numbers indicate the alpha value
fig1.set_facecolor('#EEEEEE00') #| creates a transparent figure
ax1.set_facecolor('#EEEEEE00')  #| creates transparent axes

#T# set the width of a figure with the set_figwidth function, and the height of a figure with the set_figheight function
fig1.set_figwidth(4)
fig1.set_figheight(3)
# |-----

# |-------------------------------------------------------------

#C# Parts of a plot

# |-------------------------------------------------------------
#T# basic formatting of a plot

# SYNTAX plt.plot(x, y, 'basic_formatting_string1', kwargs)
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

#C# --- Titles

# |-----
#T# put the title of the figure, in the top side, with the suptitle function
fig1 = plt.figure() # type: plt.Figure
fig1.suptitle("Title string")

#T# put the title of the axes, in the top side, with the set_title function
ax1 = plt.axes() # type: plt.Axes
ax1.set_title('Axes title string')
# |-----

#C# --- Spines

# |-----
#T# each of the four sides of the axes is called a spine, the spines attribute of an axes object is used to access each spine individually, using the spines attribute as a dictionary. The spine names are: 'left', 'bottom', 'right', 'top'
spine1 = ax1.spines['top']

#T# the set_visible function of the spines is used the set their visibility
spine1.set_visible(False)

#T# the set_position function is used to set the position of a spine, for example to make the axes intersect at the origin

# SYNTAX spine1.set_position(('position_type1', num1))
#T# 'position_type1' and num1 form a tuple, num1 indicates the exact position in which spine1 will be placed

#T# 'position_type1' is a string, its value can be
#T#     'outward', num1 is measured in points outward from the plot, so a negative value puts the spine inwards
#T#     'axes', num1 is in axes coordinates
#T#     'data', num1 is in data coordinates

spine1.set_position(('outward', 2)) # spine1 is places 2 points outwards
# |-----

#C# --- Ticks

# |-----
#T# the ticks can be modified with the tick_params function

# SYNTAX axes1.tick_params(kwargs1)
#T# this sets the ticks of axes1, setting kwargs1 which are the kwarg value pairs

#T# the direction kwarg is used to set the direction, in or out the axes, in which to draw the ticks, its value can be, 'in', 'out', 'inout'

ax1.tick_params(direction = 'inout')

#T# the ticks in the x, y axis can be set at particular values

# SYNTAX axes1.set_xtick(list1)
#T# list1 is the list of values at which a tick mark will appear in the x axis

# SYNTAX axes1.set_ytick(list1)
#T# list1 is the list of values at which a tick mark will appear in the y axis

ax1.set_xticks([-8, 0, 8, 16, 24])

#T# when the numeric ticks are float numbers, but want to be represented as fractions, the set_xticklabels, set_yticklabels functions can be used
ax1.set_xticks([0, 2/3, 4/3])
ax1.set_xticklabels(['0', '2/3', '4/3']) #| without this, the tick at 2/3 appears as 0.6666
# |-----

# |-------------------------------------------------------------

#C# Annotations

# |-------------------------------------------------------------
#T# annotations are ways to annotate an image, like text, arrows

#T# the text function serves to put text in the image

# SYNTAX plt.text(width_coord1, height_coord1, 'text_string1', kwargs1)
#T# width_coord1, height_coord1 are the horizontal, and verical coordinates, 'text_string1' is the string that will be displayed, kwargs1 are the kwarg value pairs

#T# the following are a few of the kwargs used in annotations
#T#     font, sets the font, to see the available fonts print 'matplotlib.font_manager.fontManager.ttflist'
#T#     ha, stands for horizontal alignment, it can be, 'left', 'center', 'right
#T#     size, sets the font size of the annotation
#T#     va, stands for vertical alignment, it can be, 'bottom', 'center', 'top'

fig1 = plt.Figure() # type: plt.Figure
ax1 = plt.axes() # type: plt.Axes
plt.text(1, 1, 'text in the image')
plt.text(1, 1, 'text1', font = 'cmmi10') #| this sets the font to the italic Latex default, Computer Modern Italic 10, other fonts in this family are cmr10 (roman font), cmb10 (bold font)

#T# the annotate function serves to put annotations in the image

# SYNTAX plt.annotate('text_string1', xy_tuple1, xy_text_tuple1, kwargs1)
#T# 'text_string1' is the string that will be displayed, xy_tuple1 is a tuple with the x, y coordinates of the annotation, xy_text_tuple1 is optional and is a tuple with the x, y coordinates for the text of the annotation, kwargs1 are the kwarg value pairs

#T# the arrowprops kwarg is a dictionary with the properties (also kwargs) of the arrow that connects the point of annotation with its text

#T# xy_tuple1 and xy_text_tuple1 can be input via the xy and xytext kwargs respectively

ax1.annotate('annotation in the image', (.4, .8), (.5, .7), arrowprops = {'arrowstyle': '->'})

#C# --- Latex symbols

# |-----
#T# Latex symbols can be used in annotations, they must be written within a pair of dollar signs $, and the string must be declared to be a raw string
plt.text(1, 1, r'$A = \frac{B}{\sqrt{C}}$')
# |-----

# |-------------------------------------------------------------

#C# Coordinate systems

# |-------------------------------------------------------------
#T# there are four coordinate systems, they are commonly used through the transform kwarg of different functions and constructors

#T# the following is an example
plt.clf()
fig1 = plt.Figure() # type: plt.Figure
ax1 = plt.axes([.1, .2, .4, .6]) # type: plt.Axes
ax1.axis([-4, 6, 2, 5])

#T# the display coordinates are the pixel coordinates of the display, measured from the bottom left corner of the display, these are set using the transform kwarg with a value of None
plt.text(1, 1, 'diplay coords', transform = None)

#T# the data coordinates are between the values of x, y, in the plot, so its limits are given by the limits of x (xmin, xmax), y (ymin, ymax), the transData attribute of an axes object serves to set the coordinates to data coordinates in the transform kwarg
plt.text(1, 1, 'data coords', transform = ax1.transData)

#T# the axes coordinates are a proportional location in the axes, in the horizontal axis 0 means to the left of the axes, 1 to the right, in the vertical axis 0 means the bottom, 1 is the top, the transAxes attribute of an axes object serves to set the coordinates to axes coordinates in the transform kwarg
plt.text(1, 1, 'axes coords', transform = ax1.transAxes)

#T# the figure coordinates are a proportional location in the figure, in the horizontal axis 0 means to the left of the figure, 1 to the right, in the vertical axis 0 means the bottom, 1 is the top, the transFigure attribute of a figure object serves to set the coordinates to figure coordinates in the transform kwarg
plt.text(.9, .9, 'figure coords', transform = fig1.transFigure)
# |-------------------------------------------------------------

#C# Plot types

# |-------------------------------------------------------------
#T# create a bar plot with the bar function

# SYNTAX plt.bar(list1, list2)
#T# list1 contains the categories so it can be a list of strings, list2 has the value of the bar for each category

x = ['categ1', 'categ2']
y = [3, 5]
plt.bar(x, y)

#T# plot a histogram with the hist function

# SYNTAX plt.hist(list1)
#T# the values are in list1, near values are put in the same bar

z = [4, 7.6, 4, 4, 4.36, 4]
plt.hist(z)
#T# in the example, 4.36 is the minimum value away from 4 that by default produces a new bar

#T# create a scatter plot with the scatter function

# SYNTAX plt.scatter(list1, list2)
#T# each dot in the scatter plot comes from each value in list1 paired with each value in list2 in the same position of the lists

x = [4, 1]
plt.scatter(x, y)

#T# plot an arrow with the arrow function

# SYNTAX plt.arrow(x_pos1, y_pos1, x_delta1, y_delta1, kwargs1)
#T# x_pos1, y_pos1 are the x, y coordinates of the arrow's origin, x_delta1 is the distance in the x axis traveled by the arrow, and y_delta1 is the homologous for the y axis, kwargs1 are the kwarg value pairs

#T# the shape kwarg can have one of the values, 'full', 'left', or 'right', to determine the side, or sides of the arrow to draw

plt.arrow(0, 0, 3, 5, width = 0.2, length_includes_head = True, shape = "left", overhang = 0.2, linestyle = '--', fill = False, facecolor = "#FF99DD", edgecolor = "#33FF99", hatch = '/', zorder = 3, alpha = 0.7)

#C# --- Patches

# |-----

# |--------------------------------------------------\
#T# patches are basic shapes, added through an axes object

# SYNTAX axes1.add_patch(plt.Patch1)
#T# this is a general syntax to add Patch1 to axes1

#T# create a rectangle with the Rectangle constructor

# SYNTAX plt.Rectangle(origin_tuple1, width1, height1, kwargs1)
#T# origin_tuple1 is tuple with the x, y coordinates of the rectangle's bottom left corner, width1 and height1 set width and height, kwargs1 are the kwarg value pairs

rect1 = plt.Rectangle((0, 0), 3, 5, fill = True, alpha = 0.3, hatch = '*', linewidth = 4, edgecolor = '#99DD33', facecolor = "#4499EF", linestyle = ":")
ax1.add_patch(rect1)

#T# the hatch kwarg that is used in patches can have one of the following values
#T#     '*' crosshatches with stars
#T#     '-' crosshatches with horizontal lines
#T#     '.' crosshatches with dots
#T#     '+' crosshatches with a grid of horizontal and vertical lines
#T#     'x' crosshatches with a grid of diagonals
#T#     '\\' this is a single escaped backslash, crosshatches with down right diagonals
#T#     'o' crosshatches with circles
#T#     'O' crosshatches with big circles
#T#     '|' crosshatches with vertical lines
#T#     '/' crosshatches with up right diagonals

#T# the density of any of the former hatch patterns can be increased by repeating the corresponding character, e.g. using '***' triples the density of the stars hatch pattern, '..' doubles the density of the dot hatch pattern, and so on

#T# hatch patterns may be mixed, e.g. 'Oo', '*-', etc.

rect1 = plt.Rectangle((.2,.2), .6, .4, hatch = '*-.+x\\oO|/')

#T# other patches are defined in the patches module of the matplotlib package
import matplotlib.patches as mpatches

#T# the FancyArrowPatch patch allows the creation of bidirectional arrows

# SYNTAX mpatches.FancyArrowPatch(tuple1, tuple2, kwargs1)
#T# tuple1 is a tuple with the x-y coordinates of the tail of the arrow, tuple2 is a tuple with the x-y coordinates of the head of the arrow, kwargs1 are the kwarg value pairs

#T# the mutation_scale kwarg is a number that scales the size of the arrow

#T# the arrowstyle kwarg is a string used to set the style of the arrow, its value can be
#T#     '-', no arrowhead
#T#     '->', a regular arrowhead
#T#     '<->', bidirectional regular arrowhead
#T#     '<-', tail regular arrowhead
#T#     '-[', the arrowhead is an opening bracket
#T#     ']-[', bidirectional opening bracket arrowheads
#T#     ']-', tail opening bracket arrowhead
#T#     '-|>', a filled arrowhead
#T#     '<|-|>', bidirectional filled arrowheads
#T#     '<|-', tail filled arrowhead
#T#     '|-|', bidirectional perpendicular line arrowheads

arrow1 = mpatches.FancyArrowPatch((.2, .2), (.6, .6), mutation_scale = 12, arrowstyle = '|-|')
# |--------------------------------------------------/

# |-----

# |-------------------------------------------------------------

#C# Backends

# |-------------------------------------------------------------
#T# there are two types of backends: interactive and non interactive, interactive shows windows with figures, and non interactive saves images to a file, with a given format

import matplotlib

#T# get the current backend in use
str1 = plt.get_backend() # Qt5Agg

#T# set the current backend with the use function
# SYNTAX matplotlib.use('backend_string1')
matplotlib.use('TkAgg')
# |-------------------------------------------------------------

#C# Interactive sessions

# |-------------------------------------------------------------
#T# for interactive sessions, a backend that supports interactivity must be used, such as TkAgg

#T# start an interactive plotting session with the ion function
plt.ion()

#T# end an interactive plotting session with the ioff function
plt.ioff()

#T# if the interactive session doesn't update a plot, it can be redrawn with the draw function
plt.draw()
# |-------------------------------------------------------------

#C# Configuration

# |-------------------------------------------------------------
#T# configuration is done in matplotlib with the rcParams dictionary, or with the rc function

# SYNTAX matplotlib.rcParams[part1.param1] = value1
# SYNTAX matplotlib.rc('part1', param1 = value1, param2 = value2)
#T# part1 is the part of matplotlib being configured, such as lines, or font, etcetera, param1 is the parameter being set to value1, param2 is set to value2, up to paramN set to valueN

import matplotlib
matplotlib.rcParams['lines.linewidth'] = 2
matplotlib.rcParams['lines.color'] = 'r'
matplotlib.rc('lines', linewidth = 2, color = 'r') #| equivalent to the former two lines of configuration

matplotlib.rcParams['mathtext.fontset'] = 'cm' #| sets the math text font to the Latex default 'cm' which stands for Computer Modern
# |-------------------------------------------------------------