import random
import os


def create2DArray(rows, cols):
    array =  [[0 for _ in range(cols)] for _ in range(rows)]

    for row in array: #have to display it row by row cause otherwise it just displays a long horizontal list of lists.
        print(row)

# grid = create2DArray(10,10)

def printGrid(grid):
    os.system('cls' if os.name == 'nt' else 'clear') #this clears the terminal
    for row in grid:
        print(''.join(['1' if cell else '0' for cell in row]))
    print()

def randomizeGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = random.choice([0, 1])