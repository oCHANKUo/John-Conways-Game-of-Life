
#this is the same version as the previous game of life with no GUI, but with auto run AND beginning conditions.
# Had to completely rely on ChatGPT for this

import random
import os
import time #got help from ChatGPT to come up with the time inclusion


def create2DArray(rows, cols):
    # array =  [[0 for _ in range(cols)] for _ in range(rows)]

    # for row in array: #have to display it row by row cause otherwise it just displays a long horizontal list of lists.
        # print(row)
    # return array
   return [[0 for _ in range(cols)] for _ in range(rows)]

# grid = create2DArray(10,10)

# Used to print the grid onto the terminal
def printGrid(grid):
    os.system('cls' if os.name == 'nt' else 'clear') #this clears the terminal
    for row in grid:
        print(''.join(['■' if cell else ' ' for cell in row])) #Thank you chatGPT for coming up with this visualising method
    print()

def randomizeGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = random.choice([0, 1])

def countNeighbours(grid, row, col):
    neighbours = 0
    for i in range(-1, 2):       # -1, 0, 1
        for j in range(-1, 2):   # -1, 0, 1
            if i == 0 and j == 0:
                continue #skips its own cell
            r = row + i
            c = col + j
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                neighbours += grid[r][c]
    return neighbours

def nextGeneration(grid):
    rows = len(grid)
    cols = len(grid[0])
    newGrid = create2DArray(rows, cols)

    for i in range(rows):
        for j in range(cols):
            liveNeighbours = countNeighbours(grid, i, j)

            if grid[i][j] == 1:
                newGrid[i][j] = 1 if 2 <= liveNeighbours <= 3 else 0
            else:
                newGrid[i][j] = 1 if liveNeighbours == 3 else 0

    return newGrid

#Choosing a specific pattern
def applyPattern(grid, patternName):
    midRow = len(grid) // 2
    midCol = len(grid[0]) // 2

    patterns = {
        "block": [(0, 0), (0, 1), (1, 0), (1, 1)],
        "blinker": [(-1, 0), (0, 0), (1, 0)],
        "glider": [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
        "beacon": [(0, 0), (0, 1), (1, 0), (2, 3), (3, 2), (3, 3)],
        "toad": [(1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3)],
        "lwss": [
        (0, 1), (0, 4),
        (1, 0),
        (2, 0), (2, 4),
        (3, 1), (3, 2), (3, 3), (3, 4)]
    }
    if patternName not in patterns:  #I just realised how much i skip over error handling. If i was writing this part on my own, i would not think to put error handling. Need to practice that
        print("Pattern not found. Using Random generation")
        return False
    
    for dr, dc in patterns[patternName]:
        r, c = midRow + dr, midCol + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            grid[r][c] = 1
    return True



def runGame():
    rows, cols = 20, 20
    grid = create2DArray(rows, cols)

    #option to select the pattern ("glider", "blinker", "block", "beacon", "toad", "lwss")
    selectedPattern = "block"  

    if selectedPattern:
        applyPattern(grid, selectedPattern)
    else:
        #Randomise grid if no pattern is selected
        randomizeGrid(grid)

    loops = 50 #this will be the number of generations
    delay = 0.1 #the time interval between each generation
    for generation in range(loops):
        # print(f"Generation {generation + 1}")  Commented this cus the loops going too fast and this seems like a waste
        printGrid(grid)
        grid = nextGeneration(grid)
        time.sleep(delay) #pause between each generation

runGame()