import turtle
turtle.bgcolor('black')
t = turtle.Pen()
t.speed(0)
colors = ["red", "purple", "blue", "green", "yellow", "orange"]
for x in range(380):
    t.pencolor(colors[x % 6])
    t.width(4*x/100+2)
    t.forward(x)
    t.left(63)
turtle.done()
