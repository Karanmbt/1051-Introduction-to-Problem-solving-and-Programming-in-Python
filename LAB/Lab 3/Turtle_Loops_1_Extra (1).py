import turtle


#already submitted but turtle.speed(0) next time LUL :skull:


#imperfect logo
#\/\/\/\/\/\/\/\/
#turtle 1 blue
t1=turtle.Turtle()
t1.speed(50)
t1.pensize(5) 
t1.color("blue")
t1.penup()
t1.setposition(-110, -25)
t1.pendown()
t1.circle(45)

#turtle 2 black
t2=turtle.Turtle()
t2.speed(50)
t2.pensize(5) 
t2.color("black")
t2.penup()
t2.setposition(0, -25)
t2.pendown()
t2.circle(45)

#turtle 3 red
t3=turtle.Turtle()
t3.speed(50)
t3.pensize(5) 
t3.color("red")
t3.penup()
t3.setposition(110, -25)
t3.pendown()
t3.circle(45)

#turtle 4 yellow
t4=turtle.Turtle()
t4.speed(50)
t4.pensize(5) 
t4.color("yellow")
t4.penup()
t4.setposition(-55, -75)
t4.pendown()
t4.circle(45)

#turtle 5 green
t5=turtle.Turtle()
t5.speed(50)
t5.pensize(5) 
t5.color("green")
t5.penup()
t5.setposition(55, -75)
t5.pendown()
t5.circle(45)



#perfected logo

#blue over yellow fix
t1.penup()
t1.circle(45, 50)
t1.pendown()
t1.circle(45, 50)

#hide them turtles
t1.hideturtle()
t4.hideturtle()

#black over green and yellow fix
t2.penup()
t2.circle(45, 50)
t2.pendown()
t2.circle(45, 100)
t2.penup()
t2.circle(45,140)
t2.pendown()
t2.circle(45,70)

#hide that turtle
t2.hideturtle()

#red over green fix
t3.penup()
t3.circle(45, 300)
t3.pendown()
t3.circle(45,80)

#hide them turtles
t3.hideturtle()
t5.hideturtle()

turtle.done()