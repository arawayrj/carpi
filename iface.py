import tkinter as tk
from tkinter import messagebox
top = tk.Tk()

C = tk.Canvas(top, bg="blue", height=480, width=800)
filename = tk.PhotoImage(file = "bg.png")
background_label = tk.Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

button = tk.Button(top, text="THIS IS A BUTTON", command=top.destroy)

C.pack()
button.pack(side=tk.LEFT)
top.mainloop()