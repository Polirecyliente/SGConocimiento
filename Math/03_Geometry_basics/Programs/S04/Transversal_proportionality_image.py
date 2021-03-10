#T# the following code shows how to draw three parallel lines with two transversals, to show the transversal proportionality

#T# to draw three parallel lines with two transversals, to show the transversal proportionality, to draw two triangles, one inside the other, to show triangle proportionality, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# set the aspect of the axes
ax1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

#T# create the variables that define the plot
p_l_1 = (1, 5)
p_l_2 = (5, 4)

p_m_1 = (1, 3)
p_m_2 = (5, 2)

p_n_1 = (1, 2)
p_n_2 = (5, 1)

p_t1_1 = (4.5, 5)
p_t1_2 = (3, .8)

p_t2_1 = (1.5, 5.7)
p_t2_2 = (1.8, 1)

p_mid_l_1 = (p_l_1[0] + .45*(p_l_2[0] - p_l_1[0]), p_l_1[1] + .45*(p_l_2[1] - p_l_1[1]))
p_mid_l_2 = (p_l_1[0] + .50*(p_l_2[0] - p_l_1[0]), p_l_1[1] + .50*(p_l_2[1] - p_l_1[1]))
p_mid_m_1 = (p_m_1[0] + .45*(p_m_2[0] - p_m_1[0]), p_m_1[1] + .45*(p_m_2[1] - p_m_1[1]))
p_mid_m_2 = (p_m_1[0] + .50*(p_m_2[0] - p_m_1[0]), p_m_1[1] + .50*(p_m_2[1] - p_m_1[1]))
p_mid_n_1 = (p_n_1[0] + .45*(p_n_2[0] - p_n_1[0]), p_n_1[1] + .45*(p_n_2[1] - p_n_1[1]))
p_mid_n_2 = (p_n_1[0] + .50*(p_n_2[0] - p_n_1[0]), p_n_1[1] + .50*(p_n_2[1] - p_n_1[1]))

#T# plot the figure
#ax1.plot(list_x1, list_y1, 'o-k', markersize = 3)

line_l = mpatches.FancyArrowPatch(p_l_1, p_l_2, arrowstyle = '<->', mutation_scale = 12)
line_m = mpatches.FancyArrowPatch(p_m_1, p_m_2, arrowstyle = '<->', mutation_scale = 12)
line_n = mpatches.FancyArrowPatch(p_n_1, p_n_2, arrowstyle = '<->', mutation_scale = 12)
line_t1 = mpatches.FancyArrowPatch(p_t1_1, p_t1_2, arrowstyle = '<->', mutation_scale = 12)
line_t2 = mpatches.FancyArrowPatch(p_t2_1, p_t2_2, arrowstyle = '<->', mutation_scale = 12)
ax1.add_patch(line_l)
ax1.add_patch(line_m)
ax1.add_patch(line_n)
ax1.add_patch(line_t1)
ax1.add_patch(line_t2)

mark1 = mpatches.FancyArrowPatch(p_mid_l_1, p_mid_l_2, arrowstyle = '->', mutation_scale = 18)
mark2 = mpatches.FancyArrowPatch(p_mid_m_1, p_mid_m_2, arrowstyle = '->', mutation_scale = 18)
mark3 = mpatches.FancyArrowPatch(p_mid_n_1, p_mid_n_2, arrowstyle = '->', mutation_scale = 18)
ax1.add_patch(mark1)
ax1.add_patch(mark2)
ax1.add_patch(mark3)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# create the labels
label_A = ax1.annotate(r'$A$', p_l_1, size = 18)
label_B = ax1.annotate(r'$B$', p_l_2, size = 18)
label_C = ax1.annotate(r'$C$', p_m_1, size = 18)
label_D = ax1.annotate(r'$D$', p_m_2, size = 18)
label_E = ax1.annotate(r'$E$', p_n_1, size = 18)
label_F = ax1.annotate(r'$F$', p_n_2, size = 18)

#T# drag the labels if needed
label_A.draggable()
label_B.draggable()
label_C.draggable()
label_D.draggable()
label_E.draggable()
label_F.draggable()

#T# show the results
ax1.autoscale()
plt.show()