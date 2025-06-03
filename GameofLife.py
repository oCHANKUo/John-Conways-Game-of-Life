#Tkinter is a GUI toolkit that i can use to create a GUI for this. At least attempt it.

import tkinter as tk

root = tk.Tk()

#canvas
C = tk.Canvas(root, bg="white", height=500, width=500)

C.pack()
root.mainloop()  #can use tk.mainloop() as well, but it seems like root.mainloop() is good practice