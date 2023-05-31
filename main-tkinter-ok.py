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

main_font = pygame.font.Font('font/font.ttf', 65)
font = pygame.font.Font('font/font.ttf', 45)

title_tetris = main_font.render('TETRIS', True, pygame.Color('red'))
title_score = font.render('score:', True, pygame.Color('white'))
title_record = font.render('record:', True, pygame.Color('white'))

sc.blit(title_score, (535, 780))
sc.blit(font.render(str(score), True, pygame.Color('white')), (550, 840))
sc.blit(title_record, (525, 650))
sc.blit(font.render(record, True, pygame.Color('gold')), (550, 710))

score = "0"
record = "0"

canvas.create_text(505, 30,text="TETRIS", font=("Wi Guru 2", 45),fill="red", anchor=NW)
canvas.create_text(535, 780,text="score:", font=("Wi Guru 2", 40),fill="white", anchor=NW)
canvas.create_text(550, 840,text=str(score), font=("Wi Guru 2", 40),fill="white", anchor=NW)
canvas.create_text(525, 650,text="record:", font=("Wi Guru 2", 40),fill="white", anchor=NW)
canvas.create_text(550, 710,text=record, font=("Wi Guru 2", 40),fill="gold", anchor=NW)

#canvas.create_rectangle(420,120,480,480, fill="darkgreen", outline="")
#canvas.create_text(200,500,text="Hello World!", font=("Arial", 40),fill="white")


tk.mainloop()