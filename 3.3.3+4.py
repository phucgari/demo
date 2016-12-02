def draw_star(a,b,c):
    color('white')
    setposition(a,b)
    for _ in range(5):
        color('blue')
        fd(c)
        rt(144)
from turtle import*
speed(0)
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)


