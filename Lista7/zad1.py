import numpy as np
import random
import matplotlib.pyplot as plt

grid_size = 201 
center = grid_size // 2

grid = np.zeros((grid_size, grid_size), dtype=int)

grid[center, center] = 1
cluster = {(center, center)}
boundary = set()

neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for dx, dy in neighbors:
    boundary.add((center + dx, center + dy))

def edenCluster(cluster, boundary, steps):
    for _ in range(steps):
        new_point = random.choice(list(boundary))
        x, y = new_point
        cluster.add(new_point)
        grid[x, y] = 1
        boundary.remove(new_point)

        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if (0 <= nx < grid_size and 0 <= ny < grid_size and
                (nx, ny) not in cluster and (nx, ny) not in boundary):
                boundary.add((nx, ny))

edenCluster(cluster, boundary, 1000)

x, y = zip(*cluster)
plt.figure(figsize=(6, 6))
plt.imshow(grid, cmap='Blues', origin='lower')
plt.title("Wzrost dla klustra Edena")
plt.axis("equal")
plt.show()

