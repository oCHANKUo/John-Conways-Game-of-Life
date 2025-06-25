import turtle
import random
import time

#trying to add GUI

# Create the grid with random 0s and 1s
def create2DArray(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

# Count live neighbors of a cell
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

# Compute the next generation grid
def nextGeneration(grid):
    rows = len(grid)
    cols = len(grid[0])
    newGrid = create2DArray(rows, cols)  # temp grid

    for i in range(rows):
        for j in range(cols):
            liveNeighbours = countNeighbours(grid, i, j)

            if grid[i][j] == 1:
                newGrid[i][j] = 1 if 2 <= liveNeighbours <= 3 else 0
            else:
                newGrid[i][j] = 1 if liveNeighbours == 3 else 0

    return newGrid

# Draw the grid on the turtle window
def drawGrid(grid, cell_size):
    turtle.clear()
    turtle.penup()
    rows = len(grid)
    cols = len(grid[0])
    
    # Start drawing from top-left corner (arbitrary choice)
    start_x = -cols * cell_size // 2
    start_y = rows * cell_size // 2
    
    for i in range(rows):
        for j in range(cols):
            x = start_x + j * cell_size
            y = start_y - i * cell_size
            turtle.goto(x, y)
            turtle.pendown()
            if grid[i][j] == 1:
                turtle.fillcolor("black")
            else:
                turtle.fillcolor("white")
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(cell_size)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()
    turtle.update()

def runGame():
    rows, cols = 20, 20  # can increase grid size here
    cell_size = 20       # size of each cell in pixels

    grid = create2DArray(rows, cols)

    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(0, 0)  # Turn off animation for faster drawing

    loops = 100
    delay = 0.1

    for _ in range(loops):
        drawGrid(grid, cell_size)
        grid = nextGeneration(grid)
        time.sleep(delay)

    turtle.done()

runGame()
