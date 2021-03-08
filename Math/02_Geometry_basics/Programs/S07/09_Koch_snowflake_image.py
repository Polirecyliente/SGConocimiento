#T# the following code shows how to draw a Koch snowflake with two iterations

#T# to draw a Koch snowflake with two iterations, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# the patches module of the matplotlib package is used to draw shapes
import matplotlib.patches as mpatches

#T# create the figure and axes
fig1, ax_list1 = plt.subplots(1, 3)

#T# set the aspect of the axes
for it1 in fig1.axes:
    it1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in fig1.axes:
    for it2 in ['top', 'bottom', 'left', 'right']:
        it1.spines[it2].set_visible(False)
    it1.get_xaxis().set_visible(False)
    it1.get_yaxis().set_visible(False)

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# title the axes
ypos = -.4
ax_list1[0].set_title(r'$Stage\ 0$', y = ypos + .2)
ax_list1[1].set_title(r'$Stage\ 1$', y = ypos)
ax_list1[2].set_title(r'$Stage\ 2$', y = ypos)

#T# create the variables that define the plot
A = (0.2, 1)
B = (0, 0)
C = (2.4, 2)

s0_1 = A
s0_2 = B
s0_3 = C

s0_points = (s0_1, s0_2, s0_3)

A_to_B_1b = (-(B[0] - A[0])/3, -(B[1] - A[1])/3)
B_to_C_1b = (-(C[0] - B[0])/3, -(C[1] - B[1])/3)
C_to_A_1b = (-(A[0] - C[0])/3, -(A[1] - C[1])/3)

s1_1 = (s0_1[0] + 1/3*(s0_2[0] - s0_1[0]), s0_1[1] + 1/3*(s0_2[1] - s0_1[1]))
s1_2 = (s1_1[0] + B_to_C_1b[0], s1_1[1] + B_to_C_1b[1])
s1_3 = (s0_1[0] + 2/3*(s0_2[0] - s0_1[0]), s0_1[1] + 2/3*(s0_2[1] - s0_1[1]))
s1_4 = (s0_2[0] + 1/3*(s0_3[0] - s0_2[0]), s0_2[1] + 1/3*(s0_3[1] - s0_2[1]))
s1_5 = (s1_4[0] + C_to_A_1b[0], s1_4[1] + C_to_A_1b[1])
s1_6 = (s0_2[0] + 2/3*(s0_3[0] - s0_2[0]), s0_2[1] + 2/3*(s0_3[1] - s0_2[1]))
s1_7 = (s0_3[0] + 1/3*(s0_1[0] - s0_3[0]), s0_3[1] + 1/3*(s0_1[1] - s0_3[1]))
s1_8 = (s1_7[0] + A_to_B_1b[0], s1_7[1] + A_to_B_1b[1])
s1_9 = (s0_3[0] + 2/3*(s0_1[0] - s0_3[0]), s0_3[1] + 2/3*(s0_1[1] - s0_3[1]))

s1_points = (s0_1, s1_1, s1_2, s1_3, s0_2, s1_4, s1_5, s1_6, s0_3, s1_7, s1_8, s1_9)

A_to_B_2a = ((B[0] - A[0])/9, (B[1] - A[1])/9)
B_to_C_2a = ((C[0] - B[0])/9, (C[1] - B[1])/9)
C_to_A_2a = ((A[0] - C[0])/9, (A[1] - C[1])/9)
A_to_B_2b = (-(B[0] - A[0])/9, -(B[1] - A[1])/9)
B_to_C_2b = (-(C[0] - B[0])/9, -(C[1] - B[1])/9)
C_to_A_2b = (-(A[0] - C[0])/9, -(A[1] - C[1])/9)

