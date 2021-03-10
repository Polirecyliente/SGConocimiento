#T# the following code shows how to draw two similar figures

#T# to draw two similar figures, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes
fig1, ax_list1 = plt.subplots(1, 2)

#T# set the aspect of the axes
for it1 in fig1.axes:
    it1.set_aspect('equal', adjustable = 'box')

#T# hide the spines and ticks
for it1 in fig1.axes:
    for it2 in ['top', 'bottom', 'left', 'right']:
        it1.spines[it2].set_visible(False)
    it1.xaxis.set_visible(False)
    it1.yaxis.set_visible(False)

#T# create the variables that define the plot
A = (.4, 5.5)
B = (3, 7)
C = (3.1, 6)
D = (4.7, 6.7)
E = (5, 6)
F = (5, 5)
G = (4, 4)
H = (4.8, 1)
I = (.8, 1)
J = (.6, 4.5)
K = (1.2, 5)

L = (1.9, 4.3)
M = (3.3, 4.6)
N = (3.3, 5.4)
O = (2.8, 3.3)
P = (1.7, 3.5)
Q = (2.3, 1.9)

list_x1 = [A[0], B[0], C[0], D[0], E[0], F[0], G[0], H[0], I[0], J[0], K[0], A[0]]
list_y1 = [A[1], B[1], C[1], D[1], E[1], F[1], G[1], H[1], I[1], J[1], K[1], A[1]]

list_x2 = [K[0], L[0], M[0], E[0]]
list_y2 = [K[1], L[1], M[1], E[1]]

list_x3 = [K[0], N[0], G[0]]
list_y3 = [K[1], N[1], G[1]]

list_x4 = [H[0], O[0], P[0], Q[0], I[0]]
list_y4 = [H[1], O[1], P[1], Q[1], I[1]]

list_x5 = [J[0], P[0]]
list_y5 = [J[1], P[1]]

s = 1/2

p_s_0_A = (A[0]*s, A[1]*s)
p_s_0_B = (B[0]*s, B[1]*s)
p_s_0_C = (C[0]*s, C[1]*s)
p_s_0_D = (D[0]*s, D[1]*s)
p_s_0_E = (E[0]*s, E[1]*s)
p_s_0_F = (F[0]*s, F[1]*s)
p_s_0_G = (G[0]*s, G[1]*s)
p_s_0_H = (H[0]*s, H[1]*s)
p_s_0_I = (I[0]*s, I[1]*s)
p_s_0_J = (J[0]*s, J[1]*s)
p_s_0_K = (K[0]*s, K[1]*s)
p_s_0_L = (L[0]*s, L[1]*s)
p_s_0_M = (M[0]*s, M[1]*s)
p_s_0_N = (N[0]*s, N[1]*s)
p_s_0_O = (O[0]*s, O[1]*s)
p_s_0_P = (P[0]*s, P[1]*s)
p_s_0_Q = (Q[0]*s, Q[1]*s)

list_x1_2 = [p_s_0_A[0], p_s_0_B[0], p_s_0_C[0], p_s_0_D[0], p_s_0_E[0], p_s_0_F[0], p_s_0_G[0], p_s_0_H[0], p_s_0_I[0], p_s_0_J[0], p_s_0_K[0], p_s_0_A[0]]
list_y1_2 = [p_s_0_A[1], p_s_0_B[1], p_s_0_C[1], p_s_0_D[1], p_s_0_E[1], p_s_0_F[1], p_s_0_G[1], p_s_0_H[1], p_s_0_I[1], p_s_0_J[1], p_s_0_K[1], p_s_0_A[1]]

list_x2_2 = [p_s_0_K[0], p_s_0_L[0], p_s_0_M[0], p_s_0_E[0]]
list_y2_2 = [p_s_0_K[1], p_s_0_L[1], p_s_0_M[1], p_s_0_E[1]]

list_x3_2 = [p_s_0_K[0], p_s_0_N[0], p_s_0_G[0]]
list_y3_2 = [p_s_0_K[1], p_s_0_N[1], p_s_0_G[1]]

list_x4_2 = [p_s_0_H[0], p_s_0_O[0], p_s_0_P[0], p_s_0_Q[0], p_s_0_I[0]]
list_y4_2 = [p_s_0_H[1], p_s_0_O[1], p_s_0_P[1], p_s_0_Q[1], p_s_0_I[1]]

list_x5_2 = [p_s_0_J[0], p_s_0_P[0]]
list_y5_2 = [p_s_0_J[1], p_s_0_P[1]]

#T# plot the figure
ax_list1[0].plot(list_x1, list_y1, 'k')
ax_list1[0].plot(list_x2, list_y2, 'k')
ax_list1[0].plot(list_x3, list_y3, 'k')
ax_list1[0].plot(list_x4, list_y4, 'k')
ax_list1[0].plot(list_x5, list_y5, 'k')

ax_list1[0].margins(.1)
ax_list1[1].set_xlim(ax_list1[0].get_xlim()[0], ax_list1[0].get_xlim()[1])
ax_list1[1].set_ylim(ax_list1[0].get_ylim()[0], ax_list1[0].get_ylim()[1])

ax_list1[1].plot(list_x1_2, list_y1_2, 'k')
ax_list1[1].plot(list_x2_2, list_y2_2, 'k')
ax_list1[1].plot(list_x3_2, list_y3_2, 'k')
ax_list1[1].plot(list_x4_2, list_y4_2, 'k')
ax_list1[1].plot(list_x5_2, list_y5_2, 'k')

#T# show the results
plt.show()