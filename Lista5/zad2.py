import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class ThreeBody:
    def __init__(self, N, dt, m):
        self.N = N
        self.dt = dt
        self.m = m
        self.G = 1
        self.variable = 0.1
        self.step = 0

        self.x_data = [[] for _ in range(self.N)]
        self.y_data = [[] for _ in range(self.N)]

        self.avg_distances = []

    def dist(self, x1, y1, x2, y2):
        return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def simulate(self, steps):
        fx = []
        fy = []
        # initial values for drawing an infinite symbol based on "A remarkable periodic solution of three body problem in the case of equal masses" Annals of Mathematics (2000)
        x = [0.97000436, -0.97000436, 0.0]
        y = [-0.24308753, 0.24308753, 0.0]
        vx  = [0.466203685, 0.466203685, -0.93240737]
        vy = [0.432365730, 0.432365730, -0.86473146]
        xp1 = [0] * self.N
        yp1 = [0] * self.N
        xm1 = [0] * self.N
        ym1 = [0] * self.N

        while self.step < steps:
            self.step += 1
            fx = [0] * self.N
            fy = [0] * self.N

            for i in range(self.N):
                for j in range(i + 1, self.N):
                    d = self.dist(x[i], y[i], x[j], y[j])
                    if d != 0:
                        rx = (x[i] - x[j]) / d
                        ry = (y[i] - y[j]) / d
                        F = self.G * self.m * self.m / (d * d)
                        Fx = rx * F
                        Fy = ry * F
                        fx[i] -= Fx
                        fy[i] -= Fy
                        fx[j] += Fx
                        fy[j] += Fy

            if self.step == 1:
                for b in range(self.N):
                    vx[b] += fx[b] / self.m * self.dt
                    vy[b] += fy[b] / self.m * self.dt
                    xp1[b] = x[b] + vx[b] * self.dt
                    yp1[b] = y[b] + vy[b] * self.dt
                    xm1[b] = x[b]
                    ym1[b] = y[b]
            else:
                for b in range(self.N):
                    xp1[b] = 2 * x[b] - xm1[b] + self.dt * self.dt * fx[b] / self.m
                    yp1[b] = 2 * y[b] - ym1[b] + self.dt * self.dt * fy[b] / self.m

            for b in range(self.N):
                xm1[b] = x[b]
                ym1[b] = y[b]

                x[b] = xp1[b]
                y[b] = yp1[b]

                vx[b] = (x[b] - xm1[b]) / (2 * self.dt)
                vy[b] = (y[b] - ym1[b]) / (2 * self.dt)

                self.x_data[b].append(x[b])
                self.y_data[b].append(y[b])

            curr_avg_dist = avg_distance(x, y)
            self.avg_distances.append(curr_avg_dist)

        return self.x_data, self.y_data, self.avg_distances

def avg_distance(x, y):
    d1 = np.sqrt((x[0] - x[1])**2 + (y[0] - y[1])**2)
    d2 = np.sqrt((x[0] - x[2])**2 + (y[0] - y[2])**2)
    d3 = np.sqrt((x[1] - x[2])**2 + (y[1] - y[2])**2)
    return (d1 + d2 + d3) / 3.0

def animate(x_data, y_data):
    fig, ax = plt.subplots()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.grid(True)

    points = [ax.plot([], [], 'o')[0] for _ in range(len(x_data))]
    trails = [ax.plot([], [], '-',linewidth = 0.7)[0] for _ in range(len(x_data))]

    def init():
        for point, trail in zip(points,trails):
            point.set_data([], [])
            trail.set_data([], [])
        return points + trails

    def update(frame):
        for i in range(len(x_data)):
            if frame < len(x_data[i]):
                points[i].set_data([x_data[i][frame]], [y_data[i][frame]])
                trails[i].set_data(x_data[i][:frame+1], y_data[i][:frame+1])
        return points + trails

    ani = animation.FuncAnimation(fig, update, frames=len(x_data[0]), init_func=init, interval = 30)
    plt.show()


def plot_avg_distance(avg_distances):
    steps = range(len(avg_distances))
    plt.figure()
    plt.plot(steps, avg_distances, label='Avg. distance')
    plt.xlabel('Step')
    plt.ylabel('Avg distance')
    plt.title('Avg distance between bodies')
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    test = ThreeBody(3, 0.0015, 1)
    x_data, y_data, avg_distance = test.simulate(steps=3000)
    animate(x_data, y_data)
    plot_avg_distance(avg_distance)

if __name__ == "__main__":
    main()
