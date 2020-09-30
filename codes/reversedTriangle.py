import turtle
import random

canvas = turtle.Screen()
t = turtle.Turtle()

canvas.colormode(255)
t.speed(0)
t.width(2)
canvas.bgcolor("black")
t.pencolor(255, 99, 71)


def shape(angle, side, limit):
    reverseDirection = 200
    t.forward(side)

    if side % (reverseDirection*2) == 0:
        angle = angle+2
    elif side % reverseDirection == 0:
        angle = angle - 2

    t.right(angle)
    side = side+2
    if side < limit:
        shape(angle, side, limit)


angle = 119
side = 0
limit = 600
shape(angle, side, limit)

turtle.done()
