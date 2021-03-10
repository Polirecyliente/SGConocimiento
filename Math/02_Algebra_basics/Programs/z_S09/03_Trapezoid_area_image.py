#T# the formula for the area of a trapezoid can be understood as the sum of the areas of the two triangles that appear when drawing one of its diagonals

#T# to draw the trapezoid with the two triangles, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# hide the spines and ticks
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

#T# create the vertices of the trapezoid
A, B, C, D = [0, 0], [1, 3], [5, 3], [7, 0]

#T# join the vertices and one diagonal of the trapezoid
plt.plot([B[0], C[0], D[0], A[0], B[0], D[0]], [B[1], C[1], D[1], A[1], B[1], D[1]], color = '#000000')

#T# create the height guide
plt.plot([B[0], B[0]], [A[1], B[1]], '--', color = '#000000')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# name the bases, the height, and the areas
plt.text((B[0] + C[0])/2, (B[1] + C[1])/2, r'$b$', ha = 'center', va = 'bottom', size = 18)
plt.text((A[0] + D[0])/2, (A[1] + D[1])/2 - 0.05, r'$B$', ha = 'center', va = 'top', size = 18)
plt.text(B[0] + 0.1, (A[1] + B[1])/2, r'$h$', ha = 'left', va = 'center', size = 18)
plt.text((B[0] + C[0] + D[0])/3, (B[1] + C[1] + D[1])/3, r'$A_1$', ha = 'center', va = 'center', size = 18)
plt.text((A[0] + B[0] + D[0])/3, (A[1] + B[1] + D[1])/3, r'$A_2$', ha = 'center', va = 'center', size = 18)

#T# show the result
plt.show()