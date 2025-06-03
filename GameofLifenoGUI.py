def create2DArray(rows, cols):
    array =  [[0 for _ in range(cols)] for _ in range(rows)]

    for row in array: #have to display it row by row cause otherwise it just displays a long horizontal list of lists.
        print(row)

grid = create2DArray(10,10)