import matplotlib.pyplot as plt

x = [5, 7]; y = [4, 1]

plt.plot(x, y)
ax1 = plt.axes() # plt.Axes()
ax1.margins(1,1)
plt.show()