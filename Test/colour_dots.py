import turtle  
t = turtle.Turtle() 
t.speed(0)

def draw(space,x): 
    for i in range(x):
        for j in range(x):
            if (i+j) % 2 == 0:
                t.color("red")
            else:
                t.color("blue")
            t.dot(10)
            t.penup()
            t.forward(space)
            t.pendown()
        t.penup()
        t.backward(space*x)
        t.right(90)
        t.forward(space)
        t.left(90)
        t.pendown()
  
            
t.penup()
draw(30,6) 
t.hideturtle()