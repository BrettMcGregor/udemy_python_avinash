import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

# 3D Charts
#
# fig = plt.figure()
#
# chart = fig.add_subplot(1, 1, 1, projection="3d")
# x = np.random.randn(100)
# y = np.random.randn(100)
# z = np.random.randn(100)
#
# plt.plot(x, y, z, linestyle="", marker="s")
# plt.show()


# 3D Scatter Plot
#
# fig = plt.figure()
#
# chart = fig.add_subplot(1, 1, 1, projection="3d")
# x = np.random.randn(100)
# y = np.random.randn(100)
# z = np.random.randn(100)
#
# size = 100 * np.random.randn(100)
# colors = np.random.rand(100)
#
# chart.scatter(x, y, z, s=size, c=colors, marker="^")
#
# plt.show()

# 3D Bar Charts

fig = plt.figure()

chart = fig.add_subplot(1, 1, 1, projection="3d")
x = [1, 2, 3, 4, 5]
y = [3, 6, 2, 8, 4]
z = [0, 0, 0, 0, 0]

dx = np.ones(5)
dy = np.ones(5)
dz = [1, 8, 3, 2, 5]

chart.bar3d(x, y, z, dx, dy, dz, color="red")
chart.set_xlabel("X Label")
chart.set_ylabel("Y Label")
chart.set_zlabel("Z Label")
plt.show()
