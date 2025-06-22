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

def countNeighbours(grid, row, col):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            r = row + i
            c = col + j
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                neighbours += grid[r][c]
    return neighbours

def nextGeneration(grid):
    rows = len(grid)
    cols = len(grod[0])
    newGrid = create2DArray(rows, cols)

    for i in range(rows):
        for j in range(cols):
            liveNeighbours = countNeighbours(grid, i, j)

            if grid[i][j] == 1:
                newGrid[i][j] = 1 if 2 <= liveNeighbours <= 3 else 0
            else:
                newGrid[i][j] = 1 if liveNeighbours == 3 else 0

    return newGrid

def runGame():
    rows, cols = 10, 10
    grid = create2DArray(rows, cols)
    randomizeGrid(grid)

    loops = 10 #this will be the number of generations
    for generation in range(loops):
        print(f"Generation {generation + 1}")
        printGrid(grid)
        grid = nextGeneration(grid)
        input("Press Enter to Continue")

runGame()