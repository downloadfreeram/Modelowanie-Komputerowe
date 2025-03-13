import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

class Stains:
    def __init__(self, root, grid_size=(100, 100), cell_size=5):
        self.rows, self.cols = grid_size
        self.cell_size = cell_size
        self.root = root
        
        self.grid = np.random.choice([0, 1], size=(self.rows, self.cols))
        self.history = []
        
        self.canvas = tk.Canvas(root, width=self.cols * cell_size, height=self.rows * cell_size, bg="black")
        self.canvas.pack()
        self.draw_grid()
        
        self.run_simulation()
        self.plots()

    def draw_grid(self):
        self.canvas.delete("all")
        for row in range(self.rows):
            for col in range(self.cols):
                color = "white" if self.grid[row, col] == 1 else "black"
                self.canvas.create_rectangle(
                    col * self.cell_size, row * self.cell_size,
                    (col + 1) * self.cell_size, (row + 1) * self.cell_size,
                    fill=color, outline="gray"
                )
    
    def count_neighbors(self, x, y):
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        return sum(self.grid[(x + dx) % self.rows, (y + dy) % self.cols] for dx, dy in offsets)
    
    def update_grid(self):
        new_grid = np.zeros((self.rows, self.cols), dtype=int)
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.count_neighbors(row, col)
                new_grid[row, col] = 1 if neighbors in [4, 6, 7, 8, 9] else 0
        self.grid = new_grid
        self.history.append(np.mean(self.grid))
    
    def run_simulation(self, iteration=0):
        self.update_grid()
        self.draw_grid()
        self.root.after(50, lambda: self.run_simulation(iteration + 1))

    def plots(self): 
        iteration = len(self.history) 

        # wykres plam po 10 iteracjach
        # if iteration % 10 == 0 and iteration > 0:
        #     plt.figure(1)
        #     plt.clf()
        #     plt.imshow(self.grid, cmap='gray')
        #     plt.title(f"Step {iteration}")
        #     plt.draw()
        #     plt.pause(0.1)
        
        # rozklad gestosci w czasie
        if iteration > 1:
            plt.figure(2)
            plt.clf()
            plt.plot(self.history, label="Density over time")
            plt.xlabel("Iterations")
            plt.ylabel("Density")
            plt.legend()
            plt.draw()
            plt.pause(0.1)

        self.root.after(10, self.plots)


root = tk.Tk()
simulation = Stains(root)
root.mainloop()

