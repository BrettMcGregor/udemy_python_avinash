import matplotlib.pyplot as plt
import numpy as np

# Histogram
x = np.random.randn(1000)


# plt.hist(x, bins=30, color="g", cumulative=True)  # define number of bins
# plt.hist(x, bins=[-3, 0, 3])  # define bins using values
# plt.hist(x, bins=30, color="g", cumulative=True)  # cumulative

# plt.show()

# Pie Charts
# plt.figure(figsize=(5, 5))  # make it a circle
# countries = ["USA", "India", "Australia", "NZ", "Canada"]
# values = [25, 5, 6, 33, 2]
# exp = [.1, 0, 0, .05, 0]
# col = ["blue", "cyan", "yellow", "red", "green"]
# plt.pie(values, labels=countries, autopct="%.1f%%", explode=exp, colors=col)
#
# plt.show()


# Bar Charts

# plt.figure(figsize=(7, 5))  #
# names = ["Brett", "Andrea", "Devon", "Ryan"]
# scores = [88, 57, 93, 10]
# scores2 = [90, 66, 50, 39]
# positions = np.arange(len(scores))  # creates an array to for numbering the position of each bar
# plt.bar(positions, scores, width=0.3)
# plt.bar(positions + 0.3, scores2, width=0.3)
# plt.xticks(positions + 0.3 / 2, names)
# plt.xlabel("Names")
# plt.ylabel("Scores")
# plt.title("Test Scores")
# plt.show()

# Scatter Plots

plt.figure(figsize=(7, 7))

x = np.random.randn(200)
y = np.random.randn(200)
size = 50 * np.random.rand(200)  # random sizing
colors = np.random.rand(200)  # random colors

plt.scatter(x, y, s=size, c=colors, marker="s")

plt.show()