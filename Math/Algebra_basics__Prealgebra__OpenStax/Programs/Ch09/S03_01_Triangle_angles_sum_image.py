#T# this program draws a triangle and shows that the sum of its angles is 180 degrees or pi radians

#T# to do this drawing, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax1 = plt.subplots(1, 1)

#T# hide the spines and the scales of the axes
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

#T# create the vertices of the triangle
A, B, C = [1, 2], [8, 2], [6, 6]

#T# join the vertices to create the sides
plt.plot([A[0], B[0]], [A[1], B[1]], color = '#000000')
plt.plot([A[0], C[0]], [A[1], C[1]], color = '#000000')
plt.plot([B[0], C[0]], [B[1], C[1]], color = '#000000')

#T# create the parallel line to a side that passes through the vertex opposite to said side
plt.plot([0, 9], [6, 6], color = '#000000')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# Name the vertices
plt.text(A[0], A[1], r'$A$', ha = 'right', va = 'top', size = 18)
plt.text(B[0], B[1], r'$B$', ha = 'left', va = 'top', size = 18)
plt.text(C[0] - 0.05, C[1] + 0.05, r'$C$', ha = 'center', va = 'bottom', size = 18)

#T# Name the angles
plt.text(A[0] + 0.2, A[1] + 0.0, r'$\angle A$', ha = 'left', va = 'bottom', size = 18)
plt.text(B[0] - 0.2, B[1] + 0.0, r'$\angle B$', ha = 'right', va = 'bottom', size = 18)
plt.text(C[0] + 0.1, C[1] - 0.5, r'$\angle C$', ha = 'right', va = 'top', size = 18)
plt.text(C[0] - 0.6, C[1] - 0.1, r'$\angle A$', ha = 'right', va = 'top', size = 18)
plt.text(C[0] + 0.3, C[1] - 0.1, r'$\angle B$', ha = 'left', va = 'top', size = 18)

#T# show the result
plt.show()