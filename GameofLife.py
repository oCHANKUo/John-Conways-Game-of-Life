#Tkinter is a GUI toolkit that i can use to create a GUI for this. At least attempt it.

import tkinter as tk

#create a 2d Array filled with 0s
def create2DArray(rows=10, cols=10):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def displayGrid(array):
    root = tk.Tk()
    root.title("Game of Life")

    rows = len(array)
    cols = len(array[0]) #since its a list of lists, this takes the length of the first row. ie columns

    for r in range(rows):
        for c in range(cols):

            cellValue = array[r][c]

            #colors
            if cellValue == 0:
                bg_color = "white"
                fg_color = "black"
            elif cellValue == 1:
                bg_color = "black"
                fg_color = "white"
            else:
                bg_color = "white"
                fg_color = "black"


            label = tk.Label(root, text=str(cellValue), borderwidth=1, relief="solid", width=4, height=2)
            label.grid(row=r, column=c, sticky="nsew")
    
    root.mainloop()

#canvas
#C = tk.Canvas(root, bg="white", height=500, width=500)

array = create2DArray()
displayGrid(array)