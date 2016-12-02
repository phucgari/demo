def draw_square(length,_color):
    color(_color)
    begin_fill()
    fd(length)
    lt(90)
    fd(length)
    lt(90)
    fd(length)
    lt(90)
    fd(length)
    lt(90)
from turtle import *
speed(-1)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

