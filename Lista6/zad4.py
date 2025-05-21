import numpy as np

walks = 1000
steps = 1000

def d1(steps):
    x = np.cumsum(np.random.choice([-1, 1], size=steps))
    return np.any(x == 0)

def d2(steps):
    x = np.cumsum(np.random.choice([-1, 1], size=steps))
    y = np.cumsum(np.random.choice([-1, 1], size=steps))
    return np.any((x == 0) & (y == 0))

def d3(steps):
    x = np.cumsum(np.random.choice([-1, 1], size=steps))
    y = np.cumsum(np.random.choice([-1, 1], size=steps))
    z = np.cumsum(np.random.choice([-1, 1], size=steps))
    return np.any((x == 0) & (y == 0) & (z == 0))

p_d1 = sum(d1(steps) for _ in range(walks)) / walks
p_d2 = sum(d2(steps) for _ in range(walks)) / walks
p_d3 = sum(d3(steps) for _ in range(walks)) / walks

print("prawdopodobienstwo powrotu d1: {:.3f}".format(p_d1))
print("prawdopodobienstwo powrotu d2: {:.3f}".format(p_d2))
print("prawdopodobienstwo powrotu d3: {:.3f}".format(p_d3))
