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

# # This example plots each curve separate with legend applied from keyword arg in each plot function
# x = np.arange(1, 5)
# plt.plot(x, x, label="x, x")
# plt.plot(x, x * 3, label="x, x * 3")
# plt.plot(x, x / 2, label="x, x / 2")
# plt.xlabel("This is the x axis")
# plt.ylabel("This is the y axis")
# plt.title("This is the plot title")
# plt.legend(loc="upper left")
# plt.show()


# # This example adds gridlines and manipulates the axes
# x = np.arange(1, 5)
# plt.plot(x, x, label="x, x")
# plt.plot(x, x * 3, label="x, x * 3")
# plt.plot(x, x / 2, label="x, x / 2")
# plt.xlabel("This is the x axis")
# plt.ylabel("This is the y axis")
# plt.title("This is the plot title")
# plt.legend(loc="upper left")
# plt.grid(True)
# plt.axis([0, 5, 0, 13])  # [x min, x max, y min, y max]
# plt.show()


# This example adds colour
# x = np.arange(1, 5)
# plt.plot(x, x, label="x, x", color="red")  # can also pass abbreviations, RGB or hex color
# plt.plot(x, x * 3, "green" label="x, x * 3")  # can also pass color as third argument
# plt.plot(x, x / 2, label="x, x / 2", color="blue")
# plt.xlabel("This is the x axis")
# plt.ylabel("This is the y axis")
# plt.title("This is the plot title")
# plt.legend(loc="upper left")
# plt.grid(True)
# plt.axis([0, 5, 0, 13])
# plt.show()

# # This example adds line and marker customisation
# x = np.arange(1, 5)
# plt.plot(x, x, ":d", label="x, x", color="red")  # added 'd' as marker for data points
# plt.plot(x, x * 3, "g--s", label="x, x * 3")  # note colour plus line style combined in third argument
# plt.plot(x, x / 2, "-.o", label="x, x / 2", color="blue")
# plt.xlabel("This is the x axis")
# plt.ylabel("This is the y axis")
# plt.title("This is the plot title")
# plt.legend(loc="upper left")
# plt.grid(True)
# plt.axis([0, 5, 0, 13])
# plt.show()



# This example adds line and marker customisation
# x = np.arange(1, 5)
# plt.plot(x, x, "d", label="x, x", color="red", linestyle="")  # using linestyle kwarg
# plt.plot(x, x * 3, "g--s", label="x, x * 3", linewidth=3)  # line width
# plt.plot(x, x / 2, "-.o", label="x, x / 2", color="blue",
#          markersize=10, markeredgecolor="r", markerfacecolor="c")  # marker size and coloring
# plt.xlabel("This is the x axis")
# plt.ylabel("This is the y axis")
# plt.title("This is the plot title")
# plt.legend(loc="upper left")
# plt.grid(True)
# plt.axis([0, 5, 0, 13])
# plt.show()

# Mulitple figures in same window
#
# fig = plt.figure()  # create an figure instance
#
# chart1 = fig.add_subplot(3, 1, 1)  # setup grid for charts and set position
# chart2 = fig.add_subplot(3, 1, 2)  # (rows, columns, position)
# chart3 = fig.add_subplot(3, 1, 3)
#
# x = np.arange(1, 5)
# chart1.plot(x, x, "d", label="x, x", color="red", linestyle="")  # changed to chart1 variable
# chart2.plot(x, x * 3, "g--s", label="x, x * 3", linewidth=3)  #
# chart3.plot(x, x / 2, "-.o", label="x, x / 2", color="blue",
#          markersize=10, markeredgecolor="r", markerfacecolor="c")  #
# # plt.xlabel("This is the x axis")
# # plt.ylabel("This is the y axis")
# # plt.title("This is the plot title")
# plt.legend(loc="best")
#
# plt.grid(True)
# plt.axis([0, 5, 0, 13])
#
# plt.show()

fig = plt.figure(facecolor="grey")  # specify background color

chart1 = fig.add_subplot(1, 1, 1, facecolor="black")  # chart background color
# chart2 = fig.add_subplot(3, 1, 2)  # (rows, columns, position)
# chart3 = fig.add_subplot(3, 1, 3)

x = np.arange(1, 5)
chart1.plot(x, x, "d", label="x, x", color="red", linestyle="--")  # changed to chart1 variable
chart1.tick_params(axis="x", color="white")  # set axis tick color
chart1.tick_params(axis="y", color="white")  # set axis tick color
for spine in chart1.spines:
    chart1.spines[spine].set_color("white")  # set border/spines color

# chart2.plot(x, x * 3, "g--s", label="x, x * 3", linewidth=3)  #
# chart3.plot(x, x / 2, "-.o", label="x, x / 2", color="blue",
#             markersize=10, markeredgecolor="r", markerfacecolor="c")  #
# plt.xlabel("This is the x axis")
# plt.ylabel("This is the y axis")
# plt.title("This is the plot title")
plt.legend(loc="best")

plt.grid(True)
# plt.axis([0, 5, 0, 13])

plt.show()
