from turtle import Screen, Turtle
from random import randrange, randint

# parameters
COLORS = ['green', 'blue', 'red', 'orange', 'white']
ITERATIONS = 500
VELOCITY = 5
BOX_SIZE = 512

# setting up screen
screen = Screen()
screen.setup(BOX_SIZE + 50, BOX_SIZE + 50)
screen.bgcolor('black')
screen.tracer(False)

# drawing box
turtle = Turtle()
turtle.hideturtle()
turtle.color('cyan')

turtle.penup()
turtle.goto(-BOX_SIZE/2, -BOX_SIZE/2)
turtle.pendown()

for _ in range(4):
    turtle.forward(BOX_SIZE)
    turtle.left(90)

# turtle
for color in COLORS:
    angle = randrange(360)
    x = randint(-BOX_SIZE/2, BOX_SIZE/2)
    y = randint(-BOX_SIZE/2, BOX_SIZE/2)

    turtle = Turtle()
    turtle.color(color)
    turtle.setheading(angle)
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()

# turtle movement
for _ in range(ITERATIONS):
    for turtle in screen.turtles():
        turtle.forward(VELOCITY)

        x, y = turtle.position()

        if x >= BOX_SIZE/2:
            turtle.penup()
            turtle.setx(-BOX_SIZE/2)
            turtle.pendown()
        elif x <= -BOX_SIZE/2:
            turtle.penup()
            turtle.setx(BOX_SIZE/2)
            turtle.pendown()
        elif y >= BOX_SIZE/2:
            turtle.penup()
            turtle.sety(-BOX_SIZE/2)
            turtle.pendown()
        elif y <= -BOX_SIZE/2:
            turtle.penup()
            turtle.sety(BOX_SIZE/2)
            turtle.pendown()

    screen.update()

screen.exitonclick()