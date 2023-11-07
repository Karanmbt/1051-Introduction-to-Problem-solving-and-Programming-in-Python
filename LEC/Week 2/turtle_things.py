import turtle



bob = turtle.Turtle()
bob.speed(100)
bob.shapesize(2,2)
bob.pensize(10)

colours = ['red','green','blue']
dst = 100

alice = turtle.Turtle()
alice.speed(100)
alice.shapesize(2,2)
alice.pensize(10)

colours = colours*20

for col in colours:
    bob.color(col)
    bob.fd(dst)
    bob.right(60)
    dst = dst + 5

#for col in colours:
#   alice.color(col)
#  alice.fd(200)
# alice.left(120)



turtle.done()