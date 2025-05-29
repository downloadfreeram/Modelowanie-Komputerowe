import numpy as np
import matplotlib.pyplot as plt
import random

grid_size = 200
center = grid_size // 2
max_particles = 3000

grid = np.zeros((grid_size, grid_size), dtype=int)
grid[center, center] = 1 

neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def checkIfNearCluster(x, y):
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid_size and 0 <= ny < grid_size:
            if grid[nx, ny] == 1:
                return True
    return False

def dlaCluster():
    angle = random.uniform(0, 2 * np.pi)
    radius = center - 2
    x = int(center + radius * np.cos(angle))
    y = int(center + radius * np.sin(angle))

    while True:
        dx, dy = random.choice(neighbors)
        x += dx
        y += dy

        if not (0 <= x < grid_size and 0 <= y < grid_size):
            return

        if checkIfNearCluster(x, y):
            grid[x, y] = 1
            return

for _ in range(max_particles):
    dlaCluster()

plt.figure(figsize=(6, 6))
plt.imshow(grid, origin='lower')
plt.title("Klaster DLA koncowy stan")
plt.show()
