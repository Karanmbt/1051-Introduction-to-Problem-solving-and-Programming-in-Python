import turtle as t


def ring(color,x,y):
    t.pensize(5) 
    t.color(color)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.circle(45)

ring("blue", -110, -25)
ring("black", 0, -25)
ring("red", 110, -25)
ring("yellow", -55, -75)
ring("green", 55, -75)

t.done()