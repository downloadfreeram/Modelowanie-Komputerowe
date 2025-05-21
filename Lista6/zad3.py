import numpy as np
import matplotlib.pyplot as plt

steps = 1000
walks = 10000

walk = np.random.choice([-1, 1], size=(walks, steps))
final_positions = np.sum(walk, axis=1)

plt.figure(figsize=(10, 6))
plt.hist(final_positions, bins=100, color='skyblue', edgecolor='black')
plt.title("rozklad koncowych pozycji spacerow")
plt.ylabel("liczba spacerow")
plt.xlabel("pozycja koncowa")
plt.grid(True)
plt.tight_layout()
plt.show()

# obliczanie ile spacerow zakonczylo się w konkretnej odleglosci od zera
count_dist1 = np.count_nonzero(np.abs(final_positions) == 1)
count_dist30 = np.count_nonzero(np.abs(final_positions) == 30)

print(f"liczba spacerow konczacych się w odleglosci 1: {count_dist1}")
print(f"liczba spacerow konczacych się w odleglosic 30: {count_dist30}")
