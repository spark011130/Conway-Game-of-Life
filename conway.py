import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# It took me an hour to copy it.
hammerhead = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.'],
['.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', 'X'],
['X', 'X', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.'],
['.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', 'X'],
['.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', 'X', '.', 'X', 'X', 'X', 'X', '.'],
['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', 'X', '.', 'X', 'X', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', '.', 'X', '.', 'X', 'X', '.', '.', '.', '.', '.'],
['.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', 'X', '.', 'X', 'X', 'X', 'X', '.'],
['.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', 'X'],
['X', 'X', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.'],
['.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', 'X'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.']]

def initialize_grid(n):
    """
    Initializes a grid of size n x n and places the hammerhead pattern in the center.

    Parameters:
    n (int): The size of the grid. If n is smaller than 20, it is set to 20.

    Example:
    >>> initialize_grid(20)
    [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
     ['.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', 'X'],
     ... ]
    """
    n = max(n, 20)
    grid = [['.' for _ in range(n)] for _ in range(n)]
    for y in range(len(hammerhead)):
        for x in range(len(hammerhead[0])):
            grid[n//2 + y - (len(hammerhead)//2)][n//2 + x - (len(hammerhead)//2)] = hammerhead[y][x]
    return grid

def evolve(grid):
    """
    Evolves the grid for one iteration of the Game of Life rules.

    Parameters:
    grid (list of list of str): The current state of the grid, where each cell is either '.' (empty) or 'X' (alive).

    Returns:
    list of list of str: The new state of the grid after one iteration.

    Example:
    >>> evolve([['.', '.', '.', 'X'], ['X', '.', '.', '.']])
    [['.', '.', '.', '.'], ['.', 'X', '.', '.']]
    """
    n = len(grid)
    dy = [1, 1, 1, 0, 0, -1, -1, -1]
    dx = [1, 0, -1, 1, -1, 1, 0, -1]
    new_grid = [['.' for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            temp_neighbor = 0
            for d_selecter in range(8):
                if 0 <= (y + dy[d_selecter]) < n and 0 <= (x + dx[d_selecter]) < n:
                    if grid[y+dy[d_selecter]][x+dx[d_selecter]] == 'X':
                        temp_neighbor += 1
            if grid[y][x] == '.' and temp_neighbor == 3:
                new_grid[y][x] = 'X'
            elif grid[y][x] == 'X' and temp_neighbor < 2:
                new_grid[y][x] = '.'
            elif grid[y][x] == 'X' and 2 <= temp_neighbor <= 3:
                new_grid[y][x] = 'X'
            elif grid[y][x] == 'X' and temp_neighbor > 3:
                new_grid[y][x] = '.'
    return new_grid

def visualize(grid, iteration):
    """
    Visualizes the grid for the given iteration and displays it.

    Parameters:
    grid (list of list of str): The current state of the grid.
    iteration (int): The current iteration number to be displayed as the title.

    Example:
    >>> visualize([['.', '.', '.', 'X'], ['X', '.', '.', '.']], 1)
    (Displays the grid with iteration number 1 as the title)
    """
    np_grid = np.array(grid)
    plt.imshow(np_grid == 'X', cmap='binary')
    plt.title(f"Iteration {iteration}")
    plt.axis('off')
    plt.show(block=False)
    plt.pause(0.01)
    
def save_image(grid):
    """
    Saves an image of the grid at the given iteration.

    Parameters:
    grid (list of list of str): The current state of the grid.

    Example:
    >>> save_image([['.', '.', '.', 'X'], ['X', '.', '.', '.']])
    (Saves the grid image with filename 'game_of_life.png')
    """
    np_grid = np.array(grid)
    plt.imshow(np_grid == 'X', cmap='binary')
    plt.axis('off')
    plt.savefig('game_of_life.png')

def save_video(frames):
    """
    Saves the grid evolution as a video.

    Parameters:
    frames (list of list of list of str): A list of grids, where each grid represents the state of the grid at a particular iteration.

    Example:
    >>> save_video([[['.', '.', '.', 'X'], ['X', '.', '.', '.']], [['.', '.', '.', '.'], ['.', 'X', '.', '.']]])
    (Saves the grid evolution as a video in 'game_of_life.mp4')
    """
    fig, ax = plt.subplots()
    ax.axis('off')
    imgs = []
    for i, frame in enumerate(frames):
        np_frame = np.array(frame)
        im = ax.imshow(np_frame == 'X', cmap='binary', animated=True)

        imgs.append([im])
    
    ani = animation.ArtistAnimation(fig, imgs, interval=100, blit=True)
    ani.save('game_of_life.mp4', writer='ffmpeg', fps = 10)

def main():
    """
    Main function to run the simulation. It prompts the user to input the number of iterations and performs the grid evolution.
    The final grid state is visualized and saved as both an image and video.

    Example:
    >>> main()
    (Prompts for input and runs the simulation for the entered number of iterations)
    """
    while True:
        try:
            k = int(input("input the k: "))
            if k <= 0:
                print("k has to be a positive integer.")
                print("Enter again.")
            else:
                break
        except:
            print('k has to be an integer.')
            print("Enter again.")
    n = 100
    grid = initialize_grid(n)
    frames = [grid]
    visualize(grid, 1)
    for iteration in range(1, k+1):
        grid = evolve(grid)
        if iteration % 10 == 0:
            visualize(grid, iteration)
        frames.append(grid)    
    save_image(grid, k)
    save_video(frames)
    plt.close('all')

if __name__ == '__main__':
    main()