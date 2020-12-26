#T# the following code shows how to graph a polynomial

#T# to graph a polynomial, the pyplot module of the matplotlib package is used
import matplotlib.pyplot as plt

#T# create the figure and axes to graph the polynomial
fig1 = plt.Figure()
ax1 = plt.axes()

#T# create a list of points of the polynomial in the x-axis, and another list in the y-axis
list1 = [it1 for it1 in range(-16, 20)]
list2 = [-3*it2**5 + 7*it2**4 - 3*it2**2 + 12*it2 for it2 in list1]
#| represents the polynomial $p(x) = -3x^5 + 7x^4 - 3x^2 + 12x$

#T# plot the points of the polynomial
plt.plot(list1, list2)

#T# show the results
plt.show()