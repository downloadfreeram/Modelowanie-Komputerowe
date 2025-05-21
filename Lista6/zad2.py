import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

num_steps = 1000
num_walk = 15

# 2d
plt.figure(figsize=(10, 10))
for _ in range(num_walk):
    steps_x = np.random.randint(0, 2, size=num_steps) * 2 - 1
    steps_y = np.random.randint(0, 2, size=num_steps) * 2 - 1
    path_x = np.cumsum(steps_x)
    path_y = np.cumsum(steps_y)
    plt.plot(path_x, path_y)

plt.title("Losowy spacer w 2D")
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.show()

# 3d
fig = plt.figure(figsize=(10, 10))
axis = fig.add_subplot(111, projection='3d')
for _ in range(num_walk):
    dir_x = np.random.choice([-1, 1], size=num_steps)
    dir_y = np.random.choice([-1, 1], size=num_steps)
    dir_z = np.random.choice([-1, 1], size=num_steps)
    trail_x = np.cumsum(dir_x)
    trail_y = np.cumsum(dir_y)
    trail_z = np.cumsum(dir_z)
    axis.plot(trail_x, trail_y, trail_z)

axis.set_title("Losowy spacer w 3D")
plt.tight_layout()
plt.show()
