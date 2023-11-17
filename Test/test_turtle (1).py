from time import sleep
import time
import turtle

# Your code here

bob = turtle.Turtle()
bob.color('blue')

for i in range (0,8):
    bob.up()
    bob.forward(60)
    bob.down()
    bob.forward(40)
    bob.right(45)
    bob.backward(100)
    bob.right(45)
    bob.forward(100)
    bob.right(45)
    bob.backward(45)
    bob.up()
    bob.forward(100)
    bob.down()

time.sleep(5)