#T# A proof for the pythagorean theorem can be shown by surrounding the square of the hypotenuse with repeated instances of its right triangle

#T# to draw these right triangles, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1 = plt.Figure()
ax1 = plt.axes() # type: plt.Axes

#T# set the axes aspect ratio
ax1.set_aspect('equal')

#T# hide the spines and the scales of the axes
for it1 in ['top', 'bottom', 'left', 'right']:
    ax1.spines[it1].set_visible(False)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

#T# create the vertices of the triangles
A1, B1, C1 = [2, 0], [7, 2], [7, 0]
A2, B2, C2 = [0, 5], [2, 0], [0, 0]
A3, B3, C3 = [5, 7], [0, 5], [0, 7]
A4, B4, C4 = [7, 2], [5, 7], [7, 7]

#T# join the vertices to create the sides
plt.plot([A1[0], B1[0]], [A1[1], B1[1]], color = '#000000')
plt.plot([A1[0], C1[0]], [A1[1], C1[1]], color = '#000000')
plt.plot([B1[0], C1[0]], [B1[1], C1[1]], color = '#000000')

plt.plot([A2[0], B2[0]], [A2[1], B2[1]], color = '#000000')
plt.plot([A2[0], C2[0]], [A2[1], C2[1]], color = '#000000')
plt.plot([B2[0], C2[0]], [B2[1], C2[1]], color = '#000000')

plt.plot([A3[0], B3[0]], [A3[1], B3[1]], color = '#000000')
plt.plot([A3[0], C3[0]], [A3[1], C3[1]], color = '#000000')
plt.plot([B3[0], C3[0]], [B3[1], C3[1]], color = '#000000')

plt.plot([A4[0], B4[0]], [A4[1], B4[1]], color = '#000000')
plt.plot([A4[0], C4[0]], [A4[1], C4[1]], color = '#000000')
plt.plot([B4[0], C4[0]], [B4[1], C4[1]], color = '#000000')

#T# set the math text font to the Latex default, Computer Modern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#T# Name the sides
plt.text((B1[0] + C1[0])/2 + 0.1, (B1[1] + C1[1])/2 + 0.0, r'$a$', ha = 'left', va = 'center', size = 18)
plt.text((A1[0] + C1[0])/2 + 0.0, (A1[1] + C1[1])/2 - 0.1, r'$b$', ha = 'center', va = 'top', size = 18)
plt.text((A1[0] + B1[0])/2 + 0.0, (A1[1] + B1[1])/2 + 0.0, r'$c$', ha = 'right', va = 'bottom', size = 18)

plt.text((B2[0] + C2[0])/2 + 0.0, (B2[1] + C2[1])/2 - 0.1, r'$a$', ha = 'center', va = 'top', size = 18)
plt.text((A2[0] + C2[0])/2 - 0.1, (A2[1] + C2[1])/2 + 0.0, r'$b$', ha = 'right', va = 'center', size = 18)
plt.text((A2[0] + B2[0])/2 + 0.0, (A2[1] + B2[1])/2 + 0.0, r'$c$', ha = 'left', va = 'bottom', size = 18)

plt.text((B3[0] + C3[0])/2 - 0.1, (B3[1] + C3[1])/2 + 0.0, r'$a$', ha = 'right', va = 'center', size = 18)
plt.text((A3[0] + C3[0])/2 + 0.0, (A3[1] + C3[1])/2 + 0.1, r'$b$', ha = 'center', va = 'bottom', size = 18)
plt.text((A3[0] + B3[0])/2 + 0.0, (A3[1] + B3[1])/2 + 0.0, r'$c$', ha = 'left', va = 'top', size = 18)

plt.text((B4[0] + C4[0])/2 + 0.0, (B4[1] + C4[1])/2 + 0.1, r'$a$', ha = 'center', va = 'bottom', size = 18)
plt.text((A4[0] + C4[0])/2 + 0.1, (A4[1] + C4[1])/2 + 0.0, r'$b$', ha = 'left', va = 'center', size = 18)
plt.text((A4[0] + B4[0])/2 + 0.0, (A4[1] + B4[1])/2 + 0.0, r'$c$', ha = 'right', va = 'top', size = 18)

#T# show the result
plt.show()