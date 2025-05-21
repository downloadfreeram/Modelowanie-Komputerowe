import numpy as np

steps = 1000
trials = 1000

def diffusion(steps, sim, directions):
    displacements = []
    for _ in range(sim):
        position = np.zeros(2, dtype=int)
        moves = np.random.randint(0, len(directions), size=steps)
        for move in moves:
            position += directions[move]
        r_sqrt = np.dot(position, position)
        displacements.append(r_sqrt)
    mean_square = np.mean(displacements)
    coefficient = mean_square / (4 * steps)
    return coefficient

directions4 = [
    np.array([0, 1]), np.array([0, -1]),
    np.array([1, 0]), np.array([-1, 0])
]

directions8 = directions4 + [
    np.array([1, 1]), np.array([-1, -1]),
    np.array([-1, 1]), np.array([1, -1])
]

coeff_4 = diffusion(steps, trials, directions4)
coeff_8 = diffusion(steps, trials, directions8)

print("wspolczynnik dyfuzji dla 4 kierunkow: {:.6f}".format(coeff_4))
print("wspolczynnik dyfuzji dla 8 kierunkow): {:.6f}".format(coeff_8))
