import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
# plt.plot([2, 3, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6], [1, 2, 3, 4])  # plotting two lines in single line
# plt.plot([x for x in range(4, 8)], [y for y in range(1, 5)])  # using list comprehension to generate array for chart
# plt.show()

#  using numpy

# x = np.arange(1, 5)
# plt.plot(x, x, x, x * 3, x, x / 2)
# plt.xlabel("This is the x axis")
# plt.ylabel("This is the y axis")
# plt.title("This is the plot title")
# plt.legend(["x, x", "x, x * 3", "x, x / 2"])
# plt.show()

# This example plots each curve separate with legend applied from keyword arg in each plot function
x = np.arange(1, 5)
plt.plot(x, x, label="x, x")
plt.plot(x, x * 3, label="x, x * 3")
plt.plot(x, x / 2, label="x, x / 2")
plt.xlabel("This is the x axis")
plt.ylabel("This is the y axis")
plt.title("This is the plot title")
plt.legend(loc="upper left")
plt.show()
