from tkinter import *
from tkinter import messagebox

import pygame

from main import sc, score, record

W, H = 10, 20
TILE = 45
GAME_RES = W * TILE, H * TILE
RES = 750, 940
FPS = 60

def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()


tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Tetris")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
#tk.iconbitmap("bomb-3175208_640.ico")

canvas = Canvas(tk, width=RES[0], height=RES[1], bg="red", highlightthickness=0)
canvas.pack()

img_obj1 = PhotoImage(file="img/bg.png")
canvas.create_image(0, 0, anchor=NW, image=img_obj1)

img_obj2 = PhotoImage(file="img/bg2.png")
canvas.create_image(20, 20, anchor=NW, image=img_obj2)

grid = [canvas.create_rectangle(x * TILE, y * TILE, x * TILE+TILE, y * TILE+TILE) for x in range(W) for y in range(H)]
for item in grid:
    canvas.move(item, 20, 20)



canvas.create_text(505, 30,text="TETRIS", font=("Wi Guru 2", 65),fill="red")

#canvas.create_rectangle(420,120,480,480, fill="darkgreen", outline="")
#canvas.create_text(200,500,text="Hello World!", font=("Arial", 40),fill="white")


tk.mainloop()