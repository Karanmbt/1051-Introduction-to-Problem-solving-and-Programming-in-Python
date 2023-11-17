import turtle


num_turtles = 5
my_turtles = [turtle.Turtle() for i in range(num_turtles)]


for i, turt in enumerate(my_turtles):
    turt.color("blue")
    turt.penup()
    turt.goto(-110, -25)
    turt.pendown()
    turt.circle(45)

for i, turt in enumerate(my_turtles):
    turt.color("black")
    turt.penup()
    turt.goto(0, -25)
    turt.pendown()
    turt.circle(45)