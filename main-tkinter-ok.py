from tkinter import *
from tkinter import messagebox
from random import choice, randrange


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

sc = Canvas(tk, width=RES[0], height=RES[1], bg="red", highlightthickness=0)
sc.pack()

game_sc = Canvas(tk, width=W*TILE+1, height=H*TILE+1, bg="yellow", highlightthickness=0)
game_sc.place(x=20, y=20, anchor=NW)

img_obj1 = PhotoImage(file="img/bg.png")
sc.create_image(0, 0, anchor=NW, image=img_obj1)

img_obj2 = PhotoImage(file="img/bg2.png")
game_sc.create_image(0, 0, anchor=NW, image=img_obj2)

grid = [game_sc.create_rectangle(x * TILE, y * TILE, x * TILE+TILE, y * TILE+TILE) for x in range(W) for y in range(H)]


score = "0"
record = "0"

sc.create_text(505, 30,text="TETRIS", font=("Wi Guru 2", 45),fill="red", anchor=NW)
sc.create_text(535, 780,text="score:", font=("Wi Guru 2", 40),fill="white", anchor=NW)
sc.create_text(550, 840,text=str(score), font=("Wi Guru 2", 40),fill="white", anchor=NW)
sc.create_text(525, 650,text="record:", font=("Wi Guru 2", 40),fill="white", anchor=NW)
sc.create_text(550, 710,text=record, font=("Wi Guru 2", 40),fill="gold", anchor=NW)

get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


for item in grid:
    sc.itemconfigure(item, fill=rgb_to_hex(get_color()))

for item in grid:
    sc.itemconfigure(item, fill="")


figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
#figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
field = [[0 for i in range(W)] for j in range(H)]

from copy import deepcopy
figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = get_color(), get_color()

# draw figure
for i in range(4):
    figure_rect_x = figure[i][0] * TILE
    figure_rect_y = figure[i][1] * TILE
    game_sc.create_rectangle(figure_rect_x, figure_rect_y, figure_rect_x+TILE, figure_rect_y+TILE,fill=rgb_to_hex(color))


tk.mainloop()