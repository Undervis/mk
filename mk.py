from functools import partial
from tkinter import *

root = Tk()
root.title("Drawing")

colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", 'black']
width = 2
color = 'black'

p1 = PanedWindow()
p1.pack(fill="both", expand=True)
canvas = Canvas(p1, width=500, height=500, bg="white", cursor="pencil")
p1.add(canvas)
p2 = PanedWindow(p1, orient=VERTICAL)
p1.add(p2)

def increase():
    global width
    width += 2
def decrease():
    global width
    width -= 2
def set_color(new_color):
    global color
    color = new_color


# Пишем ниже
size_increase = Button(p2, text="+", command=increase, height=5)
p2.add(size_increase)
size_decrease = Button(p2, text="-", command=decrease, height=5)
p2.add(size_decrease)

for btn in colors:
    set_new_color = partial(set_color, btn)
    color_btn = Button(p2, bg=btn, command=set_new_color, height=1)
    p2.add(color_btn)

clear_canvas = partial(canvas.delete, "all")
clear_btn = Button(p2, text="Clear", command=clear_canvas)
p2.add(clear_btn)


def draw_line(event):
    canvas.create_line(event.x, event.y, event.x + width, event.y + width, fill=color, width=width)


canvas.bind("<B1-Motion>", draw_line)
canvas.mainloop()
