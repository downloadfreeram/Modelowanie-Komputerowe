import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class ThreeBody:
    def __init__(self, N, dt, m):
        self.N = N
        self.dt = dt
        self.m = m
        self.G = 1

        self.x = [0.5 - 0.2, 0.5 + 0.2, 0.5]
        self.y = [0.5 - 0.2, 0.5 - 0.2, 0.5 + 0.2 ]
        self.vx = [0.93240737/2.0, 0.93240737 / 2.0, -0.93240737]
        self.vy = [0.86473146/2.0, 0.86473146 / 2.0, -0.86473146]

        self.prev_x = self.x.copy()
        self.prev_y = self.y.copy()

    def dist(self, x1, y1, x2, y2):
        return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def simulate_step(self):
        fx = [0.0] * self.N
        fy = [0.0] * self.N

        for i in range(self.N):
            for j in range(i+1, self.N):
                d = self.dist(self.x[i], self.y[i], self.x[j], self.y[j])
                if d != 0:
                    rx = self.x[i] - self.x[j]
                    ry = self.y[i] - self.y[j]
                    rx /= d
                    ry /= d
                    F = self.G * self.m * self.m / (d * d)
                    Fx = rx * F
                    Fy = ry * F
                    fx[i] -= Fx
                    fy[i] -= Fy
                    fx[j] += Fx
                    fy[j] += Fy

        new_x = [0.0] * self.N
        new_y = [0.0] * self.N
        for i in range(self.N):
            new_x[i] = 2 * self.x[i] - self.prev_x[i] + self.dt**2 * fx[i] / self.m
            new_y[i] = 2 * self.y[i] - self.prev_y[i] + self.dt**2 * fy[i] / self.m

            self.vx[i] = (new_x[i] - self.prev_x[i]) / (2 * self.dt)
            self.vy[i] = (new_y[i] - self.prev_y[i]) / (2 * self.dt)

        self.prev_x = self.x.copy()
        self.prev_y = self.y.copy()
        self.x = new_x
        self.y = new_y

        return self.x, self.y

    def animate(self, frames=200):
        fig, ax = plt.subplots()
        ax.set_xlim(-4, 4)
        ax.set_ylim(-4, 4)
        scat = ax.scatter(self.x, self.y)

        def update(frame):
            x, y = self.simulate_step()
            scat.set_offsets(np.c_[x, y])
            return scat,

        ani = animation.FuncAnimation(fig, update, frames=frames, interval=30, blit=True)
        plt.show()


def main():
    test = ThreeBody(3, 0.0015, 1)
    test.animate()

if __name__ == "__main__":
    main()
