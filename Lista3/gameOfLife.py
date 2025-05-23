import pygame 
import random
import matplotlib.pyplot as plt

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

width, height = 1000, 1000
tile_size = 10 
grid_width = width // tile_size
grid_height = height // tile_size
fps = 60

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

def gen(p0):
    return set([(x,y) for x in range(grid_height) for y in range(grid_width) if random.random() < p0])

def draw_grid(positions):
    ''' function to draw a grid, every tile is a position multiplied by the desired size of the tile'''
    for position in positions:
        col,row = position
        top_left = (col * tile_size, row * tile_size)
        pygame.draw.rect(screen,red, (*top_left,tile_size,tile_size))

    for row in range(grid_height):
        pygame.draw.line(screen, black, (0,row * tile_size), (width , row * tile_size))

    for col in range(grid_width):
        pygame.draw.line(screen,black,(col * tile_size,0),(col * tile_size,height))

def adjust_grid(positions):
    '''function that manages the life of the cell'''
    all_neighbors = set()
    new_positions = set()

    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)

        #fill with only those cells that are alive
        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) in [2,3]:
            new_positions.add(position)

    for position in all_neighbors:
        neighbors = get_neighbors(position)

        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) == 3:
            new_positions.add(position)

    return new_positions

def get_neighbors(pos):
    '''function to get the neighbors of the cell'''
    x,y = pos
    neighbors = []

    for dx in [-1, 0, 1]:
        if x + dx < 0 and x + dx > grid_width:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 and y + dy > grid_height:
                continue
            if dx == 0 and dy == 0:
                continue
            neighbors.append((x + dx, y + dy))

    return neighbors

def main():
    '''main function'''
    playing = True
    playSim = False
    cnt = 0
    update_freq = 120 # update the simulation after reaching some value
    p0 = 0.5
    densities = []
    positions = gen(p0)


    while(playing):
        clock.tick(fps)

        # for testing purposes, update slower
        # if playSim:
        #     cnt += 1
        
        # if cnt >= update_freq:
        #     cnt = 0
        #     density = len(positions) / (grid_width * grid_height)
        #     densities.append(density)
        #     positions = adjust_grid(positions)

        if playSim:
            cnt += 1
            density = len(positions) / (grid_width * grid_height)
            densities.append(density)
            positions = adjust_grid(positions)

        pygame.display.set_caption("Simulation started" if playSim else "Paused")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playSim = not playSim
                
                if event.key == pygame.K_c:
                    positions = gen(p0)
                    cnt = 0
                    playSim = False
                
                if event.key == pygame.K_g:
                    positions = gen(p0)

        screen.fill(white)
        draw_grid(positions)
        pygame.display.update()

    plt.plot(densities)
    plt.xlabel('Iterations')
    plt.ylabel('Density of live cells')
    plt.title(f'Behavior in p0 = {p0}')
    plt.show()

    pygame.quit()

if __name__ == "__main__":
    main()