s2_1 = (s0_1[0] + 1/3*(s1_1[0] - s0_1[0]), s0_1[1] + 1/3*(s1_1[1] - s0_1[1]))
s2_2 = (s2_1[0] + B_to_C_2b[0], s2_1[1] + B_to_C_2b[1])
s2_3 = (s0_1[0] + 2/3*(s1_1[0] - s0_1[0]), s0_1[1] + 2/3*(s1_1[1] - s0_1[1]))
s2_4 = (s1_1[0] + 1/3*(s1_2[0] - s1_1[0]), s1_1[1] + 1/3*(s1_2[1] - s1_1[1]))
s2_5 = (s2_4[0] + C_to_A_2a[0], s2_4[1] + C_to_A_2a[1])
s2_6 = (s1_1[0] + 2/3*(s1_2[0] - s1_1[0]), s1_1[1] + 2/3*(s1_2[1] - s1_1[1]))
s2_7 = (s1_2[0] + 1/3*(s1_3[0] - s1_2[0]), s1_2[1] + 1/3*(s1_3[1] - s1_2[1]))
s2_8 = (s2_7[0] + A_to_B_2a[0], s2_7[1] + A_to_B_2a[1])
s2_9 = (s1_2[0] + 2/3*(s1_3[0] - s1_2[0]), s1_2[1] + 2/3*(s1_3[1] - s1_2[1]))
s2_10 = (s1_3[0] + 1/3*(s0_2[0] - s1_3[0]), s1_3[1] + 1/3*(s0_2[1] - s1_3[1]))
s2_11 = (s2_10[0] + B_to_C_2b[0], s2_10[1] + B_to_C_2b[1])
s2_12 = (s1_3[0] + 2/3*(s0_2[0] - s1_3[0]), s1_3[1] + 2/3*(s0_2[1] - s1_3[1]))
s2_13 = (s0_2[0] + 1/3*(s1_4[0] - s0_2[0]), s0_2[1] + 1/3*(s1_4[1] - s0_2[1]))
s2_14 = (s2_13[0] + C_to_A_2b[0], s2_13[1] + C_to_A_2b[1])
s2_15 = (s0_2[0] + 2/3*(s1_4[0] - s0_2[0]), s0_2[1] + 2/3*(s1_4[1] - s0_2[1]))
s2_16 = (s1_4[0] + 1/3*(s1_5[0] - s1_4[0]), s1_4[1] + 1/3*(s1_5[1] - s1_4[1]))
s2_17 = (s2_16[0] + A_to_B_2a[0], s2_16[1] + A_to_B_2a[1])
s2_18 = (s1_4[0] + 2/3*(s1_5[0] - s1_4[0]), s1_4[1] + 2/3*(s1_5[1] - s1_4[1]))
s2_19 = (s1_5[0] + 1/3*(s1_6[0] - s1_5[0]), s1_5[1] + 1/3*(s1_6[1] - s1_5[1]))
s2_20 = (s2_19[0] + B_to_C_2a[0], s2_19[1] + B_to_C_2a[1])
s2_21 = (s1_5[0] + 2/3*(s1_6[0] - s1_5[0]), s1_5[1] + 2/3*(s1_6[1] - s1_5[1]))
s2_22 = (s1_6[0] + 1/3*(s0_3[0] - s1_6[0]), s1_6[1] + 1/3*(s0_3[1] - s1_6[1]))
s2_23 = (s2_22[0] + C_to_A_2b[0], s2_22[1] + C_to_A_2b[1])
s2_24 = (s1_6[0] + 2/3*(s0_3[0] - s1_6[0]), s1_6[1] + 2/3*(s0_3[1] - s1_6[1]))
s2_25 = (s0_3[0] + 1/3*(s1_7[0] - s0_3[0]), s0_3[1] + 1/3*(s1_7[1] - s0_3[1]))
s2_26 = (s2_25[0] + A_to_B_2b[0], s2_25[1] + A_to_B_2b[1])
s2_27 = (s0_3[0] + 2/3*(s1_7[0] - s0_3[0]), s0_3[1] + 2/3*(s1_7[1] - s0_3[1]))
s2_28 = (s1_7[0] + 1/3*(s1_8[0] - s1_7[0]), s1_7[1] + 1/3*(s1_8[1] - s1_7[1]))
s2_29 = (s2_28[0] + B_to_C_2a[0], s2_28[1] + B_to_C_2a[1])
s2_30 = (s1_7[0] + 2/3*(s1_8[0] - s1_7[0]), s1_7[1] + 2/3*(s1_8[1] - s1_7[1]))
s2_31 = (s1_8[0] + 1/3*(s1_9[0] - s1_8[0]), s1_8[1] + 1/3*(s1_9[1] - s1_8[1]))
s2_32 = (s2_31[0] + C_to_A_2a[0], s2_31[1] + C_to_A_2a[1])
s2_33 = (s1_8[0] + 2/3*(s1_9[0] - s1_8[0]), s1_8[1] + 2/3*(s1_9[1] - s1_8[1]))
s2_34 = (s1_9[0] + 1/3*(s0_1[0] - s1_9[0]), s1_9[1] + 1/3*(s0_1[1] - s1_9[1]))
s2_35 = (s2_34[0] + A_to_B_2b[0], s2_34[1] + A_to_B_2b[1])
s2_36 = (s1_9[0] + 2/3*(s0_1[0] - s1_9[0]), s1_9[1] + 2/3*(s0_1[1] - s1_9[1]))

s2_points = (s0_1, s2_1, s2_2, s2_3, s1_1, s2_4, s2_5, s2_6, s1_2, s2_7, s2_8, s2_9, s1_3, s2_10, s2_11, s2_12, s0_2, s2_13, s2_14, s2_15, s1_4, s2_16, s2_17, s2_18, s1_5, s2_19, s2_20, s2_21, s1_6, s2_22, s2_23, s2_24, s0_3, s2_25, s2_26, s2_27, s1_7, s2_28, s2_29, s2_30, s1_8, s2_31, s2_32, s2_33, s1_9, s2_34, s2_35, s2_36)

#T# plot the figure
s0 = mpatches.Polygon(s0_points, edgecolor = 'k', facecolor = 'w')
ax_list1[0].add_patch(s0)
s1 = mpatches.Polygon(s1_points, edgecolor = 'k', facecolor = 'w')
ax_list1[1].add_patch(s1)
s2 = mpatches.Polygon(s2_points, edgecolor = 'k', facecolor = 'w')
ax_list1[2].add_patch(s2)

#T# show the results
ax_list1[0].autoscale()
ax_list1[1].autoscale()
ax_list1[2].autoscale()
plt.show()