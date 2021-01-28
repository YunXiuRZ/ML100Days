import matplotlib.pyplot as plt
import numpy as np

#1
x = np.arange(0, 180)
y = np.cos(x * np.pi / 45.)
plt.plot(x, y)
plt.show()

#2
random_x = np.random.random(180)
random_y = np.random.random(180)
plt.scatter(random_x, random_y, c='R')
plt.show()