import matplotlib.pyplot as plt
import numpy as np

class ThreeBody:
    def __init__(self, N, dt, m):
        self.N = N
        self.dt = dt
        self.m = m
        self.G = 1

    def dist(self, x1,y1,x2,y2):
        return np.sqrt((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2))
    
    def simulate(self):
        fx = []
        fy = []
        x = [0.5 - 0.2, 0.5 + 0.2, 0.5]
        y = [0.5 - 0.2, 0.5 - 0.2, 0.5 + 0.2 ]
        vx = [0.93240737/2.0, 0.93240737 / 2.0, -0.93240737]
        vy = [0.86473146/2.0, 0.86473146 / 2.0, -0.86473146]
        xp1 = []
        yp1 = []
        xm1 = []
        ym1 = [] 

        step = 0

        while(step < 100):
            step = step + 1
            for i in range(self.N):
                for j in range(i+1,self.N):
                    d = self.dist(x[i], y[i], x[j], y[j])

                    if(d != 0):
                        rx = x[i] - x[j]
                        ry = y[i] - y[j]
                        rx = rx / d
                        ry = ry / d
                        Fx = rx * self.G * self.m*self.m / (d*d) 
                        Fy = ry * self.G * self.m*self.m / (d*d)

                        fx.insert(i, 0-Fx)
                        fy.insert(i, 0-Fy)
                        
                        fx.insert(j, 0+Fx)
                        fy.insert(j, 0+Fy)

            if(step == 1):
                for b in range(self.N):

                    vx.insert(b, vx[b] + fx[b] / self.m * self.dt)
                    vy.insert(b, vy[b] + fy[b] / self.m * self.dt)
                    xp1.insert(b, x[b] + vx[b] * self.dt)
                    yp1.insert(b, x[b] + vy[b] * self.dt )
            else:
                #Verlet calculations
                for b in range(self.N):

                    xp1.insert(b, 2 * x[b] - xm1[b] + self.dt * self.dt * fx[b]/ self.m)
                    yp1.insert(b, 2 * y[b] - ym1[b] + self.dt * self.dt * fy[b]/ self.m)
            
            for b in range(self.N):
                xm1.insert(b, x[b])
                ym1.insert(b, y[b])

                x[b] = xp1[b]
                y[b] = yp1[b]

                vx[b] = (x[b] - xm1[b]) / (2 * self.dt)
                vy[b] = (y[b] - ym1[b]) / (2 * self.dt)

def main():
    test = ThreeBody(3, 0.0015, 1)

    print(test.simulate())

if __name__ == "__main__":
    main()